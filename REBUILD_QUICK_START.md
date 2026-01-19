# Dashboard Rebuild - Quick Start Guide

**Last Updated:** 2026-01-12
**Purpose:** Fast-track rebuild instructions
**Read Time:** 3 minutes

---

## 📂 YOUR REBUILD DOCUMENTATION

You have **3 key documents** for rebuilding:

### 1. **[COMPLETE_REBUILD_REFERENCE.md](COMPLETE_REBUILD_REFERENCE.md)** - The Master Spec
   - **All 24 tables** with schemas
   - **All 5 relationships**
   - **150+ DAX measures** with code
   - **35+ visuals** with exact specs
   - **Power Query transformations**
   - **Design system** (colors, fonts, spacing)

### 2. **[REBUILD_REFERENCE_ADDENDUM.md](REBUILD_REFERENCE_ADDENDUM.md)** - Critical Fixes ⚠️
   - **6 corrections** to main document
   - **Bulletproof enhancements** (parameters, functions)
   - **QA measures** for validation
   - **Corrected visual specs**

   **READ THIS FIRST before rebuilding!**

### 3. **This Document** - Quick Start Steps

---

## ⚡ REBUILD IN 5 PHASES

### **Phase 1: Power Query Setup (30 min)**

**Step 1:** Create parameter `pDatasetsFolder`
```
Type: Text
Value: C:\Users\farad\Dev\WORK\HHS\repos\auto-the-big-one\dashboards\01_Live_Events_Dashboard\datasets\
```

**Step 2:** Create shared functions
- `fxTransformCTR` (handle GSC percentages)
- `fxLoadGA4Standard` (skip 6 rows, clean headers)

**Step 3:** Import all 18 CSV files
- Use parameter: `pDatasetsFolder & "filename.csv"`
- Skip 6 rows for GA4 files
- Apply CTR transformation for GSC files

**Step 4:** ⚠️ **CRITICAL FIX - ga4-titles**
```m
// Add these steps to ga4-titles query:
#"Cleaned Numbers" = Table.TransformColumns(
    Source,
    {
        {"Event count", each Text.Replace(_, ",", ""), type text},
        {"Total users", each Text.Replace(_, ",", ""), type text}
    }
),
#"Changed Type" = Table.TransformColumnTypes(
    #"Cleaned Numbers",
    {
        {"Event count", Int64.Type},
        {"Total users", Int64.Type}
    }
)
```

**Test:** All queries load without errors

---

### **Phase 2: Data Model (20 min)**

**Step 1:** Create calculated tables
```dax
// DimDate (create FIRST)
VAR MinDataDate = MIN('ga4-daily'[Date])
VAR MaxDataDate = MAX('ga4-daily'[Date])
VAR StartDate = IF(ISBLANK(MinDataDate), DATE(2025, 1, 1), MinDataDate)
VAR EndDate = IF(ISBLANK(MaxDataDate), DATE(2025, 12, 31), MaxDataDate)
RETURN
ADDCOLUMNS(
    CALENDAR(StartDate, EndDate),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "mmm yyyy"),
    "Day of Week", FORMAT([Date], "dddd"),
    "Is Weekday", IF(WEEKDAY([Date], 2) <= 5, TRUE(), FALSE())
)

// DimLivecast
SELECTCOLUMNS(
    VALUES('ga4-titles'[Page title]),
    "livecast_title", 'ga4-titles'[Page title],
    "Livecast Title", 'ga4-titles'[Page title]
)

// DimAction
SELECTCOLUMNS(
    VALUES('ga4-events'[Event name]),
    "livecast_action", 'ga4-events'[Event name],
    "Action", 'ga4-events'[Event name]
)

// Measures_Livecast
DATATABLE("Dummy", INTEGER, {{1}})

// Action Catalog & Recommended Actions
// (See main document for full code)
```

**Step 2:** Mark DimDate as date table
- Select DimDate → Table tools → Mark as date table
- Date column: Date

**Step 3:** Create relationships (IN THIS ORDER)
1. DimDate[Date] → ga4-daily[Date] (One-to-Many, Both)
2. DimDate[Date] → gsc-chart[Date] (One-to-Many, Both)
3. DimLivecast[livecast_title] → ga4-pages[Page title] (One-to-Many, Both)
4. DimAction[livecast_action] → ga4-events[Event name] (One-to-Many, Both)
5. ga4-pages[Page title] → ga4-titles[Page title] (Many-to-One, Both)

**Step 4:** Test immediately
- Add date slicer
- Add Sessions card
- Filter dates → Sessions should change
- If not, relationship is broken

---

### **Phase 3: Measures (60 min)**

**Step 1:** Create QA measures FIRST
```dax
measure 'QA - CTR Min' = MIN('gsc-chart'[CTR])
    formatString: 0.00%

measure 'QA - CTR Max' = MAX('gsc-chart'[CTR])
    formatString: 0.00%

measure 'QA - Date Filters Sessions' =
    VAR AllSessions = CALCULATE([Sessions], ALL(DimDate))
    VAR FilteredSessions = [Sessions]
    RETURN
    IF(
        AllSessions = FilteredSessions,
        "⚠️ Date slicer not impacting Sessions",
        "✅ Date slicer impacting Sessions"
    )
```

**Expected Values:**
- CTR Min: ~0%
- CTR Max: <50% (if >50%, CTR formula wrong)
- Date Filters: "✅ Date slicer impacting Sessions"

**Step 2:** Create measures by category
1. Core Metrics (11 measures)
2. Geography Metrics (8 measures)
3. Acquisition Metrics (5 measures)
4. Engagement Metrics (5 measures)
5. Device Metrics (2 measures)
6. Search Console Metrics (7 measures)
7. Time Intelligence (15 measures)
8. KPI Helpers (15 measures)
9. System Metrics (3 measures)

**Full DAX code:** See COMPLETE_REBUILD_REFERENCE.md Section 4

**Step 3:** Test key measures
```
[Sessions] → Should be thousands
[Total Engagement (Minutes)] / [Sessions] → Should be 1-10 range
[Search CTR] → Should be 0-50%
[Sessions - MoM %] → Should show trend
```

---

### **Phase 4: Column Visibility (10 min)**

Hide numeric columns in fact tables:

**ga4-pages:**
- Views, Sessions, Total users, Engagement rate, Average engagement time, Engaged sessions

**ga4-devices:**
- Sessions, Views, Total users, Engagement rate

**ga4-geography:**
- Sessions, Total users, Views

**ga4-events:**
- Event count, Total users

**All GSC tables:**
- CTR column

**Why:** Forces users to use measures (prevents wrong aggregations)

---

### **Phase 5: Build Pages (4-5 days)**

**Day 1: Apply Theme & Build Page 1**
1. File → Options → Theme → Import → USWDS_Light_Theme.json
2. Build navigation rail (60px × 1080px, white background)
3. Build header (eyebrow, title, subtitle, divider)
4. Build 4 KPI cards (295px × 100px each)
5. Build 2 charts (map, donut)
6. Build 2 tables (Top Livecast Videos, Top Pages)
7. Build Recommended Actions panel (400px × 412px)

**Day 2-3: Build Pages 2-5**
- Page 2: Explorer (matrix, treemap, bar chart)
- Page 3: Traffic & Acquisition (stacked column, bar chart, funnel)
- Page 4: Play Events (area chart, bar chart, column chart)
- Page 5: External Search (combo chart, table, scatter)

**Day 4: Build Pages 6-7**
- Page 6: AI Insights (anomaly detection, forecast, gauge)
- Page 7: Deep Dive (decomposition tree, matrix, scatter)

**Day 5: Polish & QA**
- Add navigation bookmarks
- Add info tooltips
- Test all slicers and interactions
- Add alt text to visuals
- Final validation

**Visual specs:** See COMPLETE_REBUILD_REFERENCE.md Section 5

---

## ⚠️ CRITICAL GOTCHAS TO AVOID

### **1. Wrong File Path**
❌ Absolute paths break when moving files
✅ Use parameter: `pDatasetsFolder & "filename.csv"`

### **2. ga4-titles Text Columns**
❌ `SUM('ga4-titles'[Total users])` errors if text
✅ Convert to INT64 in Power Query

### **3. CTR Conversion Order**
❌ Type cast before transforming = errors
✅ Transform → THEN type cast

### **4. Missing Date Columns**
❌ Time-series visuals with no Date in source = flatline
✅ Check source table has Date OR change to non-time-series visual

### **5. Summarizing Engagement Rate**
❌ Engagement rate summarized as SUM = wrong math
✅ Set to "Do not summarize" or "Average"

### **6. Testing Relationships**
❌ Creating all relationships then testing = debugging nightmare
✅ Test each relationship immediately after creating

---

## ✅ VALIDATION CHECKLIST

**After Phase 1 (Power Query):**
- [ ] Parameter `pDatasetsFolder` exists
- [ ] All 18 CSV queries load
- [ ] ga4-titles[Total users] is INT64 (not text)
- [ ] gsc-chart[CTR] values are 0-1 (not 0-100)

**After Phase 2 (Data Model):**
- [ ] 24 tables exist (18 CSV + 6 calculated)
- [ ] 5 relationships active
- [ ] DimDate marked as date table
- [ ] Date slicer changes [Sessions] value

**After Phase 3 (Measures):**
- [ ] [QA - CTR Max] < 0.5
- [ ] [QA - Date Filters Sessions] = "✅"
- [ ] [Total Engagement (Minutes)] / [Sessions] is 1-10 range
- [ ] All 150+ measures visible

**After Phase 4 (Visibility):**
- [ ] Can't drag ga4-pages[Views] to visual (hidden)
- [ ] Can drag [Page Views by Page] measure

**After Phase 5 (Pages):**
- [ ] All 7 pages exist
- [ ] Navigation works (bookmarks)
- [ ] Slicers impact all visuals
- [ ] No flatline charts

---

## 📚 REFERENCE DOCUMENTS BY USE CASE

**I need table schemas:**
→ COMPLETE_REBUILD_REFERENCE.md Section 2

**I need relationship map:**
→ COMPLETE_REBUILD_REFERENCE.md Section 3

**I need DAX measure code:**
→ COMPLETE_REBUILD_REFERENCE.md Section 4

**I need visual specifications:**
→ COMPLETE_REBUILD_REFERENCE.md Section 5

**I need Power Query code:**
→ COMPLETE_REBUILD_REFERENCE.md Section 6

**I need design system (colors, fonts):**
→ COMPLETE_REBUILD_REFERENCE.md Section 7

**I need to fix critical errors:**
→ REBUILD_REFERENCE_ADDENDUM.md

**I need PowerPoint wireframes:**
→ HHS_Live_Events_V4_FINAL.pptx

**I need detailed build instructions:**
→ 00_Documentation/03_Guides/COMPLETE_BUILD_GUIDE_TOP_TO_BOTTOM.md

---

## 🚀 FASTEST PATH TO WORKING DASHBOARD

**If you need a working dashboard in <1 day:**

1. **Phase 1-3 only** (Power Query + Data Model + Measures) = 2 hours
2. **Build Page 1 only** (Executive Summary) = 4 hours
3. **Test and validate** = 30 min

**Total:** 6.5 hours to functional dashboard with 1 page

**Then add pages incrementally:**
- Page 2 (Explorer) = +4 hours
- Page 3 (Traffic & Acquisition) = +4 hours
- Page 4 (Play Events) = +4 hours
- Page 5 (External Search) = +4 hours
- Pages 6-7 (AI Insights, Deep Dive) = +8 hours

**Full dashboard:** 30-32 hours total

---

## 💡 PRO TIPS

**Tip 1: Use shared functions**
Create `fxTransformCTR` once, use 6 times (GSC tables)

**Tip 2: Test relationships immediately**
Don't create all 5 relationships then test - test each one as you create it

**Tip 3: QA measures are your friend**
Create them first, check values every 30 minutes

**Tip 4: Copy-paste measures carefully**
formatString and displayFolder are part of the measure (not separate)

**Tip 5: Hide columns early**
Do Phase 4 before Phase 5 - prevents accidental column usage

---

## 🆘 IF SOMETHING GOES WRONG

**Problem:** Date slicer doesn't affect visuals
**Solution:** Check relationships exist and are active (Model view)

**Problem:** Measures return BLANK()
**Solution:** Check source table columns aren't hidden AND aren't text

**Problem:** CTR shows values >100%
**Solution:** CTR transformation didn't divide by 100 - fix Power Query

**Problem:** Time-series chart is flatline
**Solution:** Source table has no Date column - change to non-time-series visual

**Problem:** Total Engagement is millions
**Solution:** Using wrong formula - use SUMX (see addendum)

**Problem:** Can't find measure
**Solution:** Check Display Folder - measures are organized in categories

---

**Document Version:** 1.0
**Last Updated:** 2026-01-12
**Estimated Read Time:** 3 minutes
**Estimated Rebuild Time:** 30-32 hours (full dashboard)
**Estimated Rebuild Time:** 6.5 hours (1 page MVP)

---

**Start with Phase 1. Work sequentially. Test frequently. You've got this!** 🚀

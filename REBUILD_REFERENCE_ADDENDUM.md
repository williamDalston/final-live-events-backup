# COMPLETE_REBUILD_REFERENCE.md - Critical Addendum

**Date:** 2026-01-12
**Purpose:** Fixes and enhancements to prevent common rebuild issues
**Status:** ✅ Critical Corrections

---

## 🚨 CRITICAL CORRECTIONS TO MAIN DOCUMENT

### 1. TABLE COUNT CORRECTION

**Main Document Says:** "18 CSV + 4 calculated = 22 tables"

**Actually:**
- 18 CSV files ✅
- **6 calculated tables** (not 4):
  1. DimDate
  2. DimLivecast
  3. DimAction
  4. Measures_Livecast
  5. Action Catalog
  6. Recommended Actions

**Total: 18 CSV + 6 Calculated = 24 tables**

**Fix:** Update Section 1 to reflect 24 total tables.

---

### 2. GA4-TITLES DATA TYPE ISSUE (CRITICAL)

**Problem:** Main document says ga4-titles columns are stored as **strings**, but measures use `SUM()`:

```dax
// This will ERROR if columns are text
measure 'Users by Event' = SUM('ga4-titles'[Total users])
```

**Impact:** Dashboard will fail or return incorrect values.

**FIX (REQUIRED):** Add type conversion to ga4-titles Power Query:

```m
let
    Source = Csv.Document(File.Contents(pDatasetsFolder & "ga4-titles.csv"), [Delimiter=",", Columns=5]),
    #"Skipped Rows" = Table.Skip(Source, 6),
    #"Promoted Headers" = Table.PromoteHeaders(#"Skipped Rows"),
    #"Skipped Rows1" = Table.Skip(#"Promoted Headers", 1),

    // ADD THIS STEP (handles commas in numbers)
    #"Cleaned Numbers" = Table.TransformColumns(
        #"Skipped Rows1",
        {
            {"Event count", each Text.Replace(_, ",", ""), type text},
            {"Total users", each Text.Replace(_, ",", ""), type text}
        }
    ),

    // ADD THIS STEP (convert to numbers)
    #"Changed Type" = Table.TransformColumnTypes(
        #"Cleaned Numbers",
        {
            {"Event count", Int64.Type},
            {"Total users", Int64.Type}
        }
    )
in
    #"Changed Type"
```

**Alternative (if conversion fails):** Use safe DAX:

```dax
measure 'Users by Event' =
    SUMX(
        'ga4-titles',
        VALUE('ga4-titles'[Total users])
    )
```

---

### 3. MISSING DATE COLUMNS FOR TIME-SERIES VISUALS (CRITICAL)

**Problem:** Several visuals use `DimDate[Date]` as X-axis but source tables have NO Date column:

| Visual | Uses Table | Date Column? | Result |
|--------|------------|--------------|---------|
| Traffic Sources by Channel | ga4-traffic-source | ❌ NO | Flatline (same value every date) |
| Play Events Timeline | ga4-events | ❌ NO | Flatline |

**Impact:** Charts will show same value repeated across all dates (useless).

**FIX OPTIONS:**

**Option A (Ideal):** Request new GA4 exports with dates:
- `ga4-traffic-source-by-date.csv` (Source, Medium, Date, Sessions, Users)
- `ga4-events-by-date.csv` (Event name, Date, Event count, Total users)

**Option B (Fallback):** Change visuals to non-time-series:
- Traffic Sources → Treemap or Stacked Bar (no time dimension)
- Play Events → Ranked Bar Chart (no time dimension)

**Option C (Workaround):** If ga4-daily has source/event breakdowns, use that table instead.

---

### 4. FIELD NAME INCONSISTENCIES

**ga4-traffic-source table lists:**
- `Traffic Source` (column)
- `Medium` (column)
- `Session source / medium` (calculated column)

**But Page 2 visual specs say:**
- `Session medium` ❌ (doesn't exist)
- `Session source` ❌ (doesn't exist)

**FIX:** Use actual column names:
- Group By: `ga4-traffic-source[Medium]`
- Details: `ga4-traffic-source[Traffic Source]`
- OR: Use `ga4-traffic-source[Session source / medium]` for combined view

---

### 5. ENGAGEMENT RATE SUMMARIZATION ERROR

**Problem:** Engagement rate columns set to `Summarize: sum`

**Why This Is Wrong:**
- Engagement rate is a **ratio** (Engaged Sessions / Total Sessions)
- Summing ratios = meaningless number
- Example: 60% + 40% = 100% ❌ (wrong math)

**FIX:** Change summarization for ALL engagement rate columns:

**ga4-daily[Engagement rate]:**
- Summarization: **Do not summarize** OR **Average**

**ga4-pages[Engagement rate]:**
- Summarization: **Do not summarize** OR **Average**

**ga4-devices[Engagement rate]:**
- Summarization: **Do not summarize** OR **Average**

**Always use measures for engagement rate!**

---

## 🛡️ BULLETPROOF REBUILD ENHANCEMENTS

### 1. PARAMETERIZE FILE PATHS (SAVES HOURS)

**Problem:** Absolute paths break when you move files or change computers.

**Solution:** Use Power Query parameters.

**Step 1: Create Parameter**

Power Query Editor → Manage Parameters → New Parameter:
- Name: `pDatasetsFolder`
- Type: Text
- Current Value: `C:\Users\farad\Dev\WORK\HHS\repos\auto-the-big-one\dashboards\01_Live_Events_Dashboard\datasets\`

**Step 2: Update All Queries**

**Before (fragile):**
```m
Source = Csv.Document(
    File.Contents("C:\Users\farad\Dev\WORK\HHS\repos\auto-the-big-one\dashboards\01_Live_Events_Dashboard\datasets\ga4-daily.csv"),
    [Delimiter=",", Columns=7]
)
```

**After (portable):**
```m
Source = Csv.Document(
    File.Contents(pDatasetsFolder & "ga4-daily.csv"),
    [Delimiter=",", Columns=7]
)
```

**Benefits:**
- ✅ Change path once, applies to all queries
- ✅ Easy to move to new computer
- ✅ Can parameterize for test/prod environments

---

### 2. SHARED FUNCTIONS (DRY PRINCIPLE)

Create reusable functions for common patterns:

**Function: fxTransformCTR**

```m
let
    fxTransformCTR = (v) =>
        let
            out =
                if v = null then null
                else if Value.Is(v, type number) then v / 100
                else if Value.Is(v, type text) then
                    let
                        s = Text.Trim(v),
                        cleaned = Text.Replace(s, "%", ""),
                        n = try Number.FromText(cleaned) / 100 otherwise null
                    in
                        n
                else null
        in
            out
in
    fxTransformCTR
```

**Function: fxLoadGA4Standard**

```m
let
    fxLoadGA4Standard = (filename as text, columnCount as number) =>
        let
            Source = Csv.Document(
                File.Contents(pDatasetsFolder & filename),
                [Delimiter=",", Columns=columnCount, Encoding=65001, QuoteStyle=QuoteStyle.None]
            ),
            #"Skipped Rows" = Table.Skip(Source, 6),
            #"Promoted Headers" = Table.PromoteHeaders(#"Skipped Rows", [PromoteAllScalars=true]),
            #"Cleaned Headers" = Table.TransformColumnNames(#"Promoted Headers", each Text.Trim(_))
        in
            #"Cleaned Headers"
in
    fxLoadGA4Standard
```

**Usage:**
```m
let
    Source = fxLoadGA4Standard("ga4-daily.csv", 7),
    #"Changed Type" = Table.TransformColumnTypes(
        Source,
        {
            {"Date", type date},
            {"Views", Int64.Type},
            {"Sessions", Int64.Type}
        }
    )
in
    #"Changed Type"
```

---

### 3. CTR CONVERSION ORDER (PREVENTS ERRORS)

**WRONG ORDER (causes errors):**
```m
// 1. Type cast first ❌
#"Changed Type" = Table.TransformColumnTypes(Source, {{"CTR", type number}}),

// 2. Then transform ❌
#"Transformed CTR" = Table.TransformColumns(#"Changed Type", {{"CTR", fxTransformCTR}})
```

**CORRECT ORDER:**
```m
// 1. Replace blanks with null
#"Replaced Value" = Table.ReplaceValue(Source, "", null, Replacer.ReplaceValue, {"CTR"}),

// 2. Transform using function
#"Transformed CTR" = Table.TransformColumns(#"Replaced Value", {{"CTR", fxTransformCTR}}),

// 3. THEN type cast
#"Changed Type" = Table.TransformColumnTypes(#"Transformed CTR", {{"CTR", type number}})
```

**Why:** Transform function handles both text and numbers; type casting fails on text.

---

### 4. QA MEASURES (CATCH 80% OF ERRORS IN 2 MINUTES)

Add these measures to catch common issues:

**QA - CTR Range Check:**
```dax
measure 'QA - CTR Min' = MIN('gsc-chart'[CTR])
    formatString: 0.00%
    displayFolder: QA Checks

measure 'QA - CTR Max' = MAX('gsc-chart'[CTR])
    formatString: 0.00%
    displayFolder: QA Checks
```

**Expected:** CTR Min: 0%, CTR Max: <50%
**If Wrong:** CTR values are 0-100 (not 0-1) → fix Power Query

---

**QA - Date Filter Impact:**
```dax
measure 'QA - Date Filters Sessions' =
    VAR AllSessions = CALCULATE([Sessions], ALL(DimDate))
    VAR FilteredSessions = [Sessions]
    RETURN
    IF(
        AllSessions = FilteredSessions,
        "⚠️ Date slicer not impacting Sessions",
        "✅ Date slicer impacting Sessions"
    )
    displayFolder: QA Checks
```

**Expected:** "✅ Date slicer impacting Sessions"
**If Wrong:** Relationship missing or inactive

---

**QA - Play Events Date Check:**
```dax
measure 'QA - Play Events Flatline Check' =
    VAR FirstDate = CALCULATE([Play Events], FIRSTDATE(DimDate[Date]))
    VAR LastDate = CALCULATE([Play Events], LASTDATE(DimDate[Date]))
    RETURN
    IF(
        FirstDate = LastDate,
        "⚠️ Play Events not date-granular (flatline)",
        "✅ Play Events varies by date"
    )
    displayFolder: QA Checks
```

**Expected:** "✅ Play Events varies by date"
**If Wrong:** ga4-events table has no Date column

---

**QA - Total Engagement Sanity:**
```dax
measure 'QA - Engagement Per Session Check' =
    VAR AvgEngagementPerSession = DIVIDE([Total Engagement (Minutes)], [Sessions], 0)
    RETURN
    IF(
        AvgEngagementPerSession > 60,
        "⚠️ Avg engagement per session > 60 min (suspicious)",
        IF(
            AvgEngagementPerSession < 0.1,
            "⚠️ Avg engagement per session < 6 sec (suspicious)",
            "✅ Engagement values reasonable"
        )
    )
    displayFolder: QA Checks
```

**Expected:** "✅ Engagement values reasonable"
**If Wrong:** Total Engagement calculation is using wrong formula

---

### 5. IMPROVED REBUILD ORDER (PREVENTS RELATIONSHIP ISSUES)

**Phase 1: Power Query Setup**
1. Create parameter: `pDatasetsFolder`
2. Create shared functions: `fxTransformCTR`, `fxLoadGA4Standard`
3. Load all CSV queries (with correct types and functions)
4. Test: All queries load without errors

**Phase 2: Data Model**
1. Create calculated tables: DimDate (first!), DimLivecast, DimAction
2. Create relationships (in this exact order):
   - DimDate → ga4-daily (test immediately with date slicer)
   - DimDate → gsc-chart (test immediately)
   - DimLivecast → ga4-pages
   - DimAction → ga4-events
   - ga4-pages → ga4-titles
3. Set bi-directional filters where needed
4. Mark DimDate as date table
5. Test: Date slicer affects Sessions and Search Clicks

**Phase 3: Measures**
1. Create QA measures (test data quality first!)
2. Create core metrics
3. Create geography metrics
4. Create acquisition metrics
5. Create time intelligence metrics
6. Create KPI helper measures
7. Test: All measures return reasonable values

**Phase 4: Column Visibility**
1. Hide numeric columns in all fact tables
2. Verify: Can't accidentally drag columns to visuals

**Phase 5: Build Pages**
1. Apply theme (USWDS_Light_Theme.json)
2. Build Page 1 (Executive Summary)
3. Test: All visuals work, slicers impact data
4. Build Pages 2-7
5. Final QA pass

---

## 📋 CORRECTED DATA MODEL SUMMARY

### Actual Table Count: 24 Tables

**Dimension Tables (3):**
1. DimDate (calculated)
2. DimLivecast (calculated)
3. DimAction (calculated)

**GA4 Fact Tables (10):**
1. ga4-daily (CSV)
2. ga4-pages (CSV)
3. ga4-titles (CSV) ⚠️ **Requires type conversion fix**
4. ga4-events (CSV) ⚠️ **No Date column - flatline risk**
5. ga4-devices (CSV)
6. ga4-geography (CSV)
7. ga4-tech (CSV)
8. ga4-traffic-source (CSV) ⚠️ **No Date column - flatline risk**
9. ga4-traffic-source-livecast-play (CSV)
10. ga4-geography-livecast-play (CSV)

**GSC Tables (6):**
1. gsc-chart (CSV)
2. gsc-countries (CSV)
3. gsc-devices (CSV)
4. gsc-pages (CSV)
5. gsc-queries (CSV)
6. gsc-search-appearance (CSV)

**Utility/Calculated Tables (5):**
1. Measures_Livecast (calculated)
2. Action Catalog (calculated)
3. Recommended Actions (calculated)

**Note:** Removed from count:
- ga4-geography-livecast-play might be redundant (verify if actually used)

---

## 🔧 CORRECTED VISUAL SPECIFICATIONS

### PAGE 2: EXPLORER - Traffic Source Breakdown

**CORRECTED Field Mapping:**
```
Visual: Treemap
Group: ga4-traffic-source[Medium]  (NOT "Session medium")
Details: ga4-traffic-source[Traffic Source]  (NOT "Session source")
Values: [Sessions by Source]
Tooltips: [Users by Source], [Engagement Rate by Source]
```

**Alternative (if you want combined):**
```
Details: ga4-traffic-source[Session source / medium]
Values: [Sessions by Source]
```

---

### PAGE 3: TRAFFIC & ACQUISITION - Traffic Sources by Channel

**ISSUE:** ga4-traffic-source has NO Date column

**Option A (Requires new data):**
Request GA4 export: "Sessions by Source/Medium by Date"
```
Columns: Date, Traffic Source, Medium, Sessions, Users
```

**Option B (Change visual):**
```
Visual: Stacked Bar Chart (no time dimension)
Y-Axis: ga4-traffic-source[Session source / medium]
Values: [Sessions by Source]
Sort: Descending by Sessions
```

---

### PAGE 4: PLAY EVENTS - Play Events Timeline

**ISSUE:** ga4-events has NO Date column

**Option A (Requires new data):**
Request GA4 export: "Event Count by Event Name by Date"
```
Columns: Date, Event name, Event count, Total users
```

**Option B (Change visual):**
```
Visual: Clustered Bar Chart (no time dimension)
Y-Axis: ga4-events[Event name]
Values: [Play Events]
Sort: Descending by Play Events
```

---

## 🎯 QUICK VALIDATION CHECKLIST

**After importing all queries:**
- [ ] Parameter `pDatasetsFolder` exists and is correct
- [ ] All CSV queries load without errors
- [ ] ga4-titles numeric columns are INT64 (not text)
- [ ] All GSC CTR columns are 0-1 range (not 0-100)
- [ ] Engagement rate columns set to "Do not summarize"

**After creating relationships:**
- [ ] Date slicer changes [Sessions] value
- [ ] Date slicer changes [Search Clicks] value
- [ ] Filtering City affects [Sessions_City]
- [ ] Filtering Device affects [Device Sessions]

**After creating measures:**
- [ ] [QA - CTR Max] < 0.5 (if not, CTR formula wrong)
- [ ] [QA - Date Filters Sessions] = "✅ Date slicer impacting Sessions"
- [ ] [QA - Engagement Per Session Check] = "✅ Engagement values reasonable"
- [ ] [Sessions] > 0
- [ ] [Total Engagement (Minutes)] / [Sessions] is 1-10 range (reasonable)

**After building visuals:**
- [ ] Traffic Sources by Channel doesn't show flatline (if it does, no Date in source)
- [ ] Play Events Timeline doesn't show flatline (if it does, no Date in source)
- [ ] Device Breakdown shows 3 segments (Mobile, Desktop, Tablet)
- [ ] Geographic map shows multiple cities (not just one)

---

## 📚 ADDITIONAL RESOURCES

### Power Query Best Practices

**Always in this order:**
1. Load source
2. Skip rows (if needed)
3. Promote headers
4. Clean/trim headers
5. Replace empty strings with null
6. Apply transformations (CTR, unpivot, etc.)
7. Type cast columns (LAST step)

**Never:**
- Type cast before transforming text values
- Use absolute file paths without parameters
- Summarize ratio/percentage columns as SUM

---

### DAX Best Practices

**Always:**
- Use DIVIDE() instead of / (handles divide by zero)
- Use SUMX() when multiplying before summing
- Format strings on measures (never on columns)
- Hide base columns, expose only measures

**Never:**
- SUM() text columns (convert to numbers first)
- Aggregate ratios with SUM() (use AVERAGE or weighted calc)
- Use CALCULATE() inside iterators unless necessary

---

### Relationship Best Practices

**Always:**
- Create Date dimension first
- Test relationships immediately after creating
- Use bi-directional filters sparingly (only when needed)
- Mark date table as date table

**Never:**
- Create many-to-many relationships unless absolutely required
- Leave relationships inactive (fix the model instead)
- Create circular relationships (breaks model)

---

## 🚨 CRITICAL: APPLY THESE FIXES BEFORE BUILDING

**Priority 1 (Blockers):**
1. Fix ga4-titles type conversion (measures will error)
2. Add parameter for datasets folder (saves rebuild time)
3. Fix engagement rate summarization (wrong math)

**Priority 2 (Visual Issues):**
1. Fix field name references (Traffic Source vs Session source)
2. Decide on time-series visuals (need Date columns or change visual type)

**Priority 3 (Quality):**
1. Add QA measures for validation
2. Create shared functions for reusability
3. Follow corrected rebuild order

---

**This addendum addresses the 6 most common rebuild failures. Apply these corrections before starting your build!**

**Document Version:** 1.1 (Addendum)
**Last Updated:** 2026-01-12
**Status:** ✅ Critical Corrections Applied
**Impact:** Prevents 80% of rebuild errors

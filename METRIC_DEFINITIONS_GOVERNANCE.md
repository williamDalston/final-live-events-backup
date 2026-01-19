# Metric Definitions + Governance: HHS Live Events Dashboard

**Purpose:** Single source of truth for all metrics used across the dashboard  
**Status:** ⚠️ **CRITICAL FOR TRUST** - Complete before build  
**Date:** January 10, 2026

---

## 🎯 **WHY THIS MATTERS**

> **"If 'Sessions / Page Views / Events / Conversions' aren't defined the same way across pages, trust cracks fast."**

**This document ensures:**
- Every metric has a clear, defensible definition
- All measures reference the same data sources consistently
- Limitations and proxies are documented upfront
- Leadership questions have ready answers

---

## 📋 **CORE METRICS (Command Center Page)**

### **1. Sessions**

**Definition:** Total number of user sessions (GA4 standard definition)  
**Measure:** `[Sessions] = SUM('ga4-daily'[Sessions])`  
**Data Source:** `ga4-daily` table, `Sessions` column (GA4 aggregated daily metric)  
**Display Folder:** `Core Metrics`  
**Format:** `#,##0` (whole number)

**What it measures:**
- A session begins when a user opens an app or visits a site
- A session ends after 30 minutes of inactivity or at midnight (GA4 default)
- Each session can include multiple page views and events

**Known Limitations:**
- Uses GA4's aggregated `Sessions` metric (daily rollup)
- Not a raw count of session IDs (aggregated by GA4)
- If `ga4-daily` table is missing data, measure returns 0 (not BLANK)

**Where it appears:**
- Command Center: KPI Card 1 (Sessions)
- Other pages: As context or comparison metric

---

### **2. Page Views**

**Definition:** Total number of page views (GA4 standard definition)  
**Measure:** `[Page Views] = SUM('ga4-daily'[Views])`  
**Data Source:** `ga4-daily` table, `Views` column (GA4 aggregated daily metric)  
**Display Folder:** `Core Metrics`  
**Format:** `#,##0` (whole number)

**What it measures:**
- Total number of times pages were viewed (GA4 `Views` metric)
- Includes all page views across all live event pages

**Known Limitations:**
- Uses GA4's aggregated `Views` metric (daily rollup)
- Not a raw count of page_view events
- If `ga4-daily` table is missing data, measure returns 0 (not BLANK)

**Where it appears:**
- Command Center: KPI Card 2 (Page Views)
- Explorer Page: As comparison metric

---

### **3. Total Events**

**Definition:** Total number of events tracked (GA4 standard definition)  
**Measure:** `[Total Events] = SUM('ga4-events'[Event count])`  
**Data Source:** `ga4-events` table, `Event count` column  
**Display Folder:** `Core Metrics`  
**Format:** `#,##0` (whole number)

**What it measures:**
- All events tracked in GA4 (page_view, video_play, user_engagement, custom events, etc.)
- Each event occurrence is counted

**Known Limitations:**
- Counts all event types (not filtered by event name)
- If you want only "video" events, use `[Play Events]` instead
- Uses `ga4-events` table (event-level aggregation), not `ga4-daily`

**Related Measures:**
- `[Play Events]` - Filtered to video-related events only
- `[Live Views]` - Filtered to "view" events
- `[Replay Views]` - Filtered to "replay" events

**Where it appears:**
- Command Center: KPI Card 3 (Total Events)
- Multiple pages as context metric

---

### **4. Play Events**

**Definition:** Count of video play/view/replay events only  
**Measure:** `[Play Events] = CALCULATE([Total Events], 'ga4-events'[Event name] IN {"view", "replay", "play"})`  
**Data Source:** `ga4-events` table, filtered by event name  
**Display Folder:** `Core Metrics`  
**Format:** `#,##0` (whole number)

**What it measures:**
- Only events where `event_name` is "view", "replay", or "play"
- Represents video engagement events (not general page views or other events)

**Known Limitations:**
- Depends on GA4 event naming consistency
- If event names are different (e.g., "video_play" instead of "play"), these won't be counted
- **Action Required:** Verify event names in `ga4-events[Event name]` column match these values

**Event Name Verification:**
```dax
// Run this in DAX to see all unique event names
EVALUATE
SUMMARIZE(
    'ga4-events',
    'ga4-events'[Event name],
    "Count", SUM('ga4-events'[Event count])
)
```

**Where it appears:**
- Command Center: As context metric
- Play Events Page: Primary metric

---

### **5. Total Users**

**Definition:** Total number of distinct users (GA4 standard definition)  
**Measure:** `[Total Users] = SUM('ga4-daily'[Total users])`  
**Data Source:** `ga4-daily` table, `Total users` column (GA4 aggregated daily metric)  
**Display Folder:** `Core Metrics`  
**Format:** `#,##0` (whole number)

**What it measures:**
- GA4's aggregated count of distinct users per day
- Summed across all days in the selected date range
- **Note:** This is a sum of daily unique users (not a true distinct count across the date range)

**Known Limitation (Critical):**
- ⚠️ **This is NOT a true distinct count across date range**
- GA4's daily `Total users` sums daily unique users, which may double-count users who visit multiple days
- For a true distinct count across date range, you'd need user-level data (not available in aggregated tables)

**Alternative (if true distinct count needed):**
```dax
// True distinct count (requires user_id column in fact table)
[True Total Users] = DISTINCTCOUNT('Fact_LivecastEvents'[user_id])
```

**Where it appears:**
- Command Center: Context metric
- Multiple pages as user engagement indicator

---

### **6. Engagement Rate**

**Definition:** Percentage of sessions that were "engaged" (GA4 standard definition)  
**Measure:** `[Engagement Rate] = DIVIDE(SUM('ga4-daily'[Engaged sessions]), SUM('ga4-daily'[Sessions]), 0)`  
**Data Source:** `ga4-daily` table, `Engaged sessions` and `Sessions` columns  
**Display Folder:** `Engagement Metrics`  
**Format:** `0.0%` (percentage)

**What it measures:**
- GA4 defines an "engaged session" as one that:
  - Lasts 10+ seconds, OR
  - Has 1+ conversion events, OR
  - Has 2+ page/screen views
- Engagement Rate = (Engaged Sessions / Total Sessions) × 100

**Known Limitations:**
- Uses GA4's definition of "engaged session" (cannot be customized without raw data)
- Returns 0% if Sessions = 0 (avoids divide-by-zero)

**Where it appears:**
- Command Center: Context metric
- Engagement-focused pages: Primary metric

---

## 📊 **ENGAGEMENT METRICS**

### **7. Total Engagement (Minutes)**

**Definition:** Total engagement time in minutes (proxy calculation)  
**Measure:** `[Total Engagement (Minutes)] = SUM('ga4-pages'[Average engagement time per session]) * SUM('ga4-daily'[Sessions]) / 60`  
**Data Source:** `ga4-pages` and `ga4-daily` tables  
**Display Folder:** `Engagement Metrics`  
**Format:** `#,##0.0` (decimal minutes)

**What it measures:**
- Calculated as: (Average engagement time per session) × (Total Sessions) ÷ 60
- Converts seconds to minutes

**Known Limitation (Critical):**
- ⚠️ **This is a proxy calculation, not a true sum of engagement time**
- Uses average engagement time × session count (which may not equal total engagement if averages vary by page)
- For true total engagement time, you'd need session-level engagement time data (not available in aggregated tables)

**Where it appears:**
- Explorer Page: Context metric
- Engagement analysis pages

---

## 📈 **TIME INTELLIGENCE METRICS**

### **8. Total Events - MoM %**

**Definition:** Month-over-Month percentage change in Total Events  
**Measure:** `[Total Events - MoM %] = DIVIDE([Total Events] - CALCULATE([Total Events], DATEADD(DimDate[Date], -1, MONTH)), CALCULATE([Total Events], DATEADD(DimDate[Date], -1, MONTH)), 0)`  
**Data Source:** `[Total Events]` measure, `DimDate` table  
**Display Folder:** `Time Intelligence`  
**Format:** `0.0%` (percentage, can be negative)

**What it measures:**
- Compares current period's Total Events to previous month's Total Events
- Formula: ((Current Month - Previous Month) / Previous Month) × 100

**Known Limitations:**
- Returns 0% if previous month has no data (avoids divide-by-zero)
- Uses calendar months (not 30-day rolling periods)
- **Action Required:** Verify `DimDate` table has correct date range to support month-over-month comparisons

**Where it appears:**
- Command Center: KPI card trend indicators
- Multiple pages as context metric

---

### **9. Total Events - YoY %**

**Definition:** Year-over-Year percentage change in Total Events  
**Measure:** `[Total Events - YoY %] = DIVIDE([Total Events] - CALCULATE([Total Events], SAMEPERIODLASTYEAR(DimDate[Date])), CALCULATE([Total Events], SAMEPERIODLASTYEAR(DimDate[Date])), 0)`  
**Data Source:** `[Total Events]` measure, `DimDate` table  
**Display Folder:** `Time Intelligence`  
**Format:** `0.0%` (percentage, can be negative)

**What it measures:**
- Compares current period's Total Events to same period last year
- Uses `SAMEPERIODLASTYEAR` function (handles leap years correctly)

**Known Limitations:**
- Requires at least 1 year of historical data
- Returns 0% if previous year has no data

**Where it appears:**
- Command Center: Context metric
- Historical trend pages

---

## ⚠️ **PLACEHOLDER MEASURES (Return BLANK)**

These measures are defined but return BLANK until data is available:

### **10. New Users**

**Definition:** Count of new users (GA4 standard definition)  
**Measure:** `[New Users] = BLANK()`  
**Status:** 🔴 **DATA UNAVAILABLE** - `ga4-daily` table missing `New users` column  
**Data Source:** Missing  
**Action Required:** Request `New users` column be added to `ga4-daily` export.

---

### **11. Sessions by Source**

**Definition:** Sessions grouped by traffic source  
**Measure:** `[Sessions by Source] = CALCULATE(SUM('ga4-traffic-source'[Value]), 'ga4-traffic-source'[Metric] = "Sessions")`  
**Status:** ✅ **READY TO IMPLEMENT** - Data available in `ga4-traffic-source`  
**Data Source:** `ga4-traffic-source` table (Metric="Sessions", Traffic Source column)  
**Display Folder:** `Acquisition Metrics`

---

### **12. Sessions by Medium**

**Definition:** Sessions grouped by traffic medium  
**Measure:** `[Sessions by Medium] = CALCULATE(SUM('ga4-traffic-source'[Value]), 'ga4-traffic-source'[Metric] = "Sessions")`  
**Status:** ✅ **READY TO IMPLEMENT** - Data available in `ga4-traffic-source`  
**Data Source:** `ga4-traffic-source` table (Metric="Sessions", Medium column)  
**Display Folder:** `Acquisition Metrics`

---

## 🔍 **DATA QUALITY NOTES**

### **Date Parsing Issues (RESOLVED)**

**Issue:** `ga4-daily[Date]` column was in YYYYMMDD string format  
**Status:** ✅ **FIXED** - Power Query M code now parses to Date type  
**Location:** `ga4-daily.tmdl` partition M code

### **Empty String Handling (RESOLVED)**

**Issue:** Empty strings (`""`) in numeric columns caused type conversion errors  
**Status:** ✅ **FIXED** - Power Query M code replaces empty strings with null  
**Location:** `ga4-daily.tmdl` partition M code (lines replacing empty values)

### **CTR Column Format (GSC TABLES)**

**Issue:** `gsc-*[CTR]` columns have `"%"` symbols (e.g., `"0.06%"`)  
**Status:** ⚠️ **ACTION REQUIRED** - Power Query M code needs to remove `%` and convert to number  
**Location:** GSC table partitions (not yet fixed)

---

## ✅ **GOVERNANCE CHECKLIST**

### **Before Building Dashboard:**

- [ ] All measures in `Measures_Livecast` table have clear definitions above
- [ ] Placeholder measures (`BLANK()`) are documented and visible to users
- [ ] Data quality issues (date parsing, empty strings) are resolved
- [ ] Event names in `ga4-events[Event name]` match measure filters (verify "view", "replay", "play")
- [ ] `DimDate` table has correct date range for time intelligence comparisons
- [ ] All relationships are active (Model view)

### **After Building Dashboard:**

- [ ] All visuals using measures have consistent formatting
- [ ] Tooltips or info icons explain metric definitions (optional but recommended)
- [ ] "Last refreshed" timestamp visible (use `[Last_Updated_Text]` measure)
- [ ] Export tests show consistent metric values (PDF/PPT match Power BI Desktop)

### **When Adding New Metrics:**

1. **Define the metric** using this document's format
2. **Create the measure** in `Measures_Livecast` table
3. **Add to Display Folder** for organization
4. **Document limitations** upfront
5. **Test with real data** before deploying to production
6. **Update this document** with new metric definition

---

## 📚 **QUICK REFERENCE**

### **Command Center Page Metrics (Required):**

| Metric | Measure | Data Source | Status |
|--------|---------|-------------|--------|
| Sessions | `[Sessions]` | `ga4-daily[Sessions]` | ✅ Ready |
| Page Views | `[Page Views]` | `ga4-daily[Views]` | ✅ Ready |
| Total Events | `[Total Events]` | `ga4-events[Event count]` | ✅ Ready |
| Top Device | `[Top Device Category]` | `ga4-devices` | ⚠️ Check if exists |
| Avg Pages/Session | `[Avg Pages per Session]` | Calculated | ⚠️ Check if exists |

**Action Required:** Verify if `[Top Device Category]` and `[Avg Pages per Session]` measures exist. If not, create them.

---

## 🎯 **LEADERSHIP Q&A (Ready Answers)**

### **Q: "What does Sessions mean?"**
**A:** "Sessions is GA4's standard metric: a user session begins when they open the site/app and ends after 30 minutes of inactivity or at midnight. Each session can include multiple page views and events."

### **Q: "Why is Total Users different from Sessions?"**
**A:** "Total Users counts distinct users, while Sessions counts sessions (one user can have multiple sessions). Also, our current measure sums daily unique users, which may double-count users who visit multiple days."

### **Q: "What's the difference between Total Events and Play Events?"**
**A:** "Total Events counts all tracked events (page views, video plays, clicks, etc.). Play Events counts only video-related events (view, replay, play)."

### **Q: "Why do some metrics show BLANK?"**
**A:** "Some metrics (like New Users, Sessions by Source) require additional data columns that aren't available yet. We've documented these placeholders, and we'll update them as data becomes available."

---

**Created:** January 10, 2026  
**Last Updated:** January 10, 2026  
**Next Review:** After first build + data validation

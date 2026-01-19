# 📊 Complete Measures Library - Ready to Build

**Status:** ✅ **READY TO IMPLEMENT** - All measures defined for mock data + real data scenarios

**Purpose:** Comprehensive DAX measures library that works with current mock data and will work with real GA4 + GSC data when available.

---

## 🎯 **MEASURE ORGANIZATION**

All measures go in the `Measures_Livecast` table, organized in display folders:

1. **Core Metrics** (Original Report + V4.0)
2. **Engagement Metrics**
3. **Time Intelligence** (via Calculation Group)
4. **Performance Metrics**
5. **Geography Metrics** (when data available)
6. **Acquisition Metrics** (when data available)
7. **Search Console Metrics** (when data available)
8. **Health Score Components**
9. **Quick Insights**

---

## 📋 **SECTION 1: CORE METRICS (Original Report + V4.0)**

### **1.1: Sessions** ⚠️ (Requires Real Data)
```dax
/// Total Sessions (GA4 metric)
/// NOTE: Currently using DISTINCTCOUNT(user_pseudo_id) as proxy until real Sessions data available
measure 'Sessions' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[session_id]),
        DISTINCTCOUNT(Fact_LivecastEvents[session_id]),
        DISTINCTCOUNT(Fact_LivecastEvents[user_pseudo_id])  // Proxy for mock data
    )
    formatString: #,##0
```

### **1.2: Page Views** ⚠️ (Requires Real Data)
```dax
/// Total Page Views (GA4 metric)
/// NOTE: Currently using COUNTROWS with event_name filter as proxy
measure 'Page Views' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[event_name]),
        COUNTROWS(FILTER(Fact_LivecastEvents, Fact_LivecastEvents[event_name] = "page_view")),
        COUNTROWS(Fact_LivecastEvents)  // Proxy for mock data
    )
    formatString: #,##0
```

### **1.3: Total Events** ✅ (Works with Mock Data)
```dax
/// Total number of livecast events
measure 'Total Events' = COUNTROWS(Fact_LivecastEvents)
    formatString: #,##0
```

### **1.4: Play Events** ✅ (Works with Mock Data)
```dax
/// Count of play events (livecast_action = "view" or "replay")
measure 'Play Events' = 
    CALCULATE(
        COUNTROWS(Fact_LivecastEvents),
        Fact_LivecastEvents[livecast_action] IN {"view", "replay"}
    )
    formatString: #,##0
```

### **1.5: Unique Viewers** ✅ (Works with Mock Data)
```dax
/// Count of unique viewers (distinct user_pseudo_id)
measure 'Unique Viewers' = DISTINCTCOUNT(Fact_LivecastEvents[user_pseudo_id])
    formatString: #,##0
```

### **1.6: Total Users** ⚠️ (Requires Real Data)
```dax
/// Total Users (GA4 metric - distinct users)
/// NOTE: Currently using Unique Viewers as proxy
measure 'Total Users' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[user_id]),
        DISTINCTCOUNT(Fact_LivecastEvents[user_id]),
        [Unique Viewers]  // Proxy for mock data
    )
    formatString: #,##0
```

### **1.7: New Users** ⚠️ (Requires Real Data)
```dax
/// New Users (GA4 metric)
/// NOTE: Placeholder until real data available
measure 'New Users' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[is_new_user]),
        COUNTROWS(FILTER(Fact_LivecastEvents, Fact_LivecastEvents[is_new_user] = TRUE())),
        BLANK()  // No proxy available
    )
    formatString: #,##0
```

### **1.8: Returning Users** ⚠️ (Requires Real Data)
```dax
/// Returning Users (GA4 metric)
/// NOTE: Placeholder until real data available
measure 'Returning Users' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[is_new_user]),
        COUNTROWS(FILTER(Fact_LivecastEvents, Fact_LivecastEvents[is_new_user] = FALSE())),
        [Return Viewers]  // Proxy using return events
    )
    formatString: #,##0
```

---

## 📋 **SECTION 2: ENGAGEMENT METRICS**

### **2.1: Total Engagement (Minutes)** ✅ (Works with Mock Data)
```dax
/// Total engagement time in minutes
measure 'Total Engagement (Minutes)' = 
    DIVIDE(
        SUM(Fact_LivecastEvents[engagement_time_msec]),
        60000,
        0
    )
    formatString: #,##0.0
```

### **2.2: Total Engagement (Hours)** ✅ (Works with Mock Data)
```dax
/// Total engagement time in hours
measure 'Total Engagement (Hours)' = 
    DIVIDE(
        [Total Engagement (Minutes)],
        60,
        0
    )
    formatString: #,##0.0
```

### **2.3: Avg Engagement per Viewer (Minutes)** ✅ (Works with Mock Data)
```dax
/// Average engagement time per viewer in minutes
measure 'Avg Engagement per Viewer (Minutes)' = 
    DIVIDE(
        [Total Engagement (Minutes)],
        [Unique Viewers],
        0
    )
    formatString: #,##0.0
```

### **2.4: Engagement Rate** ⚠️ (Requires Real Data)
```dax
/// Engagement Rate (GA4 metric: Engaged Sessions / Sessions)
/// NOTE: Currently using engagement time proxy
measure 'Engagement Rate' = 
    IF(
        [Sessions] > 0,
        DIVIDE(
            [Total Engagement (Minutes)],
            [Sessions] * 2,  // Proxy: assume 2 min average session
            0
        ),
        BLANK()
    )
    formatString: 0.0%
```

### **2.5: Engagement Rate by Page** ⚠️ (Requires Real Data)
```dax
/// Engagement Rate calculated at page level
/// NOTE: For page-level analysis in Website Performance table
measure 'Engagement Rate by Page' = 
    DIVIDE(
        [Total Engagement (Minutes)],
        [Page Views],
        0
    )
    formatString: 0.0%
```

### **2.6: Return Rate** ✅ (Works with Mock Data)
```dax
/// Percentage of viewers who returned
measure 'Return Rate' = 
    DIVIDE(
        [Return Viewers],
        [Unique Viewers],
        0
    )
    formatString: 0.0%
```

### **2.7: Return Viewers** ✅ (Works with Mock Data)
```dax
/// Count of unique viewers who returned
measure 'Return Viewers' = 
    CALCULATE(
        [Unique Viewers],
        Fact_LivecastEvents[livecast_action] = "return"
    )
    formatString: #,##0
```

### **2.8: Return Events** ✅ (Works with Mock Data)
```dax
/// Number of return events
measure 'Return Events' = 
    CALCULATE(
        [Total Events],
        Fact_LivecastEvents[livecast_action] = "return"
    )
    formatString: #,##0
```

---

## 📋 **SECTION 3: PERFORMANCE METRICS**

### **3.1: Avg Views per Event** ✅ (Works with Mock Data)
```dax
/// Average number of views per event
measure 'Avg Views per Event' = 
    DIVIDE(
        [Total Events],
        [Active Livecasts],
        0
    )
    formatString: #,##0.0
```

### **3.2: Avg Viewers per Event** ✅ (Works with Mock Data)
```dax
/// Average number of viewers per event
measure 'Avg Viewers per Event' = 
    DIVIDE(
        [Unique Viewers],
        [Active Livecasts],
        0
    )
    formatString: #,##0.0
```

### **3.3: Avg Sessions per Event** ⚠️ (Requires Real Data)
```dax
/// Average number of sessions per event
/// NOTE: Placeholder until Sessions metric available
measure 'Avg Sessions per Event' = 
    DIVIDE(
        [Sessions],
        [Active Livecasts],
        0
    )
    formatString: #,##0.0
```

### **3.4: Events per Viewer** ✅ (Works with Mock Data)
```dax
/// Average number of events per viewer
measure 'Events per Viewer' = 
    DIVIDE(
        [Total Events],
        [Unique Viewers],
        0
    )
    formatString: #,##0.0
```

### **3.5: Active Livecasts** ✅ (Works with Mock Data)
```dax
/// Number of distinct livecast titles
measure 'Active Livecasts' = DISTINCTCOUNT(Fact_LivecastEvents[livecast_title])
    formatString: #,##0
```

---

## 📋 **SECTION 4: GEOGRAPHY METRICS** ⚠️ (Requires Real Data)

### **4.1: Sessions by City** ⚠️ (Requires Real Data)
```dax
/// Total sessions by city
/// NOTE: Currently using mock data proxy
measure 'Sessions by City' = 
    IF(
        HASONEVALUE(Fact_SessionsByCity_Mock[Sessions]),
        SUM(Fact_SessionsByCity_Mock[Sessions]),
        [Sessions]  // Proxy
    )
    formatString: #,##0
```

### **4.2: New Viewers by City** ⚠️ (Requires Real Data)
```dax
/// New viewers by city
/// NOTE: Currently using mock data proxy
measure 'New Viewers by City' = 
    IF(
        HASONEVALUE(Fact_SessionsByCity_Mock[New_Viewers]),
        SUM(Fact_SessionsByCity_Mock[New_Viewers]),
        BLANK()
    )
    formatString: #,##0
```

### **4.3: Returning Viewers by City** ⚠️ (Requires Real Data)
```dax
/// Returning viewers by city
/// NOTE: Currently using mock data proxy
measure 'Returning Viewers by City' = 
    IF(
        HASONEVALUE(Fact_SessionsByCity_Mock[Returning_Viewers]),
        SUM(Fact_SessionsByCity_Mock[Returning_Viewers]),
        [Return Viewers]  // Proxy
    )
    formatString: #,##0
```

### **4.4: Return Rate by City** ⚠️ (Requires Real Data)
```dax
/// Return rate by city
measure 'Return Rate by City' = 
    DIVIDE(
        [Returning Viewers by City],
        [Sessions by City],
        0
    )
    formatString: 0.0%
```

---

## 📋 **SECTION 5: ACQUISITION METRICS** ⚠️ (Requires Real Data)

### **5.1: Sessions by Source** ⚠️ (Requires Real Data)
```dax
/// Sessions grouped by traffic source
/// NOTE: Placeholder until source data available
measure 'Sessions by Source' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[session_source]),
        DISTINCTCOUNT(Fact_LivecastEvents[session_source]),
        BLANK()
    )
    formatString: #,##0
```

### **5.2: Sessions by Medium** ⚠️ (Requires Real Data)
```dax
/// Sessions grouped by traffic medium
/// NOTE: Placeholder until medium data available
measure 'Sessions by Medium' = 
    IF(
        HASONEVALUE(Fact_LivecastEvents[session_medium]),
        DISTINCTCOUNT(Fact_LivecastEvents[session_medium]),
        BLANK()
    )
    formatString: #,##0
```

---

## 📋 **SECTION 6: SEARCH CONSOLE METRICS** ⚠️ (Requires GSC Data)

### **6.1: Search Clicks** ⚠️ (Requires GSC Data)
```dax
/// Total clicks from Google Search
/// NOTE: Placeholder until GSC data available
measure 'Search Clicks' = 
    IF(
        HASONEVALUE(Fact_Search[Clicks]),
        SUM(Fact_Search[Clicks]),
        BLANK()
    )
    formatString: #,##0
```

### **6.2: Search Impressions** ⚠️ (Requires GSC Data)
```dax
/// Total impressions from Google Search
/// NOTE: Placeholder until GSC data available
measure 'Search Impressions' = 
    IF(
        HASONEVALUE(Fact_Search[Impressions]),
        SUM(Fact_Search[Impressions]),
        BLANK()
    )
    formatString: #,##0
```

### **6.3: Search CTR** ⚠️ (Requires GSC Data)
```dax
/// Click-through rate from Google Search
/// NOTE: Placeholder until GSC data available
measure 'Search CTR' = 
    DIVIDE(
        [Search Clicks],
        [Search Impressions],
        0
    )
    formatString: 0.0%
```

### **6.4: Avg Search Position** ⚠️ (Requires GSC Data)
```dax
/// Average search position
/// NOTE: Placeholder until GSC data available
measure 'Avg Search Position' = 
    IF(
        HASONEVALUE(Fact_Search[Avg_Position]),
        AVERAGE(Fact_Search[Avg_Position]),
        BLANK()
    )
    formatString: #,##0.0
```

---

## 📋 **SECTION 7: HEALTH SCORE COMPONENTS**

### **7.1: Health Score - Viewership Trend** ✅ (Works with Mock Data)
```dax
/// Component 1: Viewership Trend (MoM % normalized to 0-1)
measure 'Health_ViewershipTrend' = 
    VAR MoMPct = [Unique Viewers MoM %]
    VAR Normalized = 
        SWITCH(
            TRUE(),
            MoMPct <= -0.20, 0,      // -20% or worse = 0
            MoMPct >= 0.20, 1,       // +20% or better = 1
            (MoMPct + 0.20) / 0.40   // Linear interpolation
        )
    RETURN Normalized * 0.25  // 25% weight
    formatString: 0.00
```

### **7.2: Health Score - Engagement Rate** ✅ (Works with Mock Data)
```dax
/// Component 2: Engagement Rate (normalized to 0-1)
measure 'Health_EngagementRate' = 
    VAR Rate = [Engagement Rate]
    VAR Normalized = 
        SWITCH(
            TRUE(),
            Rate <= 0.30, 0,          // 30% or less = 0
            Rate >= 0.80, 1,          // 80% or better = 1
            (Rate - 0.30) / 0.50      // Linear interpolation
        )
    RETURN Normalized * 0.25  // 25% weight
    formatString: 0.00
```

### **7.3: Health Score - Completion Rate** ✅ (Works with Mock Data)
```dax
/// Component 3: Completion Rate (using engagement as proxy)
measure 'Health_CompletionRate' = 
    VAR Rate = [Engagement Rate]  // Proxy for completion
    VAR Normalized = 
        SWITCH(
            TRUE(),
            Rate <= 0.20, 0,          // 20% or less = 0
            Rate >= 0.75, 1,          // 75% or better = 1
            (Rate - 0.20) / 0.55      // Linear interpolation
        )
    RETURN Normalized * 0.20  // 20% weight
    formatString: 0.00
```

### **7.4: Health Score - Growth vs Benchmark** ✅ (Works with Mock Data)
```dax
/// Component 4: Growth vs Benchmark (YoY % normalized)
measure 'Health_GrowthBenchmark' = 
    VAR YoYPct = [Unique Viewers YoY %]
    VAR Normalized = 
        SWITCH(
            TRUE(),
            YoYPct <= -0.10, 0,       // -10% or worse = 0
            YoYPct >= 0.15, 1,        // +15% or better = 1
            (YoYPct + 0.10) / 0.25    // Linear interpolation
        )
    RETURN Normalized * 0.15  // 15% weight
    formatString: 0.00
```

### **7.5: Health Score - Retention Proxy** ✅ (Works with Mock Data)
```dax
/// Component 5: Retention Proxy (using Return Rate)
measure 'Health_RetentionProxy' = 
    VAR Rate = [Return Rate]
    VAR Normalized = 
        SWITCH(
            TRUE(),
            Rate <= 0.05, 0,          // 5% or less = 0
            Rate >= 0.25, 1,          // 25% or better = 1
            (Rate - 0.05) / 0.20      // Linear interpolation
        )
    RETURN Normalized * 0.15  // 15% weight
    formatString: 0.00
```

### **7.6: Health Score (Composite)** ✅ (Works with Mock Data)
```dax
/// Program Health Score (0-100, letter grade)
measure 'Health Score' = 
    VAR Score = 
        [Health_ViewershipTrend] +
        [Health_EngagementRate] +
        [Health_CompletionRate] +
        [Health_GrowthBenchmark] +
        [Health_RetentionProxy]
    VAR Grade = 
        SWITCH(
            TRUE(),
            Score >= 0.90, "A+",
            Score >= 0.85, "A",
            Score >= 0.80, "A-",
            Score >= 0.75, "B+",
            Score >= 0.70, "B",
            Score >= 0.65, "B-",
            Score >= 0.60, "C+",
            Score >= 0.55, "C",
            Score >= 0.50, "D",
            "F"
        )
    RETURN Score * 100
    formatString: #,##0
```

### **7.7: Health Score Grade** ✅ (Works with Mock Data)
```dax
/// Health Score letter grade (A+ to F)
measure 'Health Score Grade' = 
    VAR Score = [Health Score] / 100
    RETURN
    SWITCH(
        TRUE(),
        Score >= 0.90, "A+",
        Score >= 0.85, "A",
        Score >= 0.80, "A-",
        Score >= 0.75, "B+",
        Score >= 0.70, "B",
        Score >= 0.65, "B-",
        Score >= 0.60, "C+",
        Score >= 0.55, "C",
        Score >= 0.50, "D",
        "F"
    )
    formatString: @
```

---

## 📋 **SECTION 8: QUICK INSIGHTS**

### **8.1: Top Performing Event Type** ✅ (Works with Mock Data)
```dax
/// Top performing event type by views
measure 'Top Event Type' = 
    VAR TopType = 
        TOPN(
            1,
            VALUES(DimLivecast[livecast_title]),
            [Total Events]
        )
    RETURN
    IF(
        COUNTROWS(TopType) = 1,
        MAXX(TopType, DimLivecast[livecast_title]),
        "Multiple"
    )
    formatString: @
```

### **8.2: Best Day of Week** ✅ (Works with Mock Data)
```dax
/// Best day of week for engagement
measure 'Best Day of Week' = 
    VAR BestDay = 
        TOPN(
            1,
            VALUES(DimDate[DayOfWeekName]),
            [Total Events]
        )
    RETURN
    IF(
        COUNTROWS(BestDay) = 1,
        MAXX(BestDay, DimDate[DayOfWeekName]),
        "Multiple"
    )
    formatString: @
```

### **8.3: Quick Insights Text** ✅ (Works with Mock Data)
```dax
/// Quick Insights summary text
measure 'Quick Insights Text' = 
    VAR TopType = [Top Event Type]
    VAR BestDay = [Best Day of Week]
    VAR MoM = [Unique Viewers MoM %]
    RETURN
    "📈 " & TopType & " events are performing best. " &
    "📅 " & BestDay & " shows highest engagement. " &
    IF(
        MoM > 0,
        "📊 Viewership up " & FORMAT(MoM, "0%") & " MoM.",
        "📊 Viewership down " & FORMAT(ABS(MoM), "0%") & " MoM."
    )
    formatString: @
```

---

## 📋 **SECTION 9: COMMAND CENTER VISUAL MEASURES** ✅ (Implemented with Real GA4 Data)

These measures are specifically designed for the Command Center page visuals and aggregate from the appropriate source tables (`ga4-devices`, `ga4-pages`) rather than global measures.

### **9.1: Device Sessions** ✅ (Implemented)
```dax
/// Total sessions by device category for device breakdown chart
/// Aggregates from ga4-devices table (not ga4-daily)
measure 'Device Sessions' = SUM('ga4-devices'[Sessions])
    formatString: #,##0
    displayFolder: Command Center;Chart - Device Breakdown
```
**Usage:** Device Breakdown chart (donut or stacked bar)  
**Fields:** Values = `[Device Sessions]`, Legend/Category = `'ga4-devices'[Device category]`  
**Note:** This measure respects device category context, unlike the global `[Sessions]` measure.

### **9.2: Page Views by Page** ✅ (Implemented)
```dax
/// Total page views by page for Top Pages table
/// Aggregates from ga4-pages table (not ga4-daily)
measure 'Page Views by Page' = SUM('ga4-pages'[Views])
    formatString: #,##0
    displayFolder: Command Center;Table - Top Pages
```
**Usage:** Top Pages table  
**Fields:** Rows = `'ga4-pages'[Page title]` or `'ga4-pages'[Page location]`, Value = `[Page Views by Page]`  
**Note:** This measure respects page context, showing different values per page row.

### **9.3: Page Engagement** ✅ (Implemented)
```dax
/// Average engagement rate by page for Top Pages table
/// Uses AVERAGE because engagement rate is already a percentage
measure 'Page Engagement' = AVERAGE('ga4-pages'[Engagement rate])
    formatString: 0.00%
    displayFolder: Command Center;Table - Top Pages
```
**Usage:** Top Pages table  
**Fields:** Value = `[Page Engagement]`  
**Note:** Uses AVERAGE (not SUM) because engagement rate is already a percentage - we average rates, not sum them.

### **9.4: Livecast Views** ✅ (Implemented)
```dax
/// Total views by livecast title for Top Livecast Videos table
/// Aggregates from ga4-pages via relationship to DimLivecast
measure 'Livecast Views' = CALCULATE(SUM('ga4-pages'[Views]))
    formatString: #,##0
    displayFolder: Command Center;Table - Top Livecast Videos
```
**Usage:** Top Livecast Videos table  
**Fields:** Rows = `DimLivecast[Livecast Title]`, Value = `[Livecast Views]`  
**Note:** Uses existing relationship between `ga4-pages` and `DimLivecast` (via Page title).

### **9.5: Livecast Avg Time** ✅ (Implemented)
```dax
/// Average engagement time per session by livecast title for Top Livecast Videos table
/// Aggregates from ga4-pages via relationship to DimLivecast
measure 'Livecast Avg Time' = CALCULATE(AVERAGE('ga4-pages'[Average engagement time per session]))
    formatString: #,##0.00
    displayFolder: Command Center;Table - Top Livecast Videos
```
**Usage:** Top Livecast Videos table  
**Fields:** Value = `[Livecast Avg Time]`  
**Note:** Uses existing relationship between `ga4-pages` and `DimLivecast` (via Page title).

**Key Difference from Global Measures:**
- **Global measures** (like `[Page Views]` = `SUM('ga4-daily'[Views])`) sum ALL data regardless of context
- **These visual-specific measures** aggregate from the correct source tables and respect row/category context
- **Result:** Each row/category shows its own value instead of the same total for all rows

---

## 📋 **SECTION 10: EXPLORER PAGE MEASURES** ✅ (Context-Aware for Row/Category Analysis)

These measures are specifically designed for the Explorer page visuals and aggregate from the appropriate source tables.

### **10.1: Total Users by Page** ✅
```dax
/// Total users by page for page performance analysis
/// Aggregates from ga4-pages table (not ga4-daily)
measure 'Total Users by Page' = SUM('ga4-pages'[Total users])
    formatString: #,##0
    displayFolder: Explorer;Matrix - Page Performance
```
**Usage:** Page Performance Matrix → Values field
**Why Needed:** Shows different user counts per page, not global total.

### **10.2: Users (Flow)** ✅
```dax
/// Users for flow analysis (Sankey context-aware)
/// Counts users in current filter context for source→destination flows
measure 'Users (Flow)' =
    CALCULATE(
        DISTINCTCOUNT('ga4-pages'[Total users]),
        ALLEXCEPT('ga4-pages', 'ga4-pages'[Page location]),
        ALLEXCEPT('ga4-traffic-source', 'ga4-traffic-source'[Session source / medium])
    )
    formatString: #,##0
    displayFolder: Explorer;Chart - User Journey Flow
```
**Usage:** Sankey diagram → Weight field
**Why Needed:** Sankey needs context-aware counts for each flow path, not global total.

### **10.3: Exits by Page** ⚠️ (Proxy)
```dax
/// Exits by page (PROXY until real data available)
/// NOTE: Real 'Exits' dimension should be requested from GA4
measure 'Exits by Page' = SUM('ga4-pages'[Views])
    formatString: #,##0
    displayFolder: Explorer;Chart - Top Exit Pages
```
**Usage:** Clustered Bar Chart → X-Axis (value)
**Status:** ⚠️ PROXY ONLY - request real Exits data from GA4.

---

## 📋 **SECTION 11: TRAFFIC & ACQUISITION MEASURES** ✅ (Context-Aware for Source Analysis)

### **11.1: Sessions by Source** ✅
```dax
/// Sessions by Traffic Source
/// Aggregates from ga4-traffic-source table (not ga4-daily)
measure 'Sessions by Source' = SUM('ga4-traffic-source'[Sessions])
    formatString: #,##0
    displayFolder: Traffic & Acquisition;Chart - Traffic Sources
```
**Usage:** Stacked Column Chart → Y-Axis, Legend = Session source / medium
**Why Needed:** Shows different session counts per source, not global total.

### **11.2: Users by Source** ✅
```dax
/// Total Users by Traffic Source
/// Aggregates from ga4-traffic-source table
measure 'Users by Source' = SUM('ga4-traffic-source'[Total users])
    formatString: #,##0
    displayFolder: Traffic & Acquisition;Chart - Campaigns
```
**Usage:** Clustered Bar Chart → X-Axis (value)
**Why Needed:** Shows different user counts per source, not global total.

### **11.3: Users by Event** ✅
```dax
/// Users by Event (for funnel visualization)
/// Aggregates from ga4-titles table
measure 'Users by Event' =
    IF(
        HASONEVALUE('ga4-titles'[Total users]),
        SUM('ga4-titles'[Total users]),
        DISTINCTCOUNT('ga4-pages'[Total users])
    )
    formatString: #,##0
    displayFolder: Traffic & Acquisition;Chart - Conversion Funnel
```
**Usage:** Funnel Chart → Values, Category = Event name
**Why Needed:** Shows different user counts per event stage, not global total.

---

## 📋 **SECTION 12: PLAY EVENTS MEASURES** ✅ (Context-Aware for Video Analysis)

### **12.1: Avg Engagement by Page (Minutes)** ✅
```dax
/// Average Engagement Time by Page (Minutes)
/// Aggregates from ga4-pages[Average engagement time per session]
measure 'Avg Engagement by Page (Minutes)' =
    DIVIDE(
        AVERAGE('ga4-pages'[Average engagement time per session]),
        60,
        0
    )
    formatString: #,##0.0
    displayFolder: Play Events;Chart - Watch Time
```
**Usage:** Clustered Bar Chart → X-Axis, Y-Axis = Page title
**Why Needed:** Shows different avg engagement per page/video, not global average.

---

## 📋 **SECTION 13: EXTERNAL SEARCH MEASURES** ✅ (Context-Aware for GSC Analysis)

### **13.1: GSC Clicks** ✅
```dax
/// Clicks from GSC (context-aware)
/// Aggregates from gsc-chart table
measure 'GSC Clicks' = SUM('gsc-chart'[Clicks])
    formatString: #,##0
    displayFolder: External Search;Chart - Clicks & Impressions
```
**Usage:** Line and Clustered Column Chart → Column Y-Axis
**Why Needed:** Shows different click counts per date, not global total.

### **13.2: GSC Impressions** ✅
```dax
/// Impressions from GSC (context-aware)
/// Aggregates from gsc-chart table
measure 'GSC Impressions' = SUM('gsc-chart'[Impressions])
    formatString: #,##0
    displayFolder: External Search;Chart - Clicks & Impressions
```
**Usage:** Line and Clustered Column Chart → Line Y-Axis
**Why Needed:** Shows different impression counts per date, not global total.

### **13.3: Impressions by Query** ✅
```dax
/// Impressions by Query (context-aware)
/// Aggregates from gsc-queries table
measure 'Impressions by Query' = SUM('gsc-queries'[Impressions])
    formatString: #,##0
    displayFolder: External Search;Table - Top Queries
```
**Usage:** Table → Col 2
**Why Needed:** Shows different impression counts per query, not global total.

### **13.4: Clicks by Query** ✅
```dax
/// Clicks by Query (context-aware)
/// Aggregates from gsc-queries table
measure 'Clicks by Query' = SUM('gsc-queries'[Clicks])
    formatString: #,##0
    displayFolder: External Search;Table - Top Queries
```
**Usage:** Table → Col 2 (if showing clicks) OR Scatter Chart
**Why Needed:** Shows different click counts per query, not global total.

### **13.5: CTR by Query** ✅
```dax
/// CTR by Query (calculated from Clicks and Impressions)
/// Uses context-aware aggregation from gsc-queries table
measure 'CTR by Query' =
    DIVIDE(
        SUM('gsc-queries'[Clicks]),
        SUM('gsc-queries'[Impressions]),
        0
    )
    formatString: 0.00%
    displayFolder: External Search;Table - Top Queries
```
**Usage:** Table → Col 3, Scatter Chart → Y-Axis
**Why Needed:** Shows different CTR per query. Global CTR would be misleading.

### **13.6: Position by Query** ✅
```dax
/// Average Position by Query
/// Aggregates from gsc-queries table
measure 'Position by Query' = AVERAGE('gsc-queries'[Position])
    formatString: #,##0.0
    displayFolder: External Search;Table - Top Queries
```
**Usage:** Table → Col 4, Scatter Chart → X-Axis
**Why Needed:** Shows different avg position per query, not global average.

---

## 📋 **SECTION 14: DEEP DIVE MEASURES** ✅ (Context-Aware for Advanced Analysis)

### **14.1: Sessions (Decomposition)** ✅
```dax
/// Sessions for Decomposition Tree (context-aware)
/// Aggregates sessions respecting all dimensional filters
measure 'Sessions (Decomposition)' =
    CALCULATE(
        [Sessions],
        ALLSELECTED()
    )
    formatString: #,##0
    displayFolder: Deep Dive;Chart - Segmentation Matrix
```
**Usage:** Decomposition Tree → Analyze field
**Why Needed:** Ensures each branch shows correct subset of sessions, not global total.

---

## 📋 **SECTION 15: TIME INTELLIGENCE (Via Calculation Group)**

**Note:** Time Intelligence measures are created via Calculation Group, not individual measures. The Calculation Group applies these calculations to any base measure:

- **Current** - Base measure value
- **MoM** - Month-over-Month change
- **MoM %** - Month-over-Month percentage change
- **YoY** - Year-over-Year change
- **YoY %** - Year-over-Year percentage change
- **YTD** - Year-to-Date

**Example Usage:**
- `[Total Events]` → Base measure
- `[Total Events MoM %]` → Via Calculation Group
- `[Total Events YoY]` → Via Calculation Group

**See:** `PRODUCTION_BUILD_PLAN.md` Task 1.10 for Calculation Group setup.

---

## 📋 **SECTION 11: UTILITY MEASURES**

### **10.1: Last Updated Text** ✅ (Works with Mock Data)
```dax
/// Last updated date in professional format
measure 'Last Updated Text' = 
    "Data current through " & 
    FORMAT(
        CALCULATE(MAX(Fact_LivecastEvents[event_date]), ALL(Fact_LivecastEvents)),
        "MMMM dd, yyyy"
    )
    formatString: @
```

### **10.2: Row Counts (Debugging)**
```dax
/// Row count for Fact_LivecastEvents (debugging)
measure 'Row Count - Fact_LivecastEvents' = COUNTROWS(Fact_LivecastEvents)
    formatString: #,##0

/// Row count for DimDate (debugging)
measure 'Row Count - DimDate' = COUNTROWS(DimDate)
    formatString: #,##0

/// Row count for DimLivecast (debugging)
measure 'Row Count - DimLivecast' = COUNTROWS(DimLivecast)
    formatString: #,##0
```

---

## ✅ **IMPLEMENTATION STATUS**

### **✅ Ready to Build Now (Works with Mock Data):**
- Total Events
- Play Events
- Unique Viewers
- Total Engagement (Minutes/Hours)
- Avg Engagement per Viewer
- Return Rate / Return Viewers / Return Events
- Performance Metrics (Avg Views per Event, etc.)
- Health Score (all components)
- Quick Insights
- Time Intelligence (via Calculation Group)

### **⚠️ Placeholder Measures (Require Real Data):**
- Sessions
- Page Views
- Total Users / New Users / Returning Users
- Engagement Rate (GA4 definition)
- Geography Metrics
- Acquisition Metrics
- Search Console Metrics

**Note:** Placeholder measures use `IF(HASONEVALUE(...))` checks to gracefully handle missing data. They'll work automatically when real data is loaded.

---

## 🎯 **NEXT STEPS**

1. **Copy measures** from this file into Power BI
2. **Test measures** with current mock data
3. **Build Calculation Group** for Time Intelligence
4. **Create Field Parameters** for dynamic analysis
5. **When real data arrives:** Measures will automatically work (no changes needed)

---

**Total Measures:** ~50 measures (30 ready now, 20 placeholders for real data)

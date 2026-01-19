# Slicers by Page - HHS Live Events Dashboard

**Date:** 2026-01-18
**Purpose:** Complete slicer specifications for all 7 dashboard pages
**Status:** ✅ Build Reference Document

---

## Overview

This document defines all slicers (filters) for each page of the HHS Live Events Performance Dashboard. Slicers are organized into two categories:

1. **Global Slicers** - Synced across all pages (Date Range)
2. **Page-Specific Slicers** - Unique to each page's analysis needs

---

## Current Data Model Relationships (Baseline)

### Existing Relationships (5 Active)

```
┌─────────────┐         ┌──────────────┐
│ DimDate     │────────►│ ga4-daily    │
│ [Date]      │ 1:M     │ [Date]       │
└─────────────┘         └──────────────┘

┌─────────────┐         ┌──────────────┐
│ DimDate     │────────►│ gsc-chart    │
│ [Date]      │ 1:M     │ [Date]       │
└─────────────┘         └──────────────┘

┌─────────────┐         ┌──────────────┐
│ DimLivecast │────────►│ ga4-pages    │
│ [Title]     │ 1:M     │ [Page title] │
└─────────────┘         └──────────────┘

┌─────────────┐         ┌──────────────┐
│ DimAction   │────────►│ ga4-events   │
│ [Action]    │ 1:M     │ [Event name] │
└─────────────┘         └──────────────┘

┌─────────────┐         ┌──────────────┐
│ ga4-pages   │────────►│ ga4-titles   │
│ [Page title]│ M:1     │ [Page title] │
└─────────────┘         └──────────────┘
```

### Current Slicer Compatibility (WITHOUT Enhancements)

| Slicer Field | Related Tables | Can Filter |
|--------------|----------------|------------|
| `DimDate[Date]` | ga4-daily, gsc-chart | ✅ Date-based visuals only |
| `DimLivecast[Livecast Title]` | ga4-pages, ga4-titles | ✅ Page-level visuals |
| `DimAction[Action]` | ga4-events | ✅ Event-level visuals |
| `ga4-devices[Device category]` | ga4-devices only | ⚠️ **ISOLATED** - no cross-filter |
| `ga4-geography[City]` | ga4-geography only | ⚠️ **ISOLATED** - no cross-filter |
| `ga4-traffic-source[Session source / medium]` | ga4-traffic-source only | ⚠️ **ISOLATED** - no cross-filter |

**Problem:** Many tables are "islands" with no relationships. Slicers on these tables won't filter other visuals.

---

## Relationship Enhancements (RECOMMENDED)

To make slicers work properly across the dashboard, we need to add relationships. Here's the plan:

### Enhancement 1: Connect ga4-pages to ga4-events

**Purpose:** Allow Livecast Title slicer to filter event visuals (play counts, etc.)

```
┌─────────────┐         ┌──────────────┐
│ ga4-pages   │────────►│ ga4-events   │
│ [Page title]│ 1:M     │ [Page title] │
└─────────────┘         └──────────────┘
```

**Implementation:**
1. Verify `ga4-events` has a `Page title` column (check source data)
2. If not, may need to join via `ga4-titles` (ga4-events → ga4-titles → ga4-pages)
3. Model view → Drag relationship

**Result:** Livecast Title slicer now filters BOTH page visuals AND event visuals

---

### Enhancement 2: Create Bridge Table for Cross-Domain Filtering

**Purpose:** Enable Device/City/Source slicers to filter across all visuals

**Problem:** GA4 exports are pre-aggregated. A "Mobile" session in ga4-devices is NOT linked to specific cities or sources.

**Solution A: Accept Limitation (Recommended for MVP)**
- Keep slicers page-specific
- Document that cross-filtering is limited
- Use Decomposition Tree for multi-dimensional analysis

**Solution B: Request Granular Data (Future Enhancement)**
- Request session-level export from GA4 with all dimensions
- Build proper star schema with single fact table
- This is a data pipeline change, not a Power BI change

**Solution C: Create Synthetic Bridge (Advanced)**
```dax
// Create a bridge table that connects dimensions
// WARNING: This creates cartesian products - use carefully
BridgeTable =
    CROSSJOIN(
        DISTINCT('ga4-devices'[Device category]),
        DISTINCT('ga4-geography'[City]),
        DISTINCT('ga4-traffic-source'[Session source / medium])
    )
```
**Not recommended** - creates fake relationships that misrepresent data.

---

### Enhancement 3: Add Date to Non-Dated Tables (If Source Data Allows)

**Purpose:** Allow Date slicer to filter geography, device, and traffic visuals

**Current Problem:**
- `ga4-devices`, `ga4-geography`, `ga4-traffic-source` have NO Date column
- Date slicer only filters `ga4-daily` and `gsc-chart`

**Solution:** If your GA4 export includes date breakdowns:
1. Re-export with Date dimension included
2. Add relationship: `DimDate[Date]` → `ga4-devices[Date]` (etc.)

**If Date not available in source:**
- Accept that these visuals show **all-time totals** regardless of date selection
- Add visual subtitle: "All-time data (not filtered by date)"
- Or calculate % contribution metrics that ARE date-filtered

---

### Enhancement 4: Connect GSC Tables to Each Other

**Purpose:** Enable cross-filtering between queries, pages, and devices in External Search

**Current Problem:** GSC tables are completely isolated from each other.

**Solution:** Create a GSC Bridge via Landing Page URL:
```
┌─────────────┐         ┌──────────────┐
│ gsc-pages   │────────►│ gsc-queries  │
│ [Top pages] │ 1:M     │ [Landing URL]│ (if column exists)
└─────────────┘         └──────────────┘
```

**Check:** Does `gsc-queries` have a landing page column? If not, cross-filtering isn't possible without new data.

---

## Enhanced Slicer Compatibility (WITH Enhancements)

After implementing recommended enhancements:

| Slicer Field | Can Filter (After Enhancements) |
|--------------|--------------------------------|
| `DimDate[Date]` | ga4-daily, gsc-chart, *(ga4-devices, ga4-geography, ga4-traffic-source if dates added)* |
| `DimLivecast[Livecast Title]` | ga4-pages, ga4-titles, **ga4-events** *(new)* |
| `DimAction[Action]` | ga4-events |
| `ga4-devices[Device category]` | ga4-devices *(still isolated unless bridge created)* |
| `ga4-geography[City]` | ga4-geography *(still isolated unless bridge created)* |
| `ga4-traffic-source[Session source / medium]` | ga4-traffic-source *(still isolated unless bridge created)* |

---

## Anticipated Issues & Solutions

### Issue 1: Date Slicer Doesn't Filter Geography/Device/Traffic Visuals

**Symptom:** User selects "Last 7 days" but Sessions by City bar chart still shows all-time data.

**Root Cause:** `ga4-geography` has no Date column → no relationship to DimDate.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Add subtitle "All-time data" | Low | Sets expectation, no functionality change |
| B. Hide visuals when date filtered | Medium | Use DAX to detect date filter, show warning |
| C. Re-export GA4 with dates | High | Full functionality, requires data pipeline change |

**Recommended:** Option A for MVP, Option C for v2.

**DAX for Option B (Warning Measure):**
```dax
[Date Filter Warning] =
IF(
    ISFILTERED(DimDate[Date]),
    "⚠️ Date filter does not apply to this visual (source data has no dates)",
    BLANK()
)
```

---

### Issue 2: Livecast Title Slicer Doesn't Filter Play Events Timeline

**Symptom:** User selects a specific livecast, but Daily Play Events chart doesn't change.

**Root Cause:** `ga4-events` may not have `Page title` column, or relationship not created.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Create relationship ga4-pages → ga4-events via Page title | Low | Works if column exists |
| B. Use ga4-titles as bridge | Medium | ga4-events → ga4-titles → ga4-pages |
| C. Add visual-level filter | Low | Manually sync slicer to visual filter |

**Recommended:** Option A or B depending on data structure.

---

### Issue 3: Deep Dive Slicers Don't Cross-Filter

**Symptom:** Selecting "Mobile" in Device slicer doesn't filter City bar chart.

**Root Cause:** No relationship between ga4-devices and ga4-geography.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Accept limitation, use Decomposition Tree | Low | Tree handles multi-dimensional analysis internally |
| B. Document behavior clearly | Low | "Slicers filter their own section only" |
| C. Remove misleading slicers | Low | Simplify to Date only, rely on Decomposition Tree |

**Recommended:** Option A + B. Deep Dive's value is the Decomposition Tree, not the slicers.

---

### Issue 4: Reset Button Doesn't Clear All Filters

**Symptom:** Reset button clears slicers but visuals still show filtered state.

**Root Cause:** Cross-filter selections (clicking on bars/segments) not captured in bookmark.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Create bookmark with NO selections | Low | Must click empty canvas before creating bookmark |
| B. Use "Clear all filters" action | Low | Button action → Type: Reset filters |
| C. Multi-action bookmark | Medium | Bookmark clears slicers + visual selections |

**Recommended:** Option B - simpler and more reliable.

**Button Configuration:**
- Action: Type = **Bookmark** (not Reset)
- BUT: Create bookmark with these steps:
  1. Clear all slicer selections
  2. Click empty canvas (clears cross-highlights)
  3. THEN create bookmark with Data: ON

---

### Issue 5: Synced Date Slicer Shows Different Dates on Different Pages

**Symptom:** Date shows "Dec 1-31" on Page 1 but "Nov 1-30" on Page 2.

**Root Cause:** Sync slicer not configured correctly, or multiple date slicers exist.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Delete extra slicers, keep ONE synced slicer | Low | Single source of truth |
| B. Verify sync pane settings | Low | Check both Sync AND Visible columns |
| C. Use bookmark to navigate (preserves state) | Medium | Navigation bookmarks carry filter context |

**Recommended:** Option A + B.

**Verification Steps:**
1. View → Sync slicers
2. Select the Date slicer
3. Verify ALL 7 pages have ✅ in "Sync" column
4. Verify ALL 7 pages have ✅ in "Visible" column
5. If any page has its own Date slicer, DELETE it

---

### Issue 6: Panel Expand/Collapse Breaks When Navigating

**Symptom:** User collapses panel on Page 1, navigates to Page 2, panel state is random.

**Root Cause:** Panel state is page-specific, not global.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Accept per-page state | Low | Each page manages its own panel |
| B. Navigation bookmarks with panel state | Medium | Nav bookmarks set panel to default (expanded) |
| C. Global panel state via measure | High | Complex DAX + bookmarks, not recommended |

**Recommended:** Option A. Users expect page-specific state.

---

### Issue 7: Button Slicer (Device) Doesn't Highlight Active Selection

**Symptom:** User clicks "Mobile" button but it doesn't look selected.

**Root Cause:** Button slicer styling not configured correctly.

**Solution:**
```
Format → Slicer → Selection:
- Selection Controls: Show "Select all" = OFF (for buttons)
- Single select = ON (for mutual exclusivity)
- Padding: 6px

Format → Slicer → Buttons:
- Background (selected): #005EA2
- Font color (selected): #FFFFFF
- Background (default): #F8FAFC
- Font color (default): #565C65
- Outline: #DFE1E2
- Outline weight: 1px
- Border radius: 4px
```

---

### Issue 8: Slicer Dropdown Shows Too Many Items (Performance)

**Symptom:** City slicer takes forever to load, shows 10,000+ cities.

**Root Cause:** No Top N filter on slicer.

**Solutions:**
| Option | Effort | Result |
|--------|--------|--------|
| A. Add Top N filter to slicer | Low | Show only top 50 cities by Sessions |
| B. Enable Search box | Low | Users can type to filter |
| C. Use hierarchy (Country → Region → City) | Medium | Progressive disclosure |

**Recommended:** Option A + B.

**Top N Filter Configuration:**
1. Select slicer
2. Filters pane → Add filter → `[Sessions_City]`
3. Filter type: Top N
4. Show top: 50
5. By value: `[Sessions_City]` descending

---

## Data Model Enhancement Checklist

### Before Build (Required)

- [ ] **Verify ga4-events has Page title column**
  - If YES: Create relationship ga4-pages[Page title] → ga4-events[Page title]
  - If NO: Check if join via ga4-titles is possible

- [ ] **Verify all relationship cross-filter directions**
  - All dimension→fact relationships should be "Both"
  - Model view → Double-click relationship → Cross filter direction: Both

- [ ] **Test date slicer filtering**
  - Select date range
  - Check which visuals update
  - Document visuals that DON'T update (for subtitle warnings)

### Optional Enhancements (Post-MVP)

- [ ] Request GA4 re-export with date dimension on all tables
- [ ] Create relationship DimDate → ga4-devices (if date column added)
- [ ] Create relationship DimDate → ga4-geography (if date column added)
- [ ] Create relationship DimDate → ga4-traffic-source (if date column added)
- [ ] Verify GSC tables can be connected via landing page URL

---

## Relationship Diagram (Target State)

```
                              ┌──────────────┐
                              │   DimDate    │
                              │   [Date]     │
                              └──────┬───────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
       │  ga4-daily   │       │  gsc-chart   │       │ (Future:     │
       │  [Date]      │       │  [Date]      │       │ ga4-devices, │
       └──────────────┘       └──────────────┘       │ ga4-geography│
                                                     │ if dates     │
                                                     │ added)       │
                                                     └──────────────┘

       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
       │ DimLivecast  │──────►│  ga4-pages   │──────►│  ga4-titles  │
       │ [Title]      │       │ [Page title] │       │ [Page title] │
       └──────────────┘       └──────┬───────┘       └──────────────┘
                                     │
                                     │ (NEW - if Page title exists)
                                     ▼
                              ┌──────────────┐
                              │  ga4-events  │
                              │ [Page title] │
                              └──────────────┘
                                     ▲
                                     │
                              ┌──────┴───────┐
                              │  DimAction   │
                              │  [Action]    │
                              └──────────────┘

       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
       │ ga4-devices  │       │ga4-geography │       │ga4-traffic-  │
       │ (isolated)   │       │ (isolated)   │       │source        │
       └──────────────┘       └──────────────┘       │(isolated)    │
                                                     └──────────────┘
       Note: These remain islands unless dates added or bridge created
```

---

## Global Slicer (All Pages)

### Date Range Slicer

**Field:** `DimDate[Date]`
**Style:** Dropdown (Between - two date pickers)
**Position:** Header utility bar (top-right)
**Sync:** ✅ Synced across all 7 pages via View → Sync slicers

| Property | Value |
|----------|-------|
| X | 1672px |
| Y | 26px |
| Width | 200px |
| Height | 50px |
| Background | #FFFFFF |
| Border | 1px solid #DFE1E2 |
| Border Radius | 4px |
| Font | Segoe UI, 12pt |
| Default | Last 30 days |

**What it filters:**
- ✅ ga4-daily metrics (Sessions, Page Views, Users)
- ✅ gsc-chart metrics (Clicks, Impressions)
- ❌ ga4-pages (no Date column)
- ❌ ga4-devices (no Date column)
- ❌ ga4-geography (no Date column)
- ❌ ga4-traffic-source (no Date column)

**Sync Configuration:**
1. View → Sync slicers
2. Select Date slicer
3. Check "Sync" for all 7 pages
4. Check "Visible" for all 7 pages

---

## Page-by-Page Slicer Specifications

### Page 1: Executive Summary (Command Center)

**Philosophy:** Provide key filtering options while maintaining executive-level overview.

**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 1

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Date Range | `DimDate[Date]` | Dropdown | Header (left) | Time period selection |
| Page Path | `ga4-pages[Page path]` | Dropdown | Header (right) | Filter to specific livecast page |

**Total Slicers:** 2

**Why Page Path slicer:**
- Matches reference dashboard functionality
- Allows filtering all visuals to a specific livecast event page
- Users can quickly focus on one event's performance
- Cross-filters: Sessions by City, Device Breakdown, Referral Sources, Top Pages, Top Livecast Videos

**Slicer Positions:**
```
┌─────────────────────────────────────────────────────────────────┐
│  [Dec 1 - Dec 31 ▼]              EXECUTIVE SUMMARY   [Page path ▼] │
└─────────────────────────────────────────────────────────────────┘
```

| Slicer | X | Y | W | H |
|--------|---|---|---|---|
| Date Range | 84px | 26px | 200px | 50px |
| Page Path | 1672px | 26px | 200px | 50px |

**What Page Path filters:**
- ✅ Sessions by City (ga4-pages relationship)
- ✅ Device Breakdown (if relationship exists)
- ✅ Referral Sources table (ga4-traffic-source - limited)
- ✅ Top Pages table (ga4-pages)
- ✅ Top Livecast Videos table (ga4-pages → ga4-titles)

**Cross-Filter Behavior:**
- Click city bar → filters Device Breakdown, Top Pages, Top Livecast tables
- Click device segment → filters Sessions by City, Top Pages
- Click table row → highlights related data

---

### Page 2: Explorer (Website Performance)

**Philosophy:** Enable deep exploration of page-level performance with multiple filter dimensions.

**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 2

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Date Range | `DimDate[Date]` | Dropdown | Header (left) | Time period selection |
| Page Path | `ga4-pages[Page path]` | Dropdown | Header (right, top) | Filter to specific page |
| Livecast Title | `DimLivecast[Livecast Title]` | Dropdown | Header (right, bottom) | Filter to specific livecast event |

**Total Slicers:** 3

**Why both Page Path AND Livecast Title:**
- Matches reference dashboard functionality
- Page Path allows filtering to specific URL paths
- Livecast Title provides user-friendly event name filtering
- Together they give maximum flexibility for page-level analysis

**Slicer Positions:**
```
┌─────────────────────────────────────────────────────────────────┐
│  [Dec 1 - Dec 31 ▼]              EXPLORER          [Page path ▼] │
│  Discover patterns...                           [Livecast Title ▼] │
└─────────────────────────────────────────────────────────────────┘
```

| Slicer | X | Y | W | H |
|--------|---|---|---|---|
| Date Range | 84px | 26px | 200px | 50px |
| Page Path | 1672px | 26px | 200px | 40px |
| Livecast Title | 1672px | 70px | 200px | 40px |

**What each slicer filters:**
- ✅ Daily Pageviews chart (Date filters gsc-chart)
- ✅ Pageviews by Metro Region map (ga4-pages)
- ✅ Page Performance Table (ga4-pages)
- ✅ Most Viewed Pages chart (ga4-pages)

---

### Page 3: Traffic & Acquisition

**Philosophy:** Understand traffic sources and user acquisition paths with page-level filtering.

**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 4 (Acquisition Channels)

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Page Path | `ga4-pages[Page path]` | Dropdown | Header (top-left) | Filter to specific page |
| Date Range | `DimDate[Date]` | Dropdown | Header (below Page Path) | Time period selection |

**Total Slicers:** 2

**Why Page Path slicer:**
- Matches reference dashboard functionality
- Allows users to see traffic sources for a specific livecast page
- Filters the page title table to show only selected page
- Note: May have limited cross-filtering to traffic source tables depending on data model relationships

**Slicer Positions:**
```
┌─────────────────────────────────────────────────────────────────┐
│  [Page path ▼]                  TRAFFIC & ACQUISITION           │
│  [Dec 1 - Dec 31 ▼]             Understand how audiences...     │
└─────────────────────────────────────────────────────────────────┘
```

| Slicer | X | Y | W | H |
|--------|---|---|---|---|
| Page Path | 84px | 16px | 200px | 40px |
| Date Range | 84px | 60px | 200px | 50px |

**What each slicer filters:**
- ✅ Page Title table (ga4-pages)
- ✅ Top Referring Channels bar chart (limited - depends on relationships)
- ✅ Session Source table (ga4-traffic-source - limited)
- ✅ Medium table (ga4-traffic-source - limited)
- ⚠️ Social Channels chart (may need relationship enhancement)

**Cross-Filter Behavior:**
- Click source/medium in bar chart → filters other traffic visuals
- Click treemap segment → filters related traffic data
- Funnel chart shows event progression (ga4-titles data)

**⚠️ Data Model Note:** For full Page Path filtering on traffic visuals:
1. May need GA4 export with traffic source BY page
2. Create relationship between traffic and pages tables if not existing

---

### Page 4: Play Events

**Philosophy:** Deep analysis of video/livecast engagement with comprehensive filtering.

**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 3 (Play Events)

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Date Range | `DimDate[Date]` | Dropdown | Header (left) | Time period selection |
| Livecast Action | `DimAction[Action]` | Dropdown | Header (right, top) | Filter by action (play, replay, view) |
| Livecast Title | `DimLivecast[Livecast Title]` | Dropdown | Header (right, bottom) | Filter to specific livecast |
| Event Name | `ga4-events[Event name]` | Dropdown | Content area (below charts) | Filter by event type |
| Page Title | `ga4-pages[Page title]` | Dropdown | Content area (below charts) | Filter by page |

**Total Slicers:** 5

**Why these slicers (matching reference):**
- Livecast Action in header for quick play/replay filtering
- Livecast Title in header for event selection
- Event Name and Page Title below charts for detailed filtering of the events table
- Provides maximum flexibility for play event analysis

**Slicer Positions:**
```
┌─────────────────────────────────────────────────────────────────┐
│  [Dec 1 - Dec 31 ▼]              PLAY EVENTS    [livecast action ▼] │
│                                  Track video... [livecast title  ▼] │
├─────────────────────────────────────────────────────────────────┤
│  [Daily Play Events Chart]      [On Page Events Chart]          │
├─────────────────────────────────────────────────────────────────┤
│  [Event name ▼]                 [Page title ▼]                  │
├─────────────────────────────────────────────────────────────────┤
│  [Events Table]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Slicer | X | Y | W | H |
|--------|---|---|---|---|
| Date Range | 84px | 26px | 200px | 50px |
| Livecast Action | 1672px | 16px | 200px | 40px |
| Livecast Title | 1672px | 60px | 200px | 40px |
| Event Name | 84px | 480px | 200px | 40px |
| Page Title | 300px | 480px | 200px | 40px |

**What each slicer filters:**
| Slicer | Daily Play Events | On Page Events | KPI Cards | Event Table |
|--------|:-----------------:|:--------------:|:---------:|:-----------:|
| Date Range | ✅ | ✅ | ✅ | ✅ |
| Livecast Action | ✅ | ✅ | ✅ | ✅ |
| Livecast Title | ✅ | ✅ | ✅ | ✅ |
| Event Name | ❌ | ❌ | ❌ | ✅ |
| Page Title | ❌ | ❌ | ❌ | ✅ |

---

### Page 5: External Search (GSC)

**Philosophy:** Focus on search performance - date range is the primary filter.

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Date Range | `DimDate[Date]` | Dropdown | Header (global) | Time period selection |

**Total Slicers:** 1 (global only)

**Why no additional slicers:**
- GSC tables (gsc-chart, gsc-queries, gsc-pages) have NO relationships to each other
- Date slicer filters gsc-chart (time series) via DimDate relationship
- Query and Landing Page tables are standalone (cross-filter via clicking rows)
- Device breakdown is a single static chart

**What Date filters:**
- ✅ Clicks & Impressions Trend (gsc-chart has Date)
- ❌ Top Queries table (gsc-queries - no Date column)
- ❌ Landing Pages table (gsc-pages - no Date column)
- ❌ Device breakdown (gsc-devices - no Date column)

**Cross-Filter Behavior:**
- Click query row → highlights in scatter chart (if same table)
- Click landing page → no cross-filter (different table)
- Visual interactions are limited due to GSC data structure

---

### Page 6: AI Insights

**Philosophy:** Anomaly detection and forecasting need full date context.

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Date Range | `DimDate[Date]` | Dropdown | Header (global) | Time period for anomaly/forecast |

**Total Slicers:** 1 (global only)

**Why no additional slicers:**
- Anomaly detection needs sufficient data points to identify patterns
- Filtering too narrowly reduces statistical significance
- Forecasting accuracy depends on historical data volume
- This page surfaces signals; Deep Dive is for drilling in

**AI Analytics Requirements:**
- Minimum 30 days of data for meaningful anomaly detection
- Minimum 60 days for reliable forecasting
- Recommend setting date slicer default to "Last 90 days" on this page

---

### Page 7: Deep Dive

**Philosophy:** Maximum flexibility for advanced segmentation and ad-hoc analysis.

| Slicer | Field | Style | Position | Rationale |
|--------|-------|-------|----------|-----------|
| Date Range | `DimDate[Date]` | Dropdown | Header (global) | Time period selection |
| Device Category | `ga4-devices[Device category]` | Buttons | Content area | Quick device segmentation |
| City | `ga4-geography[City]` | Dropdown | Content area | Geographic filtering |
| Traffic Source | `ga4-traffic-source[Session source / medium]` | Dropdown | Content area | Source analysis |

**Total Slicers:** 4

**⚠️ Important Caveat:** These slicers filter their own table's data but may NOT cross-filter to other visuals due to missing relationships.

**Slicer Positions:**
```
┌─────────────────────────────────────────────────────────────────┐
│  DEEP DIVE                             [Dec 1 - Dec 31 ▼]       │
│  Advanced segmentation...                                       │
├─────────────────────────────────────────────────────────────────┤
│  [Desktop] [Mobile] [Tablet]   [City ▼]   [Traffic Source ▼]    │
├─────────────────────────────────────────────────────────────────┤
│  [Decomposition Tree]                                           │
└─────────────────────────────────────────────────────────────────┘
```

| Slicer | X | Y | W | H | Style |
|--------|---|---|---|---|-------|
| Date Range | 1672px | 26px | 200px | 50px | Dropdown |
| Device Category | 84px | 124px | 280px | 40px | Buttons (horizontal) |
| City | 380px | 124px | 200px | 40px | Dropdown |
| Traffic Source | 596px | 124px | 240px | 40px | Dropdown |

**Decomposition Tree Configuration:**
The Decomposition Tree visual can use these dimensions in "Explain By":
- `ga4-geography[City]`
- `ga4-devices[Device category]`
- `ga4-traffic-source[Session source / medium]`
- `DimDate[Day of Week]`

**Note:** The Decomposition Tree has its own internal filtering - the page slicers provide additional pre-filtering context.

---

## Summary Table

**Updated based on reference dashboard: "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf"**

| Page | Date | Page Path | Livecast Title | Livecast Action | Event Name | Page Title | Device | City | Source | Total |
|------|:----:|:---------:|:--------------:|:---------------:|:----------:|:----------:|:------:|:----:|:------:|:-----:|
| 1. Executive Summary | ✅ | ✅ | | | | | | | | **2** |
| 2. Explorer | ✅ | ✅ | ✅ | | | | | | | **3** |
| 3. Traffic & Acquisition | ✅ | ✅ | | | | | | | | **2** |
| 4. Play Events | ✅ | | ✅ | ✅ | ✅ | ✅ | | | | **5** |
| 5. External Search | ✅ | | | | | | | | | **1** |
| 6. AI Insights | ✅ | | | | | | | | | **1** |
| 7. Deep Dive | ✅ | | | | | | ✅ | ✅ | ✅ | **4** |

**Total:** 18 slicer instances across 9 unique slicer types

### Changes from Previous Version:
- **Page 1 (Executive Summary):** Added Page Path slicer (+1)
- **Page 2 (Explorer):** Added Page Path slicer (+1, now 3 total)
- **Page 3 (Traffic & Acquisition):** Added Page Path slicer (+1, now 2 total)
- **Page 4 (Play Events):** Added Event Name and Page Title slicers (+2, now 5 total)

---

## Bookmark Plan

Bookmarks enable reset functionality, navigation, panel states, and saved views.

### Bookmark Naming Convention

```
[Page#]_[Category]_[State/Action]

Examples:
P1_Reset_Default
P1_Panel_Expanded
P1_Panel_Collapsed
P4_View_PlayOnly
```

### Global Bookmarks (Apply to All Pages)

| Bookmark Name | Purpose | Settings |
|---------------|---------|----------|
| `Global_DateReset_Last30` | Reset date to last 30 days | Data: ON, Display: OFF |

### Page 1: Executive Summary Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P1_Reset_Default` | Clear all cross-filters | ✅ | ❌ | ✅ |
| `P1_Panel_Expanded` | Show Recommended Actions panel | ❌ | ✅ | ✅ |
| `P1_Panel_Collapsed` | Hide Recommended Actions panel | ❌ | ✅ | ✅ |

**Reset Button Configuration:**
- Button Action: Bookmark → `P1_Reset_Default`
- Captures: All slicers cleared, no visual selections
- Does NOT reset: Date slicer (global)

**Panel Toggle Configuration:**
- Expand Button Action: Bookmark → `P1_Panel_Expanded`
- Collapse Button Action: Bookmark → `P1_Panel_Collapsed`
- Panel group visibility toggled between states

### Page 2: Explorer Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P2_Reset_Default` | Clear Livecast Title slicer + cross-filters | ✅ | ❌ | ✅ |
| `P2_Panel_Expanded` | Show Actions panel | ❌ | ✅ | ✅ |
| `P2_Panel_Collapsed` | Hide Actions panel | ❌ | ✅ | ✅ |

### Page 3: Traffic & Acquisition Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P3_Reset_Default` | Clear all cross-filters | ✅ | ❌ | ✅ |
| `P3_Panel_Expanded` | Show Actions panel | ❌ | ✅ | ✅ |
| `P3_Panel_Collapsed` | Hide Actions panel | ❌ | ✅ | ✅ |

### Page 4: Play Events Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P4_Reset_Default` | Clear Action + Title slicers + cross-filters | ✅ | ❌ | ✅ |
| `P4_Panel_Expanded` | Show Actions panel | ❌ | ✅ | ✅ |
| `P4_Panel_Collapsed` | Hide Actions panel | ❌ | ✅ | ✅ |
| `P4_View_PlayOnly` | Filter to "play" action only | ✅ | ❌ | ✅ |
| `P4_View_ReplayOnly` | Filter to "replay" action only | ✅ | ❌ | ✅ |

### Page 5: External Search Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P5_Reset_Default` | Clear all cross-filters | ✅ | ❌ | ✅ |
| `P5_Panel_Expanded` | Show Actions panel | ❌ | ✅ | ✅ |
| `P5_Panel_Collapsed` | Hide Actions panel | ❌ | ✅ | ✅ |

### Page 6: AI Insights Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P6_Reset_Default` | Clear all cross-filters | ✅ | ❌ | ✅ |
| `P6_Panel_Expanded` | Show Actions panel | ❌ | ✅ | ✅ |
| `P6_Panel_Collapsed` | Hide Actions panel | ❌ | ✅ | ✅ |
| `P6_Date_Last90` | Set date to last 90 days (optimal for AI) | ✅ | ❌ | ✅ |

### Page 7: Deep Dive Bookmarks

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `P7_Reset_Default` | Clear Device, City, Source slicers + cross-filters | ✅ | ❌ | ✅ |
| `P7_Panel_Expanded` | Show Actions panel | ❌ | ✅ | ✅ |
| `P7_Panel_Collapsed` | Hide Actions panel | ❌ | ✅ | ✅ |
| `P7_View_MobileOnly` | Filter to Mobile device | ✅ | ❌ | ✅ |
| `P7_View_DesktopOnly` | Filter to Desktop device | ✅ | ❌ | ✅ |

### Navigation Bookmarks (7 Pages)

| Bookmark Name | Target Page | Data | Display | Current Page |
|---------------|-------------|:----:|:-------:|:------------:|
| `Nav_P1_ExecSummary` | Page 1 | ❌ | ❌ | ✅ |
| `Nav_P2_Explorer` | Page 2 | ❌ | ❌ | ✅ |
| `Nav_P3_Traffic` | Page 3 | ❌ | ❌ | ✅ |
| `Nav_P4_PlayEvents` | Page 4 | ❌ | ❌ | ✅ |
| `Nav_P5_ExtSearch` | Page 5 | ❌ | ❌ | ✅ |
| `Nav_P6_AIInsights` | Page 6 | ❌ | ❌ | ✅ |
| `Nav_P7_DeepDive` | Page 7 | ❌ | ❌ | ✅ |

**Navigation Button Configuration:**
- Each nav button in the left rail uses Page Navigation action (not bookmark)
- OR use bookmarks if you need to preserve/reset state on navigation

### Drillthrough Back Button

| Bookmark Name | Purpose | Data | Display | Current Page |
|---------------|---------|:----:|:-------:|:------------:|
| `Drill_Back` | Return from drillthrough | ❌ | ❌ | ❌ |

**Note:** Use Power BI's built-in Back button for drillthrough pages instead of custom bookmark.

---

## Bookmark Groups

Organize bookmarks in the Bookmarks pane for easier management:

```
📁 Navigation
   └── Nav_P1_ExecSummary
   └── Nav_P2_Explorer
   └── Nav_P3_Traffic
   └── Nav_P4_PlayEvents
   └── Nav_P5_ExtSearch
   └── Nav_P6_AIInsights
   └── Nav_P7_DeepDive

📁 Page 1 - Executive Summary
   └── P1_Reset_Default
   └── P1_Panel_Expanded
   └── P1_Panel_Collapsed

📁 Page 2 - Explorer
   └── P2_Reset_Default
   └── P2_Panel_Expanded
   └── P2_Panel_Collapsed

📁 Page 3 - Traffic & Acquisition
   └── P3_Reset_Default
   └── P3_Panel_Expanded
   └── P3_Panel_Collapsed

📁 Page 4 - Play Events
   └── P4_Reset_Default
   └── P4_Panel_Expanded
   └── P4_Panel_Collapsed
   └── P4_View_PlayOnly
   └── P4_View_ReplayOnly

📁 Page 5 - External Search
   └── P5_Reset_Default
   └── P5_Panel_Expanded
   └── P5_Panel_Collapsed

📁 Page 6 - AI Insights
   └── P6_Reset_Default
   └── P6_Panel_Expanded
   └── P6_Panel_Collapsed
   └── P6_Date_Last90

📁 Page 7 - Deep Dive
   └── P7_Reset_Default
   └── P7_Panel_Expanded
   └── P7_Panel_Collapsed
   └── P7_View_MobileOnly
   └── P7_View_DesktopOnly
```

**Total Bookmarks:** 32

---

## Bookmark Creation Checklist

### For Each Reset Bookmark:

1. [ ] Clear all page-specific slicers (click "Clear selections" or select all)
2. [ ] Clear all visual cross-filter selections (click empty canvas area)
3. [ ] Keep Date slicer at current selection (do NOT clear global date)
4. [ ] View → Bookmarks → Add
5. [ ] Name: `P#_Reset_Default`
6. [ ] Right-click → Update
7. [ ] Check: Data ✅, Display ❌, Current page ✅
8. [ ] Test: Apply bookmark, verify slicers clear

### For Each Panel Bookmark:

1. [ ] Set panel to desired state (expanded or collapsed)
2. [ ] Select only the panel visual group in Selection pane
3. [ ] View → Bookmarks → Add
4. [ ] Name: `P#_Panel_Expanded` or `P#_Panel_Collapsed`
5. [ ] Right-click → Update
6. [ ] Check: Data ❌, Display ✅, Current page ✅, Selected visuals ✅
7. [ ] Test: Toggle between expanded/collapsed bookmarks

### For Quick View Bookmarks:

1. [ ] Set slicer(s) to desired filter state
2. [ ] View → Bookmarks → Add
3. [ ] Name: `P#_View_[Description]`
4. [ ] Right-click → Update
5. [ ] Check: Data ✅, Display ❌, Current page ✅
6. [ ] Test: Apply bookmark, verify filter applied

---

## Slicer Styling Standards

### Dropdown Slicer (Default)

| Property | Value |
|----------|-------|
| Background | #FFFFFF |
| Border | 1px solid #DFE1E2 |
| Border Radius | 4px |
| Font Family | Segoe UI |
| Font Size | 12px |
| Font Color | #1B1B1B |
| Dropdown Arrow | #565C65 |
| Hover Background | #F8FAFC |
| Selected Background | #D4E5F7 |
| Selected Text | #005EA2 |

### Button Slicer (Device Category)

| Property | Value |
|----------|-------|
| Active Background | #005EA2 |
| Active Text | #FFFFFF |
| Inactive Background | #F8FAFC |
| Inactive Text | #565C65 |
| Border | 1px solid #DFE1E2 |
| Border Radius | 4px |
| Button Gap | 8px |

### All Slicers

| Property | Value |
|----------|-------|
| Header Icons | OFF (clean look) |
| Search Box | ON (for dropdowns with >10 items) |
| Select All | ON (where available) |
| Single Select | OFF (allow multi-select) |

---

## Troubleshooting

### "Slicer not filtering visuals"

1. Check relationship exists between slicer field table and visual's data table
2. Verify relationship is active (Model view → Manage relationships)
3. Check cross-filter direction (should be "Both" for dimension tables)
4. **Most common cause:** GA4 tables have limited relationships - see Data Model Compatibility section

### "Date slicer not synced"

1. View → Sync slicers
2. Select Date slicer
3. Verify checkmarks in both "Sync" and "Visible" columns for all pages
4. Close Sync slicers pane and test

### "Reset button not working"

1. Verify bookmark has "Data: ON" checked
2. Verify bookmark captures cleared slicer state (not filtered state)
3. Test button action points to correct bookmark
4. Check bookmark wasn't accidentally updated with wrong state

### "Panel toggle not working"

1. Verify bookmark has "Display: ON" and "Data: OFF"
2. Verify "Selected visuals" is checked and correct visuals are selected
3. Check Selection pane grouping (panel elements should be grouped)
4. Test both Expanded and Collapsed bookmarks independently

---

**Document Version:** 2.0
**Last Updated:** 2026-01-18
**Changes in v2.0:**
- Removed Page Path slicer from Page 3 (no relationship to traffic data)
- Reduced Page 4 slicers from 5 to 3 (removed redundant Event Name and Page Title)
- Added Data Model Slicer Compatibility section
- Added comprehensive Bookmark Plan with 32 bookmarks
- Added Bookmark Groups organization
- Added detailed Bookmark Creation Checklist
- Added filter compatibility tables showing what each slicer actually filters

**Status:** ✅ Build Reference Document

# HHS Live Events Dashboard - Drill Interactions

## Overview

This document defines the drill-in (expand within visual) and drillthrough (navigate to detail page) interactions configured in the dashboard.

---

## Drill-Ins (Hierarchical Expansion)

Drill-ins allow users to expand data within a visual by clicking the drill-down icon or double-clicking a data point.

### Page 1: Executive Summary

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Geographic Map | Country → State → City | United States → California → Los Angeles |
| Device Donut | Device Category → Browser → OS | Mobile → Chrome → Android |
| Session Timeline | Year → Quarter → Month → Week → Day | 2026 → Q1 → January → Week 2 → Jan 8 |

### Page 2: Explorer

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Page Performance Matrix | Page Path → Page Title | /events/ → Live Event Replay |
| Traffic Treemap | Medium → Source → Campaign | organic → google → (not set) |
| Time Series | Year → Quarter → Month → Day | 2026 → Q1 → January → Jan 8 |

### Page 3: Traffic & Acquisition

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Channel Stacked Column | Medium → Source | referral → hhs.gov |
| Source Bar Chart | Source → Campaign → Content | google → spring_promo → banner_1 |
| User Funnel | Event → Sub-event | view_item → add_to_cart |

### Page 4: Play Events

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Session Timeline | Year → Month → Week → Day | 2026 → January → Week 2 → Jan 8 |
| Watch Time Bar | Page Title → Video Title | Events Page → Opening Remarks |
| Events by Type | Event Name → Event Category | video_start → promotional |

### Page 5: External Search (GSC)

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Clicks & Impressions Line | Year → Quarter → Month → Day | 2026 → Q1 → January → Jan 8 |
| Top Queries Table | Query → Page URL | "hhs live events" → /events/live |
| Country Performance | Country → Page | United States → /events/ |

### Page 6: AI Insights

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Anomaly Timeline | Year → Month → Day | 2026 → January → Jan 8 (anomaly detected) |
| Forecast Chart | Year → Quarter → Month | 2026 → Q1 → February (forecasted) |

### Page 7: Deep Dive

| Visual | Hierarchy | Example Flow |
|--------|-----------|--------------|
| Decomposition Tree | Sessions → City → Device → Source → Day of Week | 50K → Washington DC → Mobile → Google → Tuesday |
| Correlation Scatter | (No hierarchy - continuous axes) | — |

---

## Drillthroughs (Page Navigation)

Drillthroughs allow users to right-click a data point and navigate to a detail page with that filter context applied.

### Primary Drillthrough Target: Deep Dive Page

**Configuration:**
- Deep Dive page is set as a **drillthrough destination**
- When users right-click on any supported field, they can select "Drillthrough → Deep Dive"
- The filter context travels with the user

### Drillthrough Fields (Accepted Filters)

| Field | Source Table | Example Value |
|-------|--------------|---------------|
| Page title | ga4-pages | "HHS Live Event - January 2026" |
| Traffic Source | ga4-traffic-source | "google" |
| Device category | ga4-devices | "mobile" |
| City | ga4-cities | "Washington" |
| Date | DimDate | "2026-01-08" |
| Country | gsc-countries | "United States" |
| Query | gsc-queries | "hhs live events" |

### Drillthrough Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     ANY DASHBOARD PAGE                          │
│                                                                 │
│   ┌─────────────┐    Right-click    ┌─────────────────────┐    │
│   │  Data Point │ ───────────────► │ Context Menu        │    │
│   │  (e.g.,     │                   │ • Copy              │    │
│   │  "mobile")  │                   │ • Show as table     │    │
│   └─────────────┘                   │ • Drillthrough ──►  │    │
│                                     │   └─► Deep Dive     │    │
│                                     └─────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                                │
                                │ Navigate with filter context
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DEEP DIVE PAGE                             │
│                                                                 │
│   ┌────────────────────────────────────────────────────────┐   │
│   │ Filter Bar: Device category = "mobile"                 │   │
│   └────────────────────────────────────────────────────────┘   │
│                                                                 │
│   ┌─────────────────────┐   ┌─────────────────────────────┐   │
│   │ Decomposition Tree  │   │ Correlation Scatter         │   │
│   │ (filtered to mobile)│   │ (filtered to mobile)        │   │
│   └─────────────────────┘   └─────────────────────────────┘   │
│                                                                 │
│   ┌──────────────┐                                             │
│   │ ← Back       │  ◄── Returns to source page                 │
│   └──────────────┘                                             │
└─────────────────────────────────────────────────────────────────┘
```

### Back Button Configuration

- **Location:** Top-left of Deep Dive page (below header)
- **Action:** Returns user to the page they came from
- **Type:** Built-in drillthrough back button
- **Behavior:** Clears drillthrough filter context on return

---

## Cross-Filter Interactions

In addition to drill interactions, the dashboard uses cross-filtering:

| Interaction Type | Behavior |
|------------------|----------|
| **Single-click on visual** | Cross-filters other visuals on same page |
| **Ctrl+click** | Multi-select for cumulative filtering |
| **Click empty space** | Clears all cross-filter selections |

### Cross-Filter Direction Settings

| Visual Type | Default Direction |
|-------------|-------------------|
| Slicers | Both directions (bidirectional) |
| Charts | Single direction (filters others, not filtered by others) |
| Cards | No cross-filter (display only) |
| Tables/Matrices | Single direction |

---

## Implementation Notes

### Enabling Drill-Ins

1. In Power BI Desktop, select the visual
2. Add fields to the **Axis** or **Rows** well in hierarchical order
3. The drill icons automatically appear in the visual header

### Enabling Drillthroughs

1. Navigate to Deep Dive page
2. In Visualizations pane, locate **Drillthrough** section
3. Drag fields (Page title, Device category, etc.) to drillthrough well
4. Set "Keep all filters" to ON for full context
5. Add Back button from Insert → Buttons → Back

### Testing Drill Interactions

| Test Case | Expected Result |
|-----------|-----------------|
| Double-click country on map | Drills to state level |
| Click drill-down icon, then data point | Drills one level deeper |
| Right-click → Drillthrough → Deep Dive | Navigates with filter |
| Click Back button on Deep Dive | Returns to source page |

---

## Best Practices

1. **Limit hierarchy depth** - 4-5 levels maximum for usability
2. **Consistent drill fields** - Use same fields across pages for predictable behavior
3. **Visual cues** - Ensure drill icons are visible (not hidden by small visual size)
4. **Back button prominence** - Place in expected location (top-left)
5. **Filter context clarity** - Show active drillthrough filters in visible filter bar

---

*Document Version: 1.0*
*Last Updated: January 2026*
*Dashboard Version: HHS Live Events v2.1*

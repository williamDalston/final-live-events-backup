# Plan: Programmatic Visual Generation for HHS Live Events Dashboard

## Executive Summary

Create a **Python-based generator** that produces Power BI visual.json files using your project's exact measures, grid positions, and JSON patterns. This minimizes manual work while ensuring correct bindings.

---

## What We Have (Exploration Complete)

### 1. Measures Library (240+ measures in Measures_Livecast.tmdl)

| Category | Examples |
|----------|----------|
| KPI Core | `Sessions`, `Page Views`, `Total Users`, `Avg Pages per Session` |
| Video | `Total Events`, `Unique Viewers`, `Play Events`, `Video Plays` |
| MoM % | `Sessions - MoM % (Latest Month)`, `Page Views - MoM % (Latest Month)` |
| MoM Labels | `Sessions - MoM Label (Latest Month)` (includes ▲/▼ arrows) |
| MoM Colors | `Sessions - MoM Color (Latest Month)` (#2E7D32 green, #C62828 red) |
| Alt Text | `Sessions Alt Text`, `Page Views Alt Text`, `Avg Pages Alt Text` |
| GSC | `GSC Clicks`, `GSC Impressions`, `GSC CTR`, `GSC Avg Position` |
| Signals | `Signal - Sessions MoM Drop?`, `Signal - Mobile Share Elevated?` |

### 2. Grid Positions (V5_PIXEL_GRID_REFERENCE.md)

```
Canvas: 1280 x 720 px
Content: X=56 → 953 (expanded) or → 1232 (collapsed)

KPI Row:     Y=96,  H=67,  W=197, X: [56, 261, 466, 671]
Section 1:   Y=188, H=254
Section 2:   Y=466, H=220
2-Up Layout: Left W=444, Right W=445, Gap=8px
```

### 3. JSON Patterns (from existing visual.json)

**Measure reference:**
```json
{"Measure": {"Expression": {"SourceRef": {"Entity": "Measures_Livecast"}}, "Property": "Sessions"}}
```

**Column reference:**
```json
{"Column": {"Expression": {"SourceRef": {"Entity": "DimDate"}}, "Property": "Date"}}
```

**Visual IDs:** 24-char hex strings (e.g., `018c9888d54ada2b86a8`)

---

## Implementation Plan

### Deliverables

| File | Purpose |
|------|---------|
| `generate_visuals.py` | Main Python generator script |
| `visual_config.json` | Page definitions with measures & positions |

### How It Works

1. **Config file** defines each page's visuals with measure names
2. **Generator** reads config, creates visual.json files
3. **Output** goes to correct folder structure
4. **Manual step:** Open Power BI Desktop to verify

### Example Config Structure

```json
{
  "pages": {
    "executive_summary": {
      "page_id": "88620660ba315057a1dd",
      "visuals": [
        {
          "type": "kpi_card",
          "position": {"x": 56, "y": 96, "z": 1000},
          "measure": "Sessions",
          "title": "Sessions",
          "mom_label": "Sessions - MoM Label (Latest Month)",
          "mom_color": "Sessions - MoM Color (Latest Month)",
          "alt_text": "Sessions Alt Text"
        }
      ]
    }
  }
}
```

### Visual Types Supported

| Type | visualType | Use Case |
|------|------------|----------|
| KPI Card | `cardVisual` | Metric with MoM delta |
| Bar Chart | `clusteredBarChart` | Category comparisons |
| Line Chart | `lineChart` | Trends over time |
| Area Chart | `areaChart` | Cumulative trends |
| Table | `tableEx` | Detail listings |
| Matrix | `pivotTable` | Cross-tab analysis |
| Treemap | `treemap` | Part-to-whole |
| HTML | `htmlContent...` | Actions panel |

---

## Page-by-Page Visual Requirements

### Page 1: Executive Summary
| Visual | Type | Position | Measures |
|--------|------|----------|----------|
| KPI 1 | Card | X=56 | Sessions, Sessions MoM Label/Color |
| KPI 2 | Card | X=261 | Page Views, Page Views MoM Label/Color |
| KPI 3 | Card | X=466 | Top Device Category |
| KPI 4 | Card | X=671 | Avg Pages per Session, Avg Pages MoM |
| Map | Azure Map | Section 1 Left | Sessions by City |
| Device Bar | 100% Bar | Section 1 Right | Device Sessions |
| Livecast Bar | Bar | Section 2 Left | Livecast Views |
| Top Pages | Table | Section 2 Right | Page Views, Engagement |

### Page 2: Explorer
| Visual | Type | Position | Measures |
|--------|------|----------|----------|
| KPI 1-4 | Cards | Y=96 | Active Pages, Avg Engagement, Bounce Rate, Top Source |
| Matrix | Matrix | Section 1 Full | Page title, Users, Engagement Rate |
| Treemap | Treemap | Section 2 Left | Sessions by Source |
| Bar | Bar | Section 2 Right | Page Views by Page |

### Page 3: Traffic & Acquisition
| Visual | Type | Measures |
|--------|------|----------|
| KPIs | Cards | Organic/Direct/Referral/Social Sessions |
| Stacked Col | Column | Sessions by Channel over time |
| Bar | Bar | Top Traffic Sources |
| Funnel | Funnel | User conversion stages |

### Page 4: Play Events
| Visual | Type | Measures |
|--------|------|----------|
| KPIs | Cards | Play Events, Completion Rate, Avg Watch Time, Unique Viewers |
| Area | Area | Play Events over time |
| Bar | Bar | Avg Watch Time by Video |
| Bar | Bar | Events by Type (view/replay/return) |

### Page 5: External Search
| Visual | Type | Measures |
|--------|------|----------|
| KPIs | Cards | GSC Clicks, Impressions, CTR, Position |
| Combo | Line+Column | Clicks & Impressions trend |
| Table | Table | Query, Impressions, Clicks, CTR, Position |
| Scatter | Scatter | CTR vs Position |

### Pages 6-7: AI Insights & Deep Dive
Similar structure with anomaly detection, forecasting, decomposition tree

---

## Implementation Steps

### Step 1: Create Config File
Define all 7 pages with their visuals, measures, positions

### Step 2: Build Generator Script
- Parse config
- Generate unique visual IDs
- Fill JSON templates
- Write to folder structure

### Step 3: Run Generator
```bash
python generate_visuals.py --page executive_summary
# or
python generate_visuals.py --all
```

### Step 4: Verify in Power BI Desktop
- Open report
- Check each visual has data
- Verify measure bindings

---

## Risk Mitigation

1. **Backup first:** Copy existing visuals folder before running
2. **One page at a time:** Start with Executive Summary as proof
3. **Dry-run mode:** Print JSON without writing files
4. **Compare output:** Diff generated vs existing visuals

---

## Scope (User Confirmed)

- **Priority:** Executive Summary page first (proof of concept)
- **Approach:** Add only missing visuals (keep existing ones)
- **Style:** Simple single-file script (easy to understand/modify)

---

## Final Implementation Plan

### Step 1: Audit Executive Summary
Read existing visuals in `88620660ba315057a1dd/visuals/` to identify what's missing.

### Step 2: Create `generate_visuals.py`
Single Python file (~400 lines) with:
- Embedded JSON templates for each visual type
- Config dictionary for Executive Summary visuals
- Functions to generate visual IDs and fill templates
- Write to correct folder structure

### Step 3: Generate Missing Visuals
Run script to create visual.json files for missing elements.

### Step 4: Verify in Power BI Desktop
Open report, check visuals load with correct data.

### Step 5: Expand to Other Pages
Once proven, add configs for Explorer, Traffic, etc.

---

## Script Structure (generate_visuals.py)

```python
# generate_visuals.py - HHS Live Events Visual Generator

import json
import secrets
import os
from pathlib import Path

# === TEMPLATES ===

KPI_CARD_TEMPLATE = {
    # Full JSON structure from existing 018c9888d54ada2b86a8
}

BAR_CHART_TEMPLATE = {
    # Full JSON structure from existing visuals
}

TABLE_TEMPLATE = {
    # Full JSON structure
}

# === PAGE CONFIGS ===

EXECUTIVE_SUMMARY = {
    "page_id": "88620660ba315057a1dd",
    "visuals": [
        {
            "type": "kpi_card",
            "position": {"x": 56, "y": 96, "z": 1000, "height": 67, "width": 197},
            "measure": "Sessions",
            "title": "Sessions",
            "mom_label": "Sessions - MoM Label (Latest Month)",
            "mom_color": "Sessions - MoM Color (Latest Month)",
            "alt_text": "Sessions Alt Text"
        },
        # ... more visuals
    ]
}

# === GENERATOR FUNCTIONS ===

def generate_visual_id():
    return secrets.token_hex(12)

def build_measure_ref(measure_name, entity="Measures_Livecast"):
    return {"Measure": {"Expression": {"SourceRef": {"Entity": entity}}, "Property": measure_name}}

def generate_kpi_card(config):
    # Fill template with config values
    pass

def generate_bar_chart(config):
    pass

def write_visual(page_id, visual_id, visual_json, base_path):
    folder = Path(base_path) / page_id / "visuals" / visual_id
    folder.mkdir(parents=True, exist_ok=True)
    with open(folder / "visual.json", "w") as f:
        json.dump(visual_json, f, indent=2)

# === MAIN ===

if __name__ == "__main__":
    # Generate for Executive Summary
    pass
```

---

## Executive Summary Visual Checklist

| Visual | Exists? | Action |
|--------|---------|--------|
| KPI 1: Sessions | ✅ Yes | Verify bindings |
| KPI 2: Page Views | ✅ Yes | Verify bindings |
| KPI 3: Top Device | ✅ Yes | Verify bindings |
| KPI 4: Avg Pages | ✅ Yes | Verify bindings |
| Map: Sessions by City | ? | Check/Generate |
| Bar: Device Breakdown | ? | Check/Generate |
| Bar: Top Livecast Videos | ? | Check/Generate |
| Table: Top Pages | ? | Check/Generate |
| HTML: Actions Panel | ? | Check/Generate |

---

## Verification

1. Run `python generate_visuals.py`
2. Open Power BI Desktop
3. Load the report
4. Navigate to Executive Summary
5. Confirm all visuals appear with data
6. Check Format pane for correct measure bindings

---

## Critical Files

| File | Purpose |
|------|---------|
| `Measures_Livecast.tmdl` | Source of 240+ measures to validate against |
| `018c9888d54ada2b86a8/visual.json` | Gold standard KPI card pattern |
| `DASHBOARD_BUILD_GUIDE.md` | Visual specs for each page |
| `V5_PIXEL_GRID_REFERENCE.md` | Exact positions |


# Automation Discovery for Live Events Dashboard

**Purpose:** Map existing automation tools to our Live Events Dashboard build
**Goal:** Programmatically create all shapes, layouts, and elements on 1920×1080 canvas
**Repository:** `C:\Users\farad\Dev\WORK\HHS\repos\auto-the-big-one`

---

## 0. CRITICAL ADDITIONAL RESOURCES FOUND

### 1920×1080 SVG Templates (Already Exist!)
| File | Path |
|------|------|
| Drillthrough Livecast | `02_jira/01_Themes_and_Styling/SVG_Layouts/Live_Events_Template_AddOns/Live_Events_Drillthrough_LivecastDetail_1920x1080.svg` |
| Drillthrough Page | `02_jira/01_Themes_and_Styling/SVG_Layouts/Live_Events_Template_AddOns/Live_Events_Drillthrough_PageDetail_1920x1080.svg` |
| Visual Library | `02_jira/01_Themes_and_Styling/SVG_Layouts/Visual_Library/HHS_Visual_Library_Page_1920x1080.svg` |

### Layout Optimization Guide (1920×1080 Math!)
| File | Path | Key Content |
|------|------|-------------|
| **LAYOUT_OPTIMIZATION_NARROW_PANEL.md** | `dashboards/01_Live_Events_Dashboard/00_Documentation/03_Guides/` | **Exact pixel math for 1920px:** Body=1344px, Panel=400px, Gap=20px, Total=1920px ✅ |

**Key Measurements from Layout Guide:**
```
Left margin:        84px
Body content:     1344px (was 1216px)
Gap to panel:       20px
Panel width:       400px (was 528px)
Right margin:       72px
─────────────────────────
Total:            1920px ✅

Half-width (2-col): 662px (1344 - 20) / 2
```

### Official Color Palette (USWDS 3.0)
| File | Path |
|------|------|
| **HHS_COLOR_PALETTE.md** | `05_Themes/HHS_COLOR_PALETTE.md` |
| HHS_USWDS_Theme.json | `05_Themes/HHS_USWDS_Theme.json` |
| HHS_Federal_Layout_Theme.json | `05_Themes/HHS_Federal_Layout_Theme.json` |

**Key Colors from Official Palette:**
```
Primary:          #005EA2 (main brand)
Primary Vivid:    #0076D6 (active states, links)
Primary Dark:     #1A4480 (hover states)
Primary Darker:   #162E51 (selected states)

Ink (Text):       #1B1B1B (primary text)
Base Dark:        #565C65 (secondary text)
Base:             #71767A (tertiary text)
Base Lightest:    #F0F0F0 (page background)
White:            #FFFFFF (cards, panels)

Good/Success:     #00A91C (positive trends ▲)
Bad/Error:        #D54309 (negative trends ▼)
Neutral/Warning:  #FFBE2E (caution)
```

### SVG Background Generator (Supports 1920×1080)
| File | Path | Capabilities |
|------|------|--------------|
| **hhs_svg_generator.py** | `04_Generators/utilities/hhs_svg_generator.py` | Generates custom SVG backgrounds with geometric, waves, grid, dots, hexagons, circuits patterns |

### Navigation Icon Automation
| File | Path | Details |
|------|------|---------|
| **add_navigation_icons.py** | `04_Generators/add_navigation_icons.py` | Creates nav buttons with icon positioning (26px x-position, dynamic y) |

### Bookmark Examples
| Location | Path |
|----------|------|
| Press Room Bookmarks | `press-room-dashboard.Report/definition/bookmarks/` |

---

## 1. CORE AUTOMATION SYSTEM

### Blueprint-to-PBIP Pipeline

The repository contains a production-grade **Autopilot** system that generates complete Power BI projects from JSON blueprints.

| Component | Path | Purpose |
|-----------|------|---------|
| **Main Generator** | `04_Generators/generators/generate_from_blueprint.py` | Converts JSON blueprints → complete PBIP folders |
| **Blueprint Schema** | `02_Blueprints/schema.visual_blueprint.v2.json` | JSON schema defining all blueprint properties |
| **Authoring Guide** | `02_Blueprints/AUTHORING_GUIDE.md` | Complete guide to creating blueprints |
| **Example Blueprint** | `02_Blueprints/examples/live_events_6page.json` | Multi-page live events dashboard example |

### Command to Generate Dashboard

```bash
python 04_Generators/generators/generate_from_blueprint.py \
  --blueprint 02_Blueprints/live_events_dashboard.json \
  --output LiveEventsDashboard
```

---

## 2. KEY FILES FOR OUR BUILD

### A. Generator Scripts

| File | Path | What It Does |
|------|------|--------------|
| **generate_from_blueprint.py** | `04_Generators/generators/generate_from_blueprint.py` | Core PBIP generator - creates pages, visuals, queries |
| **create_perfect_frontend.py** | `04_Generators/generators/create_perfect_frontend.py` | Creates complete report frontend with navigation |
| **create_header_elements.py** | `04_Generators/generators/create_header_elements.py` | Generates header/navigation components |
| **generate_visual_library.py** | `04_Generators/generators/generate_visual_library.py` | Creates visual patterns (530+ types) |
| **add_logo_to_pages.py** | `04_Generators/add_logo_to_pages.py` | Programmatic logo insertion |
| **add_navigation_icons.py** | `04_Generators/add_navigation_icons.py` | Navigation icon automation |

### B. Complete Workflow Scripts (Root Level)

| File | Path | What It Does |
|------|------|--------------|
| **build_complete_frontend_from_scratch.py** | Root: `build_complete_frontend_from_scratch.py` | **COMPREHENSIVE** - Creates entire report with all pages, visuals, nav, fixes (38KB) |
| **complete_report_automation.py** | Root: `complete_report_automation.py` | Adds drill-through, tooltips, interactions |
| **final_complete_automation.py** | Root: `final_complete_automation.py` | End-to-end dashboard workflow |
| **enhance_frontend_comprehensive.py** | Root: `enhance_frontend_comprehensive.py` | Frontend enhancements |

### C. PBIP Structure & Validation

| File | Path | What It Does |
|------|------|--------------|
| **PBIR_STRUCTURE_GUIDE.md** | `00_Master_Docs/PBIR_STRUCTURE_GUIDE.md` | Complete PBIP file structure reference |
| **master_pbip_validator.py** | Root: `master_pbip_validator.py` | Master validation system |
| **check_pbip_schema.py** | Root: `check_pbip_schema.py` | Validates .pbip structure |
| **validate_pbip_before_save.py** | Root: `validate_pbip_before_save.py` | Pre-save validation |

### D. SVG Background Generators

| File | Path | What It Does |
|------|------|--------------|
| **hhs_svg_generator.py** | `04_Generators/utilities/hhs_svg_generator.py` | Custom SVG background generation |
| **generate_annotated_backgrounds.py** | `04_Generators/generate_annotated_backgrounds.py` | Creates annotated blueprint SVG backgrounds |
| **generate_clean_backgrounds.py** | `04_Generators/generate_clean_backgrounds.py` | Generates clean page backgrounds |

---

## 3. BLUEPRINT FORMAT FOR OUR DASHBOARD

### Canvas Configuration (1920×1080)

```json
{
  "name": "HHS Live Events Performance Dashboard",
  "version": "2.0",
  "canvas": {
    "width": 1920,
    "height": 1080,
    "unit": "px"
  },
  "theme": {
    "file": "../../05_Themes/HHS_USWDS_Theme.json",
    "colors": {
      "primary": "#005EA2",
      "secondary": "#0076D6",
      "background": "#F0F0F0",
      "text": "#1B1B1B",
      "textSecondary": "#565C65",
      "border": "#DFE1E2",
      "accent": "#E7F2F4",
      "success": "#00A91C",
      "warning": "#FFBE2E",
      "error": "#D83933"
    }
  }
}
```

### Visual Types Supported

| Type | Blueprint Value | Use Case |
|------|-----------------|----------|
| Card | `card` | KPI cards |
| Multi-Row Card | `multiRowCard` | Multiple KPIs |
| Line Chart | `lineChart` | Trends |
| Bar Chart | `barChart`, `clusteredBarChart` | Comparisons |
| Donut Chart | `donutChart` | Parts of whole |
| Table | `table` | Data grids |
| Matrix | `matrix` | Pivot tables |
| Slicer | `slicer` | Filters |
| Text Box | `textbox` | Labels, titles |
| Shape | `shape` | Rectangles, containers |
| Image | `image` | Logos, icons |
| Button | `actionButton` | Navigation, actions |
| Page Navigator | `pageNavigator` | Nav rail |

### Position Object Format

```json
{
  "id": "kpi_sessions",
  "visualType": "card",
  "x": 84,
  "y": 124,
  "w": 295,
  "h": 100,
  "fields": {
    "values": ["[Total Sessions]"]
  },
  "formatting": {
    "background": "#FFFFFF",
    "border": true,
    "borderColor": "#DFE1E2",
    "borderRadius": 4
  }
}
```

---

## 4. MAPPING OUR ELEMENTS TO BLUEPRINT FORMAT

### Navigation Rail (60px wide)

```json
{
  "id": "nav_rail_background",
  "visualType": "shape",
  "x": 0, "y": 0, "w": 60, "h": 1080,
  "formatting": {
    "background": "#FFFFFF",
    "border": false
  }
},
{
  "id": "nav_rail_divider",
  "visualType": "shape",
  "x": 60, "y": 0, "w": 1, "h": 1080,
  "formatting": {
    "background": "#DFE1E2"
  }
}
```

### Active Indicator (per page)

```json
{
  "id": "active_indicator",
  "visualType": "shape",
  "x": 0, "y": 84, "w": 4, "h": 60,
  "formatting": {
    "background": "#005EA2"
  }
}
```

### KPI Cards Row

```json
{
  "type": "kpi_row",
  "y": 124,
  "items": [
    {"id": "kpi_1", "visualType": "card", "x": 84,   "w": 295, "h": 100, "fields": {"values": ["[Total Sessions]"]}},
    {"id": "kpi_2", "visualType": "card", "x": 391,  "w": 295, "h": 100, "fields": {"values": ["[Total Users]"]}},
    {"id": "kpi_3", "visualType": "card", "x": 698,  "w": 295, "h": 100, "fields": {"values": ["[Avg Session Duration]"]}},
    {"id": "kpi_4", "visualType": "card", "x": 1005, "w": 295, "h": 100, "fields": {"values": ["[Total Play Events]"]}}
  ]
}
```

### Visual Containers (White cards with borders)

```json
{
  "id": "container_top_left",
  "visualType": "shape",
  "x": 84, "y": 264, "w": 667, "h": 381,
  "formatting": {
    "background": "#FFFFFF",
    "border": true,
    "borderColor": "#DFE1E2",
    "borderRadius": 4
  }
}
```

### Actions Panel

```json
{
  "id": "actions_panel",
  "visualType": "shape",
  "x": 1448, "y": 201, "w": 400, "h": 412,
  "formatting": {
    "background": "#FFFFFF",
    "border": true,
    "borderColor": "#DFE1E2",
    "borderRadius": 4
  }
},
{
  "id": "actions_accent_bar",
  "visualType": "shape",
  "x": 1448, "y": 201, "w": 4, "h": 412,
  "formatting": {
    "background": "#005EA2",
    "border": false
  }
}
```

---

## 5. COMPLETE BLUEPRINT STRUCTURE FOR LIVE EVENTS

### File to Create: `02_Blueprints/hhs_live_events_1920x1080.json`

```json
{
  "$schema": "../schema.visual_blueprint.v2.json",
  "name": "HHS Live Events Performance Dashboard",
  "version": "2.0",
  "description": "7-page Live Events Dashboard with Actions Panel - 1920x1080",

  "canvas": {
    "width": 1920,
    "height": 1080,
    "unit": "px"
  },

  "theme": {
    "file": "../../05_Themes/HHS_USWDS_Theme.json",
    "colors": {
      "primary": "#005EA2",
      "background": "#F0F0F0",
      "text": "#1B1B1B",
      "textSecondary": "#565C65",
      "border": "#DFE1E2"
    }
  },

  "defaults": {
    "safeMargin": 84,
    "gridAlignment": 12,
    "cardWidth": 295,
    "cardHeight": 100,
    "borderRadius": 4,
    "borderColor": "#DFE1E2",
    "fontFamily": "Segoe UI"
  },

  "layout": {
    "nav": {"x": 0, "y": 0, "w": 60, "h": 1080, "background": "#FFFFFF"},
    "header": {"x": 60, "y": 0, "w": 1860, "h": 96, "background": "#FFFFFF"},
    "content": {"x": 84, "y": 124, "w": 1346, "h": 932, "background": "#F0F0F0"},
    "actionsPanel": {"x": 1448, "y": 201, "w": 400, "h": 412, "background": "#FFFFFF"}
  },

  "globalElements": {
    "navRailBackground": {
      "visualType": "shape",
      "x": 0, "y": 0, "w": 60, "h": 1080,
      "formatting": {"background": "#FFFFFF", "border": false}
    },
    "navRailDivider": {
      "visualType": "shape",
      "x": 60, "y": 0, "w": 1, "h": 1080,
      "formatting": {"background": "#DFE1E2"}
    },
    "headerDivider": {
      "visualType": "shape",
      "x": 84, "y": 96, "w": 1764, "h": 1,
      "formatting": {"background": "#DFE1E2"}
    }
  },

  "pages": [
    {
      "name": "CommandCenter",
      "displayName": "Command Center",
      "layoutMode": "federal",
      "activeIndicatorY": 84,
      "sections": [
        {
          "type": "navigation",
          "items": [
            {"id": "active_indicator", "visualType": "shape", "x": 0, "y": 84, "w": 4, "h": 60, "formatting": {"background": "#005EA2"}}
          ]
        },
        {
          "type": "kpi_row",
          "y": 124,
          "items": [
            {"id": "kpi_sessions", "visualType": "card", "x": 84, "y": 124, "w": 295, "h": 100, "title": "Total Sessions", "fields": {"values": ["[Total Sessions]"]}},
            {"id": "kpi_users", "visualType": "card", "x": 391, "y": 124, "w": 295, "h": 100, "title": "Total Users", "fields": {"values": ["[Total Users]"]}},
            {"id": "kpi_duration", "visualType": "card", "x": 698, "y": 124, "w": 295, "h": 100, "title": "Avg Duration", "fields": {"values": ["[Avg Session Duration]"]}},
            {"id": "kpi_play_events", "visualType": "card", "x": 1005, "y": 124, "w": 295, "h": 100, "title": "Play Events", "fields": {"values": ["[Total Play Events]"]}}
          ]
        },
        {
          "type": "chart_area",
          "items": [
            {"id": "section_header_1", "visualType": "textbox", "x": 84, "y": 240, "w": 400, "h": 28, "title": "Geographic & Device Distribution"},
            {"id": "chart_geography", "visualType": "barChart", "x": 84, "y": 264, "w": 667, "h": 381, "title": "Sessions by City"},
            {"id": "chart_devices", "visualType": "donutChart", "x": 763, "y": 264, "w": 667, "h": 381, "title": "Device Distribution"}
          ]
        },
        {
          "type": "chart_area",
          "items": [
            {"id": "section_header_2", "visualType": "textbox", "x": 84, "y": 660, "w": 400, "h": 28, "title": "Content Performance"},
            {"id": "chart_trend", "visualType": "lineChart", "x": 84, "y": 684, "w": 667, "h": 330, "title": "Sessions Over Time"},
            {"id": "chart_top_content", "visualType": "barChart", "x": 763, "y": 684, "w": 667, "h": 330, "title": "Top Content"}
          ]
        },
        {
          "type": "actions_panel",
          "items": [
            {"id": "actions_container", "visualType": "shape", "x": 1448, "y": 201, "w": 400, "h": 412},
            {"id": "actions_accent", "visualType": "shape", "x": 1448, "y": 201, "w": 4, "h": 412, "formatting": {"background": "#005EA2"}},
            {"id": "actions_title", "visualType": "textbox", "x": 1467, "y": 216, "w": 372, "h": 28, "title": "Recommended Actions"}
          ]
        }
      ]
    }
  ]
}
```

---

## 6. GENERATION WORKFLOW

### Step 1: Create Blueprint JSON
Create `02_Blueprints/hhs_live_events_1920x1080.json` with all 7 pages defined.

### Step 2: Run Generator
```bash
cd C:\Users\farad\Dev\WORK\HHS\repos\auto-the-big-one
python 04_Generators/generators/generate_from_blueprint.py \
  --blueprint 02_Blueprints/hhs_live_events_1920x1080.json \
  --output dashboards/01_Live_Events_Dashboard/LiveEvents
```

### Step 3: Validate Output
```bash
python master_pbip_validator.py dashboards/01_Live_Events_Dashboard/LiveEvents.Report
```

### Step 4: Add Enhancements
```bash
python complete_report_automation.py dashboards/01_Live_Events_Dashboard/LiveEvents.Report
```

---

## 7. FILE STRUCTURE OUTPUT

After generation, the PBIP will have:

```
LiveEvents.Report/
├── definition/
│   ├── report.json              # Report settings, theme binding
│   ├── pages/
│   │   ├── pages.json           # Page index
│   │   ├── CommandCenter/
│   │   │   ├── page.json        # Page settings
│   │   │   └── visuals/
│   │   │       ├── nav_rail_background/visual.json
│   │   │       ├── active_indicator/visual.json
│   │   │       ├── kpi_sessions/visual.json
│   │   │       ├── chart_geography/visual.json
│   │   │       └── ... (all other visuals)
│   │   ├── Explorer/
│   │   ├── TrafficAcquisition/
│   │   ├── PlayEvents/
│   │   ├── ExternalSearch/
│   │   ├── AIInsights/
│   │   └── DeepDive/
│   └── bookmarks/               # Expand/Collapse states
└── StaticResources/
    └── RegisteredResources/     # SVG backgrounds, logos
```

---

## 8. KEY INSIGHTS FOR AUTOMATION

### Shape/Container Creation
The generator creates `shape` visuals with:
- Position (x, y, width, height, z)
- Background color
- Border settings
- No data binding required

### Text Box Creation
For labels and titles:
- `visualType: "textbox"`
- `title` property for text content
- Formatting for font size, color, weight

### Card Creation
For KPIs:
- `visualType: "card"`
- `fields.values` array with measure references
- Formatting for display

### Slicer Creation
For filters:
- `visualType: "slicer"`
- `fields.values` for field binding
- `formatting.slicerType` for style (dropdown, list, tile, dateRange)

---

## 9. NEXT STEPS

1. **Create Full Blueprint** - Define all 7 pages with exact coordinates from V5_TO_1920x1080_TRANSLATION.md
2. **Map Data Fields** - Connect measures from semantic model
3. **Generate PBIP** - Run generator script
4. **Validate & Fix** - Run validators
5. **Add Bookmarks** - Configure Expand/Collapse states
6. **Test in Power BI Desktop** - Open and verify

---

**Document Version:** 1.0
**Created:** 2026-01-18
**Purpose:** Discovery guide for programmatic dashboard generation

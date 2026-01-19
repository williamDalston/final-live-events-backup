# Build Checklist by Page

**Purpose:** Page-by-page checklist with all specs in one place for each page
**Usage:** Work through one page at a time, checking off items as you complete them

---

## Pre-Build Setup (Do Once)

### Theme & Canvas
- [ ] Import `USWDS_Light_Theme.json` (View → Themes → Browse)
- [ ] Canvas size: 1920 × 1080
- [ ] Page background: #F0F0F0
- [ ] Enable gridlines: View → Gridlines
- [ ] Enable snap to grid: View → Snap to grid

### Navigation Rail (Build on Page 1, Copy to All)
Reference: `NATIVE_NAV_AND_HEADER_BUILD_GUIDE.md`

```
RAIL CONTAINER:
  Background:     X: 0, Y: 0, W: 60, H: 1080, Fill: #FFFFFF
  Divider:        X: 60, Y: 0, W: 1, H: 1080, Color: #DFE1E2

BUTTONS (all X: 0, W: 60, H: 60):
  Command Center:         Y: 84
  Explorer:               Y: 164
  Traffic & Acquisition:  Y: 244
  Play Events:            Y: 324
  External Search:        Y: 404
  AI Insights:            Y: 484
  Deep Dive:              Y: 564

BUTTON STATES:
  Default:    Fill: Transparent, Icon: #005EA2
  Hover:      Fill: #D4E5F7, Icon: #1A4480
  Selected:   Fill: #D4E5F7, Icon: #162E51

ACTIVE INDICATOR (per page):
  X: 0, W: 4, H: 60, Fill: #005EA2
  Y = same as current page button
```

### Header Template (Build on Page 1, Update per Page)
**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf"

```
HHS LOGO:     X: 84, Y: 20, W: 36, H: 36
              Image: assets/hhs_logo.svg (or .png)
              Alt text: "U.S. Department of Health and Human Services logo"

EYEBROW:      X: 128, Y: 20, Text: "HHS LIVE EVENTS"
              Font: Segoe UI Regular, 11pt, #565C65
              (positioned right of HHS logo)

PAGE TITLE:   X: 128, Y: 40
              Font: Segoe UI Semibold, 28pt, #1B1B1B
              (positioned right of HHS logo)

DIVIDER:      X: 84, Y: 96, W: 1788, H: 1, Color: #DFE1E2

DATE SLICER:  X: 1672, Y: 26, W: 200, H: 50
              Field: DimDate[Date]
              Style: Between (date range)
              Sync: ALL pages

PAGE PATH:    X: 1472, Y: 26, W: 180, H: 50
              Field: ga4-pages[Page path]
              Style: Dropdown
              (on pages that have this slicer)
```

### Visual Container Templates (V11 Mockup Reference)
**Reference:** V5_PIXEL_GRID_REFERENCE.md - Layout Templates
**Full Translation:** V5_TO_1920x1080_TRANSLATION.md

```
SCALE FACTOR: 1.5× (V5 1280×720 → Power BI 1920×1080)

SECTION LABELS:
  X: 84
  Font: Segoe UI Semibold, 14pt, #1B1B1B
  W: 400, H: 28px
  First Section Y: 240 (V5: 160 × 1.5)
  Second Section Y: 660 (V5: 440 × 1.5)

VISUAL CONTAINERS:
  Fill: #FFFFFF
  Border: 1px #DFE1E2
  Border Radius: 4px
  Shadow: OFF

  INNER STRUCTURE (offsets from container):
    Title:       +12px X, +12px Y, H=24 (12pt Semibold #1B1B1B)
    Subtitle:    +12px X, +40px Y, H=20 (11pt Regular #565C65)
    Visual Area: +18px X, +72px Y, W=container-36, H=container-100

  INNER PLACEHOLDER (optional background shape):
    Fill: #F8F9FA (light gray)
    Shows where Power BI visual sits inside container

CONTENT BOUNDARIES (Expanded State - Actions Panel Visible):
  Content Start X: 84
  Content End X: 1430 (V5: 953 × 1.5)
  Usable Width: 1346px
  Gutter to Panel: 18px
  Panel Start X: 1448

CONTENT BOUNDARIES (Collapsed State - Actions Panel Hidden):
  Content Start X: 84
  Content End X: 1848 (V5: 1232 × 1.5)
  Usable Width: 1764px
  Width Gained: +418px when panel collapsed (400 panel + 18 gutter)

TWO-COLUMN LAYOUT (Expanded, 12px gap):
  Left Container:  X: 84,  W: 667
  Right Container: X: 763, W: 667
  Right Edge: 1430px ✅

TWO-COLUMN LAYOUT (Collapsed, 12px gap):
  Left Container:  X: 84,  W: 876
  Right Container: X: 972, W: 876
  Right Edge: 1848px ✅

THREE-COLUMN LAYOUT (Expanded, 12px gaps):
  Left:   X: 84,  W: 440
  Center: X: 536, W: 440
  Right:  X: 988, W: 442
  Right Edge: 1430px ✅

TOP ROW VISUALS:
  Y: 264 (V5: 176 × 1.5)
  Height: 381px (V5: 254 × 1.5)

BOTTOM ROW VISUALS:
  Y: 684 (V5: 456 × 1.5)
  Height: 330px (V5: 220 × 1.5)
```

### Color Reference (USWDS Aligned)
```
BACKGROUNDS:
  Page/Canvas:    #F0F0F0 (light gray)
  Cards/Panels:   #FFFFFF (white)
  Inner Placeholder: #F8F9FA (subtle gray)
  Hover State:    #E7F2F4 (light teal)

BORDERS:
  Default:        #DFE1E2 (gray)
  Hover:          #0D5C6D (dark teal)

TEXT:
  Primary:        #1B1B1B (titles, values)
  Secondary:      #565C65 (labels, subtitles)
  Tertiary:       #71767A (helper text, disclaimers)

INTERACTIVE:
  Primary Blue:   #005EA2 (links, accent bars, active indicators)
  Hover Blue:     #1A4480
  Active Blue:    #162E51

SEMANTIC:
  Success/Good:   #00A91C (green up arrows)
  Critical/Bad:   #D83933 (red down arrows)
  Warning:        #FFBE2E (amber)
  High Priority:  #D83B01 (red badge)
  Medium Priority: #E5A000 (amber badge)
  Info Priority:  #0076D6 (blue badge)
```

### Manual Shapes to Create (Per Page)
**Reference:** V5_TO_1920x1080_TRANSLATION.md for exact coordinates

```
NAVIGATION RAIL (build once, copy to all pages):
  1. Rail Background:     X: 0, Y: 0, W: 60, H: 1080, Fill: #FFFFFF
  2. Rail Divider:        X: 60, Y: 0, W: 1, H: 1080, Color: #DFE1E2
  3. Active Indicator:    X: 0, W: 4, H: 60, Fill: #005EA2
                          (Y varies by page: 84, 164, 244, 324, 404, 484, 564)

HEADER AREA:
  4. Header Divider:      X: 84, Y: 96, W: 1764, H: 1, Color: #DFE1E2

KPI CARDS (4 shapes):
  5. KPI Card 1:          X: 84,   Y: 124, W: 295, H: 100
  6. KPI Card 2:          X: 391,  Y: 124, W: 295, H: 100
  7. KPI Card 3:          X: 698,  Y: 124, W: 295, H: 100
  8. KPI Card 4:          X: 1005, Y: 124, W: 295, H: 100
     All: Fill #FFFFFF, Border 1px #DFE1E2, Radius 4px

VISUAL CONTAINERS (4 shapes, Expanded State):
  9. Top Left:            X: 84,  Y: 264, W: 667, H: 381
  10. Top Right:          X: 763, Y: 264, W: 667, H: 381
  11. Bottom Left:        X: 84,  Y: 684, W: 667, H: 330
  12. Bottom Right:       X: 763, Y: 684, W: 667, H: 330
      All: Fill #FFFFFF, Border 1px #DFE1E2, Radius 4px

ACTIONS PANEL (group for bookmarks):
  13. Panel Container:    X: 1448, Y: 201, W: 400, H: 412
      Fill: #FFFFFF, Border 1px #DFE1E2, Radius 4px
  14. Accent Bar:         X: 1448, Y: 201, W: 4, H: 412
      Fill: #005EA2, No border
  15. Panel Title:        X: 1467, Y: 216, W: 372, H: 28
      Text: "Recommended Actions", 13pt Semibold #1B1B1B

ACTION CARDS (3 shapes + text):
  16. Card 1:             X: 1470, Y: 258, W: 352, H: 90
  17. Card 2:             X: 1470, Y: 365, W: 352, H: 90
  18. Card 3:             X: 1470, Y: 471, W: 352, H: 90
      All: Fill #FFFFFF, Border 1px #DFE1E2, Radius 4px

  Card Inner Content (per card):
  - Priority Badge:       X+12, Y+8, 9pt Bold UPPERCASE
                          HIGH=#D83B01, MEDIUM=#E5A000, INFO=#0076D6
  - Action Title:         X+12, Y+28, 11pt Semibold #1B1B1B
  - Description:          X+12, Y+50, 10pt Regular #565C65
  - Arrow:                X+W-24, Y+35, "→" 14pt #005EA2

  19. Disclaimer:         X: 1467, Y: 576, W: 361, H: 28
      Text: "AI-generated insights", 9pt Regular #71767A

EXPAND/COLLAPSE BUTTONS:
  20. Expand Button:      X: 1485, Y: 123, W: 159, H: 60
      Text: "Actions ❯", 12pt #005EA2
      Fill: #FFFFFF, Border 1px #DFE1E2, Radius 4px
      Hover: Fill #E7F2F4, Border #0D5C6D

  21. Collapse Button:    X: 1653, Y: 123, W: 159, H: 60
      Text: "❮ Collapse", 12pt #005EA2
      Fill: #FFFFFF, Border 1px #DFE1E2, Radius 4px
      Hover: Fill #E7F2F4, Border #0D5C6D

UTILITY BUTTONS:
  22. Reset Button:       X: 1401, Y: 26, W: 50, H: 50
      Text: "Reset", 11pt #005EA2
      Fill: #FFFFFF, Border 1px #DFE1E2, Radius 4px

  23. Info Button:        X: 1461, Y: 26, W: 50, H: 50
      Text: "i", 12pt Semibold #005EA2
      Fill: #FFFFFF, Border 1px #005EA2, Radius 4px

TOTAL: ~23+ manual shapes per page (before Power BI visuals)
```

### Bookmark Groups for Expand/Collapse
```
GROUP: grp_Actions_Expanded (visible in expanded state)
  - Panel Container (#13)
  - Accent Bar (#14)
  - Panel Title (#15)
  - Action Cards 1-3 (#16-18) + all card content
  - Disclaimer (#19)
  - Collapse Button (#21)
  - (HTML Visual if using for dynamic content)

GROUP: grp_Actions_Collapsed (visible in collapsed state)
  - Expand Button (#20)

BOOKMARK: "Actions_Expanded"
  Display: ON, Data: OFF, Current page: ON
  Visibility: grp_Actions_Expanded=visible, grp_Actions_Collapsed=hidden

BOOKMARK: "Actions_Collapsed"
  Display: ON, Data: OFF, Current page: ON
  Visibility: grp_Actions_Expanded=hidden, grp_Actions_Collapsed=visible

BUTTON ACTIONS:
  - Expand Button → Bookmark: "Actions_Expanded"
  - Collapse Button → Bookmark: "Actions_Collapsed"
```

---

## Page 1: Command Center (Executive Summary)

### Header
- [ ] HHS Logo: X=84, Y=20, 36×36 (assets/hhs_logo.svg)
- [ ] Eyebrow: "HHS LIVE EVENTS" (X=128, right of logo)
- [ ] Title: "Executive Summary" (X=128)
- [ ] Active indicator: Y = 84

### Slicers
**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 1

| Slicer | Field | Position | Size | Style |
|--------|-------|----------|------|-------|
| Date Range | DimDate[Date] | Header left (X: 84, Y: 26) | 200 × 50 | Between dropdown |
| Page Path | ga4-pages[Page path] | Header right (X: 1672, Y: 26) | 200 × 50 | Dropdown |

**Why Page Path:** Allows filtering all visuals to a specific livecast event page

### KPI Cards (Top Row)
**Reference:** V5_PIXEL_GRID_REFERENCE.md - KPI Card Positions (scaled 1.5× from 1280×720)

Build 4 cards with exact positions:
```
KPI ROW:
  Y Position: 124 (scaled from 83)
  Card Width: 295px (4 cards + 3 gaps = 1216px content width)
  Card Height: 100px (scaled from 67)
  Gap Between: 12px

CARD POSITIONS:
  KPI 1: X: 84,   Y: 124, W: 295, H: 100
  KPI 2: X: 391,  Y: 124, W: 295, H: 100
  KPI 3: X: 698,  Y: 124, W: 295, H: 100
  KPI 4: X: 1005, Y: 124, W: 295, H: 100
  Right Edge: 1300px ✅

CARD CONTAINER:
  Background:   #FFFFFF
  Border:       1px #DFE1E2
  Radius:       4px
  Shadow:       OFF

CARD CONTENT LAYOUT:
  Label:        X+12, Y+12, Font: 11pt Regular #565C65
  Value:        X+12, Y+36, Font: 28pt Regular #1B1B1B
  Delta:        X+12, Y+72, Font: 11pt Regular (semantic color + arrow)

DELTA COLORS:
  Positive (▲): #00A91C
  Negative (▼): #D83933
  Neutral (—):  #71767A
```

| KPI | Position | Measure | Expected Source |
|-----|----------|---------|-----------------|
| Total Sessions | X: 84 | [Total Sessions] | ga4-daily ✅ |
| Total Users | X: 391 | [Total Users] | ga4-daily ✅ |
| Avg Session Duration | X: 698 | [Avg Session Duration] | ga4-daily ✅ |
| Total Play Events | X: 1005 | [Total Play Events] | ga4-events ✅ |

### Section Labels & Charts
**Reference:** V5_TO_1920x1080_TRANSLATION.md - Corrected coordinates at 1.5× scale

```
SECTION 1 HEADER: "Geographic & Device Distribution"
  X: 84, Y: 240, W: 400, H: 28
  Font: Segoe UI Semibold, 14pt, #1B1B1B

TOP ROW VISUALS (Two-Column Layout, Expanded State):
  Y: 264 (V5: 176 × 1.5)
  Height: 381px (V5: 254 × 1.5)
  Left Container:  X: 84,  W: 667
  Right Container: X: 763, W: 667
  Gap: 12px
  Right Edge: 1430px (before gutter to Actions panel)

SECTION 2 HEADER: "Content Performance"
  X: 84, Y: 660, W: 400, H: 28
  Font: Segoe UI Semibold, 14pt, #1B1B1B

BOTTOM ROW VISUALS (Two-Column Layout, Expanded State):
  Y: 684 (V5: 456 × 1.5)
  Height: 330px (V5: 220 × 1.5)
  Left Container:  X: 84,  W: 667
  Right Container: X: 763, W: 667
```

**Geographic Distribution (Map/Bar Chart) - TOP LEFT**
```
Container:      X: 84, Y: 264, W: 667, H: 381
Visual Type:    Map or horizontal bar chart
Title:          "Sessions by City" (X: 96, Y: 276, 12pt Semibold #1B1B1B)
Subtitle:       "Top locations by traffic volume" (X: 96, Y: 304, 11pt Regular #565C65)
Inner Visual:   X: 102, Y: 336, W: 631, H: 281

Data:
  Y-Axis:       ga4-geography[City]
  X-Axis:       [Sessions_City]
Bar Color:      #005EA2
Source:         ga4-geography ⚠️ (NOT date-filterable)
Footer:         "All-time data" (9pt #71767A, bottom of container)
```

**Device Breakdown (Donut/Pie) - TOP RIGHT**
```
Container:      X: 763, Y: 264, W: 667, H: 381
Visual Type:    Donut chart
Title:          "Device Distribution" (X: 775, Y: 276, 12pt Semibold #1B1B1B)
Subtitle:       "Sessions by device category" (X: 775, Y: 304, 11pt Regular #565C65)
Inner Visual:   X: 781, Y: 336, W: 631, H: 281

Data:
  Legend:       ga4-devices[Device category]
  Values:       [Sessions_Device]
Colors:         Desktop: #005EA2, Mobile: #1A4480, Tablet: #71767A
Source:         ga4-devices ⚠️ (NOT date-filterable)
Footer:         "All-time data" (9pt #71767A)
```

**Sessions Trend (Line Chart) - BOTTOM LEFT**
```
Container:      X: 84, Y: 684, W: 667, H: 330
Visual Type:    Line chart
Title:          "Sessions Over Time" (X: 96, Y: 696, 12pt Semibold #1B1B1B)
Subtitle:       "Daily session trend" (X: 96, Y: 724, 11pt Regular #565C65)
Inner Visual:   X: 102, Y: 756, W: 631, H: 230

Data:
  X-Axis:       DimDate[Date]
  Y-Axis:       [Total Sessions]
Line Color:     #005EA2
Gridlines:      #DFE1E2, dashed
Source:         ga4-daily ✅ (date filterable)
```

**Top Content (Bar Chart) - BOTTOM RIGHT**
```
Container:      X: 763, Y: 684, W: 667, H: 330
Visual Type:    Horizontal bar chart
Title:          "Top Content" (X: 775, Y: 696, 12pt Semibold #1B1B1B)
Subtitle:       "Most viewed livecast events" (X: 775, Y: 724, 11pt Regular #565C65)
Inner Visual:   X: 781, Y: 756, W: 631, H: 230

Data:
  Y-Axis:       ga4-titles[Page Title (Clean)] or DimLivecast[Livecast Title]
  X-Axis:       [Total Sessions]
Bar Color:      #005EA2
Source:         ga4-pages/ga4-titles ✅
```

### Recommended Actions Panel (Right Side)
**Reference:** V5_TO_1920x1080_TRANSLATION.md - Corrected at 1.5× scale

```
PANEL CONTAINER:
  X: 1448 (V5: 965 × 1.5)
  Y: 201 (V5: 134 × 1.5)
  W: 400 (V5: 267 × 1.5)
  H: 412 (V5: 275 × 1.5)
  Fill: #FFFFFF
  Border: 1px #DFE1E2
  Border Radius: 4px

ACCENT BAR (Left Edge):
  X: 1448
  Y: 201
  W: 4 (3px scaled + 1)
  H: 412
  Fill: #005EA2 (Primary Blue)

TITLE "Recommended Actions":
  X: 1467 (panel X + 19px padding, V5: 978 × 1.5)
  Y: 216 (V5: 144 × 1.5)
  W: 372 (V5: 248 × 1.5)
  H: 28 (V5: 19 × 1.5)
  Font: Segoe UI Semibold, 13pt
  Color: #1B1B1B

ACTION CARDS (3 cards, stacked):
  Card Width: 352px (V5: 235 × 1.5)
  Card Height: 90px (V5: 60 × 1.5)
  Card Gap: 17px

  Card 1: X: 1470, Y: 258 (V5: 980, 172 × 1.5)
  Card 2: X: 1470, Y: 365 (V5: 980, 243 × 1.5)
  Card 3: X: 1470, Y: 471 (V5: 980, 314 × 1.5)

  Card Fill: #FFFFFF
  Card Border: 1px #DFE1E2
  Card Radius: 4px

ACTION CARD CONTENT (offsets from card position):
  Priority Badge:   X+12, Y+8, W: 60, H: 16
    - HIGH: #D83B01 (Red), 9pt Bold UPPERCASE
    - MEDIUM: #E5A000 (Amber), 9pt Bold UPPERCASE
    - INFO: #0076D6 (Blue), 9pt Bold UPPERCASE

  Action Title:     X+12, Y+28, 11pt Semibold #1B1B1B
  Action Desc:      X+12, Y+50, 10pt Regular #565C65
  Arrow:            X+W-24, Y+35, "→" 14pt #005EA2

DISCLAIMER TEXT:
  X: 1467 (V5: 978 × 1.5)
  Y: 576 (V5: 384 × 1.5)
  W: 361 (V5: 241 × 1.5)
  H: 28 (V5: 19 × 1.5)
  Text: "AI-generated insights based on data patterns"
  Font: 9pt Regular #71767A (tertiary)
```

### Expand/Collapse Buttons
**Reference:** V11 Mockup - Header Area (V5_MOCKUP_AUDIT.md)

```
EXPAND BUTTON (visible when panel collapsed):
  X: 1485 (scaled from 990)
  Y: 123 (scaled from 82)
  W: 159
  H: 60
  Fill: #FFFFFF
  Border: 1px #DFE1E2
  Border Radius: 4px
  Text: "Actions ❯" (or "Expand")
  Font: 12pt Regular #005EA2

  HOVER STATE:
    Fill: #E7F2F4
    Border: 1px #0D5C6D

COLLAPSE BUTTON (visible when panel expanded):
  X: 1653 (scaled from 1102)
  Y: 123
  W: 159
  H: 60
  Fill: #FFFFFF
  Border: 1px #DFE1E2
  Border Radius: 4px
  Text: "❮ Collapse" (or just "❮")
  Font: 12pt Regular #005EA2

  HOVER STATE:
    Fill: #E7F2F4
    Border: 1px #0D5C6D

BOOKMARK STATES:
  - "Actions_Expanded": Panel visible, Collapse button visible, Expand button hidden
  - "Actions_Collapsed": Panel hidden, Expand button visible, Collapse button hidden
```

### KPI Card Trend Delta Colors
**Reference:** V11 Mockup - Semantic Colors

```
TREND INDICATORS:
  Positive (▲): #00A91C (Success Green) or #4A7729
  Negative (▼): #D83933 (Critical Red)
  Neutral (—):  #71767A (Tertiary Gray)

DELTA FORMAT:
  Text: "▲ 12% vs prior period" or "▼ 5% MoM"
  Font: 11pt Regular
  Position: Below KPI value, centered
```

### Checklist
- [ ] Nav rail complete with active indicator at Y: 84
- [ ] Header with "Executive Summary" title
- [ ] Date slicer synced and positioned
- [ ] 4 KPI cards formatted consistently
- [ ] KPI cards have trend deltas with semantic colors
- [ ] Sessions trend line chart
- [ ] Top content bar chart
- [ ] Device donut with "All-time" subtitle
- [ ] Traffic sources bar with "All-time" subtitle
- [ ] Recommended Actions panel with 3 action cards
- [ ] Expand/Collapse buttons for Actions panel
- [ ] Panel bookmarks configured (Expanded/Collapsed states)
- [ ] All elements locked in Selection Pane
- [ ] Test: Date slicer filters trend line ✅
- [ ] Test: Expand/Collapse toggle works correctly

---

## Page 2: Explorer (Content Explorer)

### Header
- [ ] Title: "Content Explorer"
- [ ] Active indicator: Y = 164

### Slicers
**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 2

| Slicer | Field | Position | Size | Style |
|--------|-------|----------|------|-------|
| Date Range | DimDate[Date] | Header left (X: 84, Y: 26) | 200 × 50 | Synced dropdown |
| Page Path | ga4-pages[Page path] | Header right (X: 1672, Y: 26) | 200 × 40 | Dropdown |
| Livecast Title | DimLivecast[Livecast Title] | Header right (X: 1672, Y: 70) | 200 × 40 | Dropdown |

**Why both Page Path AND Livecast Title:** Provides maximum flexibility for page-level analysis

### Main Content

**Content Table**
```
Position:       Main content area
Size:           Full width below slicers

COLUMNS:
  - Livecast Title (from DimLivecast or ga4-titles)
  - Total Sessions
  - Total Users
  - Avg Duration
  - Play Events

TABLE STYLING:
  Header BG:        #005EA2
  Header Text:      #FFFFFF, 11pt Semibold
  Body Text:        #1B1B1B, 11pt Regular
  Alternate Rows:   #F0F0F0
  Gridlines:        1px #DFE1E2
  Row Padding:      6

Source: ga4-pages + ga4-titles ✅ (filterable by Livecast)
```

**Supporting Visuals**

| Visual | Field | Source | Date Filterable |
|--------|-------|--------|-----------------|
| Sessions by Page | ga4-pages[Page title] | ga4-pages | Indirect (via DimLivecast) |
| Events by Content | ga4-events[Event name] | ga4-events | ⚠️ Only if relationship exists |

### Checklist
- [ ] Active indicator moved to Y: 164
- [ ] Title changed to "Content Explorer"
- [ ] Livecast dropdown slicer added
- [ ] Content table with proper formatting
- [ ] Table filters when Livecast selected
- [ ] All elements aligned and locked

---

## Page 3: Traffic & Acquisition

### Header
- [ ] Title: "Traffic & Acquisition"
- [ ] Active indicator: Y = 244

### Slicers
**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 4 (Acquisition Channels)

| Slicer | Field | Position | Size | Style |
|--------|-------|----------|------|-------|
| Page Path | ga4-pages[Page path] | Header left (X: 84, Y: 16) | 200 × 40 | Dropdown |
| Date Range | DimDate[Date] | Header left (X: 84, Y: 60) | 200 × 50 | Synced |

**Why Page Path:** Allows users to see traffic sources for a specific livecast page

### Visuals

**Traffic by Channel (Bar Chart)**
```
Y-Axis:         ga4-traffic-source[Session default channel group]
X-Axis:         [Sessions_Source]
Source:         ga4-traffic-source ⚠️ (aggregate, not date-filtered)
Subtitle:       "All-time data (not filtered by date)"
```

**Traffic by Source/Medium (Table)**
```
Columns:        Source/Medium, Sessions, Users, Bounce Rate
Source:         ga4-traffic-source ⚠️ (aggregate)
```

**Sessions Trend by Channel (Line - if ga4-daily has channel)**
```
Check if ga4-daily has channel dimension
If YES: Use for date-filterable channel trend
If NO: Skip this visual or use aggregate data
```

### Data Limitations Note
```
⚠️ IMPORTANT: ga4-traffic-source is pre-aggregated
- Date slicer will NOT filter these visuals
- Add subtitle to each: "All-time data"
- Consider using ga4-daily if channel data available there
```

### Checklist
- [ ] Active indicator at Y: 244
- [ ] Title: "Traffic & Acquisition"
- [ ] Channel group slicer (filters own table only)
- [ ] Traffic by channel bar chart with subtitle
- [ ] Source/medium table
- [ ] "All-time data" subtitles on aggregate visuals
- [ ] Verify what happens when date slicer changes (should see no change)

---

## Page 4: Play Events

### Header
- [ ] Title: "Play Events"
- [ ] Active indicator: Y = 324

### Slicers
**Reference:** Based on "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 3 (Play Events)

| Slicer | Field | Position | Size | Style |
|--------|-------|----------|------|-------|
| Date Range | DimDate[Date] | Header left (X: 84, Y: 26) | 200 × 50 | Synced |
| Livecast Action | DimAction[Action] | Header right (X: 1672, Y: 16) | 200 × 40 | Dropdown |
| Livecast Title | DimLivecast[Livecast Title] | Header right (X: 1672, Y: 60) | 200 × 40 | Dropdown |
| Event Name | ga4-events[Event name] | Content area (X: 84, Y: 480) | 200 × 40 | Dropdown |
| Page Title | ga4-pages[Page title] | Content area (X: 300, Y: 480) | 200 × 40 | Dropdown |

**Why 5 slicers:** Provides comprehensive filtering for play event analysis - header slicers for quick filtering, content area slicers for detailed table filtering

### KPI Cards
| KPI | Measure | Source |
|-----|---------|--------|
| Total Play Events | [Total Play Events] | ga4-events |
| Unique Users Playing | [Play Event Users] | ga4-events |
| Avg Plays per User | [Plays per User] | ga4-events |

### Visuals

**Play Events Timeline**
```
X-Axis:         Date (need to verify source)
Y-Axis:         Play event count
Source:         Need ga4-daily with play events OR time-stamped ga4-events

⚠️ CHECK: Does ga4-events have a Date column?
   If NO: Timeline will show aggregate only
   If YES: Can filter by date
```

**Events by Type (Bar)**
```
Y-Axis:         ga4-events[Event name] (filtered to play-related)
X-Axis:         [Event Count]
Source:         ga4-events
```

**Events by Content (Table)**
```
Rows:           Content title (via ga4-titles relationship)
Columns:        Event name, Count
Source:         ga4-events → ga4-titles ✅
```

### Checklist
- [ ] Active indicator at Y: 324
- [ ] Title: "Play Events"
- [ ] Event type slicer with play-related events
- [ ] KPI cards for play metrics
- [ ] Events by type bar chart
- [ ] Events by content table
- [ ] Test: Livecast slicer filters events (if relationship exists)

---

## Page 5: External Search (GSC)

### Header
- [ ] Title: "External Search"
- [ ] Active indicator: Y = 404

### Slicers
| Slicer | Field | Position | Style |
|--------|-------|----------|-------|
| Date Range | DimDate[Date] | Header | Synced |

### KPI Cards
| KPI | Measure | Source |
|-----|---------|--------|
| Total Clicks | [GSC Clicks] | gsc-chart ✅ |
| Total Impressions | [GSC Impressions] | gsc-chart ✅ |
| Avg CTR | [GSC CTR] | gsc-chart ✅ |
| Avg Position | [GSC Position] | gsc-chart ✅ |

### Visuals

**Search Performance Trend (Line)**
```
X-Axis:         gsc-chart[Date]
Y-Axis:         Clicks, Impressions (dual axis or separate)
Source:         gsc-chart ✅ (date-filterable)
```

**Top Queries (Table)**
```
Rows:           gsc-queries[Query]
Columns:        Clicks, Impressions, CTR, Position
Source:         gsc-queries ⚠️ (verify if date-filterable)
```

**Top Pages (Table)**
```
Rows:           gsc-pages[Page]
Columns:        Clicks, Impressions, CTR, Position
Source:         gsc-pages ⚠️ (verify if date-filterable)
```

### Data Notes
```
✅ gsc-chart: Has Date column, date slicer works
⚠️ gsc-queries, gsc-pages: Verify date columns exist
   If NO date: Add "All-time data" subtitle
```

### Checklist
- [ ] Active indicator at Y: 404
- [ ] Title: "External Search"
- [ ] 4 GSC KPI cards
- [ ] Search trend line chart (date-filterable)
- [ ] Top queries table
- [ ] Top pages table
- [ ] Verify which visuals respond to date slicer

---

## Page 6: AI Insights

### Header
- [ ] Title: "AI Insights"
- [ ] Active indicator: Y = 484

### Slicers
| Slicer | Field | Position | Style |
|--------|-------|----------|-------|
| Date Range | DimDate[Date] | Header | Synced |

### Layout
```
LEFT PANEL (Recommended Actions):
  Position:       X: 84, Y: 110
  Size:           400W × 400H (or taller)
  Background:     #FFFFFF
  Border:         1px #DFE1E2
  Left Accent:    3px #005EA2

  HEADER:
    Text:         "Recommended Actions"
    Font:         Segoe UI Semibold, 14pt, #1B1B1B

  BULLETS (2-5 max):
    Font:         Segoe UI Regular, 11pt
    Title:        #1B1B1B
    Description:  #565C65
    Hover BG:     #D4E5F7

  DISCLAIMER (bottom):
    Text:         "Insights generated from data patterns"
    Font:         11pt Regular #565C65

RIGHT PANEL (Key Metrics / Smart Narrative):
  Position:       Right of actions panel
  Size:           Remaining width
  Content:        Smart Narrative visual or key metrics cards
```

### Checklist
- [ ] Active indicator at Y: 484
- [ ] Title: "AI Insights"
- [ ] Recommended Actions panel with left accent
- [ ] 2-5 action bullets
- [ ] Disclaimer text at bottom
- [ ] Supporting metrics or narrative
- [ ] Hover states on action items

---

## Page 7: Deep Dive (Analysis)

### Header
- [ ] Title: "Deep Dive Analysis"
- [ ] Active indicator: Y = 564

### Slicers
| Slicer | Field | Position | Style |
|--------|-------|----------|-------|
| Date Range | DimDate[Date] | Header | Synced |
| Device | ga4-devices[Device category] | Below header | Button slicer |
| Livecast | DimLivecast[Livecast Title] | Below header | Dropdown |

### Main Visual: Decomposition Tree
```
Position:       Main content area (large)
Size:           ~1200W × 600H

ANALYZE:        [Total Sessions] or [Total Play Events]

EXPLAIN BY (available dimensions):
  - DimLivecast[Livecast Title]
  - ga4-devices[Device category]
  - ga4-geography[City] or [Country]
  - ga4-traffic-source[Session default channel group]
  - DimDate[Month] or [Week]

STYLING:
  Background:   #FFFFFF
  Border:       1px #DFE1E2
  Radius:       4px
  Bars:         Theme colors
```

### Supporting Visuals (smaller)

**Device Breakdown**
```
Source:         ga4-daily-device ✅ (HAS date column!)
Visual:         Bar or donut
Note:           This IS date-filterable unlike ga4-devices
```

**Geographic Distribution**
```
Source:         ga4-geography ⚠️ (no date, aggregate)
Visual:         Map or bar chart
Subtitle:       "All-time data"
```

### Data Notes
```
⚠️ CROSS-FILTER LIMITATION:
  Device slicer filters ga4-devices visuals ONLY
  City data does NOT cross-filter with device
  This is expected - use Decomposition Tree for multi-dimensional analysis

✅ USE ga4-daily-device for date-filterable device analysis
```

### Checklist
- [ ] Active indicator at Y: 564
- [ ] Title: "Deep Dive Analysis"
- [ ] Decomposition Tree as main visual
- [ ] Device button slicer styled correctly
- [ ] ga4-daily-device used for date-filterable device data
- [ ] "All-time data" subtitles on aggregate visuals
- [ ] Verify Decomposition Tree allows drill-down

---

## Post-Build Validation

### Per-Page Checks
For each page, verify:
- [ ] Nav buttons navigate correctly
- [ ] Active indicator matches current page
- [ ] Date slicer synced and functional
- [ ] All visuals have proper styling (4px radius, 1px border, no shadow)
- [ ] Text meets minimum 11pt
- [ ] Colors match theme tokens

### Cross-Page Checks
- [ ] Date slicer selection persists across pages
- [ ] Nav works from every page to every other page
- [ ] Consistent header positioning
- [ ] Consistent card/visual alignment

### Export Tests
- [ ] Export to PDF - all elements crisp
- [ ] Screenshot at 100% zoom - readable
- [ ] No alignment issues or overlapping elements

---

## Quick Reference: What Filters What

| Date Slicer Filters | ✅ YES | ⚠️ NO (Aggregate) |
|---------------------|--------|-------------------|
| ga4-daily | ✅ | |
| ga4-daily-device | ✅ | |
| gsc-chart | ✅ | |
| ga4-devices | | ⚠️ |
| ga4-geography | | ⚠️ |
| ga4-traffic-source | | ⚠️ |
| gsc-queries | | ⚠️ (verify) |
| gsc-pages | | ⚠️ (verify) |

| Livecast Slicer Filters | ✅ YES | ⚠️ Limited |
|-------------------------|--------|------------|
| ga4-pages | ✅ | |
| ga4-titles | ✅ | |
| ga4-events | | ⚠️ (only if relationship exists) |

---

**Document Version:** 1.0
**Created:** 2026-01-18
**Purpose:** Single-page reference while building each dashboard page

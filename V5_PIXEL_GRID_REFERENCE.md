# V5 Power BI Pixel Grid Reference

**Canvas:** 1280 × 720 px
**Conversion:** 1 inch = 64 px (from 20" × 11.25" mockup)

---

## Actions Panel (Expanded State)

### Panel Container (Shape)
| Property | Value |
|----------|-------|
| X | 965 |
| Y | 134 |
| W | 267 |
| H | 275 |
| Fill | #FFFFFF |
| Border | #DFE1E2 (1px) |

### Accent Bar (Shape)
| Property | Value |
|----------|-------|
| X | 965 |
| Y | 134 |
| W | 3 |
| H | 275 |
| Fill | #005EA2 |

### Title "Recommended Actions" (Text Box)
| Property | Value |
|----------|-------|
| X | 978 |
| Y | 144 |
| W | 248 |
| H | 19 |
| Font | 12-13pt, bold |
| Color | #1B1B1B |

### HTML Visual (Action Cards)
| Property | Value |
|----------|-------|
| X | 978 |
| Y | 169 |
| W | 241 |
| H | 230 |

### Action Card Positions (if drawing shapes)
| Card | X | Y | W | H |
|------|---|---|---|---|
| Card 1 | 980 | 172 | 235 | 60 |
| Card 2 | 980 | 243 | 235 | 60 |
| Card 3 | 980 | 314 | 235 | 60 |

### Disclaimer Text
| Property | Value |
|----------|-------|
| X | 978 |
| Y | 384 |
| W | 241 |
| H | 19 |

---

## Expand/Collapse Buttons

### Actions Expand Button
| Property | Value |
|----------|-------|
| X | 990 |
| Y | 82 |
| W | 106 |
| H | 40 |
| Fill | #FFFFFF |
| Border | #DFE1E2 |
| Hover Fill | #E7F2F4 |
| Hover Border | #0D5C6D |

### Actions Collapse Button
| Property | Value |
|----------|-------|
| X | 1102 |
| Y | 82 |
| W | 106 |
| H | 40 |
| Fill | #FFFFFF |
| Border | #DFE1E2 |

---

## Navigation Rail

| Property | Value (px) | Value (in) |
|----------|------------|------------|
| Width | 40 | 0.62" |
| Height | 720 | 11.25" |
| Icon Size | 27 | 0.42" |
| Icon X | 6 | 0.10" |
| First Icon Y | 63 | 0.98" |
| Icon Spacing | 53 | 0.83" |
| Active Indicator W | 3 | 0.04" |

---

## Header Area

| Element | X | Y | W | H |
|---------|---|---|---|---|
| "HHS LIVE EVENTS" label | 56 | 12 | 200 | 13 |
| Page Title | 56 | 21 | 400 | 20 |
| Subtitle | 56 | 47 | 189 | 13 |
| Divider Line | 56 | 64 | 1176 | 1 |

---

## Utility Bar (Top Right)

| Element | X | Y | W | H |
|---------|---|---|---|---|
| Date Slicer | 748 | 29 | 133 | 33 |
| Reset Button | 934 | 17 | 33 | 33 |
| Info Button | 974 | 17 | 33 | 33 |
| Last Refresh Text | 1083 | 31 | 133 | 10 |

---

## KPI Cards Row

| Property | Value (px) | Value (in) |
|----------|------------|------------|
| Row Y | 83 | 1.29" |
| Card Width | 197 | 3.07" |
| Card Height | 67 | 1.04" |
| Gap Between | 8 | 0.12" |
| First Card X | 56 | 0.88" |

### KPI Card Positions
| Card | X | Y | W | H |
|------|---|---|---|---|
| KPI 1 | 56 | 83 | 197 | 67 |
| KPI 2 | 261 | 83 | 197 | 67 |
| KPI 3 | 465 | 83 | 197 | 67 |
| KPI 4 | 670 | 83 | 197 | 67 |

---

## Visual Containers

### Section Labels
| Property | Value |
|----------|-------|
| First Section Y | 160 |
| Second Section Y | 440 |
| Height | 19 |

### Top Row Visuals
| Property | Value (px) | Value (in) |
|----------|------------|------------|
| Y | 176 | 2.75" |
| Height | 254 | 3.96" |

### Bottom Row Visuals
| Property | Value (px) | Value (in) |
|----------|------------|------------|
| Y | 456 | 7.12" |
| Height | 220 | 3.44" |

---

## Content Area Boundaries

### Expanded State (with Actions Panel)
| Property | Value |
|----------|-------|
| Content Start X | 56 |
| Content End X | 953 |
| Usable Width | 897 |

### Collapsed State (no Actions Panel)
| Property | Value |
|----------|-------|
| Content Start X | 56 |
| Content End X | 1232 |
| Usable Width | 1176 |

**Width Gained When Collapsed:** +279 px *(267 panel + 12 gutter)*

### Expanded Content Boundary Rule
- Content zone: **X=56 → 953**
- Drawer gap: **953 → 965** (12 px gutter)
- Actions panel: **965 → 1232**

---

## Layout Templates by Page Type

### Template A: Full-Width Visual (Explorer, Website Performance)
Best for: Matrix, large tables, timelines

**Expanded State:**
| Visual | X | Y | W | H | Right Edge |
|--------|---|---|---|---|------------|
| Main Visual | 56 | 75 | 897 | 234 | 953 |

**Collapsed State:**
| Visual | X | Y | W | H | Right Edge |
|--------|---|---|---|---|------------|
| Main Visual | 56 | 75 | 1176 | 234 | 1232 |

### Template B: 2-Up Layout (Executive Summary, Play Events)
Best for: Map + Chart, two complementary visuals

**Expanded State (2 containers) - Perfect Edge Alignment:**
- Usable width: 897
- Left W: 444, Right W: 445 (distributes 1px remainder)
- Gap: 8

| Container | X | Y | W | H | Right Edge |
|-----------|---|---|---|---|------------|
| Left | 56 | 176 | 444 | 254 | 500 |
| Right | 508 | 176 | 445 | 254 | 953 |

**Collapsed State (2 containers):**
- Usable width: 1176
- Container W: 584 each (exact fit)

| Container | X | Y | W | H | Right Edge |
|-----------|---|---|---|---|------------|
| Left | 56 | 176 | 584 | 254 | 640 |
| Right | 648 | 176 | 584 | 254 | 1232 |

### Template C: 3-Up Layout (Acquisition Channels)
Best for: Multiple small charts

**Expanded State (3 containers) - Perfect Edge Alignment:**
- Usable width: 897
- Left W: 293, Center W: 293, Right W: 295 (distributes 2px remainder)
- Gap: 8

| Container | X | Y | W | H | Right Edge |
|-----------|---|---|---|---|------------|
| Left | 56 | 176 | 293 | 254 | 349 |
| Center | 357 | 176 | 293 | 254 | 650 |
| Right | 658 | 176 | 295 | 254 | 953 |

**Collapsed State (3 containers) - Perfect Edge Alignment:**
- Usable width: 1176
- Left W: 386, Center W: 386, Right W: 388 (distributes 2px remainder)

| Container | X | Y | W | H | Right Edge |
|-----------|---|---|---|---|------------|
| Left | 56 | 176 | 386 | 254 | 442 |
| Center | 450 | 176 | 386 | 254 | 836 |
| Right | 844 | 176 | 388 | 254 | 1232 |

---

## Current Explorer Page (Actual Values from PBIP)

| Visual | Type | X | Y | W | H | Notes |
|--------|------|---|---|---|---|-------|
| Matrix | pivotTable | 55 | 75 | 902 | 234 | **Needs correction: X→56, W→897** |
| Nav Buttons | actionButton | 0 | 161-319 | 42 | 43 | OK |

**Recommended Fix:** Align Matrix to grid (X=56, W=897 expanded / W=1176 collapsed)

---

## Bookmark Groups

### grp_Actions_Expanded (visible in expanded state)
- Panel container shape
- Accent bar shape
- Title textbox
- HTML visual
- Actions Collapse button

### grp_Actions_Collapsed (visible in collapsed state)
- Actions Expand button
- (Optional: 3px accent tab)

### State Behavior Rules
- **Actions panel position is fixed** at (965, 134) - never moves between states
- **Expanded state:** Panel visible, content ends at X=953
- **Collapsed state:** Panel hidden (not repositioned), content extends to X=1232
- **Expand button stays at (990, 82)** in both states (visible in collapsed, hidden in expanded)
- **Collapse button stays at (1102, 82)** in both states (visible in expanded, hidden in collapsed)

### Bookmark Settings (Power BI)
- ✅ Display: ON
- ❌ Data: OFF (prevents slicer/filter state from freezing)
- ✅ Current page: ON
- ✅ Selected visuals: ON (select only the two groups)

---

## Container Inner Padding Rule

For consistent visual placement inside containers (USWDS-aligned):

| Property | Offset | Description |
|----------|--------|-------------|
| Inner X | Container X + 12 | Left padding |
| Inner Y | Container Y + 32 | Top padding (room for title) |
| Inner W | Container W − 24 | Total horizontal padding |
| Inner H | Container H − 44 | Title space + bottom padding |

**Example:** Container at (56, 176, 444, 254)
- Inner visual: X=68, Y=208, W=420, H=210

---

## Coordinate Convention

**Right Edge = X + W** (boundary edge, first pixel after visual)

This is consistent throughout the document. When Power BI shows a visual at X=56, W=444, the right edge coordinate is 500.

---

## Color Reference

| Color | Hex | Usage |
|-------|-----|-------|
| Background | #F0F0F0 | Canvas/outspace |
| White | #FFFFFF | Cards, panels |
| Border Gray | #DFE1E2 | All borders |
| Inner Placeholder | #F8F9FA | Visual placeholder areas |
| HHS Blue | #005EA2 | Active indicators, accent bars |
| Dark Text | #1B1B1B | Titles, values |
| Gray Text | #565C65 | Subtitles, labels |
| Hover Fill | #E7F2F4 | Button hover state |
| Hover Border | #0D5C6D | Button hover border |
| High/Red | #D83B01 | High priority |
| Medium/Amber | #E5A000 | Medium priority |
| Info/Blue | #0076D6 | Info priority |

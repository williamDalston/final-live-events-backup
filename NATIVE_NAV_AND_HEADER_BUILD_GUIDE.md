# Native Navigation Rail & Header Build Guide

**Purpose:** Build the nav rail and page header entirely in Power BI (no background images)
**Time:** 20-30 minutes for first page, 5 minutes to copy to other pages
**Status:** Start Here First - Build this before any content

---

## Why Native (Not Background Images)

| Background Images | Native Power BI |
|-------------------|-----------------|
| Alignment issues when anything shifts | Pixel-perfect control |
| Blurry at different zoom levels | Crisp at any zoom (vector) |
| Can't be interactive | Buttons actually work |
| Export compression artifacts | Clean PDF/PPT exports |
| Maintenance nightmare | Edit directly in Power BI |

---

## Quick Reference (Copy-Paste Ready)

```
NAV RAIL:
  Container:    X: 0, Y: 0, W: 60, H: 1080
  Background:   #FFFFFF
  Divider:      X: 60, Y: 0, W: 1, H: 1080, Color: #DFE1E2

BUTTONS (7 total, 60x60 each):
  X: 0 (all buttons)
  Y: 84, 164, 244, 324, 404, 484, 564 (80px spacing)

ACTIVE INDICATOR:
  X: 0, Y: [matches current page button], W: 4, H: 60
  Color: #005EA2

HEADER AREA:
  Eyebrow:      X: 84, Y: 16
  Page Title:   X: 84, Y: 36
  Divider:      X: 84, Y: 90, W: 1216, H: 1
  Date Slicer:  X: 1650, Y: 24 (top-right)
```

---

## PHASE 1: Navigation Rail Container (5 minutes)

### 1.1 Rail Background

1. **Insert** → Shapes → Rectangle

2. **Position & Size:**
   ```
   X: 0
   Y: 0
   Width: 60
   Height: 1080
   ```

3. **Format → Shape:**
   - Fill: #FFFFFF
   - Transparency: 0%
   - Border/Line: OFF

4. **Format → Effects:**
   - Shadow: OFF
   - Glow: OFF

5. **Organize:**
   - Right-click → Send to back
   - Selection Pane → Rename to `00_Nav_Background`
   - Selection Pane → Lock

### 1.2 Rail Divider Line

1. **Insert** → Shapes → Line (or thin Rectangle)

2. **Position & Size:**
   ```
   X: 60
   Y: 0
   Width: 1
   Height: 1080
   ```

3. **Format → Shape:**
   - Fill/Line: #DFE1E2
   - Weight: 1px

4. **Organize:**
   - Selection Pane → Rename to `00_Nav_Divider`
   - Selection Pane → Position ABOVE background, BELOW buttons
   - Selection Pane → Lock

---

## PHASE 2: Navigation Buttons (10 minutes)

### Icon Options (Choose One)

**Option A: Power BI Built-in Icons (Easiest)**
- Format → Button → Icon → Choose from gallery
- Pros: No external files, always available
- Cons: Limited selection, may not match exact design

**Option B: Custom SVG Icons (Recommended)**
- Download from: https://designsystem.digital.gov/components/icon/
- Or use: Lucide, Heroicons, Material Icons (free, federal-friendly)
- Save as SVG files in project `/assets/` folder
- Pros: Crisp at any size, USWDS-aligned options available

**Option C: Custom PNG Icons**
- Create in Figma/Illustrator at 40x40px @2x (80x80px actual)
- Export as PNG with transparency
- Pros: Full control over design
- Cons: Can blur if scaled

### Button Configuration (Repeat for all 7)

**Create Button 1: Command Center**

1. **Insert** → Buttons → Blank (or Navigator if available)

2. **Position & Size:**
   ```
   X: 0
   Y: 84
   Width: 60
   Height: 60
   ```

3. **Format → Button:**
   - Style: Custom
   - **Action:** Page navigation → "Command Center"

4. **Format → Style → Default:**
   - Fill: Transparent
   - Border: OFF
   - Icon: [Your chosen icon]
   - Icon color: #005EA2
   - Icon size: 24px (centered)

5. **Format → Style → On Hover:**
   - Fill: #D4E5F7
   - Icon color: #1A4480

6. **Format → Style → On Press:**
   - Fill: #D4E5F7
   - Icon color: #162E51

7. **Format → General:**
   - Tooltip: "Command Center"
   - Alt text: "Navigate to Command Center"

8. **Organize:**
   - Selection Pane → Rename to `01_Nav_Button_CommandCenter`

---

### All 7 Button Positions

| # | Page Name | Y Position | Icon Suggestion |
|---|-----------|------------|-----------------|
| 1 | Command Center | 84 | Dashboard / Grid |
| 2 | Explorer | 164 | Search / Compass |
| 3 | Traffic & Acquisition | 244 | Users / Arrow-trending-up |
| 4 | Play Events | 324 | Play-circle / Video |
| 5 | External Search | 404 | Globe / Search |
| 6 | AI Insights | 484 | Sparkles / Lightbulb |
| 7 | Deep Dive | 564 | Layers / Chart-bar |

**Quick Math:** Each button Y = 84 + (button# - 1) × 80

---

### 2.3 Active Indicator (Current Page)

1. **Insert** → Shapes → Rectangle

2. **Position & Size:**
   ```
   X: 0
   Y: [Same as current page's button Y]
   Width: 4
   Height: 60
   ```

   Example: On Command Center page, Y = 84

3. **Format → Shape:**
   - Fill: #005EA2
   - Border: OFF
   - Corner radius: 0px

4. **Organize:**
   - Selection Pane → Rename to `00_Nav_ActiveIndicator`
   - Position: ABOVE background & divider, BELOW buttons
   - Lock

**Important:** Each page needs its own active indicator at the correct Y position:
- Command Center: Y = 84
- Explorer: Y = 164
- Traffic & Acquisition: Y = 244
- Play Events: Y = 324
- External Search: Y = 404
- AI Insights: Y = 484
- Deep Dive: Y = 564

---

## PHASE 3: Page Header (5 minutes)

### 3.1 Eyebrow Label

1. **Insert** → Text box

2. **Position & Size:**
   ```
   X: 84
   Y: 16
   Width: 300
   Height: 20
   ```

3. **Text:** "HHS LIVE EVENTS"

4. **Format → Font:**
   - Font: Segoe UI
   - Size: 11pt
   - Color: #565C65
   - Weight: Regular
   - Transform: None (type as shown)

5. **Format → Background:**
   - Fill: Transparent

6. **Organize:**
   - Selection Pane → Rename to `Header_Eyebrow`
   - Lock

### 3.2 Page Title

1. **Insert** → Text box

2. **Position & Size:**
   ```
   X: 84
   Y: 36
   Width: 500
   Height: 40
   ```

3. **Text:** "Executive Summary" (varies by page - Sentence Case)

4. **Format → Font:**
   - Font: Segoe UI Semibold
   - Size: 28pt
   - Color: #1B1B1B

5. **Format → Background:**
   - Fill: Transparent

6. **Organize:**
   - Selection Pane → Rename to `Header_PageTitle`
   - Lock

### Page Titles by Page

| Page | Title Text |
|------|------------|
| Command Center | Executive Summary |
| Explorer | Content Explorer |
| Traffic & Acquisition | Traffic & Acquisition |
| Play Events | Play Events |
| External Search | External Search |
| AI Insights | AI Insights |
| Deep Dive | Deep Dive Analysis |

### 3.3 Header Divider Line

1. **Insert** → Shapes → Line (or thin Rectangle)

2. **Position & Size:**
   ```
   X: 84
   Y: 90
   Width: 1216 (or to right edge of content area)
   Height: 1
   ```

3. **Format → Shape:**
   - Fill/Line: #DFE1E2
   - Weight: 1px

4. **Organize:**
   - Selection Pane → Rename to `Header_Divider`
   - Lock

### 3.4 Date Slicer (Header Utility Area)

1. **Insert** → Slicer → Field: `DimDate[Date]`

2. **Position & Size:**
   ```
   X: 1650
   Y: 24
   Width: 200
   Height: 50
   ```

3. **Format → Slicer Settings:**
   - Style: Between (date range)
   - Or: Dropdown

4. **Format → Slicer Header:**
   - Title: OFF (or "Date Range")
   - Font: Segoe UI, 11pt, #1B1B1B
   - Background: #FFFFFF

5. **Format → Visual:**
   - Background: #FFFFFF
   - Border: 1px #DFE1E2
   - Border radius: 4px
   - Shadow: OFF

6. **Sync Slicer:**
   - View → Sync slicers
   - Check "Sync" for ALL 7 pages
   - Check "Visible" for ALL 7 pages

7. **Organize:**
   - Selection Pane → Rename to `Header_DateSlicer`

---

## PHASE 4: Copy to Other Pages (5 minutes per page)

### Method A: Copy-Paste Elements

1. Select all nav and header elements (Ctrl+Click each, or use Selection Pane)
2. Ctrl+C to copy
3. Navigate to next page
4. Ctrl+V to paste
5. **Update:**
   - Page title text
   - Active indicator Y position
   - Verify all button actions still work

### Method B: Duplicate Page, Change Content

1. Right-click page tab → Duplicate page
2. Update page title text
3. Move active indicator to correct Y position
4. Update all page-specific content

---

## Selection Pane Z-Order (Bottom to Top)

```
00_Nav_Background          (bottom - behind everything)
00_Nav_Divider             (above background)
00_Nav_ActiveIndicator     (above divider)
01_Nav_Button_CommandCenter
02_Nav_Button_Explorer
03_Nav_Button_TrafficAcquisition
04_Nav_Button_PlayEvents
05_Nav_Button_ExternalSearch
06_Nav_Button_AIInsights
07_Nav_Button_DeepDive     (top of nav stack)
Header_Eyebrow
Header_PageTitle
Header_Divider
Header_DateSlicer
[...rest of page content...]
```

---

## Validation Checklist

### Nav Rail
- [ ] Background is #FFFFFF, full height (1080px)
- [ ] Divider line visible at X=60, color #DFE1E2
- [ ] All 7 buttons visible and evenly spaced
- [ ] Hover state works (background changes to #D4E5F7)
- [ ] Click each button - navigates to correct page
- [ ] Tooltips appear on hover
- [ ] Active indicator shows on correct button for current page
- [ ] Active indicator is #005EA2, 4px wide

### Header
- [ ] Eyebrow: "HHS LIVE EVENTS", 11pt, #565C65
- [ ] Page title: 28pt Semibold, #1B1B1B, Sentence Case
- [ ] Divider line at Y=90, color #DFE1E2
- [ ] Date slicer visible and functional
- [ ] Date slicer synced across all pages

### Export Test
- [ ] Export to PDF - nav and header look crisp
- [ ] Screenshot at 100% - readable
- [ ] No alignment issues

---

## Troubleshooting

### Button won't navigate
- Check Action is set to "Page navigation" (not Bookmark)
- Verify target page name matches exactly (case-sensitive)

### Active indicator not visible
- Check Z-order in Selection Pane (should be above background)
- Verify position overlaps with button (same Y, X=0)

### Icons blurry
- Use SVG instead of PNG
- If PNG, ensure source is 2x resolution (80x80px for 40x40 display)

### Hover state not working
- Verify "On hover" style is configured
- Some visual types don't support hover states

### Date slicer not syncing
- View → Sync slicers → Verify all pages checked
- Delete duplicate slicers on other pages (only ONE should exist)

---

## Icon Resources (Federal-Friendly, Free)

1. **USWDS Icons** (Recommended for federal)
   - https://designsystem.digital.gov/components/icon/
   - Already USWDS-compliant

2. **Lucide Icons**
   - https://lucide.dev/
   - Clean, consistent, MIT license

3. **Heroicons**
   - https://heroicons.com/
   - By Tailwind team, MIT license

4. **Material Symbols**
   - https://fonts.google.com/icons
   - Google, Apache license

**Download as SVG, save to project `/assets/icons/` folder.**

---

**Document Version:** 1.0
**Created:** 2026-01-18
**Purpose:** Replace PowerPoint background images with native Power BI elements

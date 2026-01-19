# Element Styling Guide - HHS Live Events Dashboard

**Date:** 2026-01-18
**Purpose:** Definitive styling specifications for EVERY element in the dashboard
**Status:** ✅ Master Reference - Single Source of Truth

---

## Design Philosophy

**Goal:** Federal government aesthetic that looks like it belongs on HHS.gov

**Principles:**
1. **Flat, not flashy** - No shadows, no glows, no gradients
2. **Consistent, not creative** - Same styling everywhere, no exceptions
3. **Readable, not decorative** - Function over form
4. **Accessible** - WCAG AA compliant (4.5:1 contrast minimum)
5. **Export-ready** - Must look good in PDF, PowerPoint, and Teams screenshots

---

## Design Tokens (Non-Negotiable)

### Color Palette

```
┌─────────────────────────────────────────────────────────────────┐
│ BACKGROUNDS                                                     │
├─────────────────────────────────────────────────────────────────┤
│ Page/Canvas:        #F0F0F0  (Light gray)                       │
│ Cards/Visuals:      #FFFFFF  (White)                            │
│ Table Alternate:    #F0F0F0  (Same as page)                     │
│ Hover:              #D4E5F7  (Light blue)                       │
│ Selected:           #D4E5F7  (Light blue)                       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TEXT                                                            │
├─────────────────────────────────────────────────────────────────┤
│ Primary:            #1B1B1B  (Near black - titles, values)      │
│ Secondary:          #565C65  (Dark gray - labels, subtitles)    │
│ Tertiary:           #71767A  (Medium gray - ON WHITE BG ONLY)   │
│ Inverted:           #FFFFFF  (White - on dark backgrounds)      │
│ Link:               #005EA2  (Blue - clickable text)            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ BORDERS & LINES                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Default Border:     #DFE1E2  (Light gray)                       │
│ Accent Border:      #005EA2  (Blue - for emphasis)              │
│ Divider Line:       #DFE1E2  (Same as border)                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ INTERACTIVE / BRAND                                             │
├─────────────────────────────────────────────────────────────────┤
│ Primary Blue:       #005EA2  (HHS brand - default state)        │
│ Hover Blue:         #1A4480  (Darker - hover state)             │
│ Active Blue:        #162E51  (Darkest - pressed/selected)       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SEMANTIC                                                        │
├─────────────────────────────────────────────────────────────────┤
│ Success/Good:       #00A91C  (Green)                            │
│ Warning:            #FFBE2E  (Amber)                            │
│ Error/Bad:          #D83933  (Red)                              │
│ Neutral:            #71767A  (Gray)                             │
└─────────────────────────────────────────────────────────────────┘

⚠️ ACCESSIBILITY CONTRAST RULES:
┌─────────────────────────────────────────────────────────────────┐
│ #71767A (Tertiary) → ONLY on #FFFFFF backgrounds (4.7:1 ratio)  │
│ #71767A on #F0F0F0 → FAILS WCAG AA (only 3.8:1)                 │
│                                                                 │
│ For text on gray (#F0F0F0) backgrounds, use:                    │
│   • #565C65 (Secondary) for helper/caption text                 │
│   • #1B1B1B (Primary) for all other text                        │
│                                                                 │
│ Minimum text size: 11pt (never use 10pt or smaller)             │
└─────────────────────────────────────────────────────────────────┘
```

### Typography

```
┌─────────────────────────────────────────────────────────────────┐
│ FONT FAMILY: Segoe UI (everywhere, no exceptions)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ PAGE TITLE         28pt    Semibold    #1B1B1B                  │
│ Eyebrow Label      11pt    Regular     #565C65                  │
│ Section Header     14pt    Semibold    #1B1B1B                  │
│ Card Title         14pt    Semibold    #1B1B1B                  │
│ KPI Value          32pt    Regular     #1B1B1B  (28pt if tight) │
│ KPI Label          11pt    Regular     #565C65                  │
│ KPI Delta          11pt    Regular     #71767A (or semantic)    │
│ Table Header       11pt    Semibold    #FFFFFF (on blue bg)     │
│ Table Body         11pt    Regular     #1B1B1B                  │
│ Chart Axis         11pt    Regular     #565C65                  │
│ Chart Legend       11pt    Regular     #565C65                  │
│ Button Text        11pt    Semibold    #1B1B1B                  │
│ Slicer Text        12pt    Regular     #1B1B1B                  │
│ Helper/Caption     11pt    Regular     #565C65  (on gray bg)    │
│ Tooltip            11pt    Regular     #1B1B1B                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Shape & Effects

```
┌─────────────────────────────────────────────────────────────────┐
│ UNIVERSAL RULES (Apply to everything)                           │
├─────────────────────────────────────────────────────────────────┤
│ Border Radius:      4px     (everywhere, NO exceptions)         │
│ Border Width:       1px     (default)                           │
│ Border Color:       #DFE1E2 (default)                           │
│ Shadows:            OFF     (everywhere, NO exceptions)         │
│ Glow:               OFF     (everywhere)                        │
│ Gradients:          OFF     (everywhere)                        │
└─────────────────────────────────────────────────────────────────┘
```

### Spacing

```
┌─────────────────────────────────────────────────────────────────┐
│ SPACING SCALE                                                   │
├─────────────────────────────────────────────────────────────────┤
│ 4px     Micro       Icon to text, badge padding                 │
│ 8px     Small       Element spacing within cards                │
│ 12px    Medium      Card internal padding, gaps between cards   │
│ 16px    Large       Section spacing, major gaps                 │
│ 24px    XL          Page margins, between major sections        │
│ 32px    XXL         Above page title only                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Element-by-Element Specifications

### 1. Page Canvas

```
┌─────────────────────────────────────────────────────────────────┐
│ CANVAS SETTINGS                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Size:               1920px × 1080px (16:9)                      │
│ Canvas Background:  #F0F0F0, 0% transparency                    │
│ Wallpaper:          #F0F0F0, 0% transparency (or 100% transp)   │
│ Background Image:   NONE (never use images)                     │
└─────────────────────────────────────────────────────────────────┘

Power BI Path: Click canvas → Format → Canvas background / Wallpaper
```

---

### 2. Page Header

```
┌─────────────────────────────────────────────────────────────────┐
│ EYEBROW LABEL (above title)                                     │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "HHS LIVE EVENTS"                           │
│ Font:               Segoe UI Regular                            │
│ Size:               11pt                                        │
│ Color:              #565C65                                     │
│ Position:           X: 84px, Y: 16px                            │
│ Transform:          None (not uppercase)                        │
│ Background:         Transparent                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PAGE TITLE                                                      │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "Executive Summary" (varies by page)        │
│ Font:               Segoe UI Semibold                           │
│ Size:               28pt                                        │
│ Color:              #1B1B1B                                     │
│ Position:           X: 84px, Y: 30px                            │
│ Transform:          Sentence Case (NOT uppercase per USWDS)     │
│ Background:         Transparent                                 │
│ Alignment:          Left                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PAGE SUBTITLE (optional)                                        │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "Monitor performance..." (varies by page)   │
│ Font:               Segoe UI Regular                            │
│ Size:               12pt                                        │
│ Color:              #565C65                                     │
│ Position:           X: 84px, Y: 62px                            │
│ Background:         Transparent                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ HEADER DIVIDER LINE                                             │
├─────────────────────────────────────────────────────────────────┤
│ Type:               Rectangle shape (or Line)                   │
│ Position:           X: 84px, Y: 96px                            │
│ Width:              Full content width (to right edge)          │
│ Height:             1px                                         │
│ Fill:               #DFE1E2                                     │
│ Border:             None                                        │
│ Radius:             0px (it's a line)                           │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3. Navigation Rail (Left)

```
┌─────────────────────────────────────────────────────────────────┐
│ RAIL CONTAINER                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Position:           X: 0px, Y: 0px                              │
│ Size:               60px × 1080px (full height)                 │
│ Background:         #FFFFFF                                     │
│ Border Right:       1px solid #DFE1E2                           │
│ Border Radius:      0px (full-height element)                   │
│ Shadow:             OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ NAV BUTTON (each of 7)                                          │
├─────────────────────────────────────────────────────────────────┤
│ Size:               40px × 40px                                 │
│ Position X:         10px (centered in 60px rail)                │
│ First Button Y:     84px                                        │
│ Button Spacing:     56px (vertical gap center-to-center)        │
│                                                                 │
│ DEFAULT STATE:                                                  │
│   Background:       Transparent                                 │
│   Icon Color:       #005EA2                                     │
│   Border:           None                                        │
│                                                                 │
│ HOVER STATE:                                                    │
│   Background:       #D4E5F7                                     │
│   Icon Color:       #1A4480                                     │
│   Border:           None                                        │
│   Cursor:           Pointer                                     │
│                                                                 │
│ SELECTED STATE:                                                 │
│   Background:       #D4E5F7                                     │
│   Icon Color:       #162E51                                     │
│   Left Indicator:   3px bar, #005EA2 (flush left of button)     │
│                                                                 │
│ FOCUS STATE (accessibility):                                    │
│   Outline:          2px solid #005EA2                           │
│   Offset:           2px                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ NAV ACTIVE INDICATOR                                            │
├─────────────────────────────────────────────────────────────────┤
│ Type:               Rectangle shape                             │
│ Size:               3px × 40px                                  │
│ Position:           X: 0px (flush with left edge)               │
│ Fill:               #005EA2                                     │
│ Border:             None                                        │
│ Radius:             0px                                         │
│ Visibility:         Only on current page button                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ NAV TOOLTIP                                                     │
├─────────────────────────────────────────────────────────────────┤
│ Required:           YES (every button must have tooltip)        │
│ Content:            Page name (e.g., "Executive Summary")       │
│ Position:           Right of button                             │
│ Background:         #1B1B1B                                     │
│ Text:               #FFFFFF, 11pt                               │
│ Padding:            4px 8px                                     │
│ Radius:             4px                                         │
│ Delay:              300ms                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4. KPI Cards

```
┌─────────────────────────────────────────────────────────────────┐
│ CARD CONTAINER                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Size:               295px × 100px                               │
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
│ Padding:            12px (all sides)                            │
│ Gap Between Cards:  12px                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ KPI LABEL (category)                                            │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "Sessions", "Page Views", etc.              │
│ Font:               Segoe UI Regular                            │
│ Size:               11pt                                        │
│ Color:              #565C65                                     │
│ Position:           Top of card, left-aligned                   │
│ Transform:          None (not uppercase)                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ KPI VALUE (callout)                                             │
├─────────────────────────────────────────────────────────────────┤
│ Font:               Segoe UI Regular                            │
│ Size:               32pt (theme default), 28pt if space-tight   │
│ Color:              #1B1B1B                                     │
│ Position:           Below label                                 │
│ Display Units:      Auto (K, M) - be consistent across row      │
│ Decimal Places:     0 (whole numbers)                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ KPI DELTA/TREND (optional)                                      │
├─────────────────────────────────────────────────────────────────┤
│ Font:               Segoe UI Regular                            │
│ Size:               11pt                                        │
│ Position:           Below value or right of value               │
│ Format:             "+12.5% MoM" or "▲ 12.5%"                   │
│                                                                 │
│ COLOR RULES:                                                    │
│   Positive:         #00A91C (green) + "▲" or "+"                │
│   Negative:         #D83933 (red) + "▼" or "-"                  │
│   Neutral:          #71767A (gray) + "—"                        │
│   No direction:     #71767A (gray, no arrow)                    │
│                                                                 │
│ IMPORTANT: Only use color if also showing direction indicator   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ KPI ACCENT BAR (optional, for emphasis)                         │
├─────────────────────────────────────────────────────────────────┤
│ Size:               4px × (card height - 8px)                   │
│ Position:           Left edge, inside card                      │
│ Color:              Match trend (green/red/gray) OR #005EA2     │
│ Radius:             2px (top and bottom)                        │
│                                                                 │
│ NOTE: Use sparingly - only for primary KPI or alerts            │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5. Tables

```
┌─────────────────────────────────────────────────────────────────┐
│ TABLE CONTAINER                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
│ Padding:            0px (table fills container)                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TABLE HEADER ROW                                                │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #005EA2 (HHS Blue)                          │
│ Font:               Segoe UI Semibold                           │
│ Size:               11pt                                        │
│ Color:              #FFFFFF (white)                             │
│ Alignment:          Left (text), Right (numbers)                │
│ Padding:            8px horizontal, 6px vertical                │
│ Text Transform:     None                                        │
│ Word Wrap:          ON                                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TABLE BODY ROWS                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Font:               Segoe UI Regular                            │
│ Size:               11pt                                        │
│ Color:              #1B1B1B                                     │
│ Alignment:          Left (text), Right (numbers)                │
│ Padding:            8px horizontal, 4px vertical                │
│ Row Height:         32px minimum                                │
│                                                                 │
│ ALTERNATING ROWS:                                               │
│   Even (0, 2, 4):   #FFFFFF                                     │
│   Odd (1, 3, 5):    #F0F0F0                                     │
│                                                                 │
│ HOVER STATE:                                                    │
│   Background:       #D4E5F7                                     │
│   Text:             #005EA2 (if row is clickable)               │
│                                                                 │
│ SELECTED STATE:                                                 │
│   Background:       #D4E5F7                                     │
│   Border Left:      3px solid #005EA2                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TABLE GRIDLINES                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Horizontal:         ON, 1px, #DFE1E2                            │
│ Vertical:           ON, 1px, #DFE1E2                            │
│ Outer Border:       Handled by container (don't double up)      │
│                                                                 │
│ NOTE: Keep gridlines subtle - they're for alignment, not style  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TABLE TOTALS ROW (if applicable)                                │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #F0F0F0                                     │
│ Font:               Segoe UI Semibold                           │
│ Size:               11pt                                        │
│ Color:              #1B1B1B                                     │
│ Border Top:         2px solid #DFE1E2                           │
└─────────────────────────────────────────────────────────────────┘

Power BI Path:
  Format → Grid → Horizontal/Vertical gridlines
  Format → Column headers → Back color, Font color
  Format → Values → Font color primary/secondary, Back color primary/secondary
```

---

### 6. Bar Charts (Horizontal & Vertical)

```
┌─────────────────────────────────────────────────────────────────┐
│ CHART CONTAINER                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
│ Padding:            12px (all sides)                            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CHART TITLE                                                     │
├─────────────────────────────────────────────────────────────────┤
│ Show:               ON                                          │
│ Font:               Segoe UI Semibold                           │
│ Size:               14pt                                        │
│ Color:              #1B1B1B                                     │
│ Alignment:          Left                                        │
│ Background:         Transparent                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ BARS                                                            │
├─────────────────────────────────────────────────────────────────┤
│ Color (single):     #005EA2                                     │
│ Color (series):     Use data colors palette in order            │
│ Border:             None                                        │
│ Border Radius:      4px (bar ends only - if supported)          │
│ Spacing:            20% (Inner padding in Power BI)             │
│ Min Width:          4px                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ X-AXIS (Category axis for horizontal bars)                      │
├─────────────────────────────────────────────────────────────────┤
│ Title:              OFF (usually not needed)                    │
│ Labels:             ON                                          │
│ Label Font:         Segoe UI Regular, 11pt                      │
│ Label Color:        #565C65                                     │
│ Line:               OFF                                         │
│ Gridlines:          OFF (for bar charts)                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Y-AXIS (Value axis for horizontal bars)                         │
├─────────────────────────────────────────────────────────────────┤
│ Title:              OFF (usually)                               │
│ Labels:             ON                                          │
│ Label Font:         Segoe UI Regular, 11pt                      │
│ Label Color:        #565C65                                     │
│ Line:               OFF                                         │
│ Gridlines:          ON, 1px, #DFE1E2, dashed                    │
│ Start:              0 (always start at zero)                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DATA LABELS                                                     │
├─────────────────────────────────────────────────────────────────┤
│ Show:               Optional (ON if bars are hard to read)      │
│ Font:               Segoe UI Regular, 11pt                      │
│ Color:              #1B1B1B (outside) or #FFFFFF (inside)       │
│ Position:           Outside end (preferred)                     │
│ Background:         OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ LEGEND                                                          │
├─────────────────────────────────────────────────────────────────┤
│ Show:               Only if multiple series                     │
│ Position:           Top or Bottom (be consistent)               │
│ Font:               Segoe UI Regular, 11pt                      │
│ Color:              #565C65                                     │
│ Title:              OFF                                         │
└─────────────────────────────────────────────────────────────────┘

Power BI Path:
  Format → X axis / Y axis → Title, Labels, Gridlines
  Format → Bars/Columns → Colors, Border
  Format → Data labels → Show, Font, Position
```

---

### 7. Line Charts & Area Charts

```
┌─────────────────────────────────────────────────────────────────┐
│ CHART CONTAINER (same as bar charts)                            │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ LINE                                                            │
├─────────────────────────────────────────────────────────────────┤
│ Color (single):     #005EA2                                     │
│ Stroke Width:       2px                                         │
│ Style:              Solid (not dashed)                          │
│ Smoothing:          OFF (sharp corners)                         │
│ Step:               OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ MARKERS (data points)                                           │
├─────────────────────────────────────────────────────────────────┤
│ Show:               OFF (cleaner look)                          │
│ OR if needed:       ON, Circle, 4px, same color as line         │
│                                                                 │
│ HOVER MARKER:                                                   │
│   Show:             ON (appears on hover)                       │
│   Size:             6px                                         │
│   Color:            Same as line                                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ AREA FILL (for area charts only)                                │
├─────────────────────────────────────────────────────────────────┤
│ Show:               ON                                          │
│ Color:              Same as line                                │
│ Transparency:       60% (40% opacity)                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ X-AXIS (usually Date/Time)                                      │
├─────────────────────────────────────────────────────────────────┤
│ Title:              OFF                                         │
│ Labels:             ON                                          │
│ Label Font:         Segoe UI Regular, 11pt, #565C65             │
│ Line:               ON, 1px, #DFE1E2                            │
│ Gridlines:          OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Y-AXIS (Value)                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Title:              OFF                                         │
│ Labels:             ON                                          │
│ Label Font:         Segoe UI Regular, 11pt, #565C65             │
│ Line:               OFF                                         │
│ Gridlines:          ON, 1px, #DFE1E2, dashed (optional)         │
│ Start:              0 (if data allows)                          │
└─────────────────────────────────────────────────────────────────┘
```

---

### 8. Donut/Pie Charts

```
┌─────────────────────────────────────────────────────────────────┐
│ DONUT CONFIGURATION                                             │
├─────────────────────────────────────────────────────────────────┤
│ Inner Radius:       50-60% (donut, not pie)                     │
│ Colors:             Use data colors palette                     │
│ Border:             1px #FFFFFF between slices                  │
│                                                                 │
│ INTERACTION:                                                    │
│   Hover:            Slight pull-out (3px explode)               │
│   Selected:         Pull-out + darker shade                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ LEGEND                                                          │
├─────────────────────────────────────────────────────────────────┤
│ Position:           Right or Bottom                             │
│ Font:               Segoe UI Regular, 11pt, #565C65             │
│ Title:              OFF                                         │
│ Marker Shape:       Circle (matching slice)                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DETAIL LABELS                                                   │
├─────────────────────────────────────────────────────────────────┤
│ Show:               ON (percentage)                             │
│ Position:           Inside or Outside (be consistent)           │
│ Font:               Segoe UI Regular, 11pt                      │
│ Color:              #FFFFFF (inside) or #1B1B1B (outside)       │
│ Format:             0% (no decimals)                            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CENTER LABEL (optional)                                         │
├─────────────────────────────────────────────────────────────────┤
│ Show:               Optional (for total or title)               │
│ Font:               Segoe UI Semibold, 18pt, #1B1B1B            │
│ Background:         Transparent                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 9. Maps

```
┌─────────────────────────────────────────────────────────────────┐
│ MAP CONTAINER                                                   │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ MAP STYLE                                                       │
├─────────────────────────────────────────────────────────────────┤
│ Theme:              Light/Grayscale (matches federal aesthetic) │
│ Zoom:               Auto-fit to data                            │
│ Controls:           ON (zoom buttons)                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ BUBBLES (for bubble maps)                                       │
├─────────────────────────────────────────────────────────────────┤
│ Color:              #005EA2                                     │
│ Transparency:       30% (so overlapping bubbles visible)        │
│ Border:             1px #FFFFFF                                 │
│ Size:               Scaled by value                             │
│ Min Size:           4px                                         │
│ Max Size:           40px                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FILLED MAP (choropleth)                                         │
├─────────────────────────────────────────────────────────────────┤
│ Color Scale:        Sequential (light to dark blue)             │
│   Min:              #D4E5F7 (light blue)                        │
│   Max:              #005EA2 (HHS blue)                          │
│ Border:             1px #FFFFFF                                 │
│ No Data:            #E0E0E0 (light gray)                        │
└─────────────────────────────────────────────────────────────────┘
```

---

### 10. Slicers

```
┌─────────────────────────────────────────────────────────────────┐
│ DROPDOWN SLICER                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
│ Height:             40px                                        │
│                                                                 │
│ HEADER:                                                         │
│   Show:             ON                                          │
│   Font:             Segoe UI Semibold, 11pt                     │
│   Color:            #1B1B1B                                     │
│   Background:       #FFFFFF                                     │
│                                                                 │
│ ITEMS (dropdown list):                                          │
│   Font:             Segoe UI Regular, 12pt                      │
│   Color:            #1B1B1B                                     │
│   Background:       #FFFFFF                                     │
│   Hover:            #D4E5F7                                     │
│   Selected:         #D4E5F7                                     │
│                                                                 │
│ DROPDOWN ARROW:                                                 │
│   Color:            #565C65                                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ BUTTON SLICER (for Device category, etc.)                       │
├─────────────────────────────────────────────────────────────────┤
│ Layout:             Horizontal                                  │
│ Gap Between:        8px                                         │
│                                                                 │
│ EACH BUTTON:                                                    │
│   Padding:          8px 16px                                    │
│   Border Radius:    4px                                         │
│   Font:             Segoe UI Regular, 11pt                      │
│                                                                 │
│   DEFAULT:                                                      │
│     Background:     #F0F0F0                                     │
│     Text:           #565C65                                     │
│     Border:         1px solid #DFE1E2                           │
│                                                                 │
│   HOVER:                                                        │
│     Background:     #D4E5F7                                     │
│     Text:           #1A4480                                     │
│     Border:         1px solid #1A4480                           │
│                                                                 │
│   SELECTED:                                                     │
│     Background:     #005EA2                                     │
│     Text:           #FFFFFF                                     │
│     Border:         1px solid #005EA2                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DATE RANGE SLICER                                               │
├─────────────────────────────────────────────────────────────────┤
│ Style:              Between (shows two date pickers)            │
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Font:               Segoe UI Regular, 12pt, #1B1B1B             │
│ Calendar Icon:      #565C65                                     │
│ Selected Date:      #005EA2 highlight in calendar               │
│ Today:              Subtle indicator (ring or dot)              │
└─────────────────────────────────────────────────────────────────┘

Power BI Path:
  Format → Slicer header → Font, Background
  Format → Items → Font, Background
  Format → Selection → Background (selected)
```

---

### 11. Buttons

```
┌─────────────────────────────────────────────────────────────────┐
│ PRIMARY BUTTON (main actions)                                   │
├─────────────────────────────────────────────────────────────────┤
│ Size:               Fit content, min 80px wide, 36px tall       │
│ Padding:            8px 16px                                    │
│ Border Radius:      4px                                         │
│                                                                 │
│ DEFAULT:                                                        │
│   Background:       #005EA2                                     │
│   Text:             #FFFFFF, Segoe UI Semibold, 11pt            │
│   Border:           None                                        │
│                                                                 │
│ HOVER:                                                          │
│   Background:       #1A4480                                     │
│   Text:             #FFFFFF                                     │
│                                                                 │
│ PRESSED:                                                        │
│   Background:       #162E51                                     │
│   Text:             #FFFFFF                                     │
│                                                                 │
│ DISABLED:                                                       │
│   Background:       #C6CACE                                     │
│   Text:             #71767A                                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECONDARY BUTTON (utility actions)                              │
├─────────────────────────────────────────────────────────────────┤
│ Size:               Same as primary                             │
│ Padding:            8px 16px                                    │
│ Border Radius:      4px                                         │
│                                                                 │
│ DEFAULT:                                                        │
│   Background:       #FFFFFF                                     │
│   Text:             #005EA2, Segoe UI Semibold, 11pt            │
│   Border:           1px solid #005EA2                           │
│                                                                 │
│ HOVER:                                                          │
│   Background:       #D4E5F7                                     │
│   Text:             #1A4480                                     │
│   Border:           1px solid #1A4480                           │
│                                                                 │
│ PRESSED:                                                        │
│   Background:       #D4E5F7                                     │
│   Text:             #162E51                                     │
│   Border:           1px solid #162E51                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ICON BUTTON (Reset, Info, etc.)                                 │
├─────────────────────────────────────────────────────────────────┤
│ Size:               40px × 40px (or 50px × 50px)                │
│ Border Radius:      4px                                         │
│ Icon Size:          20px × 20px (centered)                      │
│                                                                 │
│ DEFAULT:                                                        │
│   Background:       #FFFFFF                                     │
│   Icon:             #005EA2                                     │
│   Border:           1px solid #DFE1E2                           │
│                                                                 │
│ HOVER:                                                          │
│   Background:       #D4E5F7                                     │
│   Icon:             #1A4480                                     │
│   Border:           1px solid #1A4480                           │
│                                                                 │
│ PRESSED:                                                        │
│   Background:       #D4E5F7                                     │
│   Icon:             #162E51                                     │
└─────────────────────────────────────────────────────────────────┘

Power BI Path:
  Format → Button → Style → Apply settings to: Default/On hover/On press
  Format → Shape → Fill, Outline
  Format → Icon → Icon, Size, Padding
  Format → Text → Font, Size, Color
```

---

### 12. Recommended Actions Panel

```
┌─────────────────────────────────────────────────────────────────┐
│ PANEL CONTAINER                                                 │
├─────────────────────────────────────────────────────────────────┤
│ Position:           Right side of page                          │
│ Width:              400px (or ~25% of content width)            │
│ Height:             Content height (not full page)              │
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ACCENT BAR (left edge)                                          │
├─────────────────────────────────────────────────────────────────┤
│ Width:              3px                                         │
│ Height:             Full panel height                           │
│ Color:              #005EA2                                     │
│ Position:           Flush left, inside panel                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PANEL TITLE                                                     │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "Recommended Actions"                       │
│ Font:               Segoe UI Semibold, 14pt                     │
│ Color:              #1B1B1B                                     │
│ Position:           Top of panel, after accent bar indent       │
│ Margin Bottom:      16px                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ACTION CARDS (2-5 items)                                        │
├─────────────────────────────────────────────────────────────────┤
│ Each Card:                                                      │
│   Background:       #FFFFFF                                     │
│   Border:           1px solid #DFE1E2                           │
│   Border Radius:    4px                                         │
│   Padding:          12px                                        │
│   Margin Bottom:    8px                                         │
│                                                                 │
│ Priority Indicator (left edge):                                 │
│   Width:            4px                                         │
│   High:             #D83933 (red)                               │
│   Medium:           #FFBE2E (amber)                             │
│   Info:             #005EA2 (blue)                              │
│                                                                 │
│ Action Title:                                                   │
│   Font:             Segoe UI Semibold, 12pt                     │
│   Color:            #1B1B1B                                     │
│                                                                 │
│ Action Description:                                             │
│   Font:             Segoe UI Regular, 11pt                      │
│   Color:            #565C65                                     │
│   Max Lines:        2 (truncate with ellipsis)                  │
│                                                                 │
│ Hover:                                                          │
│   Background:       #D4E5F7                                     │
│   Cursor:           Pointer (if clickable)                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DISCLAIMER (bottom)                                             │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "Insights generated from data patterns"     │
│ Font:               Segoe UI Regular, 11pt                      │
│ Color:              #565C65 (passes WCAG AA on white panel)     │
│ Position:           Bottom of panel                             │
└─────────────────────────────────────────────────────────────────┘
```

---

### 13. Tooltips

```
┌─────────────────────────────────────────────────────────────────┐
│ STANDARD TOOLTIP (Power BI default)                             │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             Subtle (this is the ONE exception)          │
│ Padding:            8px                                         │
│ Max Width:          300px                                       │
│                                                                 │
│ TITLE:                                                          │
│   Font:             Segoe UI Semibold, 11pt                     │
│   Color:            #1B1B1B                                     │
│                                                                 │
│ VALUE:                                                          │
│   Font:             Segoe UI Regular, 11pt                      │
│   Color:            #1B1B1B                                     │
│                                                                 │
│ LABEL:                                                          │
│   Font:             Segoe UI Regular, 11pt                      │
│   Color:            #565C65                                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ REPORT PAGE TOOLTIP (custom tooltip pages)                      │
├─────────────────────────────────────────────────────────────────┤
│ Page Size:          320px × 200px                               │
│ Background:         #FFFFFF                                     │
│ Contents:           Contextual visuals/text for hover item      │
│ Keep it simple:     1-2 visuals max                             │
└─────────────────────────────────────────────────────────────────┘
```

---

### 14. Section Headers (Text Labels)

```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION HEADER                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Text:               "Key Metrics", "Trends", "Details", etc.    │
│ Font:               Segoe UI Semibold                           │
│ Size:               14pt                                        │
│ Color:              #1B1B1B                                     │
│ Background:         Transparent                                 │
│ Alignment:          Left                                        │
│ Margin Bottom:      8px (to card/visual below)                  │
│ Margin Top:         24px (from previous section)                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION HEADER WITH ACCENT (optional, use sparingly)            │
├─────────────────────────────────────────────────────────────────┤
│ Accent Bar:         3px × (text height), #005EA2                │
│ Position:           Left of text, 8px gap                       │
│ Use Case:           Only for most important section per page    │
└─────────────────────────────────────────────────────────────────┘
```

---

### 15. Cards/Containers (Generic Visual Wrapper)

```
┌─────────────────────────────────────────────────────────────────┐
│ STANDARD CARD (wraps any visual)                                │
├─────────────────────────────────────────────────────────────────┤
│ Background:         #FFFFFF                                     │
│ Border:             1px solid #DFE1E2                           │
│ Border Radius:      4px                                         │
│ Shadow:             OFF                                         │
│ Padding:            12px                                        │
│ Gap Between Cards:  12px                                        │
└─────────────────────────────────────────────────────────────────┘

RULE: One container = One border
      Never put a bordered card inside another bordered card
      Never double-up borders with gridlines
```

---

### 16. Data Colors (Categorical Palette)

```
Use these colors IN ORDER for multi-series charts:

┌─────────────────────────────────────────────────────────────────┐
│ SEQUENTIAL DATA COLORS (for categorical data)                   │
├─────────────────────────────────────────────────────────────────┤
│ 1.  #005EA2  (Primary Blue - HHS brand)                         │
│ 2.  #1A4480  (Navy Blue)                                        │
│ 3.  #0050D8  (Bright Blue)                                      │
│ 4.  #00BDE3  (Cyan)                                             │
│ 5.  #0F6460  (Teal)                                             │
│ 6.  #538200  (Olive Green)                                      │
│ 7.  #00A91C  (Success Green)                                    │
│ 8.  #FFBE2E  (Warning Amber)                                    │
│ 9.  #E17141  (Orange)                                           │
│ 10. #D83933  (Error Red)                                        │
│ 11. #71767A  (Neutral Gray)                                     │
│ 12. #A9AEB1  (Light Gray)                                       │
└─────────────────────────────────────────────────────────────────┘

These are USWDS-aligned colors with good contrast and accessibility.
```

---

## Quick Reference Checklists

### Visual Formatting Checklist

Before marking a visual as "done," verify:

- [ ] Background: #FFFFFF
- [ ] Border: 1px solid #DFE1E2
- [ ] Border Radius: 4px
- [ ] Shadow: OFF
- [ ] Title font: Segoe UI Semibold, 14pt, #1B1B1B
- [ ] Title alignment: Left
- [ ] Title background: Transparent
- [ ] Axis labels: Segoe UI Regular, 11pt, #565C65
- [ ] Gridlines (if shown): 1px, #DFE1E2
- [ ] Legend (if shown): Segoe UI Regular, 11pt, #565C65
- [ ] Data colors: From palette above

### Page Checklist

Before marking a page as "done," verify:

- [ ] Canvas background: #F0F0F0
- [ ] Eyebrow label: 11pt, #565C65
- [ ] Page title: 28pt Semibold, #1B1B1B
- [ ] Header divider: 1px, #DFE1E2
- [ ] All visuals follow formatting checklist above
- [ ] Consistent spacing (12px gaps, 24px margins)
- [ ] All left edges aligned
- [ ] Navigation shows correct active state
- [ ] Date slicer styled and positioned
- [ ] Recommended Actions panel styled (if present)

### Export Test Checklist

- [ ] Export to PDF - looks professional?
- [ ] Export to PowerPoint - readable?
- [ ] Screenshot at 100% - readable in Teams?
- [ ] Print preview - usable in grayscale?

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---------|----------------|------------------|
| Using shadows | Not federal aesthetic | Always OFF |
| Different border radii | Inconsistent | Always 4px |
| Centered titles | Not federal convention | Always left-aligned |
| Heavy borders + gridlines | Double visual weight | Pick one, not both |
| Random colors | Brand violation | Use palette only |
| Uppercase labels | Too aggressive | Sentence case |
| Too many font sizes | Cluttered hierarchy | Stick to type scale |
| Borders on everything | Claustrophobic | Use selectively |

---

## File References

This document consolidates and supersedes:
- VISUAL_SETTINGS_REFERENCE.md (partial overlap)
- FEDERAL_DESIGN_TOKENS_QUICK_REFERENCE.md (tokens only)
- USWDS_LIGHT_IMPLEMENTATION.md (implementation guide)

For theme JSON file, see: `USWDS_Light_Theme.json`

---

**Document Version:** 1.1
**Last Updated:** 2026-01-18
**Status:** ✅ Master Reference - Single Source of Truth

**v1.1 Changes (Accessibility & USWDS Compliance):**
- Changed page titles from UPPERCASE to Sentence Case (per USWDS guidance)
- Changed minimum text size from 10pt to 11pt for accessibility
- Added contrast warning: #71767A only valid on white backgrounds
- Changed hover color from #E7F2F4 to #D4E5F7 for USWDS consistency
- KPI value: 32pt (theme default), use 28pt only if space-constrained
- Updated helper/caption text to use #565C65 on gray backgrounds

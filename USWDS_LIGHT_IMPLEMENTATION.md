# USWDS Light Implementation Guide

**Decision:** USWDS Light theme (official HHS.gov visual language)

**Time Estimate:** ~5 hours typical (range 4-7 hours, depends on custom visual cleanup + nav button tuning)

**Risk:** Very low (aligns with USWDS / HHS.gov conventions)

**Date:** January 10, 2026

---

## 🎯 GOAL

Transform dashboard to match official HHS.gov / USWDS visual language:
- Light backgrounds (#F0F0F0 page, #FFFFFF cards)
- Dark text on light surfaces
- Subtle 1px borders
- Minimal shadows
- 4px corner radius
- USWDS color palette

**DEFINITION OF DONE:**
- ✅ Looks like HHS.gov family
- ✅ Readable at 50% zoom
- ✅ Exports clean to PDF/PPT
- ✅ Consistent across all pages

**CRITICAL NOTE:** Themes provide **defaults, not enforcement**. Existing visuals may keep prior formatting. Expect manual cleanup.

---

## ⚡ QUICK START (30 Minutes - Command Center Only)

**Test the approach on one page first before replicating to all 7.**

### **Step 1: Apply Theme JSON (5 min)**

1. Open Power BI Desktop
2. View → Themes → Browse for themes
3. Select your existing USWDS theme JSON file
4. Click "Apply"

**Theme JSON file location:**

File: `HHS_Theme_USWDS_Aligned.json` (in project root)

**Note:** The theme file has been updated to match the complete USWDS Light specifications below.

```json
{
  "name": "HHS USWDS Light Theme",
  "dataColors": [
    "#005EA2",
    "#1A4480",
    "#0050D8",
    "#00BDE3",
    "#0F6460",
    "#538200",
    "#00A91C",
    "#FFBE2E",
    "#E17141",
    "#D83933",
    "#71767A",
    "#A9AEB1"
  ],
  "background": "#FFFFFF",
  "foreground": "#1B1B1B",
  "tableAccent": "#005EA2",
  "good": "#00A91C",
  "neutral": "#71767A",
  "bad": "#D83933",
  "maximum": "#0050D8",
  "center": "#FFFFFF",
  "minimum": "#E52207",
  "null": "#DCDEE0",
  "textClasses": {
    "callout": {
      "fontSize": 32,
      "fontFace": "Segoe UI",
      "color": "#1B1B1B"
    },
    "title": {
      "fontSize": 18,
      "fontFace": "Segoe UI Semibold",
      "color": "#1B1B1B"
    },
    "header": {
      "fontSize": 14,
      "fontFace": "Segoe UI Semibold",
      "color": "#1B1B1B"
    },
    "label": {
      "fontSize": 11,
      "fontFace": "Segoe UI",
      "color": "#565C65"
    }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background": [
          {
            "color": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "transparency": 0
          }
        ],
        "border": [
          {
            "show": true,
            "color": {
              "solid": {
                "color": "#DFE1E2"
              }
            },
            "radius": 4,
            "weight": 1
          }
        ],
        "shadow": [
          {
            "show": false
          }
        ],
        "visualHeader": [
          {
            "background": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "border": {
              "solid": {
                "color": "transparent"
              }
            }
          }
        ],
        "title": [
          {
            "show": true,
            "fontColor": {
              "solid": {
                "color": "#1B1B1B"
              }
            },
            "background": {
              "solid": {
                "color": "transparent"
              }
            },
            "alignment": "left",
            "fontSize": 14,
            "fontFamily": "Segoe UI Semibold"
          }
        ]
      }
    },
    "page": {
      "*": {
        "background": [
          {
            "color": {
              "solid": {
                "color": "#F0F0F0"
              }
            },
            "transparency": 0
          }
        ],
        "outspace": [
          {
            "color": {
              "solid": {
                "color": "#F0F0F0"
              }
            },
            "transparency": 0
          }
        ]
      }
    },
    "slicer": {
      "*": {
        "general": [
          {
            "outlineColor": {
              "solid": {
                "color": "#DFE1E2"
              }
            },
            "outlineWeight": 1
          }
        ],
        "header": [
          {
            "show": true,
            "fontColor": {
              "solid": {
                "color": "#1B1B1B"
              }
            },
            "background": {
              "solid": {
                "color": "#FFFFFF"
              }
            }
          }
        ],
        "items": [
          {
            "fontColor": {
              "solid": {
                "color": "#1B1B1B"
              }
            },
            "background": {
              "solid": {
                "color": "#FFFFFF"
              }
            }
          }
        ],
        "selection": [
          {
            "selectAllCheckboxEnabled": true,
            "singleSelect": false
          }
        ]
      }
    },
    "card": {
      "*": {
        "categoryLabels": [
          {
            "show": true,
            "color": {
              "solid": {
                "color": "#565C65"
              }
            },
            "fontSize": 11,
            "fontFamily": "Segoe UI"
          }
        ],
        "labels": [
          {
            "color": {
              "solid": {
                "color": "#1B1B1B"
              }
            },
            "fontSize": 32,
            "fontFamily": "Segoe UI"
          }
        ]
      }
    },
    "tableEx": {
      "*": {
        "grid": [
          {
            "gridVertical": true,
            "gridVerticalColor": {
              "solid": {
                "color": "#DFE1E2"
              }
            },
            "gridVerticalWeight": 1,
            "gridHorizontal": true,
            "gridHorizontalColor": {
              "solid": {
                "color": "#DFE1E2"
              }
            },
            "gridHorizontalWeight": 1,
            "rowPadding": 4
          }
        ],
        "columnHeaders": [
          {
            "fontColor": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "backColor": {
              "solid": {
                "color": "#005EA2"
              }
            },
            "fontSize": 11,
            "fontFamily": "Segoe UI Semibold",
            "alignment": "Left"
          }
        ],
        "values": [
          {
            "fontColorPrimary": {
              "solid": {
                "color": "#1B1B1B"
              }
            },
            "backColorPrimary": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "fontColorSecondary": {
              "solid": {
                "color": "#1B1B1B"
              }
            },
            "backColorSecondary": {
              "solid": {
                "color": "#F0F0F0"
              }
            },
            "fontSize": 11,
            "fontFamily": "Segoe UI"
          }
        ]
      }
    }
  }
}
```

Save this file and apply it via View → Themes → Browse for themes.

---

### **Step 2: Set Page Background (2 min)**

1. Click anywhere on canvas (not on a visual)
2. Format page panel → Canvas background
3. **Canvas background:**
   - Color: #F0F0F0
   - Transparency: 0%
4. **Wallpaper:**
   - Color: #F0F0F0 (or transparency 100%)
   - Image: None - **Remove any dark gradient image**

**Note:** Setting both Canvas and Wallpaper prevents export differences in PDF/PowerPoint modes.

---

### **Step 3: Format All Visuals (15 min)**

**Select all visuals on page:**
- **Option A (Safer):** Use Selection Pane (View → Selection Pane), then Shift+click to select only charts/cards/tables
- **Option B:** Drag a selection box around visuals you want to format
- **Avoid:** Ctrl+A (selects everything including shapes/text boxes you may not want to format)

**Format → General → Effects:**

#### **Background:**
- Color: #FFFFFF (White)
- Transparency: 0%

#### **Visual Border:**
- Show: On
- Color: #DFE1E2
- Rounded corners: 4
- Width: 1

**Note:** If you don't see "Rounded corners," check **Format → General → Style** or **Container** (varies by visual type).

**Border Rule:** Use borders on **cards/containers**, but consider turning borders **off** for large "hero" charts if the page starts to feel too boxed-in.

#### **Shadow:**
- Show: Off

**Format → General → Title:**
- Show: On
- Text: [Keep existing]
- Font: Segoe UI Semibold
- Font size: 14
- Font color: #1B1B1B
- Alignment: Left
- Background color: Transparent

---

### **Step 4: Format KPI Cards Specifically (5 min)**

**For each KPI card visual (Sessions, Page Views, etc.):**

**Format → Callout value:**
- Color: #1B1B1B
- Font family: Segoe UI
- Font size: 32
- Display units: None
- Value decimal places: 0

**Format → Category label:**
- Color: #565C65
- Font family: Segoe UI
- Font size: 11

---

### **Step 5: Format Tables (3 min)**

**For each table visual:**

**If table looks "half themed" (headers styled but values not):**
- Format pane → **Reset to default** → Then reapply settings below

**Format → Grid:**
- Vertical grid: On
- Color: #DFE1E2
- Width: 1
- Horizontal grid: On
- Color: #DFE1E2
- Width: 1
- Row padding default: **4**
- **If stakeholder readability is priority:** **6**
- Text size: 11

**Format → Column headers:**
- Font color: #FFFFFF
- Background color: #005EA2
- Font size: 11
- Font family: Segoe UI Semibold
- Alignment: Left

**Format → Values:**
- Font color (primary): #1B1B1B
- Background (primary): #FFFFFF
- Font color (alternate): #1B1B1B
- Background (alternate): #F0F0F0
- Font size: 11
- Font family: Segoe UI

---

## ✅ VALIDATION (Command Center Page)

After completing Steps 1-5, check:

- [ ] Page background is light gray (#F0F0F0)
- [ ] All cards have white backgrounds (#FFFFFF)
- [ ] All cards have subtle gray borders (1px #DFE1E2)
- [ ] Corner radius is 4px (small, not very round)
- [ ] No shadows visible
- [ ] Text is dark (#1B1B1B) on light backgrounds
- [ ] Labels are medium gray (#565C65)
- [ ] Tables have blue headers (#005EA2 background, white text)
- [ ] Overall look feels "official" not "app-like"

**Squint Test:** Zoom to 50%. Can you still read section headers? → Should be YES

**Screenshot Test:** Take a screenshot. Does it look like it belongs on HHS.gov? → Should be YES

**Teams Screen Share Test:** Zoom to 100%, take screenshot, paste into Teams chat, view at actual size (not zoomed). Can you read labels? → Should be YES

---

## 🔄 REPLICATION (Remaining 6 Pages - 3 Hours)

### **Option A: Manual Replication (Most Control)**

**For each of the 6 remaining pages:**

1. Navigate to page
2. Repeat Steps 2-5 above
3. Validate consistency

**Time:** 30-40 min per page × 6 pages = 3-4 hours

---

### **Option B: Format Painter (Faster)**

**Use Power BI's format painter:**

1. On Command Center page, select a formatted visual
2. Home → Format Painter (paintbrush icon)
3. Click on same visual type on another page
4. Repeat for each visual type

**Time:** 20-30 min per page × 6 pages = 2-3 hours

**Note:** Page background must be set manually on each page.

---

### **Option C: Theme JSON Override (Advanced)**

If theme JSON doesn't auto-apply to all visuals:

1. File → Options and settings → Options
2. Report settings → Reset to default theme
3. Re-apply your custom USWDS theme JSON
4. Manually adjust any visuals that didn't update

**Time:** 1-2 hours (but requires troubleshooting)

---

## 🎨 SPECIFIC VISUAL FORMATTING

### **Navigation Buttons (Left Rail)**

**For each nav button:**

**Format → Style → Custom:**
- Fill: #FFFFFF
- Border: 1px solid #DFE1E2
- Radius: 4px

**Format → Icon:**
- Default state: (your base .svg file)
  - Example: `nav_01_command_center.svg`
- On hover: (your hover .svg file)
  - Example: `nav_01_command_center_hover.svg`
- Selected: (your active .svg file)
  - Example: `nav_01_command_center_active.svg`

**Format → Text:**
- Font: Segoe UI
- Size: 11pt
- Color: #1B1B1B
- Alignment: Left

**Recommended Icon Colors (USWDS-aligned):**
- Default state: #005EA2
- Hover state: #1A4480 (darker USWDS blue, more federal than #4A90E2)
- Active/Selected: #162E51 (darkest USWDS blue)

**Note:** If using #4A90E2 for hover/active (from original icon set), it will work fine - just slightly more "SaaS" feel than pure USWDS.

---

### **Utility Buttons (Top Right)**

**For utility buttons (Clear Filters, Refresh, Export, etc.):**

**Format → Style → Custom:**
- Fill: #FFFFFF
- Border: 1px solid #DFE1E2
- Radius: 4px

**Format → Icon:**
- Default: `util_[function].svg`
- Hover: `util_[function]_hover.svg`

**On Click → Action:**
- Set appropriate action (bookmark, reset filters, etc.)

---

### **Date Range Slicer**

**Format → General:**
- Background: #FFFFFF
- Border: 1px solid #DFE1E2
- Radius: 4px

**Format → Header:**
- Font color: #1B1B1B
- Font size: 11pt
- Font family: Segoe UI Semibold

**Format → Items:**
- Font color: #1B1B1B
- Font size: 11pt
- Font family: Segoe UI

**Format → Selection controls:**
- Fill: #005EA2 (when selected)
- Border: #005EA2

---

### **"RECOMMENDED ACTIONS" Panel (Right Column)**

**Option 1: Shape as Background**
1. Insert → Shapes → Rectangle
2. Size: Width to match right column (35% of page width)
3. Height: Full page height
4. Fill: #F0F0F0 (same as page background) OR #FFFFFF (white)
5. Border: 2px solid #005EA2 (left side only)
6. Radius: 4px
7. Send to back (Right-click → Send to back)
8. **IMMEDIATELY LOCK IT:** Selection Pane → Lock icon (prevents accidental movement)

**Option 2: Visual Container**
1. Group all right-column visuals
2. Format group → Background: #F0F0F0 or #FFFFFF
3. Border: 2px solid #005EA2 (accent on left)
4. Radius: 4px

**Text Formatting:**
- Header "RECOMMENDED ACTIONS": #1B1B1B, Segoe UI Semibold, 18pt
- Bullet points: #1B1B1B, Segoe UI, 11pt, line-height 1.6
- Bullet icons: #005EA2

---

## 🎯 FEDERAL DESIGN TOKENS (Non-Negotiable Global Rules)

**Goal:** Make it undeniably federal - looks like it could live inside an HHS.gov ecosystem page, exports cleanly to PDF/PPT, and still feels modern.

**Principles:** Flatter surfaces, fewer effects, ruthless consistency, readability over vibes.

---

### **1. COLOR TOKENS (Lock These First)**

```
Page Background:  #F0F0F0
Card Background:  #FFFFFF
Border:           #DFE1E2 (1px)
Primary Text:     #1B1B1B
Secondary Text:   #565C65
Tertiary/Helper:  #71767A
Primary Blue:     #005EA2
Hover Blue:       #1A4480
Active Blue:      #162E51
Good/Success:     #00A91C
Bad/Critical:     #D83933
Warning:          #FFBE2E
```

**⚠️ CRITICAL:** Once these are consistent across all 7 pages, the whole report snaps into "official product."

---

### **2. SHAPE + DEPTH TOKENS**

```
Radius Everywhere:  4px (NO exceptions)
Shadows:            OFF (everywhere, unless one tiny exception later)
Glow/Inner Shadow:  OFF
Border Weight:      1px default
```

**Rule:** One container = one border. No double frames, no inset panels unless truly necessary (like table header bands).

---

### **3. SPACING TOKENS (Pick One Base Unit & Stick To It)**

```
Outer Page Padding:    24px
Between Sections:      16px
Inside Card Padding:   12-16px (choose one and stay consistent)
KPI Card Gaps:         12px
Section Header Offset: 8-12px above card group
```

**Power BI Tip:** View tab → Gridlines + Snap to grid. Then lock everything in Selection Pane once aligned.

---

### **4. TYPOGRAPHY TOKENS (Segoe UI Family)**

```
Page Title:        24-28pt, Semibold, #1B1B1B
Section Header:    14pt, Semibold, #1B1B1B
Card Label:        11pt, Regular, #565C65 (secondary text)
KPI Value:         28-32pt, Regular, #1B1B1B
Table Body:        11-12pt, Regular, #1B1B1B
Helper Text:       10-11pt, Regular, #71767A (tertiary)
Eyebrow Label:     11pt, Regular, #565C65 (above page title)
```

**Power BI Tip:** Set display units intentionally (K/M) and be consistent across KPI row.

---

## 📊 COLOR REFERENCE (Quick Copy-Paste)

### **Backgrounds:**
```
Page: #F0F0F0
Visuals: #FFFFFF
Alternate rows (tables): #F0F0F0
```

### **Text:**
```
Primary (titles, values): #1B1B1B
Secondary (labels): #565C65
Tertiary (helper text): #71767A
```

### **Borders:**
```
Default: #DFE1E2
Accent: #005EA2
```

### **Interactive Elements:**
```
Default: #005EA2 (USWDS Blue)
Hover: #1A4480 (Darker USWDS Blue)
Selected: #162E51 (Darkest USWDS Blue)

Note: Original icon set uses #4A90E2 for hover/active - works fine, slightly more SaaS feel
```

### **Semantic Colors:**
```
Positive/Good: #00A91C
Negative/Bad: #D83933
Warning: #FFBE2E
Neutral: #71767A
```

### **Table Headers:**
```
Background: #005EA2
Text: #FFFFFF
```

---

## 🎯 PAGE-BY-PAGE CHECKLIST

**Use this to track progress:**

### **Page 1: Command Center** ✅
- [ ] Theme JSON applied
- [ ] Page background: #F0F0F0
- [ ] All visuals: white backgrounds, gray borders, 4px radius
- [ ] KPI cards formatted
- [ ] Tables formatted
- [ ] Navigation buttons formatted
- [ ] Right column formatted
- [ ] Validated (screenshot test)

### **Page 2: Explorer**
- [ ] Page background: #F0F0F0
- [ ] All visuals formatted (copy from Command Center)
- [ ] Navigation buttons show active state when on this page
- [ ] Right column formatted
- [ ] Validated

### **Page 3: Traffic & Acquisition**
- [ ] Page background: #F0F0F0
- [ ] All visuals formatted
- [ ] Navigation buttons show active state
- [ ] Right column formatted
- [ ] Validated

### **Page 4: Play Events**
- [ ] Page background: #F0F0F0
- [ ] All visuals formatted
- [ ] Navigation buttons show active state
- [ ] Right column formatted
- [ ] Validated

### **Page 5: External Search**
- [ ] Page background: #F0F0F0
- [ ] All visuals formatted
- [ ] Navigation buttons show active state
- [ ] Right column formatted
- [ ] Validated

### **Page 6: AI Insights / Pattern Diagnostics**
- [ ] Page background: #F0F0F0
- [ ] All visuals formatted
- [ ] Navigation buttons show active state
- [ ] Right column formatted
- [ ] Disclaimer text formatted (#71767A, 10pt)
- [ ] Validated

### **Page 7: Deep Dive**
- [ ] Page background: #F0F0F0
- [ ] All visuals formatted
- [ ] Breadcrumb navigation formatted
- [ ] Filter pills formatted
- [ ] Field Parameter dropdown formatted
- [ ] Back button formatted
- [ ] Validated

---

## 🎯 "100% FEDERAL" DESIGN TOKENS (Complete Federal UI Spec)

**Goal:** Make it undeniably federal - looks like it could live inside an HHS.gov ecosystem page, export cleanly to PDF/PPT, and still feels modern.

**Principles:** Flatter surfaces, fewer effects, ruthless consistency, readability over vibes.

---

### **1. LOCK THE DESIGN TOKENS (Global Rules - Non-Negotiables)**

Once these are consistent, the whole report snaps into "official product."

#### **Color Tokens:**
```
Page Background:  #F0F0F0
Card Background:  #FFFFFF
Border:           #DFE1E2 (1px)
Primary Text:     #1B1B1B
Secondary Text:   #565C65
Tertiary/Helper:  #71767A
Primary Blue:     #005EA2
Hover Blue:       #1A4480
Active Blue:      #162E51
Good/Success:     #00A91C
Bad/Critical:     #D83933
Warning:          #FFBE2E
```

#### **Shape + Depth Tokens:**
```
Radius Everywhere:  4px (NO exceptions)
Shadows:            OFF (everywhere, unless one tiny exception later)
Glow/Inner Shadow:  OFF
Border Weight:      1px default
```

#### **Spacing Tokens (Pick One Base Unit & Stick To It):**
```
Outer Page Padding:    24px
Between Sections:      16px
Inside Card Padding:   12-16px (choose one and stay consistent)
KPI Card Gaps:         12px
Section Header Offset: 8-12px above card group
```

#### **Typography Tokens (Segoe UI Family):**
```
Page Title:        24-28pt, Semibold, #1B1B1B
Section Header:    14pt, Semibold, #1B1B1B
Card Label:        11pt, Regular, #565C65 (secondary text)
KPI Value:         28-32pt, Regular, #1B1B1B
Table Body:        11-12pt, Regular, #1B1B1B
Helper Text:       10-11pt, Regular, #71767A (tertiary)
Eyebrow Label:     11pt, Regular, #565C65 (above page title)
```

**Power BI Tip:** View tab → Gridlines + Snap to grid. Lock everything in Selection Pane once aligned.

---

### **2. PAGE SHELL LAYOUT (Make It "Federal UI", Not "Slide Cover")**

#### **Header Area:**
**Do this:**
- Left align everything
- Put small eyebrow label above title: "HHS LIVE EVENTS" (11pt, #565C65)
- Main page title: "COMMAND CENTER" (24-28pt Semibold, #1B1B1B)
- Single subtle divider line under header: 1px #DFE1E2 spanning content width

**Avoid:**
- Centered mega titles
- Thick rules
- Gradients behind header

#### **Canvas Background:**
- **Canvas:** #F0F0F0, 0% transparency
- **Wallpaper:** Same or 100% transparent, but be consistent across pages
- Remove any background images for final

---

### **3. KILL THE "DOUBLE FRAME" EFFECT (Biggest Polish Win)**

**Rule:** One container = one border.

**Container Rule:**
- Outer border: 1px #DFE1E2
- Radius: 4px
- Fill: #FFFFFF
- No inner frame unless it's a table header band or true sub-section

**If you want a "header strip" inside a card:**
- Use a **text label** floating above the card instead of inset panel
- Or use very subtle header band: background #F9F9F9 (optional), no border, just padding

---

### **4. KPI ROW (Make It Look Like USWDS Cards)**

**For each KPI card:**
- Background: #FFFFFF
- Border: 1px #DFE1E2
- Radius: 4px
- Shadow: OFF

**Text:**
- Label (Sessions): 11pt, #565C65
- Value: 28-32pt, #1B1B1B
- Delta: 11pt, #71767A
- Only use green/red if it's truly directional and you also include an arrow or +/-

**Power BI Tip:** Set display units intentionally (K/M), but be consistent across KPI row.

---

### **5. SECTION HEADERS (Your Narrative "Spine")**

This is how you make it feel like an "official briefing tool" instead of "charts on a page."

**Use section headers like:**
- Key Performance Indicators
- Trends
- Breakdowns
- Details
- Recommended Actions

**Spec:**
- 14pt Semibold, #1B1B1B
- Left aligned
- 8-12px above its card group

**Optional:** Tiny left accent rule (very subtle):
- 3px wide rectangle in #005EA2, height equal to text height
- Use sparingly, only for most important sections

---

### **6. CHARTS (Clean + Readable)**

**Chart Formatting:**
- Gridlines: Very light #DFE1E2 or OFF
- Axis labels: #565C65
- Axis titles: Usually OFF unless needed
- Data labels: Only where it helps, not everywhere
- Legend: Top or bottom, consistent across pages
- Avoid heavy borders inside charts

**Trend Charts:**
- Don't box the plot area with a border if the card already has one
- Keep whitespace around the plot so it doesn't feel cramped

---

### **7. TABLES (Make Them Look Like a Gov Report)**

Tables are where "printability" matters most.

**Spec:**
- Header background: #005EA2
- Header text: #FFFFFF, 11pt Semibold
- Body text: #1B1B1B, 11pt Regular
- Alternate rows: #F0F0F0
- Gridlines: 1px #DFE1E2
- Row padding: 6 (if it feels tight at 4)

**Avoid:**
- Very dark zebra striping
- Heavy borders + heavy gridlines together

---

### **8. NAVIGATION RAIL (Make Icons-Only Feel "Government Safe")**

Icons-only is fine if it's implemented like a serious system.

**Rail Container:**
- Background: #FFFFFF
- Border: 1px #DFE1E2
- Radius: 4px (or no radius if full-height rail, but keep consistent)

**Button States (Must Be Obvious):**
- Default icon: #005EA2
- Hover icon: #1A4480
- Selected icon: #162E51
- Selected indicator: 3-4px left bar in #005EA2

**Accessibility Must-Haves:**
- Add tooltips for every icon
- Ensure focus state is visible (if Power BI focus outline is weak, simulate with 2px outline in #005EA2 via bookmarks)

**Most "Federal" Upgrade:**
- Icon + short label (11pt) on the rail
- Even tiny labels dramatically reduce "mystery-meat navigation"

---

### **9. "RECOMMENDED ACTIONS" PANEL (Make It the Hero, Not an Afterthought)**

This is where your dashboard becomes a decision tool.

**Panel Styling:**
- Background: #FFFFFF
- Border: 1px #DFE1E2
- Left accent rule: 3px #005EA2
- Title: "Recommended Actions" 14-16pt Semibold

**Content Format:**
Use 2-5 bullets maximum, each bullet must be:
- One sentence
- Action verb first
- Measurable if possible

**Example Pattern:**
- "Investigate spike in traffic from X on Jan 08."
- "Fix URL canonicalization for Y to consolidate metrics."
- "Monitor play event Z, engagement down 12% WoW."

---

### **10. GET RUTHLESS ABOUT ALIGNMENT (This Is What Makes It Feel "Real")**

This is the hidden superpower.

**Do a pass where you enforce:**
- All left edges aligned to same x
- Consistent card heights within a row
- Consistent gutter spacing
- Consistent title offsets

**Power BI Trick:** View tab → Gridlines + Snap to grid. Then lock everything in Selection Pane once aligned.

---

### **11. EXPORT-PROOFING (PDF/PPT)**

**Before you declare victory:**
- Test Export to PDF
- Test Export to PPT
- Screenshot at 100% and paste into Teams

**Fixes if export looks "off":**
- Make Canvas + Wallpaper consistent (already noted above)
- Avoid transparency-heavy overlays
- Avoid background images (they compress weirdly)

---

### **12. FINAL QUALITY CHECKLIST (The "100%" Gate)**

**If all these are true, you're done:**

✅ Every card has the same radius (4px) and border (1px #DFE1E2)  
✅ No shadows or inner glows anywhere  
✅ Page titles left-aligned and consistent size  
✅ Section headers exist and guide the eye  
✅ Tables readable at 100% on Teams  
✅ Nav has clear selected state + tooltips  
✅ Actions panel contains 2-5 crisp bullets  
✅ No double frames / inset panels unless truly necessary  
✅ All left edges aligned to same x  
✅ Consistent card heights within rows  
✅ Consistent gutter spacing  
✅ Consistent title offsets  
✅ Export to PDF/PPT looks professional  
✅ Screenshot at 100% is readable in Teams  

---

### **ORDER OF OPERATIONS (What I'd Do First)**

1. **Set radius/border/shadow rules everywhere**
2. **Remove double frames and inset containers**
3. **Normalize header/title alignment and sizes**
4. **Make nav states + tooltips perfect**
5. **Tune tables for readability**
6. **Add section headers across pages**
7. **Export tests and tiny adjustments**

---

### **🎯 THE "100%" PUNCH LIST**

If you upload one "filled" page (with real visuals, not placeholders), use this format for feedback:

**Example Punch List Format:**
- "This border off" → Specific border to remove
- "This padding to 16" → Specific element and spacing
- "This header move left 24px" → Specific alignment fix

Once one page is locked as the template, the other 6 pages become fast, mechanical replication.

---

## 🚀 FINAL VALIDATION (All 7 Pages)

### **Consistency Check:**
- [ ] Navigate through all 7 pages - does each feel like same system?
- [ ] All page backgrounds are #F0F0F0
- [ ] All card backgrounds are #FFFFFF
- [ ] All borders are 1px #DFE1E2
- [ ] All radius is 4px
- [ ] No shadows visible
- [ ] Text colors consistent (#1B1B1B, #565C65)

### **Navigation Test:**
- [ ] Click through all 7 nav buttons
- [ ] Active state shows correctly on each page (filled icon + vertical bar)
- [ ] Hover states work on all buttons
- [ ] Back button works from Deep Dive page

### **Export Test:**
- [ ] Export to PDF - looks professional? ✅
- [ ] Export to PowerPoint - readable? ✅
- [ ] Save as image - high quality? ✅
- [ ] Print preview - usable in grayscale? ✅

### **Presentation Mode Test (Conference Room Reality):**
- [ ] Zoom to 100%, take screenshot, paste into Teams
- [ ] View at actual size in Teams (not zoomed)
- [ ] Can elderly stakeholders read helper text? ✅
- [ ] If any text disappears → Increase contrast/size

### **Accessibility Test:**
- [ ] Use WebAIM Contrast Checker on key text
  - Page title (#1B1B1B on #F0F0F0): Should be >7:1 ✅
  - Labels (#565C65 on #FFFFFF): Should be >4.5:1 ✅
  - Table headers (#FFFFFF on #005EA2): Should be >4.5:1 ✅
- [ ] Tab through interactive elements - logical order? ✅
- [ ] Test with screen reader (if available)

### **Stakeholder Readiness:**
- [ ] Take screenshot of Command Center page
- [ ] Show to non-designer colleague
- [ ] Ask: "Does this look official?" → Answer should be YES
- [ ] Ask: "Is text readable?" → Answer should be YES
- [ ] If both YES → Ready for stakeholder showing ✅

---

## 💡 TIPS & TRICKS

### **Faster Formatting:**
1. Format one KPI card perfectly
2. Right-click → Copy formatting
3. Select all other KPI cards → Right-click → Paste formatting

### **Lock Critical Shapes Early:**
Lock background shapes and right-column containers IMMEDIATELY after positioning:
- View → Selection pane
- Lock icon next to shape/container name
- Prevents accidental movement that breaks alignment

### **Save Incremental Versions:**
- Save as: `HHS_Dashboard_v1_USWDS_Light_CommandCenter.pbix`
- After each page: `...v2_Explorer.pbix`, etc.
- Allows rollback if formatting breaks

### **Test on Different Screens:**
- Laptop screen (your default)
- External monitor (conference room simulation)
- Zoom/Teams screen share (if possible)

---

## 📋 COMMON ISSUES & FIXES

### **Issue: Theme doesn't apply to all visuals**
**Fix:** Manually format visuals using format pane. Theme JSON provides defaults, not overrides.

### **Issue: Icons look blurry or thin on white background**
**Fix:**
- Your icons use #005EA2 and #4A90E2 - both have good contrast on white
- If blurry: Increase SVG viewBox or icon size in button settings
- **If icons feel thin:** Increase SVG **stroke-width** slightly (e.g., from 1.5 to 2). That's often the fix, more than viewBox.

### **Issue: Right column doesn't stand out**
**Fix:**
- Option A: Keep background same (#F0F0F0 or #FFFFFF) but add 2px #005EA2 left border
- Option B: Use very subtle background difference (#F9F9F9 vs #FFFFFF)

### **Issue: Tables feel cramped**
**Fix:**
- Increase row padding: Format → Grid → Row padding: 6 (from 4)
- Increase font size: Format → Values → Font size: 12 (from 11)

### **Issue: KPI values too large**
**Fix:** Reduce font size: Format → Callout value → Font size: 28 (from 32)

### **Issue: Page feels too "flat"**
**Fix:** This is intentional for government aesthetic. If you must add depth:
- Add very subtle shadow: 1px blur, 1px distance, 95% transparency
- Use #DFE1E2 borders consistently
- Rely on spacing/whitespace for hierarchy

---

## 🎯 SUCCESS METRICS

**You've succeeded when:**

✅ **Visual Quality:**
- Design looks "official" not "custom app"
- Hierarchy clear without shadows
- Text readable at 50% zoom
- Consistent across all 7 pages

✅ **Technical Quality:**
- All formatting from theme JSON or manual settings
- No visual glitches or misalignments
- Fast page load times (<2 seconds per page)
- Works in all export formats

✅ **Stakeholder Quality:**
- Non-designer colleague says "looks professional"
- Can read helper text on Teams screen share
- Prints well in black & white
- Feels like "HHS.gov" family

✅ **Championship Quality:**
- Story-first layout preserved (two-column)
- Tight theming (USWDS colors only)
- Accessibility baked in (WCAG AA)
- Clean information density

---

## 📈 TIMELINE

**Hour 1:**
- Apply theme JSON
- Format Command Center page completely
- Validate and screenshot

**Hour 2:**
- Format Explorer page
- Format Traffic & Acquisition page

**Hour 3:**
- Format Play Events page
- Format External Search page

**Hour 4:**
- Format AI Insights page
- Format Deep Dive page
- Final consistency check

**Hour 5:**
- Export tests (PDF, PowerPoint, Image)
- Accessibility validation
- Final polish and adjustments

**Typical: 5 hours** for all 7 pages, fully validated, stakeholder-ready (range 4-7 hours).

---

## 🚀 NEXT STEPS

1. **Create/Apply Theme JSON** (Step 1 above)
2. **Format Command Center page** (Steps 2-5 above)
3. **Validate Command Center** (screenshot test, squint test)
4. **Share screenshot for feedback** (optional)
5. **Replicate to remaining 6 pages** (Format Painter method)
6. **Final validation** (all tests above)
7. **Ready for stakeholder showing** ✅

---

**Document Status:** ✅ READY TO IMPLEMENT

**Estimated Completion:** ~5 hours (range 4-7 hours)

**Risk Level:** Very Low

**Stakeholder Confidence:** High (aligns with USWDS / HHS.gov conventions)

**Created:** January 10, 2026
**For:** HHS Live Events Dashboard V4.0 - USWDS Light Implementation

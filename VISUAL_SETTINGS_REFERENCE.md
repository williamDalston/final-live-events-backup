# 🎨 Visual Settings Reference - Standard Configurations

**Date:** January 9, 2026  
**Purpose:** Standard visual configurations for consistent look across all pages  
**Status:** ✅ **REFERENCE DOCUMENT - Use When Formatting Visuals**

---

## 📋 **TABLE OF CONTENTS**

1. [KPI Cards](#kpi-cards)
2. [Tables](#tables)
3. [Charts (Bar, Line, Area, Donut)](#charts-bar-line-area-donut)
4. [Text Boxes](#text-boxes)
5. [Headers & Footers](#headers--footers)
6. [Slicers](#slicers)
7. [Quick Reference Card](#quick-reference-card)

---

## 🎯 **KPI CARDS**

### **Dimensions**
- **Width:** 240px (or ~3.2 inches)
- **Height:** 140px (or ~1.9 inches)
- **Aspect Ratio:** ~1.7:1

### **Background & Border**
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E2E8F0 (Silver)
- **Border-radius:** 8px (subtle rounding)
- **Shadow:** `0 1px 3px rgba(0,0,0,0.08)`

### **Hover State**
- **Shadow:** `0 4px 12px rgba(0,0,0,0.12)`
- **Transform:** `translateY(-2px)` (slight lift)
- **Transition:** `200ms ease`

### **Left Accent Bar** (Trend Indicator)
- **Width:** 4px
- **Color by Trend:**
  - Positive: #00A878 (Success Green)
  - Negative: #E63946 (Critical Red)
  - Neutral: #64748B (Storm Gray)
  - Attention: #F4A261 (Warning Amber)

### **Typography**

**Value (Main Number):**
- **Font:** Segoe UI Bold
- **Size:** 32px
- **Color:** #1E293B (Charcoal)
- **Line-height:** 1.1

**Label (Above Value):**
- **Font:** Segoe UI Semibold
- **Size:** 11px
- **Color:** #64748B (Storm)
- **Transform:** Uppercase
- **Letter-spacing:** 0.5px
- **Line-height:** 1.2

**Context Text (Below Value):**
- **Font:** Segoe UI Regular
- **Size:** 11px
- **Color:** #64748B (Storm)
- **Line-height:** 1.4

**Trend Badge:**
- **Font:** Segoe UI Semibold
- **Size:** 11px
- **Padding:** 4px 8px
- **Border-radius:** 4px
- **Background:**
  - Positive: #E8F5E9 (Success Light)
  - Negative: #FFEBEE (Critical Light)
  - Neutral: #F1F5F9 (Storm Light)
- **Text Color:**
  - Positive: #00A878
  - Negative: #E63946
  - Neutral: #64748B

### **Sparkline** (Mini Chart)
- **Height:** 40px
- **Width:** Full width (240px - 20px padding)
- **Color:** Match trend color (green/red/amber)
- **Stroke Width:** 2px
- **Show Data Points:** No (cleaner look)

### **Spacing**
- **Padding:** 16px all sides
- **Gap between elements:** 8px (label to value), 4px (value to context)

---

## 📊 **TABLES**

### **Overall**
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E2E8F0 (Silver)
- **Border-radius:** 8px
- **Shadow:** `0 1px 3px rgba(0,0,0,0.08)`

### **Header Row**
- **Background:** #F8FAFC (Snow)
- **Font:** Segoe UI Semibold
- **Size:** 12px
- **Color:** #1E293B (Charcoal)
- **Padding:** 12px horizontal, 10px vertical
- **Border-bottom:** 2px solid #E2E8F0
- **Text-transform:** None (not uppercase)
- **Alignment:** Left for text, Right for numbers

### **Data Rows**
- **Font:** Segoe UI Regular
- **Size:** 12px
- **Color:** #1E293B (Charcoal)
- **Padding:** 10px horizontal, 8px vertical
- **Alternating Rows:**
  - Even: #FFFFFF (White)
  - Odd: #F8FAFC (Snow)
- **Hover Background:** #D4E5F7 (Ice Blue)
- **Hover Text:** #005EA2 (HHS Blue) - for clickable rows

### **Borders**
- **Gridlines:** 1px solid #E2E8F0 (horizontal only, no vertical)
- **Row Border:** None (cleaner look)

### **Sort Indicators**
- **Icon:** Standard Power BI sort arrows
- **Color:** #64748B (Storm)

### **Drillthrough Indicator** (if applicable)
- **Arrow Icon:** ► (right-pointing triangle)
- **Color:** #005EA2 (HHS Blue)
- **Position:** Right side of row
- **On Hover:** Slide right 4px

### **Spacing**
- **Row Height:** 36px minimum
- **Column Padding:** 12px horizontal

---

## 📈 **CHARTS (Bar, Line, Area, Donut)**

### **Color Palette** (Standard)
```
Primary:   #005EA2 (HHS Blue)
Success:   #00A878 (Success Green)
Warning:   #F4A261 (Warning Amber)
Critical:  #E63946 (Critical Red)
Neutral:   #64748B (Storm Gray)
Light:     #D4E5F7 (Ice Blue)
```

### **Bar Chart**
- **Bar Width:** Auto (Power BI default)
- **Bar Spacing:** 0.2 (20% gap between categories)
- **Border:** None (clean look)
- **Border-radius:** 4px (top corners only, subtle rounding)
- **Hover:** Lift 2px, shadow increase

### **Column Chart**
- **Same as Bar Chart** (but vertical)

### **Line Chart**
- **Stroke Width:** 2px
- **Data Points:** Hidden (cleaner look) OR Small circles (4px) if needed
- **Area Fill:** None (line only) OR 40% opacity area fill if area chart variant
- **Smoothing:** None (sharp lines)

### **Area Chart**
- **Fill Opacity:** 40% (area fill)
- **Stroke Width:** 2px
- **Stroke Color:** Same as fill (darker shade)
- **Stacking:** Standard (if multiple series)

### **Donut Chart**
- **Inner Radius:** 60% (thin donut) OR 40% (thicker donut) - adjust based on data
- **Border:** 1px #FFFFFF (white separator between slices)
- **Hover:** Pull out 3px (explode effect)
- **Legend:** Position right, 11px font

### **Axes**

**X-Axis (Category):**
- **Font:** Segoe UI Regular
- **Size:** 11px
- **Color:** #64748B (Storm)
- **Title:** 12px Semibold #1E293B
- **Gridlines:** 1px #E2E8F0 (light gray)

**Y-Axis (Value):**
- **Font:** Segoe UI Regular
- **Size:** 11px
- **Color:** #64748B (Storm)
- **Title:** 12px Semibold #1E293B
- **Gridlines:** 1px #E2E8F0 (dashed, 5px dash)
- **Format:** Match measure format (#,##0 or 0.0%)

### **Legend**
- **Position:** Right (default) OR Bottom (if space constrained)
- **Font:** Segoe UI Regular
- **Size:** 11px
- **Color:** #64748B (Storm)
- **Title:** None (unless needed)
- **Spacing:** 8px between items

### **Tooltip** (Chart Tooltip)
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E2E8F0
- **Border-radius:** 4px
- **Shadow:** `0 4px 12px rgba(0,0,0,0.15)`
- **Font:** Segoe UI Regular 11px
- **Padding:** 8px

### **Data Labels**
- **Show:** Optional (only if critical for readability)
- **Font:** Segoe UI Regular
- **Size:** 10px
- **Color:** #1E293B (Charcoal)
- **Position:** Above bars/points, inside donut slices

---

## 📝 **TEXT BOXES**

### **Page Header**
- **Font:** Segoe UI Semibold
- **Size:** 32px (Display size)
- **Color:** #1E293B (Charcoal)
- **Line-height:** 1.2
- **Alignment:** Left
- **Padding:** 0px (use page padding instead)

### **Section Header**
- **Font:** Segoe UI Semibold
- **Size:** 18px (Heading 2)
- **Color:** #1E293B (Charcoal)
- **Line-height:** 1.4
- **Alignment:** Left
- **Margin-top:** 24px (space from previous section)
- **Margin-bottom:** 16px (space to content)

### **Body Text**
- **Font:** Segoe UI Regular
- **Size:** 13px
- **Color:** #1E293B (Charcoal)
- **Line-height:** 1.5
- **Alignment:** Left
- **Max-width:** 600px (for readability)

### **Caption/Secondary Text**
- **Font:** Segoe UI Regular
- **Size:** 12px
- **Color:** #64748B (Storm)
- **Line-height:** 1.4
- **Alignment:** Left

### **Footer Text**
- **Font:** Segoe UI Regular
- **Size:** 11px
- **Color:** #64748B (Storm)
- **Line-height:** 1.4
- **Alignment:** Left or Center
- **Opacity:** 80% (subtle)

### **Background**
- **Background:** Transparent (default) OR #FFFFFF if needed
- **Border:** None
- **Padding:** 8px (if background applied)

---

## 📅 **SLICERS**

### **Date Range Slicer**
- **Style:** Between (two date pickers)
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E2E8F0
- **Border-radius:** 4px
- **Font:** Segoe UI Regular 12px
- **Height:** 32px

### **Dropdown Slicer**
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E2E8F0
- **Border-radius:** 4px
- **Font:** Segoe UI Regular 12px
- **Padding:** 8px
- **Dropdown Arrow:** #64748B (Storm)
- **Hover Background:** #F8FAFC (Snow)

### **List Slicer**
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E2E8F0
- **Border-radius:** 4px
- **Item Font:** Segoe UI Regular 12px
- **Item Height:** 32px
- **Item Padding:** 8px horizontal
- **Selected Background:** #D4E5F7 (Ice Blue)
- **Selected Text:** #005EA2 (HHS Blue)
- **Hover Background:** #F8FAFC (Snow)
- **Checkbox:** Standard, color #005EA2 when checked

### **Toggle Slicer** (Yes/No, True/False)
- **Style:** Buttons or Toggle switch
- **Active Background:** #005EA2 (HHS Blue)
- **Active Text:** #FFFFFF (White)
- **Inactive Background:** #F8FAFC (Snow)
- **Inactive Text:** #64748B (Storm)
- **Border-radius:** 4px

---

## 🎨 **HEADERS & FOOTERS**

### **Page Header Section**
- **Height:** 80px
- **Background:** #FFFFFF (White)
- **Border-bottom:** 2px solid #E2E8F0
- **Padding:** 20px horizontal, 16px vertical
- **Layout:** Horizontal (Title left, Filters/Date Range right)

### **Section Header** (Within Page)
- **Background:** Transparent
- **Font:** Segoe UI Semibold 18px
- **Color:** #1E293B (Charcoal)
- **Margin-top:** 32px (first section) or 24px (subsequent sections)
- **Margin-bottom:** 16px
- **Border-bottom:** Optional 1px solid #E2E8F0 (subtle separator)

### **Footer Section**
- **Height:** 60px
- **Background:** #F8FAFC (Snow)
- **Border-top:** 1px solid #E2E8F0
- **Padding:** 16px horizontal, 12px vertical
- **Font:** Segoe UI Regular 11px
- **Color:** #64748B (Storm)
- **Layout:** Horizontal (Data notes left, Last updated right)

---

## 🎯 **QUICK REFERENCE CARD**

### **Font Stack**
```
Headings:    "Segoe UI Semibold", system-ui
Body:        "Segoe UI", system-ui
Data:        "Segoe UI", system-ui (same, but bold for numbers)
```

### **Color Palette**
```
Primary Text:    #1E293B (Charcoal)
Secondary Text:  #64748B (Storm)
Tertiary Text:   #94A3B8 (Muted)
Link:            #005EA2 (HHS Blue)
Link Hover:      #0076D6 (Bright Blue)

Success:         #00A878
Warning:         #F4A261
Critical:        #E63946
Neutral:         #64748B

Background:      #FFFFFF (White)
Canvas:          #F8FAFC (Snow)
Border:          #E2E8F0 (Silver)
```

### **Type Scale**
```
Display:     32px Semibold (Page titles)
Heading 1:   24px Semibold (Section heads)
Heading 2:   18px Semibold (Card titles, subsections)
Heading 3:   14px Semibold (Sub-subsections)
Body:        13px Regular (Body text)
Body Small:  12px Regular (Secondary text)
Caption:     11px Regular (Labels, notes)
Overline:    10px Semibold Uppercase (KPI labels)
Data Large:  32px Bold (KPI values)
Data Medium: 24px Semibold (Chart labels)
Data Small:  12px Regular (Table data)
```

### **Spacing Scale**
```
2px:   Minimal gap (icon to text)
4px:   Small gap (badge padding, icon spacing)
8px:   Standard gap (element spacing)
12px:  Medium gap (section spacing)
16px:  Large gap (card padding, major spacing)
24px:  Section margin (between major sections)
32px:  Page margin (top of page, between pages)
```

### **Border Radius**
```
2px:   Small elements (badges, small buttons)
4px:   Standard elements (inputs, dropdowns)
8px:   Cards, containers (most visuals)
12px:  Large containers (rarely used)
```

### **Shadows**
```
Subtle:  0 1px 3px rgba(0,0,0,0.08)  (default card)
Hover:   0 4px 12px rgba(0,0,0,0.12) (lifted card)
Modal:   0 8px 24px rgba(0,0,0,0.15) (tooltips, modals)
```

---

## ✅ **VISUAL CONFIGURATION CHECKLIST**

### **When Formatting Any Visual:**

- [ ] Font family matches standard (Segoe UI)
- [ ] Font size matches type scale
- [ ] Colors match palette (no random colors)
- [ ] Spacing matches spacing scale (8px, 16px, 24px)
- [ ] Border-radius matches standard (4px, 8px)
- [ ] Shadow matches elevation (subtle, hover, modal)
- [ ] Alt text bound (if visual)
- [ ] Hover state defined (if interactive)

### **When Formatting KPI Cards:**

- [ ] Dimensions: 240w × 140h
- [ ] Left accent bar: 4px, color by trend
- [ ] Value: 32px Bold, #1E293B
- [ ] Label: 11px Semibold Uppercase, #64748B
- [ ] Trend badge: Proper colors and padding
- [ ] Sparkline: 40px height, trend color
- [ ] Shadow: Subtle (default), Hover (lifted)

### **When Formatting Tables:**

- [ ] Header: #F8FAFC background, 12px Semibold
- [ ] Rows: Alternating #FFFFFF / #F8FAFC
- [ ] Hover: #D4E5F7 background
- [ ] Gridlines: 1px #E2E8F0 (horizontal only)
- [ ] Border-radius: 8px container

### **When Formatting Charts:**

- [ ] Colors: Standard palette (#005EA2, #00A878, etc.)
- [ ] Axis labels: 11px Regular #64748B
- [ ] Axis titles: 12px Semibold #1E293B
- [ ] Legend: 11px Regular, positioned right
- [ ] Gridlines: 1px #E2E8F0
- [ ] Data labels: 10px (optional, only if needed)

---

## 🎯 **APPLYING TO VISUALS**

### **Step 1: Create Visual**
- Drag visual to canvas
- Bind measures/dimensions from visual-specific folders

### **Step 2: Apply Standard Settings**
- Open Format visual pane
- Apply settings from this reference document
- Use Format Painter to copy to similar visuals

### **Step 3: Bind Alt-Text** (if visual)
- Format visual → General → Alt text
- Click "fx" button
- Select measure from `Accessibility;Alt Text;[Page]`

### **Step 4: Verify Consistency**
- Check against this reference document
- Use Format Painter to match other visuals
- Verify colors, fonts, spacing match standard

---

## 📋 **COMMON PATTERNS**

### **Pattern 1: KPI Card Row**
```
7 KPI Cards in a row:
- Card 1: Sessions
- Card 2: Page Views
- Card 3: Total Events
- Card 4: Play Events
- Card 5: Unique Viewers
- Card 6: Engagement Rate
- Card 7: Health Score

Spacing: 16px gap between cards
Container: Full width, 16px padding on sides
```

### **Pattern 2: Section Layout**
```
Section Header (18px Semibold)
↓ 16px gap
Visual Content (charts, tables, cards)
↓ 24px gap (to next section)
```

### **Pattern 3: Two-Column Layout**
```
Left Column (60% width): Main visualization
Right Column (40% width): Supporting table or details
Gap: 24px between columns
```

---

**Status:** ✅ **REFERENCE DOCUMENT READY** - Use when formatting visuals for consistent look across all pages!

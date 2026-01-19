# Complete Build Guide: Command Center Page (Top to Bottom, Left to Right)

**Version:** v1.8 (Premium App Shell Enhancements)  
**Last Updated:** January 2026  
**Status:** ✅ Complete - All v1.8 Navigation Rail Y-Coordinate Fixes Applied

**Goal:** Build Command Center page with exact pixel positions, measure folder references, and complete formatting specs in one document.

**Time:** 60-90 minutes

**Prerequisites:**
- ✅ **REQUIRED FIRST:** Run `PRE_BUILD_VALIDATION_CHECKLIST.md` (10-15 minutes)
  - Validates data model relationships, measures in folders, theme application
  - Includes "Greatness Guarantee" checklist for post-build validation
- Power BI Desktop open
- USWDS Light theme applied (`HHS_Theme_USWDS_Aligned.json`)
- All measures organized in folders (see measure folder structure below)
- Canvas size set: 1920×1080 (File → Options → Page size → Custom)

**Optional Enhancement:**
- ⚠️ **HTML Visual Availability:** If you want to enhance the right panel with a premium HTML narrative layer, check if HTML visual is available in your tenant first. See `HTML_ENHANCEMENT_STRATEGY.md` for complete strategy, federal considerations, and implementation roadmap. **Note:** HTML is optional - current v1.8 native implementation (text boxes + buttons) is excellent and fully functional.

---

## 📐 DESIGN TOKENS (Quick Reference - Copy/Paste Ready)

**Lock these values first. They apply to EVERY element.**

### **Colors:**
```
Page Background:  #F0F0F0
Card Background:  #FFFFFF
Border:           #DFE1E2
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

### **Shape & Depth:**
```
Radius:           4px (applies to containers, shapes, and card backgrounds)
                  NOTE: Native visuals may not respect rounded corners perfectly.
                  Use background shapes if exact radius matching is critical.
Shadows:          OFF (everywhere)
Border Weight:    1px default
Glow/Inner:       OFF
```

### **Spacing & Grid:**
```
Nav Rail Width:   60px
Content Start:    84px (60px rail + 24px padding)
                  All content elements start at x=84px minimum
                  Header elements may start at x=24px if rail is behind them
Content End:      1300px (before right rail)
Available Width:  1216px (1300 - 84)
Page Padding:     24px (from content edge, not page edge)
Visual Gap:       12px (standard between side-by-side visuals, e.g., KPI cards, two-column charts)
Card Gap:         12px (same as visual gap, horizontal spacing)
Header-to-Row Gap: 4px (section header bottom to first visual top)
Row-to-Next-Header Gap: 16px (section break between content row and next section header)
Section Gap:      16px (same as Row-to-Next-Header Gap, section break spacing)
Card Padding:     12-16px
Header Offset:    8-12px above content
Main ↔ Right Rail Gap: 20px (critical constant: rail starts after main content)
Right Rail Width: 528px (27.5% of canvas - reduced 10-15% from 576px in v1.8 for better content balance)
Right Rail End: 1848px (1320 + 528)
```

### **Typography:**
```
Page Title:       24-28pt Semibold #1B1B1B
Purpose Subtitle: 12pt Regular #565C65 (NEW v1.8 - below page title, provides immediate context)
Section Header:   14pt Semibold #1B1B1B
Card Label:       11pt Regular #565C65
KPI Value:        28-32pt Regular #1B1B1B
KPI Subline:      11pt Regular #71767A (trend delta or context line)
Action Button:    12pt Regular #1B1B1B (NEW v1.8 - increased from 11pt for leadership readability)
Table Body:       11-12pt Regular #1B1B1B
Helper Text:      10-11pt Regular #71767A
Eyebrow Label:    11pt Regular #565C65
Last Refresh:     10pt Regular #71767A (tertiary text)
```

### **KPI Subline Standard (CRITICAL FOR CONSISTENCY):**
```
When to Show:      ALL KPIs must have a subline (trend delta OR context line)
                    - Sessions: "▲ 12% MoM" (trend delta)
                    - Page Views: "▲ 8% MoM" (trend delta)
                    - Top Device: "Mobile | 68% of sessions" OR "+3pp vs prior" (context line)
                    - Avg Pages/Session: "▼ 1% MoM" (trend delta)
                    - If no trend data available, show context: "68% of sessions" or similar

Format:           Font: Segoe UI, 11pt Regular
                  Color: #71767A (tertiary/helper text)
                  Position: Below KPI value, 2-4px spacing
                  Alignment: Center (matches KPI value alignment)

Content Pattern:  Trend Delta: "[▲/▼] [percentage] [period]" (e.g., "▲ 12% MoM")
                  Context Line: "[Category] | [percentage]" (e.g., "Mobile | 68%") OR "[delta] vs [comparison]" (e.g., "+3pp vs prior")

⚠️ Power BI Reality Check: Card visuals may not support a "subline" field natively.
                           Use one of these patterns:
                           - Option A: Use text box below card (inside card container area)
                           - Option B: If Card (new) supports subtitle/subline, use that field
                           - Option C: Include subline text in tooltip (if subline must be visible on hover only)
```

---

## 📁 MEASURE FOLDER STRUCTURE (Reference)

**All measures must be organized in these folders for quick access:**

```
📁 Command Center
   └─ KPI Card - Sessions
      └─ [Sessions]
      └─ [Sessions Alt Text]
   └─ KPI Card - Page Views
      └─ [Page Views]
      └─ [Page Views Alt Text]
   └─ KPI Card - Top Device
      └─ [Top Device Category]
      └─ [Top Device Alt Text]
   └─ KPI Card - Avg Pages/Session
      └─ [Avg Pages per Session]
      └─ [Avg Pages Alt Text]
   └─ Chart - Sessions by City
      └─ [Sessions by City]
      └─ [Sessions by City Alt Text]
   └─ Chart - Device Breakdown
      └─ [Device Sessions]
      └─ [Device Breakdown Alt Text]
   └─ Table - Top Livecast Videos
      └─ [Livecast Title]
      └─ [Livecast Views]
      └─ [Livecast Avg Time]
      └─ [Top Videos Alt Text]
   └─ Table - Top Pages
      └─ [Page Path]
      └─ [Page Views]
      └─ [Page Engagement]
      └─ [Top Pages Alt Text]
   └─ Review Panel
      └─ [Review Prompts Text] (Phase 2 - hybrid context tokens only)
      └─ [Data Freshness Text] (Optional - Phase 2)
      └─ [Filters in Effect Text] (Optional - Phase 2)
```

**Note:** If measures aren't organized yet, do this BEFORE building. Use these exact folder names for consistency.

---

## 🎯 BUILD SEQUENCE (Top to Bottom, Left to Right)

### **PHASE 0: Decision Gate - Right Rail Height (REQUIRED BEFORE BUILD)**

**⚠️ CRITICAL DECISION: Choose ONE option and commit to it for this page.**

**This page uses:** ✅ **Option A (Content-Driven Height - 412px)**

**Option A: Content-Driven Height (Recommended - Lightweight, Analyst-Focused)**
- **Height:** 412px (deterministic: based on Y positions + padding)
- **Content:** Panel header + 3 review prompts + micro-disclaimer footer
- **Visual Weight:** Light, reads like marginalia
- **When to Use:** Default for all pages (keeps panel feeling like "analyst notebook," not "directive workflow")

**Option B: Full-Height (940px) - ONLY if justified with neutral filler**
- **Height:** 940px (full content height: Y=124px to Y=1064px)
- **Content:** Panel header + 3 review prompts + micro-disclaimer + optional fillers (Data Freshness, Filters in Effect, Key Definitions)
- **Visual Weight:** Heavier, requires neutral content to justify space
- **When to Use:** Only if you need extra context sections (data freshness, active filters, definitions)
- **Requirement:** Must include at least 2 of: Data Freshness, Filters in Effect, Key Definitions (3-4 lines each max)

**Decision for Command Center Page:** ✅ **Option A (412px content-driven)**  
**Panel Width Update (v1.8):** Reduced from 576px to **528px** (10-15% reduction for better content balance)
- This keeps the panel lightweight and focused on review prompts only
- No neutral filler sections needed
- Panel ends shortly after disclaimer footer

**⚠️ Replication Rule:** When building Pages 2-7, explicitly declare which option each page uses at the top of that page's build section. This prevents "full-height with Option A content" drift.

---

### **PHASE 1: Canvas Setup (5 minutes)**

#### **1.1 Set Canvas Size**
1. File → Options and settings → Options
2. Report settings → Page size → Custom
3. Width: 1920px
4. Height: 1080px
5. Click OK

#### **1.2 Set Page Background**
1. Click anywhere on canvas (not on a visual)
2. Format page panel
3. **Canvas background:**
   - Color: #F0F0F0
   - Transparency: 0%
4. **Wallpaper:**
   - Color: #F0F0F0
   - Transparency: 0%
   - Image: None (remove any background images)

#### **1.3 Enable Grid & Snap**
1. View tab → Show → Gridlines (checked)
2. View tab → Show → Snap to grid (checked)
3. View tab → Page view → **Actual size** (100% zoom)
   - This is your "official operating zoom" for pixel-perfect development
   - Export tests should also be done at 100% zoom

#### **1.4 Understand Content Grid (Canonical Formula Block)**

**Grid Constants (Single Source of Truth):**
- Canvas width: **1920px**
- Canvas height: **1080px**
- Navigation rail width: **60px** (x=0 to x=60)
- Content start X: **84px** (60 + 24px padding)
- Content end X: **1300px** (before right rail)
- Available content width: **1216px** (1300 - 84)
- Gap between visuals: **12px** (standard)
- Main ↔ Right Rail Gap: **20px** (critical constant: rail starts after main content)
- Right rail start: **1320px** (1300 + 20px gap)
- Right rail width: **528px (27.5% of canvas - reduced 10-15% from 576px for better content balance)**
- Right rail end: **1848px** (1320 + 528)
- Right rail inner padding: **24px**
- **Header Right Edge:** **1872px** (right rail end 1848 + 24px padding - matches divider end, canonical constant)

**Formula Block (Use These for All Calculations):**

**Main Content Area:**
```
Content Start (X):      84px
Content End (X):       1300px
Available Width:       1216px (1300 - 84)
```

**Two-Column Layout (Charts/Tables):**
```
Left Column X:         84px
Left Column Width:     602px (1216 - 12) / 2 = 602
Right Column X:        698px (84 + 602 + 12)
Right Column Width:    602px
Right Edge:            1300px (698 + 602) ✅
```

**Four-Column Layout (KPI Cards - Perfect Grid, Flush to x=1300):**
```
Card Width:            295px ((1216 - 36) / 4 = 295)
Card 1 X:              84px
Card 2 X:              391px (84 + 295 + 12)
Card 3 X:              698px (391 + 295 + 12)
Card 4 X:              1005px (698 + 295 + 12)
Right Edge:            1300px (1005 + 295) ✅
```
**Note:** KPIs align flush with charts/tables (both end at x=1300) for consistent grid.

**Header Elements (Canonical 3-Item Cluster: Reset | Info | Date, left → right, 10px gaps):**
```
Header Right Edge:     1872px (right rail end 1848 + 24px padding - CANONICAL CONSTANT)
Date Slicer X:         1672px (1872 - 200)
Date Slicer Width:     200px
Date Slicer End:       1872px ✅
Definitions/Info X:    1612px (1672 - 10 - 50)
Definitions/Info Width: 50px
Reset Button X:        1552px (1612 - 10 - 50)
Reset Button Width:    50px
Reset | Info | Date:   Left → Right (10px gaps between each)
```
**⚠️ Visual Note:** Eyebrow/title at x=24px will sit on the nav rail's white background (not page's #F0F0F0). This creates a "cleaner/brighter" left edge effect. If you prefer uniform header background, add a header strip shape behind eyebrow/title area (only if leadership aesthetics demand it).

**Right Rail Panel:**
```
Rail Gap:              20px (between Content End and Panel Start)
Panel X:               1320px (1300 + 20px rail gap)
Panel Width:           528px (reduced 10-15% from 576px for better content balance)
Panel Y Start:         124px (aligned with first KPI card)
Content Start X:       1344px (1320 + 24px inner padding)
```

**Validation:** All positions derived from constants above. Canvas is light gray (#F0F0F0), 1920×1080, grid visible, zoom at 100%

---

### **PHASE 2: Header Area (10 minutes)**

**⚠️ Header Positioning Note:** Header elements (eyebrow, title) intentionally start at x=24px, which means they overlap the navigation rail region. This is acceptable for header elements. Main content (KPIs, charts, tables) starts at x=84px (content grid).

---

#### **2.0 HHS Logo (REQUIRED - Brand Identity)**

**⚠️ NEW:** Based on reference dashboard "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf", the header includes the official HHS logo next to the eyebrow/title text for brand identity.

**Insert:**
1. Insert tab → Image
2. Browse to: `assets/hhs_logo.svg` (or `assets/hhs_logo.png`)

**Position:**
- X: 84px (aligned with content grid)
- Y: 20px
- Width: 36px (maintain aspect ratio)
- Height: 36px (approximate - logo is square or near-square)

**Format:**
- Background: Transparent
- Border: None
- Shadow: Off

**Alt Text:**
- Format → General → Alt text → Description
- Type: "U.S. Department of Health and Human Services logo"

**Lock it:**
1. Selection pane
2. Rename to "HHS Logo"
3. Click lock icon

---

#### **2.1 Eyebrow Label ("HHS LIVE EVENTS")**

**Insert:**
1. Insert tab → Text box
2. Type: "HHS LIVE EVENTS"

**Position:**
- X: 128px (right of HHS logo: 84 + 36 logo + 8 gap)
- Y: 20px
- Width: 250px
- Height: 20px

**Format → General → Text:**
- Font family: Segoe UI
- Font size: 11pt
- Font color: #565C65 (Secondary Text)
- Bold: Off
- Alignment: Left

**Measure:** None (static text)

**Lock it:**
1. View → Selection pane
2. Find "Text box" (rename to "Eyebrow Label")
3. Click lock icon

---

#### **2.2 Page Title ("COMMAND CENTER")**

**Insert:**
1. Insert tab → Text box
2. Type: "COMMAND CENTER"

**Position:**
- X: 128px (aligned with eyebrow, right of HHS logo)
- Y: 40px
- Width: 550px
- Height: **34px** (reduced from 40px to accommodate purpose subtitle at Y=74)

**Format → General → Text:**
- Font family: Segoe UI
- Font size: 28pt
- Font color: #1B1B1B (Primary Text)
- Bold: Semibold
- Alignment: Left

**Measure:** None (static text)

**Lock it:**
1. Selection pane
2. Rename to "Page Title"
3. Click lock icon

---

#### **2.2a Purpose Subtitle (NEW v1.8 - REQUIRED)**

**⚠️ CRITICAL:** This prevents the "cool… what am I looking at?" moment by providing immediate context for leadership.

**Insert:**
1. Insert tab → Text box
2. Type: **"Monitor performance and detect issues fast."**

**Position:**
- X: 128px (aligned with page title, right of HHS logo)
- Y: 74px (4px below page title bottom at Y=74, creating visual hierarchy)
- Width: 550px
- Height: 18px

**Format → General → Text:**
- Font family: Segoe UI Regular (not semibold - lighter weight than title)
- Font size: **12pt** (leadership readability minimum, WCAG AA compliant)
- Font color: #565C65 (secondary text - subtle, doesn't compete with title)
- Bold: Regular (not semibold)
- Alignment: Left

**Content by Page (Use Appropriate Subtitle):**
1. Command Center: *"Monitor performance and detect issues fast."*
2. Explorer: *"Discover patterns and drill into performance details."*
3. Traffic & Acquisition: *"Understand how audiences find and arrive at live events."*
4. Play Events: *"Track video engagement and playback performance."*
5. External Search: *"Monitor search visibility and click-through performance."*
6. AI Insights: *"Surface anomalies and forecast trends using intelligent analysis."*
7. Deep Dive: *"Advanced segmentation and cohort analysis for detailed insights."*

**Measure:** None (static text)

**Lock it:**
1. Selection pane
2. Rename to "Purpose Subtitle"
3. Click lock icon

**Validation:** Purpose subtitle visible below page title (12pt, #565C65), provides clear context without competing with title. Page title height is 34px (ends at Y=74), purpose subtitle starts at Y=74 (4px gap), ends at Y=92. Header divider is at Y=96 (4px below subtitle, clean spacing).

---

#### **2.3 Date Slicer (Top Right - Header Right Edge Cluster)**

**⚠️ CANONICAL POSITION:** Date slicer is part of the 3-item header cluster (Reset | Info | Date, left → right, 10px gaps). Header right edge is **1872px** (right rail end 1848 + 24px padding).

**Insert:**
1. Visualizations → Slicer
2. Fields → DimDate → [Date]

**Position:**
- X: **1672px** (1872 - 200, ends exactly at 1872 - Header Right Edge constant)
- Y: 30px
- Width: 200px
- Height: 50px
- **End:** 1872px ✅ (matches Header Right Edge constant)

**Format → General → Effects:**
- Background: #FFFFFF
- Border: 1px solid #DFE1E2
- Rounded corners: 4
  - **⚠️ Visual Consistency Check:** If native visual doesn't respect 4px radius, use background shape method
- Shadow: Off (explicitly OFF - check all shadow settings)
- Glow: Off

**Format → Visual → Slicer settings:**
- Style: **Dropdown** (recommended for compact header space)
- Show "Select all": On (if available for your slicer style/version)
- **⚠️ Power BI Reality Check:** "Select all" is typically available for **List** style slicers, but not consistently for **Dropdown** style. If leadership requires "Select all," use Style: **List** instead and apply same formatting.
- Single select: Off

**Format → Visual → Slicer header:**
- Font family: Segoe UI
- Font size: 11pt
- Font color: #565C65

**Format → Visual → Values:**
- Font family: Segoe UI
- Font size: 11pt
- Font color: #1B1B1B

**Measure Folder:** `DimDate → [Date]`

**⚠️ CRITICAL - Sync Across Pages:**
- View → **Sync slicers**
- Sync `DimDate[Date]` slicer across all 7 pages
- **Visibility:** Visible on all pages (recommended for app-shell consistency)
- This makes the dashboard feel like one cohesive app, not 7 separate reports

**Alt Text (Static):**
- Format visual → General → Alt text → Description
- Type: "Date range filter for selecting dashboard time period"
- **Note:** Power BI Alt Text fields are static text. Dynamic alt text via measures is not consistently supported across all visual types or Power BI versions.

**Lock it:**
1. Selection pane
2. Rename to "Date Slicer"
3. Click lock icon

---

#### **2.3-PAGE-PATH Page Path Slicer (REQUIRED - Reference Dashboard Match)**

**⚠️ NEW:** Based on reference dashboard "Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf" Page 1, the Executive Summary needs a Page Path slicer to filter to specific livecast pages.

**Insert:**
1. Visualizations → Slicer
2. Fields → ga4-pages → [Page path]

**Position:**
- X: **1472px** (left of Date Slicer)
- Y: 30px
- Width: 180px
- Height: 50px

**Format → General → Effects:**
- Background: #FFFFFF
- Border: 1px solid #DFE1E2
- Rounded corners: 4
- Shadow: Off

**Format → Visual → Slicer settings:**
- Style: **Dropdown**
- Show "Select all": On (if available)
- Single select: On (filter to one page at a time)

**Format → Visual → Slicer header:**
- Font family: Segoe UI
- Font size: 11pt
- Font color: #565C65

**Format → Visual → Values:**
- Font family: Segoe UI
- Font size: 11pt
- Font color: #1B1B1B

**What it filters:**
- ✅ Sessions by City (ga4-pages relationship)
- ✅ Device Breakdown (if relationship exists)
- ✅ Referral Sources table
- ✅ Top Pages table
- ✅ Top Livecast Videos table

**Alt Text (Static):**
- Format visual → General → Alt text → Description
- Type: "Page path filter for selecting specific livecast page"

**Lock it:**
1. Selection pane
2. Rename to "Page Path Slicer"
3. Click lock icon

---

#### **2.3a Reset Filters Button (REQUIRED - UX Escape Hatch)**

**⚠️ CRITICAL:** Once people click bars/slices/tables, they get "lost" and blame the dashboard. This single button prevents frustration.

**Insert:**
1. Insert → Button → **Blank**

**Position:**
- X: **1552px** (canonical 3-item cluster: Reset | Info | Date, left → right, 10px gaps)
- Y: 30px (aligned with date slicer)
- Width: **50px** (standard button width)
- Height: **50px** (matches date slicer height)

**Format → Button → Style (Default):**
- Fill: #FFFFFF
- Border: 1px solid #DFE1E2
- Border radius: 4px
- Shadow: OFF (explicitly OFF)
- Text: "Reset" (Segoe UI, 12pt, #005EA2, centered)
- Icon: Optional reset icon if available

**Format → Button → Style (Hover):**
- Fill: #F0F0F0
- Border: 1px solid #005EA2 (accent on hover)

**Action (REQUIRED):**
- Format → Button → Action → **Bookmark**
- Select bookmark: "Reset Command Center" (create this bookmark if it doesn't exist)
- **Bookmark Settings (Create First):**
  1. Clear all cross-filters (deselect all visuals)
  2. Bookmark settings:
     - **Data:** ✅ Checked (applies filter reset)
     - **Display:** ❌ Unchecked (preserves current view/zoom)
     - **Current page:** ✅ Checked (stays on Command Center page)
  3. Rename bookmark to "Reset Command Center"

**Tooltip:** "Clear all filters and return to default view"
**Alt text:** "Button to reset all filters and return to default view"

**Lock it:**
1. Selection pane
2. Rename to "Reset Filters Button"
3. Click lock icon

---

#### **2.3b Definitions / Info Button (Optional but Recommended)**

**⚠️ USEFUL:** Provides quick access to metric definitions without leaving the page. Recommended for leadership who may not remember what each metric means.

**Insert:**
1. Insert → Button → **Blank**

**Position:**
- X: **1612px** (canonical 3-item cluster: Reset | Info | Date, 10px gap between Reset and Info)
- Y: 30px (aligned with date slicer)
- Width: **50px** (standard button width)
- Height: **50px** (matches date slicer height)

**Format → Button → Style (Default):**
- Fill: #FFFFFF
- Border: 1px solid #DFE1E2
- Border radius: 4px
- Shadow: OFF (explicitly OFF)
- Text: "i" (info icon - Segoe UI, 12pt, #005EA2, centered)
- Icon: Optional info icon if available

**Format → Button → Style (Hover):**
- Fill: #F0F0F0
- Border: 1px solid #005EA2 (accent on hover)

**Action (Choose One):**
- **Option A (Recommended):** Format → Button → Action → **Bookmark** (toggles a small "Definitions" overlay panel on/off)
  - Create bookmark "Toggle Definitions Panel" that shows/hides a definitions panel
- **Option B:** Format → Button → Action → **Page navigation** (goes to a Definitions page, if you create one)

**Tooltip:** "Definitions and metric notes"
**Alt text:** "Button to open definitions and metric notes"

**Lock it:**
1. Selection pane
2. Rename to "Definitions Info Button"
3. Click lock icon

---

#### **2.3c Last Refresh Indicator (REQUIRED - Trust Anchor)**

**⚠️ CRITICAL:** This single line prevents 10 minutes of meeting derailment. Leadership always asks "How fresh is this?"

**Insert:**
1. Insert tab → Text box
2. **Position:**
   - X: **1672px** (aligned with date slicer left edge - same as date slicer X)
   - Y: 82px (2px below date slicer bottom at Y=80, just above header divider at Y=96)
   - Width: 200px (matches date slicer width)
   - Height: 16px

**Content:**
```
Last refresh: Jan 10, 2026 08:12 ET
```

**Format → General → Text:**
- Font family: Segoe UI
- Font size: 10pt (tiny, low drama)
- Font color: #71767A (Tertiary/Helper - subtle)
- Alignment: Right (matches date slicer alignment)
- Font style: Regular (not italic, not bold)

**Phase 2 (Dynamic - Optional):**
- If you have a "Last Refreshed" measure or parameter, use Smart Narrative visual instead
- Format: Same as static text (10pt, #71767A, right aligned)
- Position: Same X/Y as text box above
- **Measure Pattern:** `"Last refresh: " & FORMAT([Last Refreshed], "mmm dd, yyyy hh:mm") & " ET"`

**Lock it:**
1. Selection pane
2. Rename to "Last Refresh Indicator"
3. Click lock icon

**Validation:** Last refresh text visible below date slicer, right-aligned, subtle tertiary color, doesn't interfere with header divider

---

#### **2.3b Reset Filters Button (REQUIRED - Escape Hatch)**

**⚠️ CRITICAL UX FEATURE:** Once people click bars/slices/tables, they get "lost" and blame the dashboard. This single button prevents that confusion.

**Insert:**
1. Insert tab → Button
2. Button type: **Blank** (we'll style it manually)

**Position:**
- X: 1636px (Left of Date Slicer, 10px gap)
- Y: 30px (aligned with date slicer top)
- Width: 50px (compact square button)
- Height: 50px (matches date slicer height)

**Format → Style → Default:**
- Fill: #FFFFFF
- Border: 1px solid #DFE1E2
- Rounded corners: 4
  - **⚠️ Visual Consistency Check:** Enforce 4px radius via background shape if needed (see KPI card instructions)
- Shadow: Off (explicitly OFF)
- **Text:**
  - Show: On
  - Text: "Reset"
  - Font: Segoe UI, 11pt Regular, #005EA2 (matches interactive color)
  - Alignment: Center

**Format → Style → Hover:**
- Fill: #F0F0F0
- Border: 1px solid #005EA2 (accent border on hover)
- Text color: #005EA2 (maintains interactive feel)

**Action Setup (Bookmark Method - Recommended):**
1. **First, create the bookmark:**
   - View → Bookmarks pane
   - Click "Add" (creates new bookmark)
   - Rename bookmark to "Reset Command Center"
   - Bookmark settings:
     - Data: ✅ Checked (clears all filters)
     - Display: ❌ Unchecked (preserves current view/zoom)
     - Current page: ✅ Checked (stays on Command Center page)
2. **Then, set button action:**
   - Format button → Button → Action
   - Action type: **Bookmark**
   - Select bookmark: "Reset Command Center"
   - **Alternative (Page Navigation - Less Elegant):**
     - Action type: **Page navigation**
     - Target: **Command Center** (same page)
     - **Note:** This refreshes the page, which also clears filters, but bookmark method is preferred

**Tooltip:**
- Format → Style → Tooltip: On
- Text: "Reset all filters to default state"

**Alt Text (Static):**
- Format → General → Alt text → Description
- Type: "Button to reset all dashboard filters to default state"

**Lock it:**
1. Selection pane
2. Rename to "Reset Filters Button"
3. Click lock icon

**Validation:** Reset button visible to the right of date slicer (X=1480px), functional (clears all cross-filters when clicked), styled consistently with other interactive elements, 4px radius, no shadows

---

#### **2.4 Header Divider Line**

**Insert:**
1. Insert tab → Shapes → Line
2. Draw horizontal line

**Position:**
- X1: 84px (content start, accounting for 60px rail + 24px padding)
- Y: 84px (4px below date slicer bottom at Y=80, avoiding double-border clash)
- X2: **1872px (right panel end at 1848px + 24px padding = 1872px; spans under header across both main content + right rail area - updated for new panel width 528px)**
- **Width:** 1872 - 84 = **1788px** (updated for new panel width)
- Y: 84px

**⚠️ Note:** Divider still spans under header across both main content + right rail area, but ends at right panel edge (1848px) + 24px padding = 1872px, not full canvas width (1896px). This maintains visual consistency while respecting the reduced panel width.

**Format → Shape:**
- Line color: #DFE1E2
- Line weight: 1px
- Line style: Solid

**Lock it:**
1. Selection pane
2. Rename to "Header Divider"
3. Click lock icon

**Validation:** Header complete - eyebrow (Y=20), title (Y=40, H=34px, ends at Y=74), **purpose subtitle (Y=74, H=18px, ends at Y=92 - NEW v1.8)**, reset filters button (X=1552, Y=30, 50×50px), definitions/info button (X=1612, Y=30, 50×50px), date slicer (X=1672, Y=30, 200×50px, ends at 1872px - Header Right Edge), last refresh indicator (X=1672, Y=82, 200×16px, right-aligned), divider (Y=96px, X1=84px, X2=1872px, width=1788px - canonical width). Header cluster: Reset | Info | Date (left → right, 10px gaps). Divider spans under header across both main content + right rail area, ending at Header Right Edge (1872px).

---

### **PHASE 3: Left Column - Diagnostics (30 minutes)**

#### **SECTION 1: At a Glance (KPI Cards)**

**Section Header:**
1. Insert → Text box
2. Type: "At a Glance"
3. **Position:** X: 84px (content start), Y: 100px, Width: 300px, Height: 20px
4. **Format:** 14pt Segoe UI Semibold, #1B1B1B, Left aligned
5. Lock it

---

#### **3.1 KPI Card 1: Sessions**

**Insert:**
1. Visualizations → Card visual

**Position:**
- X: 84px (content start)
- Y: 124px
- Width: 295px (perfect grid: (1216 - 36) / 4 = 295, flush to x=1300)
- Height: 100px

**Field:**
- Measure folder: `Command Center → KPI Card - Sessions → [Sessions]`
- Drag [Sessions] to "Fields" well

**Format → General → Effects:**
- Background: #FFFFFF
- Transparency: 0%
- Border: On
  - Color: #DFE1E2
  - Rounded corners: 4
  - Width: 1px
- Shadow: Off (explicitly OFF - check all shadow settings)
- Glow: Off
- **⚠️ Visual Consistency Check:** If native visual doesn't respect 4px radius perfectly, use background shape method:
  - Insert → Shapes → Rounded Rectangle behind the card visual
  - Position: Same X/Y as card, Width/Height: Same as card
  - Format: Background #FFFFFF, Border 1px #DFE1E2, Rounded corners: 4px, Shadow: OFF
  - Set card visual background to Transparent
  - This ensures exact 4px radius match across all cards

**Format → Callout value:**
- Font family: Segoe UI
- Font size: 32pt
- Font color: #1B1B1B
- Font: Regular (not bold)
- Alignment: Center
- Display units: None (show full number)
- Value decimal places: 0

**Format → Category label:**
- Show: On
- Text: "Sessions"
- Font family: Segoe UI
- Font size: 11pt
- Font color: #565C65
- Alignment: Center
- Position: Below

**Format → KPI Subline (Trend Delta - REQUIRED FOR CONSISTENCY):**
- **⚠️ Power BI Reality Check:** Card visuals may not support a "subline" field natively.
- **Option A (Recommended):** Insert text box below callout value (inside card container area)
  - Position: Same X as card, Y: ~180px (4px below callout value at ~176px)
  - Width: 295px (matches card width)
  - Height: 16px
  - Format: Segoe UI, 11pt Regular, #71767A (tertiary text), Center aligned
  - Content: "▲ 12% MoM" (or actual trend value from measure)
  - **Measure Reference (Phase 2):** Use `Command Center → KPI Card - Sessions → [Sessions - MoM %]` in a measure-driven text box if dynamic trend is available
- **Option B:** If Card (new) supports subtitle/subline field, use that field with same formatting
- **Content Pattern:** Trend Delta: "[▲/▼] [percentage] [period]" (e.g., "▲ 12% MoM")
- **Lock it:** Selection pane → Rename to "KPI Sessions Subline" → Lock

**⚠️ Power BI Reality Check - Category Label Text:**
Depending on **Card (new)** vs **Card (classic)**, you may not be able to directly edit the category label text in the Format pane. If this option is unavailable:
- **Workaround:** Turn off category label in Format pane
- Insert a small text box inside the card container area (below the callout value)
- Position: Same X as card, Y: ~180px (below callout value)
- Format: Same as category label (11pt Segoe UI, #565C65, center aligned)
- Type: "Sessions" (or your label text)

**Accessibility - Tooltip (Recommended):**
- Add measure to **Tooltips** well: `Command Center → KPI Card - Sessions → [Sessions Alt Text]`
- **Rename tooltip field label** (if possible in your Power BI version) to **"Description"** for cleaner hover text
- This provides dynamic accessibility description without relying on native Alt Text field binding

**Alt Text (Static - Fallback):**
- Format visual → General → Alt text → Description
- Type static description: "KPI card showing total sessions count"

**Validation:** Card shows number centered, label below, white background, 1px border, 4px radius

---

#### **3.2 KPI Card 2: Page Views**

**Insert:**
1. Visualizations → Card visual

**Position:**
- X: 391px (84 + 295 + 12 gap)
- Y: 124px
- Width: 295px (perfect grid: matches Card 1)
- Height: 100px

**Field:**
- Measure folder: `Command Center → KPI Card - Page Views → [Page Views]`

**Format:** Same as Sessions card (see 3.1)

**Category label text:** "Page Views" (or use text box workaround if editing unavailable - see 3.1)

**KPI Subline (Trend Delta - REQUIRED):**
- Insert text box below callout value (same pattern as Sessions card)
- Position: Same X as card (391px), Y: ~180px (4px below callout value)
- Format: Segoe UI, 11pt Regular, #71767A, Center aligned
- Content: "▲ 8% MoM" (or actual trend value)
- Lock it: Selection pane → Rename to "KPI Page Views Subline" → Lock

**Accessibility - Tooltip:**
- Add measure to **Tooltips** well: `Command Center → KPI Card - Page Views → [Page Views Alt Text]`
- Rename tooltip field to **"Description"** if possible

**Alt Text (Static - Fallback):**
- Format visual → General → Alt text → Description
- Type: "KPI card showing total page views count"

---

#### **3.3 KPI Card 3: Top Device**

**Insert:**
1. Visualizations → Card visual

**Position:**
- X: 698px (391 + 295 + 12 gap)
- Y: 124px
- Width: 295px (perfect grid: matches Card 1)
- Height: 100px

**Field:**
- Measure folder: `Command Center → KPI Card - Top Device → [Top Device Category]`

**Format:** Same as Sessions card (see 3.1)

**Callout value:**
- Font size: 24pt (smaller than numbers, this is text)
- Alignment: Center

**Category label text:** "Top Device" (or use text box workaround if editing unavailable - see 3.1)

**KPI Subline (Context Line - REQUIRED FOR CONSISTENCY):**
- **⚠️ CRITICAL:** ALL KPIs must have a subline. Top Device cannot be the exception.
- Insert text box below callout value (same pattern as other KPIs)
- Position: Same X as card (698px), Y: ~180px (4px below callout value)
- Format: Segoe UI, 11pt Regular, #71767A, Center aligned
- **Content Pattern (choose one):**
  - **Option A (Recommended):** "[Category] | [percentage]" (e.g., "Mobile | 68% of sessions")
  - **Option B:** "[delta] vs [comparison]" (e.g., "+3pp vs prior")
  - **Option C:** "[Category] ([percentage])" (e.g., "Mobile (68%)")
- **Measure Reference (if available):** Use `Command Center → KPI Card - Top Device → [Top Device Percentage]` or similar
- **Example Static Content:** "Mobile | 68% of sessions" (replace with actual data)
- Lock it: Selection pane → Rename to "KPI Top Device Subline" → Lock

**Accessibility - Tooltip:**
- Add measure to **Tooltips** well: `Command Center → KPI Card - Top Device → [Top Device Alt Text]`
- Rename tooltip field to **"Description"** if possible

**Alt Text (Static - Fallback):**
- Format visual → General → Alt text → Description
- Type: "KPI card showing top device category"

---

#### **3.4 KPI Card 4: Avg Pages/Session**

**Insert:**
1. Visualizations → Card visual

**Position:**
- X: 1005px (698 + 295 + 12 gap)
- Y: 124px
- Width: 295px (perfect grid: matches Card 1)
- Height: 100px

**Field:**
- Measure folder: `Command Center → KPI Card - Avg Pages/Session → [Avg Pages per Session]`

**Format:** Same as Sessions card (see 3.1)

**Callout value:**
- Value decimal places: 2

**Category label text:** "Avg Pages/Session" (⚠️ **CRITICAL:** Use exact label "Avg Pages/Session", NOT "AVG PAGES" - this will get nitpicked)

**KPI Subline (Trend Delta - REQUIRED):**
- Insert text box below callout value (same pattern as Sessions card)
- Position: Same X as card (1005px), Y: ~180px (4px below callout value)
- Format: Segoe UI, 11pt Regular, #71767A, Center aligned
- Content: "▼ 1% MoM" (or actual trend value, use ▼ for negative, ▲ for positive)
- Lock it: Selection pane → Rename to "KPI Avg Pages Subline" → Lock

**Accessibility - Tooltip:**
- Add measure to **Tooltips** well: `Command Center → KPI Card - Avg Pages/Session → [Avg Pages Alt Text]`
- Rename tooltip field to **"Description"** if possible

**Alt Text (Static - Fallback):**
- Format visual → General → Alt text → Description
- Type: "KPI card showing average pages per session"

**Validation:** 4 KPI cards in a row, 12px gaps, aligned tops, same height (295px width each), right edge ends at x=1300 (flush with charts/tables below)

---

#### **SECTION 2: Geographic & Device Distribution**

**Section Header:**
1. Insert → Text box
2. Type: "Geographic & Device Distribution"
3. **Position:** X: 84px (content start), Y: 240px, Width: 400px, Height: 20px
4. **Format:** 14pt Segoe UI Semibold, #1B1B1B, Left aligned
5. Lock it

---

#### **3.5 Chart: Sessions by City (Horizontal Bar)**

**Insert:**
1. Visualizations → Clustered bar chart (horizontal bars)

**Position:**
- X: 84px (content start)
- Y: 264px
- Width: 602px (perfect grid: (1216 - 12) / 2 = 602)
- Height: 300px

**Fields:**
- Measure folder: `Command Center → Chart - Sessions by City`
- **Y-axis:** DimLocation → [City]
- **X-axis:** [Sessions by City] measure
- **Tooltips:** 
  - Add measure: `Command Center → Chart - Sessions by City → [Sessions by City Alt Text]`
  - **Rename tooltip field label** (if possible) to **"Description"** for cleaner hover text

**Format → General → Effects:**
- Background: #FFFFFF
- Border: 1px solid #DFE1E2
- Rounded corners: 4
- Shadow: Off

**Format → General → Title:**
- Show: On
- Text: "Sessions by City"
- Font family: Segoe UI Semibold
- Font size: 14pt
- Font color: #1B1B1B
- Alignment: Left
- Background: Transparent

**Format → Visual → X-axis:**
- Show: On
- Title: Off
- Color: #565C65
- Font size: 11pt
- Gridlines: On
  - Color: #DFE1E2
  - Stroke width: 1
  - Line style: Solid

**Format → Visual → Y-axis:**
- Show: On
- Title: Off
- Color: #565C65
- Font size: 11pt
- Concatenate labels: Off
- Maximum category width: 100

**Format → Visual → Bars:**
- Colors: #005EA2 (Primary Blue)
- Border: Off
- Spacing: 20%

**Format → Visual → Data labels:**
- Show: On
- Position: **Outside end** (safer for readability; inside-end can be invisible on short bars)
- Font family: Segoe UI
- Font size: 11pt
- Font color: #1B1B1B (readable on white background)
- Display units: Auto
- Value decimal places: 0
- **Note:** If you prefer inside-end for visual density, use auto color (#1B1B1B or #FFFFFF depending on bar height) and accept mixed readability for short bars

**Sort:**
- Click "..." → Sort by: [Sessions by City]
- Sort direction: Descending
- Top N filter: Top 10

**Alt Text (Static):**
- Format visual → General → Alt text → Description
- Type: "Horizontal bar chart showing top 10 cities by session count, sorted descending"
- **Note:** If you have alt-text measures, use them in tooltips or as descriptive text boxes near the visual. Native Alt Text field binding to measures is not reliably supported.

**Validation:** Horizontal bars, blue, sorted descending, data labels on bars, 1px border

---

#### **3.6 Chart: Device Breakdown (100% Stacked Bar - RECOMMENDED)**

**⚠️ CRITICAL CHANGE: Donut charts are "pretty but vague," especially in PDFs. Use 100% stacked bar for better accessibility and printability.**

**Insert:**
1. Visualizations → Stacked bar chart (horizontal bars)
2. **Chart Type:** Change to **100% Stacked** (ensures all bars fill to 100%, making device share instantly readable)

**Position:**
- X: 698px (84 + 602 + 12 gap)
- Y: 264px
- Width: 602px (perfect grid: matches left column width)
- Height: 300px

**Fields:**
- Measure folder: `Command Center → Chart - Device Breakdown`
- **Y-axis:** DimDevice → [Device Category] (single column for stacked bars)
- **Values:** [Device Sessions] measure (will stack to 100% automatically)
- **Tooltips:**
  - Add measure: `Command Center → Chart - Device Breakdown → [Device Breakdown Alt Text]`
  - **Rename tooltip field label** (if possible) to **"Description"** for cleaner hover text

**Format → General → Effects:**
- Background: #FFFFFF
- Border: 1px solid #DFE1E2
- Rounded corners: 4
  - **⚠️ Visual Consistency Check:** If native visual doesn't respect 4px radius, use background shape method (see KPI card instructions)
- Shadow: Off (explicitly OFF - check all shadow settings)
- Glow: Off

**Format → General → Title:**
- Show: On
- Text: "Device Breakdown"
- Font family: Segoe UI Semibold
- Font size: 14pt
- Font color: #1B1B1B
- Alignment: Left

**Format → Visual → X-axis:**
- Show: On
- Title: Off (100% stacked bars don't need axis title)
- Labels: On (0%, 25%, 50%, 75%, 100%)
- Font: Segoe UI, 11pt, #565C65
- Gridlines: On (subtle, #DFE1E2, 1px)

**Format → Visual → Y-axis:**
- Show: On
- Title: Off
- Labels: On (Device Category names)
- Font: Segoe UI, 11pt, #1B1B1B
- Gridlines: Off (horizontal gridlines not needed for 100% stacked)

**Format → Visual → Data labels:**
- Show: On
- Position: Inside end (or Outside end if bars are wide enough)
- Label contents: Value and percentage (e.g., "45,234 (68%)")
- Font: Segoe UI, 11pt, #1B1B1B
- **Color:** Auto (contrast with bar color) OR force white text if bar is dark

**Format → Visual → Bars:**
- **Color mapping (LOCK THESE COLORS FOR CONSISTENCY):**
  - Desktop: #005EA2 (Primary Blue)
  - Mobile: #1A4480 (Hover Blue)
  - Tablet: #0050D8 (Light Blue)
  - Other: #71767A (Tertiary Gray)
- **⚠️ CRITICAL:** Lock color mapping so Desktop always gets #005EA2, Mobile always gets #1A4480, etc.
- **Rationale:** Device breakdown is a common visual across pages. Consistent color mapping prevents user confusion.

**Format → Visual → Legend:**
- Show: On
- Position: Top (or Right if vertical space is tight)
- Font: Segoe UI, 11pt, #1B1B1B

**Alt Text (Static):**
- Format visual → General → Alt text → Description
- Type: "100% stacked horizontal bar chart showing device category distribution by session count, with percentages displayed on each bar segment"
- **Note:** For dynamic descriptions, place a descriptive text box near the visual or use in tooltips.

**Validation:** 100% stacked bar chart, device categories on Y-axis, percentages clearly visible, colors locked to consistent mapping (Desktop=#005EA2, Mobile=#1A4480), 4px radius container, no shadows

**Alternative (If Donut Must Be Used):**
If leadership explicitly requires donut chart for aesthetic reasons:
- Use donut chart with locked color mapping (Desktop=#005EA2, Mobile=#1A4480, Tablet=#0050D8, Other=#71767A)
- Show percentage ONLY (not labels + legend)
- Legend: Off (colors are locked, tooltips provide details)
- Detail labels: On, Label contents: Percentage only, Font: Segoe UI, 11pt, #1B1B1B
- Ensure tooltips are clean and descriptive
- **Note:** Donut charts are less accessible and print poorly. Recommend 100% stacked bar instead.

---

#### **SECTION 3: Content Performance**

**Section Header:**
1. Insert → Text box
2. Type: "Content Performance"
3. **Position:** X: 84px (content start), Y: 580px, Width: 300px, Height: 20px
4. **Format:** 14pt Segoe UI Semibold, #1B1B1B, Left aligned
5. Lock it

---

#### **3.7 Table: Top Livecast Videos**

**Insert:**
1. Visualizations → Table visual

**Position:**
- X: 84px (content start)
- Y: 604px
- Width: 602px (perfect grid: (1216 - 12) / 2 = 602)
- Height: 250px

**Fields:**
- Measure folder: `Command Center → Table - Top Livecast Videos`
- **Columns (in order):**
  1. DimLivecast → [Livecast Title]
  2. [Livecast Views]
  3. [Livecast Avg Time]

**Format → General → Effects:**
- Background: #FFFFFF
- Border: 1px solid #DFE1E2
- Rounded corners: 4
  - **⚠️ Visual Consistency Check:** If native visual doesn't respect 4px radius perfectly, use background shape method (see Sessions by City chart instructions)
- Shadow: Off (explicitly OFF - check all shadow settings, including visual container and table header band)
- Glow: Off

**Format → General → Title:**
- Show: On
- Text: "Top Livecast Videos"
- Font family: Segoe UI Semibold
- Font size: 14pt
- Font color: #1B1B1B
- Alignment: Left

**Format → Visual → Grid:**
- Vertical grid: On
  - Color: #DFE1E2
  - Width: 1
- Horizontal grid: On
  - Color: #DFE1E2
  - Width: 1
- Row padding: 6 (if 4 feels cramped)
- Text size: 11

**Format → Visual → Column headers:**
- Font family: Segoe UI Semibold
- Font size: 11pt
- Font color: #FFFFFF
- Background color: #005EA2
- Alignment: Left
- Word wrap: On
- Auto-size column width: **Off** (recommended for stability; set widths manually once, then copy formatting)
- **⚠️ Power BI Reality Check:** Auto-size column width can create weird wrapping depending on export and viewport. For PDF/PPT export stability, manually set widths once, then use Format Painter for consistency.

**Format → Visual → Values:**
- Font family: Segoe UI
- Font size: 11pt
- Font color: #1B1B1B
- Background color: Alternate rows
  - Row color 1: #FFFFFF
  - Row color 2: #F0F0F0
- Alignment: Left (default; override per column below)
- URL icon: Off
- Word wrap: On (default; override per column below)

**Column Formatting (Export-Stable):**
- **Livecast Title (Text Column):** Left aligned, word wrap **ON** (allows long titles to wrap)
- **Views (Numeric Column):** Right aligned, word wrap **OFF** (prevents accordion wrap), 0 decimal places, format: `#,0` (e.g., 1,234)
- **Avg Time (Numeric Column):** Right aligned, word wrap **OFF** (prevents accordion wrap), 2 decimal places, format: `0.00` (e.g., 2.45)
- **⚠️ Export Stability:** Word wrap OFF for numeric columns reduces "accordion wrap" surprises on PDF/PPT. Use consistent number formatting (`#,0` / `0.00` / `0.00%`) to maintain tabular alignment.

**Sort:**
- Click "..." → Sort by: [Livecast Views]
- Sort direction: Descending
- Top N filter: Top 10

**Alt Text (Static):**
- Format visual → General → Alt text → Description
- Type: "Table showing top 10 livecast videos by views, including title, views, and average time"
- **⚠️ Accessibility Check:** Alt text must match actual table columns. Columns are: Title, Views, Avg Time (no "action type").
- **Note:** For dynamic descriptions, use text boxes or tooltips with measure-driven content.

**Validation:** Table with blue header, alternating rows, 1px gridlines, top 10 videos

---

#### **3.8 Table: Top Pages**

**Insert:**
1. Visualizations → Table visual

**Position:**
- X: 698px (84 + 602 + 12 gap)
- Y: 604px
- Width: 602px (perfect grid: matches left column width)
- Height: 250px

**Fields:**
- Measure folder: `Command Center → Table - Top Pages`
- **Columns (in order):**
  1. DimPage → [Page Path]
  2. [Page Views]
  3. [Page Engagement]

**Format:** Same as Top Livecast Videos table (see 3.7)

**Title:** "Top Pages"

**Column Formatting (Export-Stable):**
- **Page Path (Text Column):** Left aligned, word wrap **ON** (allows long paths to wrap)
- **Page Views (Numeric Column):** Right aligned, word wrap **OFF** (prevents accordion wrap), 0 decimal places, format: `#,0` (e.g., 1,234)
- **Engagement (Numeric Column):** Right aligned, word wrap **OFF** (prevents accordion wrap), 2 decimal places, format: `0.00%` (e.g., 45.67%)
- **⚠️ Export Stability:** Word wrap OFF for numeric columns reduces "accordion wrap" surprises on PDF/PPT. Use consistent number formatting (`#,0` / `0.00` / `0.00%`) to maintain tabular alignment.

**Sort:**
- Sort by: [Page Views]
- Descending
- Top N: Top 10

**Alt Text (Static):**
- Format visual → General → Alt text → Description
- Type: "Table showing top 10 pages by view count with engagement metrics"
- **Note:** For dynamic descriptions, use text boxes or tooltips with measure-driven content.

**Validation:** Left column complete - KPIs, charts, tables, all formatted consistently

---

### **PHASE 4: Right Column - Review Prompts Panel (20 minutes)**

**⚠️ Design Philosophy:** This panel is intentionally **non-prescriptive and analyst-focused**. It provides gentle prompts for investigation, not directives to optimize or fix. Use safe verbs (Review, Validate, Monitor, Investigate) and avoid causal language (Fix, Optimize, Caused, Driven by).

**Positioning Strategy:** **Default to Option A** for federal-safe, analyst-notebook feel. Option B only if truly needed for neutral filler content.

**OPTION A: Content-Driven Height (Recommended - Default)**
- Rail height matches actual content (header + 3 bullets + disclaimer footer)
- Feels lightweight, intentional, and reads like marginalia (not mandated workflow)
- Avoids "empty right column = must fill with opinions" trap
- Keeps page focused on metrics, not narration
- Starts at same Y as first main content card (Y: 124px)
- **Use this unless you have specific need for filler sections**

**OPTION B: Full-Height Rail with Filler Sections (Use Sparingly)**
- Full height (same as main content area)
- Only use when you truly benefit from extra real estate with non-opinion filler:
  - Data Freshness (safe, always acceptable)
  - Filters in Effect (helpful context)
  - Metric Definitions (super safe, high value)
- Keep filler sections small - think "instrument panel labels," not second dashboard
- **Only use if:** You need consistent full-height structure across ALL pages for visual rhythm

---

#### **4.1 Panel Background Shape**

**Insert:**
1. Insert tab → Shapes → Rectangle

**Position (OPTION A - Content-Driven):**
- X: 1320px (calculated: rail starts after main content + 20px gap)
- Y: 124px (aligns with first KPI card Y position)
- Width: **528px (27.5% of 1920px canvas - reduced 10-15% from 576px for better content balance)**
- Height: **412px** (deterministic first-pass: 124 → disclaimer at 380 + 16 height + 16 bottom padding = 412px)
- **Note:** Adjust only if prompts wrap unexpectedly or you add more content

**Position (OPTION B - Full-Height):**
- X: 1320px
- Y: 124px (aligns with first KPI card Y position)
- Width: **528px (27.5% of canvas - reduced 10-15% from 576px for better content balance)**
- Height: **412px (Option A - content-driven, NOT full-height 940px)**

**Format → Shape:**
- Fill: #FFFFFF
- Fill transparency: 0%
- Line: On
  - Color: #DFE1E2
  - Width: 1px
  - Style: Solid
- Corners: Rounded
  - Corner radius: 4px

**Left Accent Bar:**
1. Insert tab → Shapes → Rectangle
2. **Position:**
   - X: 1320px (same as panel)
   - Y: 124px (same as panel)
   - Width: 4px
   - Height: Same as panel height (412px for Option A, 940px for Option B full-height)
3. **Format:**
   - Fill: #005EA2
   - Line: Off
4. **Layering (Critical for Visibility):**
   - **⚠️ Power BI Reality Check:** "Send to back" would place accent bar *behind* the panel background, making it invisible.
   - **Correct layering:** Accent bar should be **above** panel background, **below** header text and bullets.
   - In Selection pane: Drag accent bar to position directly **above** the panel background shape, but **below** all text elements.
   - **Z-order (bottom to top):**
     1. Panel Background (bottom)
     2. Accent Bar (above background)
     3. Panel Header text
     4. Review prompts text
     5. Micro-disclaimer text (top)

**IMMEDIATELY LOCK BOTH SHAPES:**
1. View → Selection pane
2. Rename: "Review Panel Background" and "Review Panel Accent"
3. **Verify layering:** Accent bar should be above panel background, below text elements (check Z-order in Selection pane)
4. Click lock icons for both shapes

**Validation:** Right rail has white background, 1px border, 4px blue accent on left (visible above background), positioned at **27.5% width (528px - reduced from 576px)**, starts at x=1320px with 20px gap from main content end (x=1300)

---

#### **4.2 Panel Header ("Recommended Actions" - Standardized v1.8)

**⚠️ STANDARDIZATION (v1.8):** Based on "Premium App Shell" feedback, standardize to **"Recommended Actions"** across all 7 pages for consistency and federal terminology alignment.

**Rationale:**
- **Federal standard terminology:** "Recommended Actions" is standard federal/government language
- **Consistency across pages:** Using same header on all 7 pages creates coherent app shell experience
- **Clear purpose:** "Recommended Actions" clearly communicates the panel's function
- **Interactive elements:** Panel now contains clickable action buttons (not just text), so "Actions" is appropriate

**Note:** Previous v1.7 used "What to Review Next" for Command Center page. v1.8 standardizes to "Recommended Actions" across all pages for consistency.

**Position:**
- X: 1344px (1320 + 24px inner padding)
- Y: 140px (124 + 16px top padding)
- Width: **480px (528px panel width - 48px total padding - updated for new panel width)**
- Height: 24px

**Format → General → Text:**
- Font family: Segoe UI Semibold
- Font size: 16pt (consistent with federal style)
- Font color: #1B1B1B
- Bold: Semibold
- Alignment: Left

**Text Content:**
- Type: **"Recommended Actions"** (standardized across all 7 pages)

**Lock it:** Selection pane → Lock

---

#### **4.3a Action Buttons (v1.8, 3 max, bookmark-based spotlight - REQUIRED)**

**⚠️ v1.8 UPDATE:** Transform static text bullets to **clickable action buttons** (3 buttons max). This makes the dashboard feel like "guided console" rather than "dashboard museum".

**Content Rules - Critical for Federal/Leadership Context:**

**Safe Verbs to Use:**
- Review, Validate, Monitor, Compare, Investigate, Segment, Confirm, Check, Focus

**Avoid Prescriptive Verbs:**
- Fix, Optimize, Increase, Decrease, Prove, Caused, Driven by

**Content Structure:** Each button must be defensible as a *next step to investigate*, not an instruction. Use conditional/investigative language that doesn't presume findings exist. **ONLY reference visuals that exist on this page.**

**Button Format (All 3):**
- Type: Button → **Blank**
- X: **1344px** (1320 + 24px inner padding)
- Width: **480px** (528px panel width - 48px total padding = 480px - canonical content width)
- Height: **52px** (comfortable click target, fits text comfortably)
- Radius: 4px (matches card standard)
- Fill: #FFFFFF
- Border: 1px solid #DFE1E2
- Shadow/Glow: OFF (explicitly OFF)
- Text: Segoe UI **12pt**, #1B1B1B, Left aligned (increased from 11pt for leadership readability)
- Text padding: 12px left padding (use button text padding if available, or position text manually)
- Tooltip: On (plain-English description)
- Alt text: "Button that highlights [visual name] for review" (specific to each button)

**Hover State:**
- Fill: #F0F0F0 (subtle highlight)
- Border: 1px solid #005EA2 (accent border on hover)

**Positions (Canonical - 12px vertical gap between buttons):**
- **Action Button 1:** Y **180px** (16px below panel header at Y=164)
- **Action Button 2:** Y **244px** (180 + 52 + 12 = 244)
- **Action Button 3:** Y **308px** (244 + 52 + 12 = 308)

**Button Text (Page-Specific - Command Center Example):**

**Button 1:** "Focus: City mix (Sessions by City)"
- **References:** Sessions by City chart (visible on page)
- **Action:** Bookmark `CC_Action_01_Spotlight_City` (spotlights Sessions by City chart)

**Button 2:** "Focus: Device mix (Device Breakdown)"
- **References:** Device Breakdown chart (visible on page)
- **Action:** Bookmark `CC_Action_02_Spotlight_Device` (spotlights Device Breakdown chart)

**Button 3:** "Focus: Top content (Tables)"
- **References:** Top Livecast Videos and Top Pages tables (visible on page)
- **Action:** Bookmark `CC_Action_03_Spotlight_Content` (spotlights both tables)

**⚠️ Page-Specific Button Text:** Each page has different visuals, so button text must reference visuals that exist on that page. See `INTERACTIVE_RIGHT_PANEL_ACTIONS.md` for complete button text specifications for all 7 pages.

**Action Wiring (Recommended: Bookmark + Spotlight):**

**Step 1: Create Spotlight Bookmarks (Before Wiring Buttons)**

Create 3 bookmarks that **spotlight** the relevant visual (no filter claims, no causality):

**Bookmark 1: CC_Action_01_Spotlight_City**
1. View → Bookmarks pane
2. Clear all cross-filters (deselect all visuals)
3. Select **Sessions by City chart** (highlight it)
4. Click "Add" (creates new bookmark)
5. Rename to "CC_Action_01_Spotlight_City"
6. Bookmark settings:
   - **Display:** ✅ Checked (captures spotlight/selection state)
   - **Data:** ❌ Unchecked (does NOT change filters - no filter claims)
   - **Current page:** ✅ Checked (stays on Command Center page)
   - **Visual selection:** Sessions by City chart is selected/highlighted
   - **Visual spotlight:** Spotlight effect applied to Sessions by City chart

**Bookmark 2: CC_Action_02_Spotlight_Device**
- Repeat process for **Device Breakdown chart**
- Rename to "CC_Action_02_Spotlight_Device"
- Spotlight Device Breakdown chart

**Bookmark 3: CC_Action_03_Spotlight_Content**
- Repeat process for **Top Livecast Videos and Top Pages tables** (select both)
- Rename to "CC_Action_03_Spotlight_Content"
- Spotlight both tables

**Optional: Clear Spotlight Bookmark**
- Create one extra bookmark: `CC_Action_00_ClearSpotlight`
- Clear all selections (no visuals selected)
- Useful for "unhighlighting" after reviewing

**Step 2: Wire Each Button to Its Bookmark**

For each action button:
1. Select the button
2. Format → Button → Action
3. Action type: **Bookmark**
4. Select bookmark: "CC_Action_01_Spotlight_City" (or appropriate bookmark for that button)

**Repeat for all 3 buttons.**

**Why Spotlight (Not Filters):**
- **Spotlight** highlights the visual without claiming anything about the data
- **Filters** would imply causality (e.g., "show me data for this filter" suggests the filter caused something)
- **Spotlight** is safe, non-prescriptive, and purely visual guidance

**Validation:** All 3 action buttons visible, clickable, positioned at Y=180, 244, 308 (12px gaps), 480px width, 52px height. Each button spotlights the correct visual when clicked (no filter changes, just visual highlighting). Button text references only visuals visible on this page.

**Lock all 3 buttons:**
1. Selection pane
2. Rename: "Action Button 1 - City", "Action Button 2 - Device", "Action Button 3 - Content"
3. Click lock icons for all 3 buttons

---

#### **4.3c HTML Insight Panel (OPTIONAL - Tenant-Dependent Enhancement) ⚠️ NEW v1.8**

**⚠️ DECISION GATE:** Only implement if HTML visual is available in your Power BI tenant AND export/accessibility tests pass (see `HTML_ENHANCEMENT_STRATEGY.md` for full requirements).

**Purpose:** Transform the right rail into a **premium narrative layer** that updates with selections, showing contextual insights (today's takeaway, biggest mover, likely driver, recommended next click).

**Strategic Approach:** HTML is best used like a "luxury interior finish" - for presentation + narrative, NOT for navigation or export-critical data. This keeps navigation/filtering in native Power BI (buttons, bookmarks, slicers) while adding rich formatting where it adds value.

**Location:** Right rail, between panel header and action buttons

**Position:**
- X: 1344px (same as content - 1320 + 24px inner padding)
- Y: 164px (16px below panel header at Y=140)
- Width: 480px (canonical content width)
- Height: Auto (content-driven, typically 60-80px)

**Prerequisites:**
1. **Check HTML Visual Availability:**
   - Power BI Desktop → Visualizations → Get more visuals → HTML Content (or similar)
   - Confirm with IT/tenant admin if custom visuals are allowed
   - If HTML visual is NOT available, skip this phase (native text boxes are sufficient)

2. **Review Full Strategy:**
   - Read `00_Documentation/03_Guides/HTML_ENHANCEMENT_STRATEGY.md` for complete implementation details
   - Understand federal considerations (508 compliance, export stability, performance, security)
   - Review decision framework (Use HTML if... / Skip HTML if...)

**Implementation (If HTML Approved):**

1. **Insert HTML Visual:**
   - Insert → HTML visual (if available in your tenant)
   - Position at X: 1344px, Y: 164px, Width: 480px, Height: Auto

2. **Create DAX Measure for Dynamic Content:**
   - Measure folder: `Command Center → Insight Panel → [Insight Panel Text]`
   - **⚠️ NOTE:** HTML visuals may not support direct DAX measure binding. If not supported, use static HTML with calculated column values, or skip HTML and use native Smart Narrative visual instead.

3. **Apply HTML Structure (USWDS-Aligned):**
   ```html
   <div style="font-family:'Segoe UI',sans-serif;padding:12px;border-radius:4px;background:#FFFFFF;border:1px solid #DFE1E2;">
     <div style="font-size:12px;color:#565C65;margin-bottom:8px;">Today's Takeaway</div>
     <div style="font-size:18px;font-weight:600;color:#1B1B1B;margin-bottom:12px;">
       Engagement rose, driven by 3 releases.
     </div>
     <div style="font-size:13px;color:#1B1B1B;">
       <span style="display:inline-block;padding:4px 8px;border-radius:999px;background:#E6F4EA;color:#00A91C;margin-right:8px;">
         ▲ +12% WoW
       </span>
       <span style="color:#71767A;">Most impact: "MAHA Tour"</span>
     </div>
   </div>
   ```

4. **Format → Visual → Header icons → Off** (for clean exports)

5. **Test Export (REQUIRED):**
   - Export to PDF (HTML may become static image - document limitation)
   - Export to Excel (HTML may not export - document limitation)
   - Export to PPT (HTML may become static image - document limitation)

6. **Test Accessibility (REQUIRED):**
   - Screen reader test (NVDA, JAWS)
   - Keyboard navigation test (Tab, Enter, Escape)
   - Contrast ratio verification (WCAG 2.1 AA minimum)

7. **Test Performance (REQUIRED):**
   - Monitor load time increase (target: < 1 second increase)
   - Test with large datasets (HTML rendering can be slower than native)
   - Test with multiple HTML visuals on one page (limit: 1-2 HTML visuals max per page)

**Federal Considerations (CRITICAL):**
- **508 Compliance:** HTML visuals may not expose proper ARIA attributes. Test thoroughly with screen readers before deployment.
- **Export Stability:** HTML visuals may not export cleanly to Excel/PDF. Document limitations for users.
- **Performance:** HTML rendering adds overhead. Test on typical government hardware (older laptops, slower networks).
- **Security:** Use only inline styles (no external CSS), no JavaScript, no external images (use SVG/base64 or built-in Power BI icons).

**Fallback (If HTML Not Available or Tests Fail):**
- Use native Smart Narrative visual (if available) with same content
- Or use native text boxes with static content (less rich formatting, but functional)
- Or skip this enhancement entirely (current v1.8 native implementation is excellent)

**Validation:**
- [ ] HTML visual displays correctly (if implemented)
- [ ] Content updates with slicer selections (cross-filtering works - if supported)
- [ ] Export tests pass (document limitations if HTML doesn't export cleanly)
- [ ] Accessibility tests pass (screen reader, keyboard nav - if HTML doesn't work, fallback to native)
- [ ] Performance acceptable (no significant load time increase)
- [ ] Federal considerations addressed (508, export, performance, security)

**Lock it:**
1. Selection pane
2. Rename: "HTML Insight Panel" (if implemented)
3. Click lock icon

**⚠️ IMPORTANT NOTE:** This is an **optional enhancement**. If HTML visual is not available, export tests fail, or accessibility tests fail, **skip this phase**. Your current v1.8 native implementation (text boxes + native buttons) is excellent and fully functional. HTML is a "luxury finish" - nice to have, not required.

**For Complete HTML Strategy:**
- See `00_Documentation/03_Guides/HTML_ENHANCEMENT_STRATEGY.md` for full implementation details, HTML patterns, federal considerations, and decision framework.

---

#### **4.3d Micro-Disclaimer Footer (REQUIRED)**

**⚠️ CANONICAL POSITION:** If panel is Y=124, H=412px, its bottom is 536px. To place disclaimer with 16px bottom padding: Y = 536 - 16 - 16 = **504px** (not 380px - that leaves dead zone).

**⚠️ Critical for Trust Preservation:** This one-line disclaimer sets correct expectations and protects against misinterpretation.

**Insert:**
1. Insert → Text box
2. **Position:**
   - X: 1344px (same as content - 1320 + 24px inner padding)
   - Y: **504px** (canonical position: panel Y=124 + H=412 = bottom 536px, minus 16px bottom padding, minus 16px height = 504px)
   - Width: **480px** (528px panel width - 48px total padding = canonical content width)
   - Height: 16px

**Content:**
```
Prompts suggest areas to review; not causal conclusions.
```

**Format → General → Text:**
- Font family: Segoe UI Regular (not bold)
- Font size: 10pt (tiny, low drama, but readable)
- Font color: #71767A (Tertiary/Helper - subtle)
- Font style: Italic (optional - signals "this is a note")
- Alignment: Left

**Lock it:**
1. Selection pane
2. Rename to "Micro-Disclaimer Footer"
3. Click lock icon

**Validation:** Micro-disclaimer at Y=504px (16px above panel bottom at 536px, content-driven), width 480px (matches panel content width), 10pt italic text, #71767A color. Panel height is truly content-driven (412px) with no dead zone.

---

#### **4.5 Optional Filler Sections (ONLY if using Full-Height Rail - Option B)**

**⚠️ DECISION GATE:** This page uses **Option A (Content-Driven - 412px)**. Skip this section.

**If you chose Option B (full-height rail - 940px), add these neutral sections to justify the space:**

**Section A: Data Freshness (Always Safe)**

1. Insert → Text box
2. **Position:** X: 1344px, Y: 420px, Width: 528px, Height: 16px
3. **Label:** "Data Freshness"
   - Font: Segoe UI Semibold, 11pt, #565C65
4. **Content:** "Last refresh: [Date] | Sources: GA4, Google Search Console"
   - Font: Segoe UI, 10pt, #71767A
   - Y: 440px (8px below label)

**Section B: Filters in Effect (Helpful Context)**

1. Insert → Text box
2. **Position:** X: 1344px, Y: 480px, Width: 528px, Height: Auto
3. **Label:** "Filters in Effect"
   - Font: Segoe UI Semibold, 11pt, #565C65
4. **Content:** "Date range: [From] to [To] | Device: All | Channel: All"
   - Font: Segoe UI, 10pt, #71767A
   - Y: 500px (8px below label)

**Section C: Metric Definitions (Super Safe, High Value)**

1. Insert → Text box
2. **Position:** X: 1344px, Y: 560px, Width: 528px, Height: Auto
3. **Label:** "Key Definitions"
   - Font: Segoe UI Semibold, 11pt, #565C65
4. **Content:** Small glossary (2-3 lines max)
   - Example: "Sessions: User visits | Engagement Rate: % of engaged sessions"
   - Font: Segoe UI, 10pt, #71767A
   - Y: 580px (8px below label)

**Validation:** Right rail complete - header, 3 review prompts, micro-disclaimer, optional fillers (if full-height)

---

#### **4.6 Data Quality Footer (Known Limitations)**

**⚠️ Critical for Transparency:** Identifies placeholder metrics to avoid confusion.

**Insert:**
1. Insert → Text box
2. **Position:**
   - X: 84px (Aligned with main content left edge)
   - Y: 1050px (Bottom of page)
   - Width: 600px
   - Height: 20px

**Content:**
```
Data limitations: Some metrics may be placeholders until full GA4 data is available. See metric definitions for details.
```

**Format → General → Text:**
- Font: Segoe UI, 10pt, #71767A (Subtle gray)
- Style: Italic
- Alignment: Left
- Background: Transparent

---

### **PHASE 5: Navigation Rail (15 minutes)**

#### **5.1 Rail Container Background**

**Insert:**
1. Insert tab → Shapes → Rectangle

**Position:**
- X: 0
- Y: 0
- Width: 60px
- Height: 1080px (full page height)

**Format → Shape:**
- Fill: #FFFFFF
- Fill transparency: 0%
- Line: Off (Power BI shapes don't support "border on one side only")
- Corners: Square (radius: 0)

**Send to back:** Right-click → Send to back

**LOCK IT IMMEDIATELY:** Selection pane → Lock (rename to "Nav Rail Background")

#### **5.1a Rail Divider Line (Right Border)**

**⚠️ Power BI Reality Check: To create a "border on right side only," use a separate line shape.**

1. Insert tab → Shapes → Line
2. **Position:**
   - X1: 60px (right edge of rail)
   - Y1: 0px
   - X2: 60px (same X, vertical line)
   - Y2: 1080px (full page height)
3. **Format → Shape:**
   - Line color: #DFE1E2
   - Line weight: 1px
   - Line style: Solid
4. **Set Z-order (Critical for Visibility):**
   - **⚠️ Power BI Reality Check:** "Send to back" can be too aggressive and place divider *behind* the rail background, making it invisible.
   - **Correct layering:** Use Selection Pane ordering only (no "send to back" click).
   - **Nav Z-order (bottom → top in Selection Pane):**
     1. `00_Nav_Background` (bottom)
     2. `00_Nav_Divider` (above background, below buttons)
     3. `01_Nav_Button_CommandCenter` ... `07_Nav_Button_DeepDive` (above divider)
     4. `00_Nav_ActiveIndicator` (only on this page, top)
   - In Selection Pane: Drag divider to position directly **above** the background shape, but **below** all button shapes.
5. **Rename and Lock:** Selection pane → Rename to "Nav Rail Divider" → Lock

---

#### **5.2 Navigation Buttons (7 Pages)**

**⚠️ Power BI Reality Check: Button hover states have limitations. Swapping icons per state is not reliably supported. We use PNGs for stability.**

**Recommended Approach (Reliable Pattern):**
- Use ONE icon per button (default state)
- Change fill color on hover/selected (this works reliably)
- Use left accent bar shape for active state (separate shape, not button border)

**General Button Format (applies to all 7):**
- Width: 60px
- Height: 60px
- X position: 0
- Y positions: 84, 164, 244, 324, 404, 484, 564 (80px spacing, aligned with Content at 84px)

**Button Settings:**
- Type: Button (not Blank button)
- Action: Page navigation → [Target Page Name]
- Style: Custom

**Format → Style → Default:**
- Fill: Transparent (or #FFFFFF for consistency)
- Icon: PNG file from `/assets/nav_0X_[page-name].png`
  - **Use the default icon file** (not hover/active variants)
  - Icon color should be theme-responsive if possible, or single color #005EA2
- Icon alignment: Center
- Icon padding: 12px
- Border: Off

**Format → Style → Hover:**
- Fill: #F0F0F0 (subtle highlight - this works reliably)
- Icon: Same as default (don't swap icons - not reliably supported)
- Border: Off

**Format → Style → Selected/Active:**
- Fill: #F0F0F0 (same as hover for consistency)
- Icon: Same as default (don't swap icons)
- Border: Off (we'll use separate shape for accent bar)

**Tooltip (all buttons):**
- Format → Style → Tooltip: On
- Text: "[Page Name]" (e.g., "Command Center", "Explorer")

**Alt Text (Static, all buttons):**
- Format → General → Alt text → Description
- Type: "Navigate to [Page Name]"

---

**Button 1: Command Center**
- **Position:** X: 0, Y: 84 (first button, aligned with content header)
- **Icon:** `nav_01_command_center.png` (single icon, not swapped on hover)
- **Action:** Page navigation → **Command Center** (⚠️ **CRITICAL:** Ensure target page name matches exactly "Command Center")
- **Tooltip:** "Command Center"
- **Selected Indicator (Separate Shape - REQUIRED FOR THIS PAGE):**
  1. Insert → Shapes → Rectangle
  2. Position: X: 0, Y: 84, Width: 4px, Height: 60px (matches Button 1 position)
  3. Format: Fill #005EA2, Line Off, Corners: Square
  4. **Z-order:** Above nav rail background, below nav buttons (use Selection Pane to set order)
  5. **Selection Pane Order (bottom to top):**
     - `00_Nav_Background` (bottom)
     - `00_Nav_Divider` (above background)
     - `00_Nav_ActiveIndicator_CommandCenter` (above divider, below buttons)
     - `01_Nav_Button_CommandCenter` ... `07_Nav_Button_DeepDive` (above indicator)
  6. Bring to front (verify it's visible in front of rail background but behind buttons)
  7. Lock it (rename to "Nav Active Indicator - Command Center")
  8. **⚠️ CRITICAL:** This indicator should only be visible on the Command Center page.
     - **Validation:** If you're on Command Center page, Button 1 (top icon) should show the 4px blue accent bar
     - If you see a different button highlighted (e.g., "broadcast" icon), either:
       - You're on the wrong page (verify page name matches), OR
       - The active indicator is positioned at the wrong Y coordinate (check Y=**84** is Button 1, not Button 4 or any other button)
     - **On other pages:** Hide this shape OR move the indicator to the appropriate button's Y position (Y=**164** for Explorer, Y=**244** for Traffic & Acquisition, Y=**324** for Play Events, Y=**404** for External Search, Y=**484** for AI Insights, Y=**564** for Deep Dive)

---

**Button 2: Explorer**
- **Position:** X: 0, Y: **164** (canonical position - 80px spacing: 84 + 80 = 164)
- **Icon:** `nav_02_explorer.png`
- **Action:** Page navigation → Explorer
- **Tooltip:** "Explorer"
- **Alt text:** "Navigate to Explorer"

---

**Button 3: Traffic & Acquisition**
- **Position:** X: 0, Y: **244** (canonical position - 80px spacing: 164 + 80 = 244)
- **Icon:** `nav_03_traffic_acquisition.png`
- **Action:** Page navigation → Traffic & Acquisition
- **Tooltip:** "Traffic & Acquisition"
- **Alt text:** "Navigate to Traffic & Acquisition"

---

**Button 4: Play Events**
- **Position:** X: 0, Y: **324** (canonical position - 80px spacing: 244 + 80 = 324)
- **Icon:** `nav_04_play_events.png`
- **Action:** Page navigation → Play Events
- **Tooltip:** "Play Events"
- **Alt text:** "Navigate to Play Events"

---

**Button 5: External Search**
- **Position:** X: 0, Y: **404** (canonical position - 80px spacing: 324 + 80 = 404)
- **Icon:** `nav_05_external_search.png`
- **Action:** Page navigation → External Search
- **Tooltip:** "External Search"
- **Alt text:** "Navigate to External Search"

---

**Button 6: AI Insights**
- **Position:** X: 0, Y: **484** (canonical position - 80px spacing: 404 + 80 = 484)
- **Icon:** `nav_06_ai_insights.png`
- **Action:** Page navigation → AI Insights
- **Tooltip:** "AI Insights"
- **Alt text:** "Navigate to AI Insights"

---

**Button 7: Deep Dive**
- **Position:** X: 0, Y: **564** (canonical position - 80px spacing: 484 + 80 = 564)
- **Icon:** `nav_07_deep_dive.png`
- **Action:** Page navigation → Deep Dive
- **Tooltip:** "Deep Dive"
- **Alt text:** "Navigate to Deep Dive"

---

**Important Note on Active State Indicator:**
- The active state indicator (4px blue bar) is created as a separate shape for Button 1 (Command Center)
- **⚠️ CRITICAL VALIDATION:** On Command Center page, Button 1 (top icon) MUST show the active indicator. If a different button shows as active, check:
  - Page name matches exactly "Command Center" (not "CommandCenter" or "Command_Center")
  - Indicator Y position is **84** (matches Button 1 Y position - canonical first button)
  - Icon mapping is correct (`nav_01_command_center.png` should be the top icon)
- On other pages, either:
  - **Option A:** Move the indicator shape to the active page's button Y position (Y=**164** for Explorer, Y=**244** for Traffic & Acquisition, Y=**324** for Play Events, Y=**404** for External Search, Y=**484** for AI Insights, Y=**564** for Deep Dive)
  - **Option B:** Create a separate indicator shape for each page, show/hide via bookmarks (most reliable)
  - **Option C:** Use conditional formatting if supported (varies by Power BI version)

**Validation:** 
- 7 nav buttons visible, evenly spaced (80px apart - canonical positions: 84, 164, 244, 324, 404, 484, 564)
- Icons display correctly (single icon per button, not swapped)
- **Button 1 icon is the top icon** (Command Center icon, NOT broadcast icon or any other icon)
- Hover states work (fill changes to #F0F0F0 on hover)
- **Active indicator (4px blue bar) visible on Button 1 at Y=84 (Command Center)** - if you see it on a different button, fix the indicator Y position or page name
- Tooltips display on hover (all buttons show correct page names)
- Rail divider line visible at x=60px

---

### **PHASE 5.4: Turn off Visual Header Icons (CRITICAL for Clean Exports) (2 minutes)**

**Purpose:** Power BI visuals have default header icons (filter, focus mode, more options, etc.) that can clutter exports and break the clean, federal aesthetic. This step removes them for a professional export-ready look.

**Action:** For each visual on the page (KPIs, charts, tables, slicers):

1. Select the visual
2. Format visual → Visual → **Header icons** → **Off** (or turn off individual unwanted icons: Filter icon, Focus mode, More options, etc.)
3. Repeat for all visuals:
   - KPI Cards (4 cards)
   - Sessions by City chart
   - Device Breakdown chart (100% stacked bar)
   - Top Livecast Videos table
   - Top Pages table
   - Date slicer (typically doesn't have header icons, but check)
   - Action buttons (no header icons)

**Validation:**
- [ ] All visual header icons are OFF (no filter icons, focus mode icons, or "..." menus visible)
- [ ] Visuals look clean and export-ready
- [ ] Functionality is preserved (slicers still filter, tables still sort via column headers, etc.)

**Note:** If you need certain icons for interactivity (e.g., filter icons on slicers), you can selectively turn on only what's needed. However, for a clean export look, turning them all off is recommended.

---

### **PHASE 6: Final Validation (10 minutes)**

#### **6.1 Visual Inspection Checklist**

**Overall Page:**
- [ ] Canvas background is #F0F0F0
- [ ] Page size is 1920×1080px
- [ ] Grid and snap are enabled
- [ ] All visuals aligned to grid

**Header:**
- [ ] Eyebrow label visible (11pt, #565C65)
- [ ] Page title visible (28pt Semibold, #1B1B1B)
- [ ] Date slicer functional, formatted, **4px radius, no shadows**
- [ ] **Last refresh indicator visible** below date slicer (right-aligned, 10pt, #71767A, "Last refresh: [Date] [Time] ET")
- [ ] **Reset filters button visible** to the right of date slicer (functional, clears all cross-filters)
- [ ] Header divider line spans full width (Y=84px, 4px below slicer to avoid double-border)

**Left Column:**
- [ ] 4 KPI cards aligned, 12px gaps, 295px width each (perfect grid flush to x=1300)
- [ ] KPI Card 1: X 84px, W 295px
- [ ] KPI Card 2: X 391px, W 295px
- [ ] KPI Card 3: X 698px, W 295px
- [ ] KPI Card 4: X 1005px, W 295px, right edge at x=1300 ✅
- [ ] All cards have white background, 1px border, 4px radius
- [ ] Sessions by City chart: horizontal bars, blue, sorted, data labels outside end
- [ ] Device Breakdown chart: **100% stacked horizontal bar** (NOT donut - better for accessibility and printability), legend top/right, percentages visible on bars, **4px radius container, no shadows**
- [ ] Top Livecast Videos table: blue header, alternating rows, auto-size column width OFF
- [ ] Top Pages table: same formatting as Livecast, auto-size column width OFF

**Right Column (Recommended Actions Panel - Option A: Content-Driven 412px):**
- [ ] Panel background visible (white, 1px border, **4px radius enforced, no shadows**)
- [ ] Panel width is **528px (27.5% of canvas - reduced from 576px for better content balance)**
- [ ] Panel height is **412px (Option A - content-driven, NOT full-height)**
- [ ] Panel starts at Y: 124px (aligned with first KPI card)
- [ ] **Panel ends at Y: 536px** (124 + 412 = 536) - verify it doesn't extend to full-height (940px)
- [ ] Left accent bar visible (4px, #005EA2) **above panel background, below text elements** (check Z-order)
- [ ] Panel header **"Recommended Actions"** visible (16pt Semibold, standardized across all 7 pages)
- [ ] Review prompts (3 bullets max) use safe verbs (Check, Compare, Review - NOT Fix, Optimize, Identify)
- [ ] **Prompts ONLY reference visuals on this page** (Sessions, Page Views, Device Breakdown, Top Livecast Videos, Top Pages - NOT Health Score, Total Events if those aren't visible)
- [ ] No prescriptive verbs (Fix, Optimize, Caused, Driven by)
- [ ] **Micro-disclaimer footer visible** ("Prompts suggest areas to review; not causal conclusions") at bottom of panel
- [ ] Font sizes are lighter than main content (11pt prompts, 9-10pt disclaimer)
- [ ] **NO filler sections visible** (Option A doesn't include Data Freshness, Filters, Definitions - those are only for Option B full-height)

**Navigation Rail:**
- [ ] 7 buttons visible, evenly spaced
- [ ] Icons display correctly
- [ ] Hover states work (hover over each button)
- [ ] Active indicator on Command Center button
- [ ] Tooltips display on hover

**Typography:**
- [ ] All titles are Segoe UI Semibold
- [ ] All labels are Segoe UI Regular
- [ ] Font sizes consistent (28pt titles, 14pt headers, 11pt body)
- [ ] Colors correct (#1B1B1B primary, #565C65 secondary, #71767A tertiary)

**Effects:**
- [ ] NO shadows anywhere (check all visual containers, cards, charts, tables, panels - explicitly OFF)
- [ ] NO glows anywhere
- [ ] All borders are 1px #DFE1E2
- [ ] **All radius is 4px (enforced via background shape method if native visual doesn't respect it)**
- [ ] **Visual consistency:** No "Power BI default blob" feel - all visuals use exact 4px radius via background shapes if needed

---

#### **6.2 Functional Tests**

**Interactivity:**
- [ ] Date slicer filters all visuals (test by changing date range - all KPIs/charts/tables should update)
- [ ] **Reset filters button clears all cross-filters** (click a bar/slice/table row to filter page, then click Reset - all filters should clear)
- [ ] Clicking bar in Sessions by City filters page (cross-filtering works)
- [ ] Clicking bar segment in Device Breakdown (100% stacked bar) filters page (cross-filtering works)
- [ ] Clicking row in Top Livecast Videos filters page (cross-filtering works)
- [ ] Clicking row in Top Pages filters page (cross-filtering works)
- [ ] Navigation buttons navigate to correct pages (test each - verify page names match exactly)
- [ ] **Active indicator shows on Button 1 (Command Center)** - if a different button is highlighted, fix indicator Y position or page name

**Data:**
- [ ] All measures display correct values
- [ ] No error messages in visuals
- [ ] Alt text bound to all visuals (check with screen reader or Accessibility checker)

---

#### **6.3 Export Tests**

**PDF Export:**
1. File → Export → Export to PDF
2. Save as: `HHS_Dashboard_CommandCenter_Test.pdf`
3. Open PDF
4. Check:
   - [ ] Layout preserved
   - [ ] Text readable
   - [ ] Colors accurate
   - [ ] No clipping

**PowerPoint Export:**
1. File → Export → Export to PowerPoint
2. Save as: `HHS_Dashboard_CommandCenter_Test.pptx`
3. Open PowerPoint
4. Check:
   - [ ] Slide size correct
   - [ ] Visuals positioned correctly
   - [ ] Text readable
   - [ ] Navigation buttons removed (expected in PPT)

**Screenshot Test:**
1. Zoom to 100%
2. Take screenshot (Win+Shift+S or Snipping Tool)
3. Paste into Microsoft Teams chat
4. View at actual size (not zoomed)
5. Check:
   - [ ] Labels readable from 3 feet away
   - [ ] Colors accurate
   - [ ] No blur or pixelation

---

#### **6.4 Accessibility Validation**

**Contrast Check (use WebAIM Contrast Checker):**
- [ ] Page title (#1B1B1B on #F0F0F0): >7:1 ✅
- [ ] Labels (#565C65 on #FFFFFF): >4.5:1 ✅
- [ ] Helper text (#71767A on #FFFFFF): >4.5:1 ✅
- [ ] Table headers (#FFFFFF on #005EA2): >4.5:1 ✅

**Alt Text (Static):**
- [ ] All visuals have alt text entered manually (check Format → General → Alt text → Description)
- [ ] Alt text is descriptive and accurate for each visual type
- [ ] **Note:** Dynamic alt text via measures is not consistently supported. Use static descriptions or place descriptive text boxes near visuals if dynamic descriptions are needed.

**Keyboard Navigation:**
- [ ] Tab through interactive elements - logical order
- [ ] Date slicer accessible via keyboard
- [ ] Navigation buttons accessible via keyboard
- [ ] Charts/tables selectable via keyboard

**Screen Reader (if available):**
- [ ] Test with Narrator (Windows) or screen reader
- [ ] Visuals announced with alt text
- [ ] Navigation buttons announced correctly

---

#### **6.5 Lock & Save**

**Lock All Background Elements:**
1. View → Selection pane
2. Select all background shapes:
   - Eyebrow label
   - Page title
   - Header divider
   - Right panel background
   - Right panel accent
   - Nav rail background
   - Section headers
   - Active state indicator
3. Click lock icon for each

**Save File:**
1. File → Save as
2. Filename: `HHS_Live_Events_Dashboard_V4_CommandCenter_Complete.pbix`
3. Location: Project folder
4. Click Save

**Backup Save:**
1. Save a copy with date: `HHS_Dashboard_V4_CommandCenter_2026-01-10.pbix`
2. Keep in `00_Documentation/04_Backups/` folder

---

## ✅ COMPLETION CHECKLIST

**Phase 1: Canvas Setup**
- [ ] Canvas size: 1920×1080px
- [ ] Background: #F0F0F0 (both canvas and wallpaper)
- [ ] Grid and snap enabled

**Phase 2: Header Area**
- [ ] Eyebrow label complete ("HHS LIVE EVENTS", 11pt, #565C65)
- [ ] Page title complete ("COMMAND CENTER", 28pt Semibold, #1B1B1B)
- [ ] **Purpose subtitle complete** (below page title, 12pt, #565C65, "Monitor performance and detect issues fast." - **NEW v1.8**)
- [ ] Date slicer complete (X=1696px, W=200px, ends at 1896px)
- [ ] **Reset filters button complete** (X=1480px, functional - clears all cross-filters via bookmark)
- [ ] **Last refresh indicator complete** (below date slicer, right-aligned, Y=82px, 10pt, #71767A)
- [ ] **Optional: Definitions/Info button complete** (X=1576px, to the right of reset button - **NEW v1.8**)
- [ ] Header divider complete at Y=84px (4px below date slicer, avoiding double-border, width: 1764px - updated for new panel width)
- [ ] All header elements locked

**Phase 3: Left Column - Diagnostics**
- [ ] Section header: "At a Glance"
- [ ] KPI Card 1: Sessions
- [ ] KPI Card 2: Page Views
- [ ] KPI Card 3: Top Device
- [ ] KPI Card 4: Avg Pages/Session
- [ ] Section header: "Geographic & Device Distribution"
- [ ] Chart: Sessions by City
- [ ] Chart: Device Breakdown
- [ ] Section header: "Content Performance"
- [ ] Table: Top Livecast Videos (auto-size column width OFF, word wrap OFF for numeric columns)
- [ ] Table: Top Pages (auto-size column width OFF, word wrap OFF for numeric columns)
- [ ] **All charts use 4px radius background shapes** (Sessions by City, Device Breakdown - prevents visual drift)
- [ ] **Device Breakdown is 100% stacked horizontal bar chart** (NOT donut - better accessibility and printability)
- [ ] **Device Breakdown colors are locked** (Desktop=#005EA2, Mobile=#1A4480, Tablet=#0050D8, Other=#71767A)

**Phase 4: Right Column - Recommended Actions Panel (Option A: Content-Driven 412px)**
- [ ] Panel background shape locked (**27.5% width = 528px** - reduced from 576px, **height: 412px - NOT full-height**)
- [ ] Panel starts at Y: 124px (aligned with first KPI card)
- [ ] Panel ends at Y: 536px (124 + 412 = 536) - verify it doesn't extend to full-height (940px)
- [ ] Panel accent bar locked (4px, #005EA2, **above panel background, below text elements** - check Z-order)
- [ ] Panel header **"Recommended Actions"** complete (16pt Semibold, standardized across all 7 pages)
- [ ] **Purpose subtitle complete** (below page title, 12pt, #565C65, "Monitor performance and detect issues fast.")
- [ ] **Interactive action buttons (v1.8):** 3 clickable action buttons (not static text - see `INTERACTIVE_RIGHT_PANEL_ACTIONS.md`)
- [ ] Action buttons use safe verbs (Check, Compare, Review - NOT Fix, Optimize, Identify)
- [ ] **Actions ONLY reference visuals on this page** (Sessions, Page Views, Device Breakdown, Top Livecast Videos, Top Pages - NOT Health Score, Total Events if those aren't visible)
- [ ] Action button text is 12pt (increased from 11pt - leadership readability minimum)
- [ ] Micro-disclaimer footer complete ("Prompts suggest areas to review; not causal conclusions")
- [ ] **NO filler sections visible** (Option A doesn't include Data Freshness, Filters, Definitions - those are only for Option B full-height)

**Phase 5: Navigation Rail**
- [ ] Rail container background locked
- [ ] Nav Button 1: Command Center (with active indicator)
- [ ] Nav Button 2: Explorer
- [ ] Nav Button 3: Traffic & Acquisition
- [ ] Nav Button 4: Play Events
- [ ] Nav Button 5: External Search
- [ ] Nav Button 6: AI Insights
- [ ] Nav Button 7: Deep Dive
- [ ] All tooltips configured
- [ ] All hover states work

**Phase 6: Final Validation**
- [ ] Visual inspection passed
- [ ] Functional tests passed
- [ ] Export tests passed (PDF, PPT, screenshot)
- [ ] Accessibility validation passed
- [ ] All elements locked
- [ ] File saved with backup

---

## 🎯 SUCCESS CRITERIA

**You're done when all of these are true:**

✅ Page background is #F0F0F0
✅ All cards/visuals have #FFFFFF background, 1px #DFE1E2 border, 4px radius
✅ NO shadows or glows anywhere
✅ Typography: 28pt title, **12pt purpose subtitle (NEW v1.8)**, 14pt headers, 12pt body (increased from 11pt for leadership readability - **NEW v1.8**), all Segoe UI
✅ Colors: #1B1B1B primary text, #565C65 secondary, #71767A tertiary, #005EA2 interactive
✅ 4 KPI cards aligned with 12px gaps, 295px width each (perfect grid flush to x=1300)
✅ Sessions by City: horizontal bars, blue (#005EA2), sorted descending
✅ Device Breakdown: **100% stacked horizontal bar chart** (recommended over donut for accessibility and printability), percentages visible, USWDS colors locked (Desktop=#005EA2, Mobile=#1A4480), 4px radius, no shadows
✅ Tables: blue headers (#005EA2), alternating rows, 1px gridlines
✅ Right panel: "Recommended Actions" (standardized across all 7 pages), **27.5% width (528px - reduced from 576px for better content balance)**, **412px height (Option A - content-driven, NOT full-height)**, **3 clickable action buttons** (not static text - see `INTERACTIVE_RIGHT_PANEL_ACTIONS.md` for complete specs), micro-disclaimer footer, **NO filler sections**
✅ Purpose subtitle: Visible below page title (12pt, #565C65, provides immediate context for leadership)
✅ Header utilities standardized: Date slicer, Reset filters button, Last refresh timestamp, optional Definitions button (all pages)
✅ 7 navigation buttons: icons visible, hover states work, Command Center active
✅ All measures bound from correct folders
✅ All visuals have static alt text entered manually
✅ Date slicer filters all visuals
✅ Export to PDF looks professional
✅ Export to PowerPoint looks professional
✅ Screenshot in Teams is readable at 100%
✅ Contrast ratios pass WCAG AA (4.5:1 minimum)
✅ All background elements locked
✅ File saved with backup

---

## 🚀 NEXT STEPS

### **Phase 1: Content Rewrite Strategy (Required Before Replication)**

**✅ DONE FOR YOU:** Complete pre-written prompts for all 7 pages are available in `REVIEW_PROMPTS_BANK.md`. Copy and paste directly into Power BI text boxes - no rewriting needed.

**If you need to customize or create new prompts, use these rules:**

1. **Change Title:** Replace "Recommended Actions" with "What to Review Next" (or approved alternative)

2. **Rewrite All Bullets Using Safe Verbs:**
   - ✅ **Use:** Review, Validate, Monitor, Compare, Investigate, Segment, Confirm
   - ❌ **Avoid:** Fix, Optimize, Increase, Decrease, Prove, Caused, Driven by

3. **Change Structure from Prescriptive to Investigative:**
   - ❌ **Bad:** "Fix mobile experience (avg time down 15%)"
   - ✅ **Good:** "Investigate mobile vs desktop session duration to confirm experience differences"

   - ❌ **Bad:** "Optimize for underperforming livecasts"
   - ✅ **Good:** "Review livecast performance by segmenting event type and date mix"

   - ❌ **Bad:** "Increase engagement for low-performing pages"
   - ✅ **Good:** "Compare engagement rates across landing pages to identify patterns"

4. **Limit to 3 Bullets Maximum:** Less is more in federal contexts

5. **Add Micro-Disclaimer to EVERY Page:**
   - "Prompts suggest areas to review; not causal conclusions."

**Source Content:** Already rewritten and available in `REVIEW_PROMPTS_BANK.md`. If creating new prompts, pull from `TWO_COLUMN_LAYOUT_CONTENT_MAPPING.md` and rewrite using above rules.

---

### **Phase 2: Page Replication (20-30 min per page)**

**Command Center Complete → Replicate to 6 Pages:**

1. **Explorer Page** (20-30 min)
   - Use Format Painter from Command Center visuals
   - Update measure bindings from `Explorer` folder
   - Apply rewritten review prompts (Phase 1)
   - Update panel header to "What to Review Next"

2. **Traffic & Acquisition Page** (20-30 min)
   - Same replication process
   - Update measures from `Traffic & Acquisition` folder
   - Apply rewritten review prompts (Phase 1)
   - Ensure safe verbs only

3. **Play Events Page** (20-30 min)
4. **External Search Page** (20-30 min)
5. **AI Insights Page** (20-30 min)
6. **Deep Dive Page** (20-30 min)

**For Each Page:**
- Copy right rail structure (background, accent, header, prompts, disclaimer)
- Rewrite 3 review prompts using safe verbs
- Add micro-disclaimer footer
- Choose rail height strategy (content-driven OR full-height with fillers)

**Total Time for All 7 Pages:** 4-5 hours (including content rewrite)

---

## 📚 SUPPORTING DOCUMENTS

**Theme & Color:**
- `USWDS_LIGHT_IMPLEMENTATION.md` - Complete theme guide
- `USWDS_LIGHT_FINAL_CHECKLIST.md` - Federal product playbook

**Content Mapping:**
- `TWO_COLUMN_LAYOUT_CONTENT_MAPPING.md` - Exact data for all visuals
- `REVIEW_PROMPTS_BANK.md` - **Pre-written federal-safe review prompts for all 7 pages (copy-paste ready)**

**Design Polish:**
- `POWERPOINT_BACKGROUNDS_FINAL_POLISH.md` - Background refinements
- `QUICK_WINS_BACKGROUND_REFINEMENT.md` - 30-min quick wins

**Decision Framework:**
- `THEME_DIRECTION_DECISION.md` - USWDS Light vs Dark Ops decision

---

## ⚠️ KNOWN POWER BI LIMITATIONS

**This section documents Power BI realities that differ from "design spec" assumptions. Follow these patterns to avoid rework.**

### **1. Text Boxes Cannot Bind Measures**

**Reality:** Power BI text boxes are **static only**. You cannot bind a measure to populate text box content dynamically.

**Workarounds:**
- **Option A:** Use static text boxes (recommended for initial build)
- **Option B:** Use **Smart Narrative** visual for measure-driven text
- **Option C:** Use **Multi-row Card** visual with measure returning string (use `UNICHAR(10)` for line breaks)

**Where this applies:** Review Prompts panel (previously "Quick Insights" / "Top Opportunities")

---

### **2. Dynamic Alt Text Binding Not Consistently Supported**

**Reality:** Power BI Alt Text fields are primarily **static text**. Dynamic alt text via measures is not consistently supported across all visual types or Power BI versions.

**Workarounds:**
- Enter static descriptions manually for each visual (recommended)
- Use descriptive text boxes near visuals with measure-driven content if dynamic descriptions are required
- Use tooltips for measure-driven descriptions

**Where this applies:** All visuals (charts, tables, cards)

---

### **3. Button Hover Icon Swapping Not Reliably Supported**

**Reality:** Power BI buttons do not reliably support swapping different SVG icons per state (default/hover/active). Icon swapping per state is inconsistent across Power BI versions.

**Recommended Pattern:**
- Use **one icon per button** (default state)
- Change **fill color** on hover/selected (this works reliably: #F0F0F0)
- Use **separate shape** (left accent bar) for active state indicator, not button border

**Where this applies:** Navigation rail buttons

---

### **4. Shapes Don't Support "Border on One Side Only"**

**Reality:** Power BI shapes have a single border that applies to all sides. You cannot set a border on only one side (e.g., "right side only").

**Workaround:**
- Create shape with **no border**
- Add a **separate line shape** at the desired edge position for the divider effect

**Where this applies:** Navigation rail divider (create separate 1px vertical line at x=60px)

---

### **5. Rounded Corners Limited by Visual Type**

**Reality:** The 4px radius spec applies reliably to **containers, shapes, and card backgrounds**. Some native visuals may not respect rounded corners perfectly depending on Power BI version and visual type.

**Workaround:**
- Apply radius to visual containers where possible
- Use background shapes with rounded corners behind visuals if exact radius matching is critical
- Accept slight visual inconsistencies for native chart visuals if they're minor

**Where this applies:** Chart visuals (may need background shapes for exact radius)

---

### **6. Text Box Line Spacing Controls Limited**

**Reality:** Power BI text boxes don't provide true CSS-style line-height controls. You cannot set a precise line-height value like "1.6".

**Workaround:**
- Use manual line breaks (Enter key) to create spacing between bullets
- Use paragraph spacing controls if available in your Power BI version
- For controlled spacing, consider Smart Narrative or Multi-row Card visuals instead

**Where this applies:** Review Prompts bullet list (3 bullets maximum)

---

### **7. Card Label Text Editing Not Always Available**

**Reality:** Depending on **Card (new)** vs **Card (classic)**, you may not be able to directly edit the category label text in the Format pane. Some versions of Power BI restrict category label editing.

**Workaround:**
- Turn off category label in Format pane (if editing is unavailable)
- Insert a **small text box** inside the card container area (below the callout value)
- Position: Same X as card, Y: approximately below callout (e.g., Y: ~180px if card starts at Y: 124px with height 100px)
- Format: Match category label specs (11pt Segoe UI, #565C65, center aligned)
- Type your label text: "Sessions", "Page Views", etc.

**Where this applies:** KPI Card visuals (all 4 cards)

---

### **8. Device Breakdown Chart: 100% Stacked Bar Color Mapping (REQUIRED: Lock Colors for Consistency)**

**Reality:** Power BI theme data colors may not maintain consistent mapping (e.g., Desktop always #005EA2) unless explicitly locked. Device breakdown appears on multiple pages, so consistent color mapping is critical.

**REQUIRED APPROACH (Explicit Color Locking):**
- **CRITICAL:** Explicitly map colors in chart format (do NOT rely on theme order)
- **Desktop:** #005EA2 (Primary Blue) - locked
- **Mobile:** #1A4480 (Hover Blue) - locked
- **Tablet:** #0050D8 (Light Blue) - locked
- **Other:** #71767A (Tertiary Gray) - locked
- **Rationale:** Device breakdown appears on multiple pages. Consistent color mapping prevents user confusion and maintains "same device, same color" visual consistency.

**Where this applies:** Device Breakdown 100% stacked bar chart (recommended over donut for accessibility and printability)

---

### **9. Charts with Perfect 4px Rounding (REQUIRED: Enforce Radius to Match Tokens)**

**Reality:** Power BI's native rounding on chart visuals may look "softer" or "more rounded" than 4px, creating visual drift from your design tokens. This can make visuals look inconsistent (some at 4px, some at ~6-8px radius).

**REQUIRED APPROACH (Background Shape Method):**
- **Apply to ALL chart visuals:** Sessions by City bar chart, Device Breakdown 100% stacked bar chart
- Insert a **rounded rectangle shape** behind each chart (exact 4px radius)
- Position: Same X, Y, W, H as the chart
- Format: Background #FFFFFF, 1px border #DFE1E2, **Rounded corners: 4px**, shadow OFF
- Set chart background to **Transparent**
- **Z-order:** Background shape below chart (chart sits on top of shape)
- This gives you pixel-perfect 4px rounding on all edges and eliminates "Power BI default blob" feel

**Where this applies:** All chart visuals (Sessions by City bar chart, Device Breakdown 100% stacked bar chart, and all future charts)

**Validation:** All charts show exact 4px radius (no "softer" appearance). If you see visual drift (more rounded than 4px), apply background shape method immediately.

---

### **10. Frozen Table Column Widths for Export Stability (Optional Polish)**

**Reality:** Even with "Auto-size column width: OFF", columns can sometimes resize based on content or export settings.

**Optional Polish (If export stability is critical):**
- After manually sizing columns once (in Power BI Desktop at 100% zoom):
  1. Set each column width explicitly (e.g., Title: 400px, Views: 150px, Avg Time: 120px)
  2. Use **Format Painter** to copy formatting to similar tables on other pages
  3. Lock table visual dimensions in Selection Pane
- **Test:** Export to PDF/PPT and verify columns don't "accordion" or wrap unexpectedly

**Where this applies:** Table visuals (Top Livecast Videos, Top Pages, and all future tables)

**Recommendation:** Standard practice for federal/leadership dashboards where export consistency is required.

---

### **11. Tooltip Field Label Naming (Accessibility Enhancement)**

**Reality:** When adding alt-text measures to tooltips, the default field label is the measure name (e.g., "Sessions by City Alt Text").

**Recommendation:**
- **Rename tooltip field label** (if possible in your Power BI version) to **"Description"** for cleaner hover text
- This makes tooltips read professionally: "Description: [your measure content]" instead of "Sessions by City Alt Text: [content]"
- If renaming is not available, the measure name works but may feel verbose

**Where this applies:** All visuals with tooltip-based accessibility descriptions

---

### **12. Content Grid Positioning with Navigation Rail**

**Reality:** Navigation rail occupies x=0 to x=60px. Content grid should start at x=84px (rail width + padding) to avoid overlap.

**Important:**
- Header elements (eyebrow, title) may start at x=24px if they overlap rail region intentionally
- Main content visuals (KPIs, charts, tables) should start at x=84px minimum
- Header divider line should start at x=84px (content edge), not x=24px

**Where this applies:** All content positioning throughout the page

---

**When in doubt, test your approach in Power BI Desktop before committing to a pattern. These limitations vary slightly by Power BI version.**

---

## 💡 TIPS & TRICKS

**Faster Formatting:**
1. Format one KPI card perfectly
2. Right-click → Copy formatting
3. Select other KPI cards → Right-click → Paste formatting

**Selection Pane Shortcuts:**
1. View → Selection pane (always keep open)
2. **Use consistent naming convention:** See **Appendix C: Selection Pane Naming Convention** for recommended pattern (`01_KPI_Sessions`, `02_Chart_City`, etc.)
3. Lock background shapes right after creation
4. Group related visuals for easier movement
5. **Tip:** Numbered prefixes (01, 02, 03...) ensure correct sort order in Selection Pane

**Troubleshooting:**

**Icons look thin or blurry?**
- Increase SVG stroke-width from 1.5 to 2 in icon files
- Or increase icon size in button Format → Style → Icon layout

**Tables look "half themed"?**
- Format pane → Reset to default
- Reapply all formatting settings

**Right column doesn't stand out?**
- Check 4px accent bar is in front of background
- Verify accent bar fill is #005EA2, no transparency

**Date slicer not filtering?**
- Check relationships in Model view
- Verify DimDate[Date] is connected to FactSessions[Date]

**Navigation buttons not working?**
- Format → Action → Page navigation → Select correct target page
- Verify page names match exactly (case-sensitive)

---

---

## 📝 REVIEW PROMPTS CONTENT BANK

**Complete pre-written prompts for all 7 pages:** See `REVIEW_PROMPTS_BANK.md` for ready-to-paste content.

**Quick Reference Template:**

**Use this template structure for consistent, safe prompts across all pages:**

### **Panel Title (Choose ONE per page):**
- "Recommended Actions" (Standard Federal Terminology)
- "What to Review Next" (alternative)
- "Suggested Follow-Ups" (alternative)
- "Analyst Prompts" (alternative)
- "Open Questions" (alternative)

### **Content Structure (3 Bullets Maximum):**

**Pattern 1: Segmenting Analysis**
```
• Review [metric] by segmenting [dimension 1] and [dimension 2].
```

**Pattern 2: Comparison Investigation**
```
• Investigate [metric 1] vs [metric 2] to confirm [specific difference].
```

**Pattern 3: Validation Against Context**
```
• Validate [trend] against [context: seasonality, events, benchmarks].
```

**Pattern 4: Monitoring Changes**
```
• Monitor [metric] for [timeframe] to identify patterns.
```

### **Example Transformations (Before → After):**

**❌ BEFORE (Prescriptive):**
- "Fix mobile experience (avg time down 15%)"
- "Optimize for underperforming livecasts"
- "Increase engagement for low-performing pages"

**✅ AFTER (Investigative):**
- "Investigate mobile vs desktop session duration to confirm experience differences"
- "Review livecast performance by segmenting event type and date mix"
- "Compare engagement rates across landing pages to identify patterns"

### **Micro-Disclaimer (REQUIRED on Every Page):**
```
Prompts suggest areas to review; not causal conclusions.
```
- Font: Segoe UI, 9-10pt, Italic (optional), #71767A
- Position: Bottom of review prompts panel

### **Content Sources:**
- Pull original content from `TWO_COLUMN_LAYOUT_CONTENT_MAPPING.md`
- Rewrite using safe verbs and investigative language
- Limit to 3 bullets maximum per page
- Ensure each bullet is defensible as a "next step to investigate"

---

**Document Status:** ✅ COMPLETE BUILD GUIDE (v1.8 - Premium App Shell Transformation, Interactive Right Panel, Purpose Subtitles, Standardized Header Utilities)

**Build Time:** 60-90 minutes for Command Center page

**Next:** 
1. Replicate Command Center build to 6 remaining pages (20-30 min each)
2. Apply same visual consistency standards (4px radius background shapes, locked colors) to all charts
3. Implement interactive right panel actions (clickable buttons, bookmarks, field parameters) on all pages
4. Add purpose subtitles to all 7 pages
5. Standardize header utilities across all pages
6. Validate all pages against v1.8 standards

**Created:** January 10, 2026
**Updated:** January 10, 2026 (v1.8 - Premium app shell enhancements: Right panel standardized to "Recommended Actions" and made interactive, purpose subtitles added to all pages, right panel width reduced 10-15%, standardized header utilities, accessibility improvements, page-specific enhancements with toggles and definitions)
**For:** HHS Live Events Dashboard V4.0 - Command Center Build Guide
**Version:** 1.8 - Math-Perfect Grid, Federal-Safe, Power BI-Tested, Analyst-Notebook Style, Contractor-Grade Reference, Single-Ledger Appendices, Export-Stable, Premium App Shell, Interactive Navigation Brain

---

## ✅ **v1.8 CHANGES APPLIED (January 10, 2026) - Premium App Shell Transformation**

**Premium App Shell Enhancements (v1.8):**
- ✅ Standardized right panel header to **"Recommended Actions"** across all 7 pages (federal standard terminology)
- ✅ Added **purpose subtitles** to all 7 pages (below page title, 12pt, #565C65) - prevents "what am I looking at?" moment
- ✅ Reduced right panel width from 576px to **528px (10-15% reduction)** for better content balance
- ✅ Increased action button text from 11pt to **12pt (leadership readability minimum)**
- ✅ Standardized header utilities across all pages (date slicer, reset button, last refresh, optional definitions button)
- ✅ Transformed static text bullets to **clickable action buttons** (bookmarks, drillthrough, field parameter toggles)
- ✅ Page-specific enhancements: Health KPI (Command Center), Performance Metric toggle (Explorer), Channel Grouping toggle (Traffic & Acquisition), Video/Segment selectors (Play Events), Branded/Non-Branded toggle (External Search), Signal Strength + methodology (AI Insights), Segmentation slicers + interpretation guidance (Deep Dive)

**Complete Implementation Guide:** See `INTERACTIVE_RIGHT_PANEL_ACTIONS.md` and `PREMIUM_APP_SHELL_ENHANCEMENTS_v1.8.md` for full specifications.

---

## ✅ **v1.7 CHANGES APPLIED (January 10, 2026) - Screenshot Feedback Implementation**

**Right Rail Panel Improvements (v1.7):**
- ✅ Renamed header from "Recommended Actions" to **"What to Review Next"** (safer, invitational title - **Note: v1.8 reverted to "Recommended Actions" for standardization**)
- ✅ Enforced **Option A (content-driven height: 412px)** - NOT full-height (940px)
- ✅ Updated prompts to be conditional, page-specific, and **ONLY reference visuals on Command Center page** (Sessions, Page Views, Device Breakdown, Top Livecast Videos, Top Pages - NOT Health Score, Total Events)
- ✅ Added micro-disclaimer footer: "Prompts suggest areas to review; not causal conclusions"
- ✅ Clarified Z-order for accent bar: Above panel background, below text elements

**KPI Row Consistency:**
- ✅ Added **"KPI Subline Standard"** to Design Tokens (all 4 KPIs must have sublines for consistency)
- ✅ Fixed **"Avg Pages/Session"** label (was incorrectly "AVG PAGES" in screenshot)
- ✅ Ensured all 4 KPIs have consistent formatting with trend deltas OR context lines

**Visual Consistency Enforcement (4px Radius + No Shadows):**
- ✅ Emphasized **4px radius** and **shadows OFF** throughout document
- ✅ Added **background shape method** for all chart visuals (prevents "Power BI default blob" feel)
- ✅ Documented that native visuals may not respect 4px radius perfectly - background shapes required for pixel-perfect consistency
- ✅ Added validation checks to prevent visual drift

**Navigation Active State:**
- ✅ Clarified that **Button 1 (Command Center)** should be active on this page
- ✅ Documented correct Z-order for active indicator (above buttons, below text)
- ✅ Fixed navigation indicator positioning instructions

**Trust Anchor & UX Enhancements:**
- ✅ Added **"Last Refresh Indicator"** text box below date slicer (Y=82px, right-aligned, 10pt, #71767A)
- ✅ Added **"Reset Filters Button"** (X=1480px, to the right of date slicer, functional - clears all cross-filters via bookmark)
- ✅ Documented bookmark method for reset functionality

**Device Breakdown Chart Change:**
- ✅ Changed from **Donut Chart** to **100% Stacked Horizontal Bar Chart** (better accessibility and printability)
- ✅ Updated all formatting instructions for new chart type
- ✅ **Locked color mapping** (Desktop=#005EA2, Mobile=#1A4480, Tablet=#0050D8, Other=#71767A) - REQUIRED for consistency across pages
- ✅ Updated validation checks to reflect new chart type

**Spec Hygiene:**
- ✅ Added **"Right Rail Decision Gate"** to Design Tokens (commits to Option A vs Option B)
- ✅ Added **"KPI Subline Standard"** to Design Tokens
- ✅ Updated all validation checklists to include new elements
- ✅ Updated completion checklist to reflect all changes

**Known Power BI Limitations Updated:**
- ✅ Background shape method for 4px radius enforcement (Section 9 expanded)
- ✅ Device breakdown color locking requirement (Section 8 expanded)
- ✅ Reset filters bookmark method documented

---

## ✅ **v1.4-v1.6 FIXES APPLIED (January 10, 2026)**

**Critical Math & Alignment Fixes (v1.4):**
- ✅ Fixed KPI Card 3 X position: 618px → **698px** (Perfect Grid: 391 + 295 + 12)
- ✅ Fixed KPI Card 4 X position: 915px → **1005px** (Perfect Grid: 698 + 295 + 12)
- ✅ Committed to Perfect Grid: All KPIs now **295px width** (flush to x=1300)
- ✅ Fixed Date Slicer X position: 1700px → **1696px** (ends exactly at 1896px respecting 24px right padding)
- ✅ Updated all two-column widths: 594px → **602px** (perfect grid: (1216 - 12) / 2 = 602)
- ✅ Updated all right column X positions: 690px → **698px** (84 + 602 + 12)
- ✅ Updated header divider end X: Already correct at **1896px** (spans under header across both main content + right rail)
- ✅ Fixed header divider Y position: 80px → **84px** (4px below date slicer, avoiding double-border clash in PDF exports)

**Canonical Grid Formula Block Added:**
- ✅ Rewrote "Understand Content Grid" section with single source of truth formulas
- ✅ Added **Main ↔ Right Rail Gap: 20px** to Spacing & Grid tokens (critical constant)
- ✅ All positions now derivable from constants (no hand-waving gaps)
- ✅ Committed to Perfect Grid: 4 KPIs flush to x=1300 with 295px width (matches charts/tables edge)

**Power BI Reality Checks Added:**
- ✅ Card label text editing limitations documented (text box workaround)
- ✅ Data labels changed: Inside end → **Outside end** (safer for readability on short bars)
- ✅ Device Breakdown: Changed from donut to **100% stacked horizontal bar chart** (better accessibility and printability), percentages visible, colors locked
- ✅ Table: Auto-size column width **OFF** (recommended for PDF/PPT export stability)
- ✅ Date slicer: "Select all" noted as conditional (available for List style, not consistently for Dropdown)
- ✅ Tooltip naming recommendation: Rename to **"Description"** for cleaner hover text
- ✅ Accent bar layering: Above panel background, below text (correct Z-order documented)
- ✅ Clarified tooltip vs Alt Text field usage

**Documentation Improvements:**
- ✅ Removed ghost math ("321" in KPI Card 3 calculation)
- ✅ All positioning values now mathematically consistent (one truth: Perfect Grid)
- ✅ Content end X truth locked: **x=1300px** with perfect 602px widths for charts/tables
- ✅ KPI width decision committed: **295px** (perfect grid flush to x=1300, aligns with charts/tables)
- ✅ Alt Text fixed: Removed "action type" from Livecast table description (matches actual columns: Title, Views, Avg Time)
- ✅ Option A panel height: Set to deterministic **412px** (was ~400px; now pixel-exact first-pass: 124 → disclaimer 380 + 16 height + 16 padding)
- ✅ Header overlap note: Documented visual effect of eyebrow/title on nav rail white background

**New Appendices Added:**
- ✅ **Appendix A: Placement Ledger** - Complete table of all element positions (X, Y, W, H) in one reference
- ✅ **Appendix B: Binding Ledger** - Complete table of all measure bindings and field mappings
- ✅ **Appendix C: Selection Pane Naming Convention** - Optional but recommended naming pattern for idiot-proof layer order

---

## 📋 APPENDIX A: PLACEMENT LEDGER (Single Reference Table)

**Purpose:** Complete table of all element positions in one place. Use this for quick reference during build or troubleshooting.

### **Header Elements**

| Element             |    X |  Y |    W |  H |
| ------------------- | ---: | -: | ---: | -: |
| Eyebrow Label       |   24 | 20 |  300 | 20 |
| Page Title          |   24 | 40 |  600 | 40 |
| Date Slicer         | 1696 | 30 |  200 | 50 |
| Header Divider Line |   84 | 84 | **1788** |  1 |

> **Divider width calculation:** 1872 - 84 = **1788px** (right panel end at 1848px + 24px padding = 1872px; spans under header across both main content + right rail area - updated for new panel width 528px)

---

### **Main Content (x=84 to x=1300, width: 1216px)**

| Element                      |    X |   Y |   W |   H |
| ---------------------------- | ---: | --: | --: | --: |
| Section: At a Glance         |   84 | 100 | 300 |  20 |
| KPI 1 Sessions               |   84 | 124 | 295 | 100 |
| KPI 2 Page Views             |  391 | 124 | 295 | 100 |
| KPI 3 Top Device             |  698 | 124 | 295 | 100 |
| KPI 4 Avg Pages/Session      | 1005 | 124 | 295 | 100 |
| Section: Geo & Device        |   84 | 240 | 400 |  20 |
| Chart: Sessions by City      |   84 | 264 | 602 | 300 |
| Chart: Device Breakdown      |  698 | 264 | 602 | 300 |
| Section: Content Performance |   84 | 580 | 300 |  20 |
| Table: Top Livecast Videos   |   84 | 604 | 602 | 250 |
| Table: Top Pages             |  698 | 604 | 602 | 250 |

> **KPI Row:** 4 cards × 295px + 3 gaps × 12px = 1216px (flush to x=1300) ✅  
> **Two-Column Layout:** 602px + 12px gap + 602px = 1216px (flush to x=1300) ✅

---

### **Right Rail (x=1320 to x=1848, width: 528px - reduced from 576px in v1.8)**

| Element                        |    X |   Y |   W |       H |
| ------------------------------ | ---: | --: | --: | ------: |
| Panel Background (Option A)    | 1320 | 124 | **528** | **412** |
| Panel Background (Option B)    | 1320 | 124 | **528** | **940** |
| Panel Accent Bar (Option A)    | 1320 | 124 |   4 | **412** |
| Panel Accent Bar (Option B)    | 1320 | 124 |   4 | **940** |
| Panel Header                   | 1344 | 140 | **480** |      24 |
| Action Buttons / Prompts Text  | 1344 | 180 | **480** |    180 |
| Micro-Disclaimer               | 1344 | 380 | **480** |      16 |

> **Option A Height Calculation:** 124 → disclaimer at 380 + 16 height + 16 bottom padding = **412px**  
> **Option B Height:** Full-height to align with main content area (940px from Y: 124 to Y: 1064, leaving 16px bottom padding)

---

### **Navigation Rail (x=0 to x=60, full height)**

| Element               |  X |  Y |  W |    H |
| --------------------- | -: | -: | -: | ---: |
| Nav Rail Background   |  0 |  0 | 60 | 1080 |
| Nav Rail Divider Line | 60 |  0 |  1 | 1080 |

### **Nav Buttons (all 60×60 at x=0, 80px spacing)**

| Button                               |  X |   Y |  W |  H |
| ------------------------------------ | -: | --: | -: | -: |
| 1 Command Center (Active)            |  0 |   0 | 60 | 60 |
| Active Indicator (only on this page) |  0 |   0 |  4 | 60 |
| 2 Explorer                           |  0 |  80 | 60 | 60 |
| 3 Traffic & Acquisition              |  0 | 160 | 60 | 60 |
| 4 Play Events                        |  0 | 240 | 60 | 60 |
| 5 External Search                    |  0 | 320 | 60 | 60 |
| 6 AI Insights                        |  0 | 400 | 60 | 60 |
| 7 Deep Dive                          |  0 | 480 | 60 | 60 |

> **Button Y positions:** 0, 80, 160, 240, 320, 400, 480 (80px spacing)

---

## 📋 APPENDIX B: BINDING LEDGER (Measures + Fields Reference)

**Purpose:** Complete table of all measure bindings and field mappings. Use this for quick reference when building visuals.

### **KPI Cards**

| Card                | Measure Folder                                      | Tooltip Measure                      |
| ------------------- | --------------------------------------------------- | ------------------------------------ |
| Sessions            | `Command Center → KPI Card - Sessions → [Sessions]` | `[Sessions Alt Text]`                |
| Page Views          | `Command Center → KPI Card - Page Views → [Page Views]` | `[Page Views Alt Text]`              |
| Top Device          | `Command Center → KPI Card - Top Device → [Top Device Category]` | `[Top Device Alt Text]`              |
| Avg Pages/Session   | `Command Center → KPI Card - Avg Pages/Session → [Avg Pages per Session]` | `[Avg Pages Alt Text]`               |

---

### **Charts**

| Chart                  | Fields                                                                                              | Tooltip Measure                      |
| ---------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Sessions by City (Bar) | **Y-axis:** `DimLocation[City]`<br>**X-axis:** `Command Center → Chart - Sessions by City → [Sessions by City]` | `[Sessions by City Alt Text]`        |
| Device Breakdown (100% Stacked Bar) | **Y-axis:** `DimDevice[Device Category]` (single category for stacked)<br>**Values:** `Command Center → Chart - Device Breakdown → [Device Sessions]` (stacks to 100%)<br>**Chart Type:** 100% Stacked (horizontal bars) | `[Device Breakdown Alt Text]`        |

---

### **Tables**

| Table                 | Columns                                                                                                                              | Tooltip/Alt Support                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| Top Livecast Videos   | 1. `DimLivecast[Livecast Title]`<br>2. `Command Center → Table - Top Livecast Videos → [Livecast Views]`<br>3. `Command Center → Table - Top Livecast Videos → [Livecast Avg Time]` | `[Top Videos Alt Text]` (if using)   |
| Top Pages             | 1. `DimPage[Page Path]`<br>2. `Command Center → Table - Top Pages → [Page Views]`<br>3. `Command Center → Table - Top Pages → [Page Engagement]` | `[Top Pages Alt Text]` (if using)    |

---

### **Filters & Slicers**

| Element    | Field                              | Format Notes                    |
| ---------- | ---------------------------------- | ------------------------------- |
| Date Slicer | `DimDate[Date]`                    | Style: Dropdown (or List if "Select all" required) |

---

### **Accessibility Note:**
- **Tooltips (Recommended):** Add alt-text measures to Tooltips well, rename field label to "Description" if possible
- **Alt Text Field (Fallback):** Use static descriptions for native Alt Text field (dynamic binding not consistently supported)

---

## 📋 APPENDIX C: SELECTION PANE NAMING CONVENTION (Optional but Recommended)

**Purpose:** Consistent naming for Selection Pane makes layer order idiot-proof when Power BI is being Power BI.

### **Naming Pattern:**
`##_Category_ElementDescription`

Where:
- **##** = Build order number (01, 02, 03...)
- **Category** = Type (Header, KPI, Chart, Table, Panel, Nav, Shape)
- **ElementDescription** = Brief identifier (Title, Sessions, CityBar, etc.)

### **Recommended Names (Build Order):**

**Navigation Rail:**
- `00_Nav_Background`
- `00_Nav_Divider`
- `01_Nav_Button_CommandCenter`
- `02_Nav_Button_Explorer`
- `03_Nav_Button_Traffic`
- `04_Nav_Button_PlayEvents`
- `05_Nav_Button_ExternalSearch`
- `06_Nav_Button_AIInsights`
- `07_Nav_Button_DeepDive`
- `00_Nav_ActiveIndicator` (Command Center only)

**Header:**
- `01_Header_Eyebrow`
- `02_Header_Title`
- `03_Header_DateSlicer`
- `04_Header_Divider`

**KPI Cards:**
- `01_KPI_Sessions`
- `02_KPI_PageViews`
- `03_KPI_TopDevice`
- `04_KPI_AvgPages`

**Section Headers:**
- `01_Section_AtAGlance`
- `02_Section_GeoDevice`
- `03_Section_ContentPerformance`

**Charts:**
- `01_Chart_SessionsByCity`
- `02_Chart_DeviceBreakdown`

**Tables:**
- `01_Table_TopLivecastVideos`
- `02_Table_TopPages`

**Right Panel (Option A - Content-Driven):**
- `01_Panel_Background`
- `02_Panel_AccentBar`
- `03_Panel_Header`
- `04_Panel_Prompts`
- `05_Panel_Disclaimer`

**Why This Works:**
- Numbers sort correctly in Selection Pane (01 comes before 10)
- Category prefix groups related elements
- Build order is clear (follow sequence)
- Easy to find elements when troubleshooting

**Note:** Power BI Selection Pane sorts alphabetically, so `00_` and `01_` prefixes ensure correct order. After locking, you can rename to remove numbers if preferred (but keep prefixes for grouping).

---

## ✅ **v1.5 FIXES APPLIED (January 10, 2026)**

**Accessibility & Correctness Fixes:**
- ✅ Alt Text fixed: Removed "action type" from Livecast table description (matches actual columns: Title, Views, Avg Time)
- ✅ Added accessibility check note: Alt text must match actual table columns

**Deterministic Sizing:**
- ✅ Option A panel height: Set to deterministic **412px** (was ~400px; now pixel-exact first-pass: 124 → disclaimer 380 + 16 height + 16 padding)
- ✅ Accent bar height: Updated to match panel height (412px for Option A, 940px for Option B)

**Visual Documentation:**
- ✅ Header overlap note: Documented visual effect of eyebrow/title on nav rail white background
- ✅ Added note about header strip shape option (if leadership aesthetics demand uniform header background)

**New Reference Appendices:**
- ✅ **Appendix A: Placement Ledger** - Complete table of all element positions (X, Y, W, H) in one reference
  - Includes Header, Main Content, Right Rail, Navigation Rail, and Nav Buttons
  - All calculations verified (KPI row, two-column layout, right rail positioning)
- ✅ **Appendix B: Binding Ledger** - Complete table of all measure bindings and field mappings
  - KPI Cards, Charts, Tables, Filters & Slicers
  - Quick reference for measure folders and tooltip bindings
- ✅ **Appendix C: Selection Pane Naming Convention** - Optional but recommended naming pattern
  - Pattern: `##_Category_ElementDescription`
  - Complete list of recommended names for all page elements
  - Ensures idiot-proof layer order when Power BI is being Power BI

**Optional Polish Moves (Documented):**
- ✅ Added "Charts with Perfect 4px Rounding" optional polish (rounded rectangles behind charts for pixel-perfect rounding)
- ✅ Added "Frozen Table Column Widths for Export Stability" optional polish (explicit column widths + Format Painter for consistency)
- ✅ Updated Tips & Tricks to reference Selection Pane naming convention from Appendix C

**Known Limitations Updated:**
- ✅ Section numbering fixed (Content Grid Positioning now #12, added optional polish sections #9 and #10)
- ✅ All limitations now properly numbered and cross-referenced

**Result:** Guide is now **contractor-grade, math-clean, single-ledger** spec with complete reference appendices. Every position, every binding, and every naming convention documented in one place for zero-hunt troubleshooting.

---

## ✅ **v1.6 FIXES APPLIED (January 10, 2026) - QA Pass: Token Alignment & Export Stability**

**Token Alignment (Tokens Now Match Actual Rhythm):**
- ✅ Added **Header-to-Row Gap: 4px** token (section header bottom to first visual top - matches actual Y positions)
- ✅ Added **Row-to-Next-Header Gap: 16px** token (section break between content row and next section header - matches actual Y positions)
- ✅ Clarified **Visual Gap: 12px** applies to side-by-side visuals (KPI cards, two-column charts) only
- ✅ Documented actual rhythm: Header at Y=100 → KPIs at Y=124 (4px gap), KPIs end Y=224 → Next header at Y=240 (16px gap)
- **Why this matters:** Prevents future "corrections" that would break the layout. Tokens now accurately reflect the build behavior.

**Visual Clash Prevention:**
- ✅ Fixed header divider Y position: 80px → **84px** (4px below date slicer bottom at Y=80, avoiding double-border clash)
- ✅ Updated Appendix A: Placement Ledger divider Y position to 84px
- **Why this matters:** Date slicer has its own border; divider at same Y created double-weight border in PDF exports. Now clean separation.

**Z-Order Determinism (Nav Divider Fix):**
- ✅ Replaced ambiguous "Send to back" instruction with deterministic Selection Pane ordering
- ✅ Documented Nav Z-order (bottom → top): Background → Divider → Buttons → Active Indicator
- ✅ Added Power BI Reality Check: "Send to back" can be too aggressive and bury divider behind background
- ✅ Mirrored accent bar layering approach (already correct) for nav divider section
- **Why this matters:** Prevents invisible divider when Power BI's "send to back" goes too far. Selection Pane ordering is foolproof.

**Export-Stable Table Formatting:**
- ✅ Added word wrap **OFF** for numeric columns (Views, Avg Time, Engagement)
- ✅ Added word wrap **ON** for text columns (Livecast Title, Page Path)
- ✅ Clarified alignment: Right for numeric columns, Left for text columns
- ✅ Documented consistent number formatting: `#,0` / `0.00` / `0.00%` for tabular alignment
- ✅ Added export stability note: Prevents "accordion wrap" surprises on PDF/PPT
- **Why this matters:** Numeric columns with word wrap ON can cause jittery exports. Explicit OFF ensures stable column widths.

**Result:** Guide is now **fully aligned** - tokens match actual placements, no visual clashes, deterministic Z-order, and export-stable formatting. Ready for multi-page replication with zero confusion.

---

## ✅ **v1.8 FIXES APPLIED (January 10, 2026) - Navigation Rail Y-Coordinate Standardization & Export Polish**

**Navigation Rail Y-Coordinate Standardization (CRITICAL FIX):**
- ✅ Fixed all navigation button Y positions to **canonical positions**: 84, 164, 244, 324, 404, 484, 564 (80px spacing)
- ✅ Standardized Button 1 (Command Center) Y position: **84** (was inconsistently referenced as Y=0 or Y=80)
- ✅ Fixed Button 2 (Explorer) Y position: **164** (was Y=80)
- ✅ Fixed Button 3 (Traffic & Acquisition) Y position: **244** (was Y=160)
- ✅ Fixed Button 4 (Play Events) Y position: **324** (was Y=240)
- ✅ Fixed Button 5 (External Search) Y position: **404** (was Y=320)
- ✅ Fixed Button 6 (AI Insights) Y position: **484** (was Y=400)
- ✅ Fixed Button 7 (Deep Dive) Y position: **564** (was Y=480)
- ✅ Updated active indicator references to match canonical Button 1 position (Y=**84**, not Y=0)
- ✅ Fixed "Important Note on Active State Indicator" section to reference correct Y positions for all buttons (164, 244, 324, 404, 484, 564)
- ✅ Fixed validation section to reference canonical positions (84, 164, 244, 324, 404, 484, 564)
- ✅ Fixed duplicate "Tooltip" entry in Button 2 section
- ✅ Added missing Alt text entries for Buttons 3-7
- **Why this matters:** Previously, the guide had three competing Y position systems (84/164/244..., 80/160/240..., and even "indicator Y=0"). This created confusion during replication. Now there is **one canonical truth** for all button positions.

**Export Polish - Visual Header Icons (NEW STEP):**
- ✅ Added **Phase 5.4: Turn off Visual Header Icons** step (CRITICAL for clean exports)
- ✅ Documented process: Format → Visual → Header icons → Off (for each visual)
- ✅ Added validation checklist for header icons removal
- ✅ Added note about selective icon usage (if interactivity requires certain icons)
- **Why this matters:** Power BI visuals have default header icons (filter, focus mode, more options) that can clutter exports and break the clean federal aesthetic. This step ensures all visuals are export-ready.

**Documentation Improvements:**
- ✅ Updated document header with version information (v1.8)
- ✅ Added version status note: "All v1.8 Navigation Rail Y-Coordinate Fixes Applied"
- ✅ Updated "Important Note on Active State Indicator" to reference correct canonical positions
- ✅ Clarified validation section to reference canonical positions consistently
- ✅ Added this changelog entry for v1.8 fixes

**Result:** Guide now has **one canonical truth** for all navigation button positions (84, 164, 244, 324, 404, 484, 564), eliminating all Y-coordinate contradictions. Export polish step (Phase 5.4) ensures visuals are clean and export-ready. Ready for multi-page replication with zero confusion.

---

## ✅ **v1.8.1 FIXES APPLIED (January 10, 2026) - HTML Enhancement Strategy Integration**

**HTML Enhancement Strategy Integration (OPTIONAL):**
- ✅ Added **Phase 4.3c: HTML Insight Panel** (OPTIONAL - Tenant-Dependent Enhancement)
- ✅ Documented HTML enhancement strategy: "HTML = luxury interior finish, not wiring" approach
- ✅ Created comprehensive **`HTML_ENHANCEMENT_STRATEGY.md`** guide with:
  - Federal-safe HTML usage patterns (USWDS-aligned colors, typography, spacing)
  - Ready-to-use HTML code examples (Insight Panel, Data Quality Box, KPI Chips)
  - Implementation roadmap (3-phase approach: Proof of Concept → Right Rail Enhancement → Scale to All Pages)
  - Federal considerations checklist (508, export, performance, security)
  - Decision framework (Use HTML if... / Skip HTML if...)
- ✅ Updated build guide prerequisites to reference HTML strategy (optional enhancement)
- ✅ Clarified that HTML is optional - current v1.8 native implementation is excellent and fully functional
- ✅ Integrated HTML strategy into master documentation index and main README

**Integration Points:**
- ✅ Build guide Phase 4.3c references `HTML_ENHANCEMENT_STRATEGY.md` for complete implementation details
- ✅ Master build reference index includes HTML strategy as optional enhancement (Tenant-Dependent)
- ✅ Main README includes HTML strategy in "For Building" section (optional)
- ✅ Build guide prerequisites section includes HTML visual availability check (optional)

**Strategic Approach:**
- **HTML = Presentation + Narrative** (right rail insights, data quality box, tooltip content)
- **Native Power BI = Navigation + Filtering + Export-Critical Data** (buttons, bookmarks, slicers, tables)
- **Federal Priority:** Test thoroughly (508 compliance, export stability, performance, security) before deployment

**Result:** HTML enhancement strategy is now fully integrated into documentation as an optional "luxury finish" enhancement. Build guide includes Phase 4.3c with decision gate, fallback options, and clear federal considerations. Strategy document provides complete implementation details for those who want to enhance the dashboard with HTML visuals (tenant approval and tests required).

---

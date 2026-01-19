# 🎨 HHS Live Events Dashboard - Assets Folder

**Purpose:** Complete asset library for the HHS Live Events Performance Dashboard V4.0
**Design System:** Mission Control Aesthetic
**Last Updated:** January 9, 2026

---

## 📂 **FOLDER CONTENTS**

### **✨ New Mission Control Icons (28 files)**

Professional, technical icons designed specifically for the 7-page dashboard:

- **7 Navigation Icons** (base + hover = 14 files)
- **7 Utility Icons** (base + hover = 14 files)
- **Color Scheme:** HHS Blue (#005EA2) → Ocean Blue (#4A90E2) on hover
- **Format:** SVG (scalable vector graphics)
- **Size:** 24×24px standard

### **🏛️ HHS Brand Assets (10 files)**

Official HHS logos, seals, and branding elements:

- HHS Logo (multiple formats: SVG, PNG, WebP)
- Official HHS Seal (multiple variants)
- Federal header elements
- Accent lines and decorative elements

### **📦 Legacy Icons (16 files)**

Older generic-style icons (archived in `legacy/` subfolder):

- Basic functional icons (home, chart, search, etc.)
- Simple design style
- Kept for reference/backwards compatibility

---

## 🚀 **QUICK START**

### **For New Users:**

1. **Start Here:** Read `QUICK_START_ICONS.md` for 5-minute implementation guide
2. **Need Details?** See `ICON_CATALOG.md` for complete documentation
3. **Power BI Setup:** Follow button configuration steps in Quick Start

### **File Naming Convention:**

```
nav_[page]_[name].svg           - Navigation icons (base state)
nav_[page]_[name]_hover.svg     - Navigation icons (hover state)
util_[function].svg              - Utility icons (base state)
util_[function]_hover.svg        - Utility icons (hover state)
hhs_[asset].svg                  - HHS brand assets
legacy/icon_[name].svg           - Old icons (archived)
```

---

## 📋 **NAVIGATION ICONS**

### **7 Dashboard Pages (14 icon files)**

| Page | Icon Description | Base File | Hover File |
|------|------------------|-----------|------------|
| **Command Center** | 4-quadrant dashboard grid with health indicator | `nav_01_command_center.svg` | `nav_01_command_center_hover.svg` |
| **Explorer** | Radar scanner with sweep arm and data points | `nav_02_explorer.svg` | `nav_02_explorer_hover.svg` |
| **Traffic & Acquisition** | Network flow from sources to hub to destination | `nav_03_traffic_acquisition.svg` | `nav_03_traffic_acquisition_hover.svg` |
| **Play Events** | Broadcast waves with play button and live dot | `nav_04_play_events.svg` | `nav_04_play_events_hover.svg` |
| **External Search** | Globe with magnifying glass and external link | `nav_05_external_search.svg` | `nav_05_external_search_hover.svg` |
| **AI Insights** | Neural network with pathways and insight spark | `nav_06_ai_insights.svg` | `nav_06_ai_insights_hover.svg` |
| **Deep Dive** | Layered data with focus beam and magnifier | `nav_07_deep_dive.svg` | `nav_07_deep_dive_hover.svg` |

---

## 🔧 **UTILITY ICONS**

### **7 Dashboard Functions (14 icon files)**

| Function | Icon Description | Base File | Hover File | Use Case |
|----------|------------------|-----------|------------|----------|
| **Clear Filters** | Eraser clearing filter funnel with X mark | `util_clear_filters.svg` | `util_clear_filters_hover.svg` | Reset all crossfiltering |
| **Refresh** | Circular sync arrows with center indicator | `util_refresh.svg` | `util_refresh_hover.svg` | Reload data |
| **Filter** | Funnel with data particles being filtered | `util_filter.svg` | `util_filter_hover.svg` | Apply filters |
| **Export** | Document with download arrow and output tray | `util_export.svg` | `util_export_hover.svg` | Export data |
| **Info** | Circle with info symbol (i) | `util_info.svg` | `util_info_hover.svg` | Help/tooltips |
| **Settings** | Technical gear with 8 teeth | `util_settings.svg` | `util_settings_hover.svg` | Configuration |
| **Calendar** | Calendar with date grid and highlighted day | `util_calendar.svg` | `util_calendar_hover.svg` | Date picker |

---

## 🎨 **DESIGN SPECIFICATIONS**

### **Color Palette**

```
HHS Blue (Base):       #005EA2
Ocean Blue (Hover):    #4A90E2
Success Green:         #4A7729
Warning Amber:         #E5A000
Critical Red:          #D83933
Live Indicator:        #E63C34
```

### **Technical Specs**

```
Format:          SVG (Scalable Vector Graphics)
Dimensions:      24×24px (viewBox="0 0 24 24")
Stroke Weight:   1.5-2px (base), 1.8-2.5px (hover)
File Size:       1-3KB per icon
Background:      Transparent
Color Space:     sRGB
```

### **Hover State Effects**

- Brighter blue color (#4A90E2)
- Slightly thicker strokes (+0.3-0.5px)
- Subtle glow rings (0.3 opacity)
- Larger key elements (+0.2-0.3 units)

---

## 💻 **POWER BI USAGE**

### **Button Configuration (3 Steps)**

```
1. Insert → Button → Blank
2. Format → Style → Custom → Icon → Custom
   - Default: Select base .svg file
   - On Hover: Select _hover.svg file
3. Action → Page navigation or custom action
```

### **Recommended Sizes**

```
Navigation Icons:  32×32px or 40×40px (nav rail)
Utility Icons:     24×24px or 28×28px (header/toolbar)
Small Icons:       16×16px or 20×20px (inline)
```

### **Placement Guidelines**

```
Navigation Rail (Left):
- Vertical stack
- 60px width (collapsed) or 200px (expanded)
- Dark background (#0D1B2A)
- 8px spacing between icons

Utility Bar (Top/Header):
- Horizontal row
- Right-aligned
- Light or dark background
- 12px spacing between icons
```

---

## 📚 **DOCUMENTATION FILES**

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.md** | Overview and quick reference | You are here! |
| **QUICK_START_ICONS.md** | 5-minute implementation guide | First time setup |
| **ICON_CATALOG.md** | Complete technical documentation | Detailed reference |

---

## 🗂️ **FILE STRUCTURE**

```
assets/
│
├── 📁 Navigation Icons (14 files)
│   ├── nav_01_command_center.svg
│   ├── nav_01_command_center_hover.svg
│   ├── nav_02_explorer.svg
│   ├── nav_02_explorer_hover.svg
│   ├── nav_03_traffic_acquisition.svg
│   ├── nav_03_traffic_acquisition_hover.svg
│   ├── nav_04_play_events.svg
│   ├── nav_04_play_events_hover.svg
│   ├── nav_05_external_search.svg
│   ├── nav_05_external_search_hover.svg
│   ├── nav_06_ai_insights.svg
│   ├── nav_06_ai_insights_hover.svg
│   ├── nav_07_deep_dive.svg
│   └── nav_07_deep_dive_hover.svg
│
├── 🔧 Utility Icons (14 files)
│   ├── util_clear_filters.svg
│   ├── util_clear_filters_hover.svg
│   ├── util_refresh.svg
│   ├── util_refresh_hover.svg
│   ├── util_filter.svg
│   ├── util_filter_hover.svg
│   ├── util_export.svg
│   ├── util_export_hover.svg
│   ├── util_info.svg
│   ├── util_info_hover.svg
│   ├── util_settings.svg
│   ├── util_settings_hover.svg
│   ├── util_calendar.svg
│   └── util_calendar_hover.svg
│
├── 🏛️ HHS Brand Assets (10 files)
│   ├── hhs_logo.svg
│   ├── hhs-logo-2025.png
│   ├── hhs-seal.svg
│   ├── hhs-seal-alt.svg
│   ├── hhs-seal-official.svg
│   ├── hhs-website-logo.svg
│   ├── logo-white-bg.svg
│   ├── trans_logo.webp
│   ├── hhs_federal_header.svg
│   └── hhs_accent_line.svg
│
├── 📦 Legacy Icons (16 files in legacy/ subfolder)
│   └── legacy/icon_*.svg
│
├── 📄 Documentation
│   ├── README.md (this file)
│   ├── QUICK_START_ICONS.md
│   └── ICON_CATALOG.md
│
└── 📊 Other Assets
    └── Make_A_Clone_of_This_Live_Events_Performance_Dashboard.pdf
```

---

## ✨ **HIGHLIGHTS**

### **What's New (Jan 2026)**

✅ **14 Navigation Icons** - Custom mission control design for 7 pages
✅ **14 Utility Icons** - Professional dashboard controls with hover states
✅ **Clear Filters Icon** - Eraser design for crossfilter reset
✅ **Complete Documentation** - 3 guide documents for easy implementation
✅ **Organized Structure** - Legacy icons archived, new icons ready to use
✅ **Mission Control Aesthetic** - Technical precision, confident design

### **Why These Icons Are Better**

| Before | After |
|--------|-------|
| Generic emoji (◉ ▶️ 🔍) | Custom mission control icons |
| Single state only | Base + hover states |
| Limited functions | Complete utility set |
| No clear filters | Professional eraser icon |
| Mixed styles | Consistent design system |

---

## 🎯 **COMMON USE CASES**

### **Navigation Setup**

```
Add navigation buttons to left rail:
1. Command Center button → Page: Command Center
2. Explorer button → Page: Explorer
3. Traffic button → Page: Traffic & Acquisition
... (repeat for all 7 pages)
```

### **Utility Bar Setup**

```
Add utility buttons to header:
1. Clear Filters → Action: Reset all filters
2. Refresh → Action: Refresh data
3. Calendar → Action: Show date slicer
4. Export → Action: Export data
5. Settings → Action: Open settings panel
```

### **Tooltip Integration**

```
Use util_info.svg for tooltips:
- Place next to metric cards
- Hover shows explanation
- Maintains clean design
```

---

## 🆘 **NEED HELP?**

### **Quick Troubleshooting**

❓ **Icon not showing?**
- Check file path is correct
- Verify SVG opens in browser
- Ensure button icon is turned ON

❓ **Hover not working?**
- Confirm style is "Custom"
- Check hover image is selected
- Test in Desktop mode

❓ **Colors look wrong?**
- Should be #005EA2 (base) and #4A90E2 (hover)
- Open SVG in text editor to verify

### **Resources**

- **Quick Start:** `QUICK_START_ICONS.md`
- **Complete Guide:** `ICON_CATALOG.md`
- **Master Spec:** `00_Documentation/MASTER_SPECIFICATION.md`
- **Design System:** Master Spec Section 10

---

## 📊 **STATISTICS**

```
Total Assets:        54 files
New Icons:           28 files (14 base + 14 hover)
Navigation Icons:    14 files (7 pages × 2 states)
Utility Icons:       14 files (7 functions × 2 states)
Brand Assets:        10 files
Legacy Icons:        16 files (archived)
Documentation:       3 files
Total Size:          ~350KB (highly optimized)
```

---

## 🚀 **NEXT STEPS**

1. ✅ **Review this README** - You're doing it!
2. 📖 **Read Quick Start** - 5 minutes to understand basics
3. 💻 **Open Power BI** - Start adding buttons
4. 🎨 **Import Icons** - Use nav_* and util_* files
5. 🎉 **Enjoy!** - Professional dashboard with custom icons

---

**Created:** January 9, 2026
**Version:** 1.0
**Status:** ✅ Complete and Production-Ready

**Questions?** See `ICON_CATALOG.md` or `QUICK_START_ICONS.md`

---

*These icons were custom-designed for the HHS Live Events Performance Dashboard V4.0 following the Mission Control aesthetic: "NASA mission control meets modern fintech dashboard."*

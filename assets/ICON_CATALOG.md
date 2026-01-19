# 🎨 HHS Live Events Dashboard - Icon Catalog

**Design System:** Mission Control Aesthetic
**Created:** January 2026
**Color Palette:** HHS Blue (#005EA2) → Ocean Blue (#4A90E2) on hover

---

## 📋 **ICON INVENTORY**

### **🧭 Navigation Icons (7 Dashboard Pages)**

All navigation icons have base and hover states:

| Icon | File Name (Base) | File Name (Hover) | Purpose | Design Concept |
|------|------------------|-------------------|---------|----------------|
| **Command Center** | `nav_01_command_center.svg` | `nav_01_command_center_hover.svg` | Main dashboard | 4-quadrant grid with health indicator |
| **Explorer** | `nav_02_explorer.svg` | `nav_02_explorer_hover.svg` | Ad-hoc analysis | Radar/scanner with sweep arm |
| **Traffic & Acquisition** | `nav_03_traffic_acquisition.svg` | `nav_03_traffic_acquisition_hover.svg` | Traffic sources | Network flow diagram |
| **Play Events** | `nav_04_play_events.svg` | `nav_04_play_events_hover.svg` | Video/livecast | Broadcast waves + play button |
| **External Search** | `nav_05_external_search.svg` | `nav_05_external_search_hover.svg` | GSC data | Globe + magnifier + external link |
| **AI Insights** | `nav_06_ai_insights.svg` | `nav_06_ai_insights_hover.svg` | AI analysis | Neural network pathways |
| **Deep Dive** | `nav_07_deep_dive.svg` | `nav_07_deep_dive_hover.svg` | Drillthrough detail | Layered data with focus beam |

---

### **🔧 Utility Icons (Dashboard Functions)**

All utility icons have base and hover states:

| Icon | File Name (Base) | File Name (Hover) | Purpose |
|------|------------------|-------------------|---------|
| **Clear Filters** | `util_clear_filters.svg` | `util_clear_filters_hover.svg` | Reset all crossfiltering |
| **Refresh** | `util_refresh.svg` | `util_refresh_hover.svg` | Refresh data |
| **Filter** | `util_filter.svg` | `util_filter_hover.svg` | Apply filters |
| **Export** | `util_export.svg` | `util_export_hover.svg` | Export data |
| **Info** | `util_info.svg` | `util_info_hover.svg` | Help/information |
| **Settings** | `util_settings.svg` | `util_settings_hover.svg` | Configuration |
| **Calendar** | `util_calendar.svg` | `util_calendar_hover.svg` | Date picker |

---

### **🏛️ Brand Assets (HHS Official)**

| Asset | File Name | Purpose | Notes |
|-------|-----------|---------|-------|
| **HHS Logo** | `hhs_logo.svg` | Primary logo | Official HHS branding |
| **HHS Logo 2025** | `hhs-logo-2025.png` | Logo (PNG) | Raster version |
| **HHS Seal** | `hhs-seal.svg` | Official seal | Government seal |
| **HHS Seal Official** | `hhs-seal-official.svg` | Official seal variant | Alternative |
| **HHS Seal Alt** | `hhs-seal-alt.svg` | Seal alternate | Different styling |
| **HHS Website Logo** | `hhs-website-logo.svg` | Web version | Website-optimized |
| **Logo White BG** | `logo-white-bg.svg` | White background | For dark themes |
| **Transparent Logo** | `trans_logo.webp` | Transparent | WebP format |
| **Federal Header** | `hhs_federal_header.svg` | Header element | Official header |
| **Accent Line** | `hhs_accent_line.svg` | Decorative | Visual accent |

---

### **📦 Legacy Icons (Older Generic Style)**

These icons use a simpler design style. Consider replacing with mission control versions:

| Icon | File Name | Status | Notes |
|------|-----------|--------|-------|
| Home | `icon_home.svg` | ⚠️ Generic | Replace with nav_01_command_center |
| Chart | `icon_chart.svg` | ⚠️ Generic | Can use for generic chart references |
| Search | `icon_search.svg` | ⚠️ Generic | Replace with nav_05_external_search |
| Clear Filters | `icon_clear_filters.svg` | ⚠️ Replaced | Use util_clear_filters instead |
| Channels | `icon_channels.svg` | ✅ Keep | Good for multi-channel analysis |
| Date Filter | `icon_date_filter.svg` | ⚠️ Replaced | Use util_calendar instead |
| Dictionary | `icon_dictionary.svg` | ✅ Keep | Good for metric dictionary |
| Download | `icon_download.svg` | ⚠️ Replaced | Use util_export instead |
| Export | `icon_export.svg` | ⚠️ Replaced | Use util_export instead |
| Filter | `icon_filter.svg` | ⚠️ Replaced | Use util_filter instead |
| Info | `icon_info.svg` | ⚠️ Replaced | Use util_info instead |
| Refresh | `icon_refresh.svg` | ⚠️ Replaced | Use util_refresh instead |
| Release Detail | `icon_release_detail.svg` | ✅ Keep | Specific use case |
| Releases | `icon_releases.svg` | ✅ Keep | Specific use case |
| Settings | `icon_settings.svg` | ⚠️ Replaced | Use util_settings instead |
| Table | `icon_table.svg` | ✅ Keep | Good for table views |

---

## 🎨 **DESIGN SPECIFICATIONS**

### **Color Palette**

```css
/* Base State (Primary HHS Blue) */
Base Color: #005EA2
Stroke Width: 1.5 - 2px
Opacity: 100%

/* Hover State (Ocean Blue) */
Hover Color: #4A90E2
Stroke Width: 1.8 - 2.5px (slightly thicker)
Opacity: 100%
Glow Effect: 0.3 opacity outer rings

/* Accent Colors (for special indicators) */
Success: #4A7729 (Green)
Warning: #E5A000 (Amber)
Critical: #D83933 (Red)
Live Indicator: #E63C34 (Bright Red with pulse)
```

### **Icon Dimensions**

```
Standard Size: 24×24px
ViewBox: 0 0 24 24
Format: SVG (scalable)
Background: Transparent
```

### **Design Principles**

1. **Mission Control Aesthetic**
   - Clean geometric shapes
   - Technical precision
   - Subtle depth with layering
   - Confident lines (no rounded/bubbly)

2. **Hover States**
   - Brighter color (#4A90E2)
   - Slightly thicker strokes (+0.3-0.5px)
   - Subtle glow effects (0.3 opacity outer rings)
   - Larger key elements (+0.2-0.3 units)

3. **Consistency**
   - All icons use same base color (#005EA2)
   - All hover states use same hover color (#4A90E2)
   - Similar stroke weights across set
   - Unified visual language

4. **Technical Quality**
   - Clean SVG paths (no embedded images)
   - Optimized for small sizes (24px standard)
   - Readable at various scales
   - Printer-friendly (solid colors)

---

## 💻 **POWER BI IMPLEMENTATION**

### **How to Use in Power BI**

#### **Method 1: Direct SVG Import (Recommended)**

```
1. Insert → Image → Browse
2. Select .svg file
3. Power BI renders as vector (scalable)
4. No quality loss at any zoom level
```

#### **Method 2: Image Control for Hover States**

For buttons with hover effects:

```
1. Insert → Button
2. Type: Blank
3. Format → Style: Custom
4. Icon → Custom
   - Default: Select base SVG (e.g., nav_01_command_center.svg)
   - On Hover: Select hover SVG (e.g., nav_01_command_center_hover.svg)
5. Action: Navigate to page or custom action
```

#### **Method 3: Bookmarks for Interactive States**

```
1. Create two bookmarks per page:
   - Page_Normal (base icon visible)
   - Page_Hover (hover icon visible)
2. Assign bookmarks to button states
3. More complex but allows custom animations
```

### **Navigation Implementation Example**

```
Command Center Page:
├─ Button: "Command Center"
│  ├─ Default Image: nav_01_command_center.svg
│  ├─ Hover Image: nav_01_command_center_hover.svg
│  ├─ Action: Navigate to "Command Center" page
│  └─ Position: Top-left nav rail (60px width)
│
Explorer Page:
├─ Button: "Explorer"
│  ├─ Default Image: nav_02_explorer.svg
│  ├─ Hover Image: nav_02_explorer_hover.svg
│  ├─ Action: Navigate to "Explorer" page
│  └─ Position: Below Command Center
```

---

## 🎯 **NAMING CONVENTIONS**

### **File Naming Structure**

```
[category]_[number]_[name].svg
[category]_[number]_[name]_hover.svg

Categories:
- nav_     = Navigation icons (7 pages)
- util_    = Utility/function icons
- icon_    = Legacy generic icons (old style)
- hhs_     = Official HHS brand assets

Examples:
✅ nav_01_command_center.svg
✅ nav_01_command_center_hover.svg
✅ util_clear_filters.svg
✅ util_clear_filters_hover.svg
```

### **Folder Organization**

Current structure (flat):
```
assets/
├── nav_01_command_center.svg
├── nav_01_command_center_hover.svg
├── ... (all icons)
├── hhs_logo.svg
└── ICON_CATALOG.md (this file)
```

Recommended structure (organized):
```
assets/
├── icons/
│   ├── navigation/
│   │   ├── nav_01_command_center.svg
│   │   ├── nav_01_command_center_hover.svg
│   │   └── ... (all 7 pages × 2 states)
│   ├── utilities/
│   │   ├── util_clear_filters.svg
│   │   ├── util_clear_filters_hover.svg
│   │   └── ... (all utility icons)
│   └── legacy/
│       └── ... (old icon_*.svg files)
├── brand/
│   ├── hhs_logo.svg
│   └── ... (all HHS brand assets)
└── ICON_CATALOG.md
```

---

## ✅ **USAGE CHECKLIST**

Before implementing icons in Power BI:

- [ ] All navigation icons (7 pages × 2 states = 14 files) created
- [ ] All utility icons with hover states created
- [ ] Icons tested in Power BI Desktop
- [ ] Hover states work correctly on buttons
- [ ] Colors match Master Specification (#005EA2, #4A90E2)
- [ ] Icons are readable at 24px size
- [ ] SVG files optimized (no embedded images)
- [ ] Consistent naming convention used
- [ ] Legacy icons archived or replaced
- [ ] Documentation updated (this file)

---

## 🔄 **VERSION HISTORY**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 9, 2026 | Initial mission control icon set created |
|  |  | - 7 navigation icons with hover states |
|  |  | - 7 utility icons with hover states |
|  |  | - Clear filters/eraser icon added |
|  |  | - Catalog documentation created |

---

## 📝 **NOTES**

### **Icon Design Philosophy**

These icons follow the **Mission Control aesthetic** from the Master Specification:
- "NASA mission control meets modern fintech dashboard"
- "Confident authority with warmth"
- "Data is serious, interface is inviting"

### **Why Two Files Per Icon?**

Power BI buttons support separate images for:
1. **Default state** - User sees this normally
2. **Hover state** - User sees this when hovering

This creates subtle micro-interactions that enhance UX without complex code.

### **Color Rationale**

- **#005EA2 (HHS Blue)** - Official USWDS color, government-standard
- **#4A90E2 (Ocean Blue)** - Lighter, more vibrant for interactive states
- Contrast ratio meets WCAG AA standards (4.5:1 minimum)

### **Performance Considerations**

- SVG files are small (< 5KB each)
- Total icon library: ~200KB (28 icons × 2 states × 4KB avg)
- Minimal impact on .pbix file size
- Fast rendering in Power BI Service

---

## 🆘 **TROUBLESHOOTING**

### **Icon not appearing in Power BI**
- Verify file path is correct
- Check SVG file isn't corrupted (open in browser)
- Ensure viewBox attribute exists: `viewBox="0 0 24 24"`

### **Hover state not working**
- Confirm button is set to "Custom" style
- Verify separate hover image is selected
- Test in Power BI Desktop (not preview mode)

### **Colors look wrong**
- Check fill/stroke colors in SVG
- Ensure no embedded styles overriding colors
- Verify HEX codes: #005EA2 (base), #4A90E2 (hover)

### **Icon looks blurry**
- SVG should never be blurry (vector format)
- If blurry, may be rasterized PNG instead
- Re-export as proper SVG from source

---

## 🔗 **RELATED RESOURCES**

- **Master Specification:** `00_Documentation/MASTER_SPECIFICATION.md`
- **Design System:** Master Spec Section 10 (Visual Design System)
- **Color Palette:** `HHS_Theme_USWDS_Aligned.json`
- **Background Images:** `00_Documentation/05_Design_Assets/BACKGROUND_IMAGES_GUIDE.md`

---

**Last Updated:** January 9, 2026
**Status:** ✅ Complete Icon Set Ready for Implementation

**Questions?** See Master Specification or review SVG files in assets folder.

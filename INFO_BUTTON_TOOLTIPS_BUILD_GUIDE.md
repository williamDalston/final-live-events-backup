# Info Button Tooltips - Complete Build Guide

**Date:** 2026-01-12
**Status:** ✅ **READY TO BUILD**

---

## 🎯 OVERVIEW

This guide provides step-by-step instructions to create 7 tooltip pages (one per dashboard page) that appear when users hover over the info button (i).

---

## 📐 TOOLTIP PAGE SPECIFICATIONS

### Canvas Settings (All 7 Tooltips):

| Setting | Value |
|---------|-------|
| Page Type | Tooltip |
| Canvas Width | 320 pixels |
| Canvas Height | 200 pixels |
| Background | #FFFFFF (white) |
| Border | 1px solid #DFE1E2 |
| Padding | 16px all sides |

---

## 🔨 HOW TO CREATE TOOLTIPS

### Step 1: Create Tooltip Page

1. **Add new page** in Power BI Desktop
2. **Right-click page tab** → Page Information
3. **Enable "Allow use as tooltip"** ✅
4. **Set Canvas size:**
   - Type: Tooltip
   - Width: 320 pixels
   - Height: 200 pixels
5. **Rename page** to match pattern: "[Page Name] Info"
   - Example: "Command Center Info"

### Step 2: Format Canvas Background

1. **Canvas Settings** → Canvas background
2. **Color:** #FFFFFF (white)
3. **Transparency:** 0%

### Step 3: Add Text Box with Content

1. **Insert** → Text box
2. **Position:** X: 16, Y: 16
3. **Size:** Width: 288px, Height: 168px
4. **Paste content** (see content sections below)
5. **Format text:**
   - Title: 16pt, Segoe UI Semibold, #1B1B1B
   - Description: 11pt, Segoe UI, #565C65
   - Bullet headers: 11pt, Segoe UI Semibold, #1B1B1B
   - Bullet text: 11pt, Segoe UI, #565C65

---

## 📝 TOOLTIP CONTENT (Copy-Paste Ready)

### Tooltip 1: Command Center Info

**Page Name:** Command Center Info

**Text Box Content:**
```
Command Center
Monitor performance and detect issues fast.

Key Features:
• Top-level KPIs showing sessions, users, engagement, and play rate
• Geographic distribution map and device breakdown charts
• Most popular live event content ranked by views and engagement
```

**Formatting:**
- Line 1: "Command Center" - 16pt Bold, #1B1B1B
- Line 2: "Monitor performance..." - 11pt Regular, #565C65
- Line 3: (blank line)
- Line 4: "Key Features:" - 11pt Bold, #1B1B1B
- Lines 5-7: Bullet points - 11pt Regular, #565C65

---

### Tooltip 2: Explorer Info

**Page Name:** Explorer Info

**Text Box Content:**
```
Explorer
Discover patterns and drill into performance details.

Key Features:
• Page-by-page performance matrix with views, users, and engagement
• Traffic source breakdown showing organic, referral, and email channels
• Most viewed pages ranked by traffic volume (Top 10)
```

**Formatting:** Same as above

---

### Tooltip 3: Traffic & Acquisition Info

**Page Name:** Traffic & Acquisition Info

**Text Box Content:**
```
Traffic & Acquisition
Understand how audiences find and arrive at live events.

Key Features:
• Traffic trends by channel (organic, referral, email, direct)
• Top campaigns ranked by sessions and user volume
• Conversion funnel showing event engagement progression
```

**Formatting:** Same as above

---

### Tooltip 4: Play Events Info

**Page Name:** Play Events Info

**Text Box Content:**
```
Play Events
Track video engagement and playback performance.

Key Features:
• Play events timeline showing video engagement trends over time
• Average watch time per video ranked by total engagement minutes
• Completion rate distribution showing viewer retention patterns
```

**Formatting:** Same as above

---

### Tooltip 5: External Search Info

**Page Name:** External Search Info

**Text Box Content:**
```
External Search
Monitor search visibility and click-through performance.

Key Features:
• Clicks and impressions trends from Google Search Console
• Top queries with impressions, CTR, and average position metrics
• CTR by position scatter chart analyzing search ranking performance
```

**Formatting:** Same as above

---

### Tooltip 6: AI Insights Info

**Page Name:** AI Insights Info

**Text Box Content:**
```
AI Insights
Surface anomalies and forecast trends using intelligent analysis.

Key Features:
• Anomaly detection timeline identifying unusual traffic patterns
• 30-day traffic forecast with confidence intervals
• Key influencers analysis showing what drives metric changes
```

**Formatting:** Same as above

---

### Tooltip 7: Deep Dive Info

**Page Name:** Deep Dive Info

**Text Box Content:**
```
Deep Dive
Advanced segmentation and cohort analysis for detailed insights.

Key Features:
• Decomposition tree breaking down sessions by multiple dimensions
• Cohort retention analysis tracking user behavior over time
• Correlation explorer showing relationships between metrics
```

**Formatting:** Same as above

---

## 🎨 TEXT FORMATTING REFERENCE

### Typography Hierarchy:

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Page Title | Segoe UI | 16pt | Semibold | #1B1B1B |
| Description | Segoe UI | 11pt | Regular | #565C65 |
| "Key Features:" | Segoe UI | 11pt | Semibold | #1B1B1B |
| Bullet Points | Segoe UI | 11pt | Regular | #565C65 |

### Spacing:
- **Between title and description:** 4px
- **Between description and "Key Features:":** 8px
- **Between bullet points:** 6px
- **Line height:** 1.3 (130%)

---

## 🔘 INFO BUTTON SETUP

### Create Info Button (on each dashboard page):

1. **Insert** → Shapes → Oval
2. **Position:** X: 1612px, Y: 30px
3. **Size:** Width: 50px, Height: 50px
4. **Format Shape:**
   - Fill: None (transparent)
   - Border: Solid line
   - Border color: #005EA2 (USWDS Blue Primary)
   - Border width: 1px

5. **Add Text:**
   - Insert text box inside circle
   - Text: "i"
   - Font: Segoe UI
   - Size: 14pt
   - Color: #005EA2
   - Alignment: Center (horizontal and vertical)

6. **Assign Tooltip:**
   - Select the shape
   - Format → Tooltips
   - Type: **Report page**
   - Page: Select corresponding "[Page Name] Info"

---

## 📋 BUILD CHECKLIST

### For Each Dashboard Page:

#### Command Center:
- ⏭️ Create tooltip page "Command Center Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

#### Explorer:
- ⏭️ Create tooltip page "Explorer Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

#### Traffic & Acquisition:
- ⏭️ Create tooltip page "Traffic & Acquisition Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

#### Play Events:
- ⏭️ Create tooltip page "Play Events Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

#### External Search:
- ⏭️ Create tooltip page "External Search Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

#### AI Insights:
- ⏭️ Create tooltip page "AI Insights Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

#### Deep Dive:
- ⏭️ Create tooltip page "Deep Dive Info"
- ⏭️ Set canvas size (320×200px)
- ⏭️ Add text box with formatted content
- ⏭️ Create info button shape (1612, 30)
- ⏭️ Assign tooltip to button
- ⏭️ Test hover interaction

---

## 🖼️ VISUAL MOCKUP

### Tooltip Appearance:

```
┌────────────────────────────────────────────┐
│  Command Center                            │
│  Monitor performance and detect issues     │
│  fast.                                     │
│                                            │
│  Key Features:                             │
│  • Top-level KPIs showing sessions,        │
│    users, engagement, and play rate        │
│  • Geographic distribution map and         │
│    device breakdown charts                 │
│  • Most popular live event content         │
│    ranked by views and engagement          │
└────────────────────────────────────────────┘
   ↑
   Appears when hovering over (i) button
```

---

## 🎯 INTERACTION FLOW

1. **User hovers** over info button (i) at top right
2. **Tooltip appears** next to cursor (320×200px)
3. **User reads** page description and key features
4. **User moves mouse away** → tooltip disappears
5. **Non-disruptive** - no page navigation, no clicking required

---

## ⚙️ ALTERNATIVE: DYNAMIC TOOLTIP (ADVANCED)

### If You Want ONE Tooltip for All Pages:

Instead of 7 separate tooltips, create a single dynamic tooltip using DAX:

**Create Calculated Table:**
```dax
PageInfo =
DATATABLE(
    "PageName", STRING,
    "Title", STRING,
    "Description", STRING,
    "Feature1", STRING,
    "Feature2", STRING,
    "Feature3", STRING,
    {
        {"Command Center", "Command Center", "Monitor performance and detect issues fast.",
         "Top-level KPIs showing sessions, users, engagement, and play rate",
         "Geographic distribution map and device breakdown charts",
         "Most popular live event content ranked by views and engagement"},

        {"Explorer", "Explorer", "Discover patterns and drill into performance details.",
         "Page-by-page performance matrix with views, users, and engagement",
         "Traffic source breakdown showing organic, referral, and email channels",
         "Most viewed pages ranked by traffic volume (Top 10)"},

        {"Traffic & Acquisition", "Traffic & Acquisition", "Understand how audiences find and arrive at live events.",
         "Traffic trends by channel (organic, referral, email, direct)",
         "Top campaigns ranked by sessions and user volume",
         "Conversion funnel showing event engagement progression"},

        {"Play Events", "Play Events", "Track video engagement and playback performance.",
         "Play events timeline showing video engagement trends over time",
         "Average watch time per video ranked by total engagement minutes",
         "Completion rate distribution showing viewer retention patterns"},

        {"External Search", "External Search", "Monitor search visibility and click-through performance.",
         "Clicks and impressions trends from Google Search Console",
         "Top queries with impressions, CTR, and average position metrics",
         "CTR by position scatter chart analyzing search ranking performance"},

        {"AI Insights", "AI Insights", "Surface anomalies and forecast trends using intelligent analysis.",
         "Anomaly detection timeline identifying unusual traffic patterns",
         "30-day traffic forecast with confidence intervals",
         "Key influencers analysis showing what drives metric changes"},

        {"Deep Dive", "Deep Dive", "Advanced segmentation and cohort analysis for detailed insights.",
         "Decomposition tree breaking down sessions by multiple dimensions",
         "Cohort retention analysis tracking user behavior over time",
         "Correlation explorer showing relationships between metrics"}
    }
)
```

**Create Measure to Get Current Page:**
```dax
Current Page Info =
VAR CurrentPage = SELECTEDVALUE(PageInfo[PageName])
RETURN
IF(
    ISBLANK(CurrentPage),
    "Hover over (i) for page information",
    CurrentPage
)
```

**Note:** This approach requires page-level filtering logic. The simple approach (7 separate tooltips) is recommended for easier maintenance.

---

## 🔍 TESTING CHECKLIST

### Verify Each Tooltip:

- ✅ **Hover interaction works** (tooltip appears)
- ✅ **Tooltip size correct** (320×200px)
- ✅ **Content displays fully** (no truncation)
- ✅ **Text formatting correct** (fonts, sizes, colors)
- ✅ **Alignment proper** (left-aligned text, proper spacing)
- ✅ **Tooltip disappears** when mouse moves away
- ✅ **No performance lag** (tooltip appears instantly)
- ✅ **Accessible** (keyboard navigation works with Tab key)

---

## 📚 RELATED DOCUMENTATION

- **Layout Guide:** [LAYOUT_OPTIMIZATION_COMPLETE.md](../../LAYOUT_OPTIMIZATION_COMPLETE.md)
- **Recommended Actions:** [RECOMMENDED_ACTIONS_PANEL_GUIDE.md](RECOMMENDED_ACTIONS_PANEL_GUIDE.md)
- **USWDS Colors:** [VISUAL_SETTINGS_REFERENCE.md](VISUAL_SETTINGS_REFERENCE.md)

---

## ✅ COMPLETION CRITERIA

**Tooltips are complete when:**

1. ✅ 7 tooltip pages created (one per dashboard page)
2. ✅ All tooltips sized correctly (320×200px)
3. ✅ All content formatted with proper typography
4. ✅ Info buttons created on all 7 dashboard pages
5. ✅ Tooltips assigned to corresponding buttons
6. ✅ All hover interactions tested and working
7. ✅ Tooltips accessible via keyboard navigation

---

**READY TO BUILD** ✅

**Estimated Time:** 30-45 minutes (all 7 tooltips)
**Difficulty:** Easy (copy-paste content, basic formatting)
**Benefit:** Professional help system for end users

**Last Updated:** 2026-01-12

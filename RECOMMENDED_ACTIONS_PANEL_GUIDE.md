# Recommended Actions Panel - Implementation Guide

**Date:** 2026-01-12
**Status:** ✅ **ONE MEASURE WORKS ON ALL PAGES**

---

## 🎯 QUICK ANSWER

**YES - Use the same `[Recommended Actions HTML (Dynamic)]` measure on every page.**

The measure is **context-aware** and automatically shows different recommendations based on:
1. The current page filter context
2. Date range selections
3. Which signals are triggered by the data

You do **NOT** need separate measures per page.

---

## 📊 HOW IT WORKS

### The Measure: `Recommended Actions HTML (Dynamic)`

**Location:** Measures_Livecast table, lines 1124-1214

**What It Does:**
1. **Checks 4 signal detection measures** to see if any conditions are met:
   - `[Signal - Sessions MoM Drop?]` - Sessions dropped >10% vs. prior month
   - `[Signal - Mobile Share Elevated?]` - Mobile traffic >60% of sessions
   - `[Signal - Geo Concentrated?]` - Top city has >40% of sessions
   - `[Signal - Play Rate Opportunity?]` - Play rate <30%

2. **Filters the Action Catalog table** to only rows where signal = 1 (triggered)

3. **Generates HTML cards** for each active signal with:
   - Priority-based color coding (HIGH = red, MEDIUM = yellow, INFO = blue)
   - Icon (📉, 📱, 🌍, ▶️)
   - Title and description
   - Suggested action

4. **Shows empty state** if no signals are triggered

---

## 🔍 THE 4 SIGNALS EXPLAINED

### Signal 1: Sessions MoM Drop (📉 HIGH)
**Trigger:** Sessions decreased >10% compared to previous month

**Action Catalog Entry:**
- **Title:** "Investigate Drop in Viewership"
- **Prompt:** "Check traffic sources and email campaign performance."
- **Priority:** HIGH (red border)

**Example HTML Output:**
```html
📉 REVIEW
Investigate Drop in Viewership
Signal observed: Sessions down 15% vs prior month.
Suggested check: Check traffic sources and email campaign performance.
```

---

### Signal 2: Mobile Share Elevated (📱 MEDIUM)
**Trigger:** Mobile sessions >60% of total sessions

**Action Catalog Entry:**
- **Title:** "Optimize for Mobile Viewers"
- **Prompt:** "Validate player controls and layout on small screens."
- **Priority:** MEDIUM (yellow border)

**Example HTML Output:**
```html
📱 REVIEW
Optimize for Mobile Viewers
Signal observed: Mobile share at 67%.
Suggested check: Validate player controls and layout on small screens.
```

---

### Signal 3: Regional Interest Detected (🌍 INFO)
**Trigger:** Top city accounts for >40% of sessions

**Action Catalog Entry:**
- **Title:** "Regional Interest Detected"
- **Prompt:** "Consider targeting specific content for this region."
- **Priority:** INFO (blue border)

**Example HTML Output:**
```html
🌍 REVIEW
Regional Interest Detected
Signal observed: Top city share at 45%.
Suggested check: Consider targeting specific content for this region.
```

---

### Signal 4: Play Rate Opportunity (▶️ MEDIUM → HIGH if triggered)
**Trigger:** Play rate <30% (play events / sessions)

**Action Catalog Entry:**
- **Title:** "Improve Play Rate"
- **Prompt:** "Ensure video player is above the fold and auto-play is configured correctly."
- **Priority:** MEDIUM (or HIGH if triggered - line 1141)

**Example HTML Output:**
```html
▶️ REVIEW
Improve Play Rate
Signal observed: Play rate at 22%.
Suggested check: Ensure video player is above the fold and auto-play is configured correctly.
```

---

## 🎨 VISUAL IMPLEMENTATION

### How to Add to Any Page:

1. **Insert HTML Content visual** from Visualizations pane
2. **Add field:** Drag `[Recommended Actions HTML (Dynamic)]` to Values field
3. **Position:** Place in right panel area (typically 528px wide)
4. **No filters needed** - measure respects page context automatically

### Recommended Placement:
```
┌──────────────────────────────────────────────────┐
│  PAGE HEADER                                     │
├────────────────────────┬─────────────────────────┤
│                        │ Recommended Actions     │
│  Main Content Area     │ ┌─────────────────────┐ │
│                        │ │ 📉 REVIEW           │ │
│  (Charts/Tables)       │ │ Investigate Drop... │ │
│                        │ │                     │ │
│                        │ ├─────────────────────┤ │
│                        │ │ 📱 REVIEW           │ │
│                        │ │ Optimize Mobile...  │ │
│                        │ └─────────────────────┘ │
└────────────────────────┴─────────────────────────┘
```

---

## ✅ WHY ONE MEASURE WORKS FOR ALL PAGES

### Context-Aware Design:

The measure uses **filter context** from:
- **Page-level filters:** If Command Center filters to specific dates, signals check those dates
- **Date slicer:** Respects user-selected date ranges
- **Cross-page filters:** If you filter by device/geography, signals adjust accordingly

### Examples by Page:

**Command Center:**
- Shows all 4 signals if triggered (high-level overview)
- User sees: MoM drop, Mobile share, Geo concentration, Play rate

**Explorer:**
- Same measure, but might show different signals based on filtered subset
- If user drills into specific pages, Play Rate signal uses only those pages

**Traffic & Acquisition:**
- Signals still work because they use global measures ([Sessions], [Device Sessions], etc.)
- MoM Drop and Mobile Share particularly relevant here

**Play Events:**
- Play Rate signal is most relevant
- Other signals still show if triggered (provides broader context)

**External Search:**
- Signals still work (uses session-level metrics)
- Geo concentration might be particularly interesting for search traffic patterns

**AI Insights:**
- Same measure used to show what anomalies the AI should investigate
- All signals relevant for anomaly detection context

**Deep Dive:**
- Signals help guide which dimensions to decompose
- Shows what's worth investigating in detail

---

## 🚫 WHAT YOU DON'T NEED

### ❌ DON'T Create:
- Separate measures per page
- Page-specific signal logic
- Custom HTML per page
- Hardcoded page names in DAX

### ❌ DON'T Add:
- Page filters to the HTML visual
- Bookmarks to show/hide different versions
- Slicers to control which signals appear

---

## ✅ WHAT YOU DO NEED

### ✅ DO Ensure:
1. **Action Catalog table exists** ✅ (already created)
2. **All 4 signal measures exist** ✅ (already created)
3. **Supporting measures exist:**
   - `[Sessions - MoM %]` ✅
   - `[Device Sessions]` ✅
   - `[Sessions_City]` ✅
   - `[Play Events]` ✅
   - `[Mobile Share %]` ✅
   - `[Top City Share %]` ✅
   - `[Play Rate %]` ✅

### ✅ DO Consider:
- **Adding more signals** in the future (edit Action Catalog table)
- **Adjusting thresholds** (e.g., change MoM drop from -10% to -15%)
- **Customizing priority levels** (e.g., make Play Rate always HIGH)

---

## 🔧 HOW TO CUSTOMIZE (OPTIONAL)

### Add a New Signal:

**Step 1:** Add row to Action Catalog table (lines 63-68):
```dax
{5, "CTR_LOW", "MEDIUM", "🔍", "Improve Click-Through Rate", "Review page titles and meta descriptions for search visibility."}
```

**Step 2:** Create signal detection measure:
```dax
measure 'Signal - CTR Low?' =
    VAR AvgCTR = AVERAGE('gsc-queries'[CTR])
    RETURN
    IF(
        NOT(ISBLANK(AvgCTR)) && AvgCTR < 0.03,
        1,
        0
    )
```

**Step 3:** Add to SWITCH statements in HTML measure (lines 1131-1151):
```dax
"CTR_LOW",   [Signal - CTR Low?],
```

**Step 4:** Add signal text:
```dax
"CTR_LOW", "Signal observed: Avg CTR at " & FORMAT([Search CTR], "0.0%") & ".",
```

### Adjust Signal Threshold:

Edit the signal detection measure. Example - Change MoM threshold from -10% to -15%:

**Before (line 1036):**
```dax
IF(NOT(ISBLANK(MoMPct)) && MoMPct < -0.10, 1, 0)
```

**After:**
```dax
IF(NOT(ISBLANK(MoMPct)) && MoMPct < -0.15, 1, 0)
```

---

## 📋 IMPLEMENTATION CHECKLIST

### For Each Page:

- ⏭️ **Command Center:** Insert HTML visual, add measure
- ⏭️ **Explorer:** Insert HTML visual, add measure
- ⏭️ **Traffic & Acquisition:** Insert HTML visual, add measure
- ⏭️ **Play Events:** Insert HTML visual, add measure
- ⏭️ **External Search:** Insert HTML visual, add measure
- ⏭️ **AI Insights:** Insert HTML visual, add measure
- ⏭️ **Deep Dive:** Insert HTML visual, add measure

### Testing:

- ✅ **Test with different date ranges:** Verify signals trigger correctly
- ✅ **Test with filters:** Check if signals adjust to filtered context
- ✅ **Test empty state:** Confirm "No review flags" message appears when all signals = 0
- ✅ **Test multiple signals:** Verify cards stack correctly when 2+ signals trigger

---

## 🎨 STYLING REFERENCE

### Color Coding (from measure lines 1184-1187):

| Priority | Border Color | Background Color | Use Case |
|----------|-------------|------------------|----------|
| HIGH | #D83933 (red) | #FFF1F0 (light red) | Critical issues (MoM drop, low play rate when triggered) |
| MEDIUM | #FFBE2E (yellow) | #FFF8E6 (light yellow) | Optimization opportunities (mobile share, play rate) |
| INFO | #005EA2 (blue) | #E7F2E8 (light green) | Insights/patterns (geo concentration) |
| Default | #71767A (gray) | #F0F0F0 (light gray) | Fallback |

### Typography (from measure lines 1164-1203):

- **Header:** 14px, Segoe UI Semibold, #1B1B1B
- **"REVIEW" label:** 11px, Segoe UI Bold, Priority color, uppercase, 0.3px letter-spacing
- **Card title:** 12px, Segoe UI Semibold, #1B1B1B
- **Signal text:** 11px, Segoe UI, #565C65 (gray)
- **Prompt label:** 11px, Segoe UI Semibold, #3D4551 (dark gray)

---

## 📊 EXAMPLE OUTPUTS

### Scenario 1: No Signals Triggered
```html
Areas to Review
┌─────────────────────────────────────────────┐
│ No review flags for the selected period    │
│ Adjust date range or filters to explore    │
│ patterns.                                   │
└─────────────────────────────────────────────┘
```

### Scenario 2: Single Signal (MoM Drop)
```html
Areas to Review
┌─────────────────────────────────────────────┐
│ 📉 REVIEW                                   │
│ Investigate Drop in Viewership             │
│ Signal observed: Sessions down 15% vs      │
│ prior month.                                │
│ Suggested check: Check traffic sources and │
│ email campaign performance.                 │
└─────────────────────────────────────────────┘
```

### Scenario 3: Multiple Signals
```html
Areas to Review
┌─────────────────────────────────────────────┐
│ 📉 REVIEW (HIGH)                            │
│ Investigate Drop in Viewership             │
│ ...                                         │
├─────────────────────────────────────────────┤
│ 📱 REVIEW (MEDIUM)                          │
│ Optimize for Mobile Viewers                │
│ ...                                         │
├─────────────────────────────────────────────┤
│ ▶️ REVIEW (MEDIUM)                          │
│ Improve Play Rate                           │
│ ...                                         │
└─────────────────────────────────────────────┘
```

---

## ⚠️ KNOWN LIMITATIONS

1. **HTML Content visual required:** Standard Card visual won't render HTML
2. **No click interactions:** HTML is display-only (no drill-through or actions)
3. **Limited to 4 signals:** Can add more, but measure needs updating
4. **Static thresholds:** Signal triggers are hardcoded (not user-adjustable)
5. **No signal history:** Shows current state only (no trend of signals over time)

---

## 🚀 FUTURE ENHANCEMENTS (OPTIONAL)

### Phase 2 Ideas:
- Add "Dismiss" functionality (requires Write-back table)
- Add severity scoring (combine multiple signals into risk score)
- Add historical signal tracking (log when signals trigger)
- Add email alerts (Power Automate integration)

### Phase 3 Ideas:
- AI-generated recommendations (GPT integration)
- Predictive signals (forecast issues before they happen)
- Automated remediation (auto-adjust campaigns)

---

## 📚 RELATED DOCUMENTATION

- **Action Catalog Table:** [Action Catalog.tmdl](../../HHS Live Events Performance Dashboard.SemanticModel/definition/tables/Action Catalog.tmdl)
- **Signal Measures:** Measures_Livecast.tmdl lines 1032-1091
- **HTML Measure:** Measures_Livecast.tmdl lines 1124-1214

---

## ✅ FINAL ANSWER

**Can you use the same measure on every page?**
**YES - Absolutely! ✅**

The `[Recommended Actions HTML (Dynamic)]` measure is designed to work universally across all pages. It automatically:
- Adjusts to page filter context
- Respects date range selections
- Shows only relevant triggered signals
- Displays empty state when no issues detected

**Implementation:** Simply insert one HTML Content visual per page, add the measure, and you're done. No page-specific customization needed.

---

**GUIDE COMPLETE** ✅

**Last Updated:** 2026-01-12
**Measure Location:** Measures_Livecast.tmdl, lines 1124-1214
**Status:** Production-ready, works on all pages
**Customization Required:** None (optional enhancements available)

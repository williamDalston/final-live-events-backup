# 🎯 Federal Design Tokens - Quick Reference Checklist

**Purpose:** Quick copy-paste reference while implementing USWDS Light theme  
**Source:** Complete specifications in `USWDS_LIGHT_IMPLEMENTATION.md`  
**Use:** Keep this open while formatting in Power BI Desktop

---

## 🔧 DESIGN TOKENS (Lock These First)

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
Good:             #00A91C
Bad:              #D83933
Warning:          #FFBE2E
```

### **Shape:**
```
Radius:           4px (everywhere, no exceptions)
Shadow:           OFF (everywhere)
Glow:             OFF
Border Weight:    1px
```

### **Spacing:**
```
Outer Page Padding: 24px
Between Sections:   16px
Inside Card:        12-16px (pick one, stay consistent)
KPI Card Gaps:      12px
Section Header:     8-12px above card
```

### **Typography:**
```
Page Title:       24-28pt, Semibold, #1B1B1B
Section Header:   14pt, Semibold, #1B1B1B
Card Label:       11pt, Regular, #565C65
KPI Value:        28-32pt, Regular, #1B1B1B
Table Body:       11-12pt, Regular, #1B1B1B
Helper Text:      10-11pt, Regular, #71767A
Eyebrow:          11pt, Regular, #565C65
```

---

## ✅ IMPLEMENTATION CHECKLIST

### **Page Shell:**
- [ ] Canvas background: #F0F0F0
- [ ] Wallpaper: #F0F0F0 (or 100% transparent)
- [ ] No background images
- [ ] Header left-aligned
- [ ] Eyebrow label: "HHS LIVE EVENTS" (11pt, #565C65)
- [ ] Page title: 24-28pt Semibold, #1B1B1B
- [ ] Subtle divider: 1px #DFE1E2 under header

### **KPI Cards:**
- [ ] Background: #FFFFFF
- [ ] Border: 1px #DFE1E2
- [ ] Radius: 4px
- [ ] Shadow: OFF
- [ ] Label: 11pt, #565C65
- [ ] Value: 28-32pt, #1B1B1B
- [ ] Delta: 11pt, #71767A (only color if directional with arrow)
- [ ] Display units: Consistent (K/M)

### **Charts:**
- [ ] White card background
- [ ] Border: 1px #DFE1E2
- [ ] Radius: 4px
- [ ] Shadow: OFF
- [ ] Gridlines: Very light #DFE1E2 or OFF
- [ ] Axis labels: #565C65
- [ ] Legend: Top or bottom (consistent)
- [ ] No double border around plot area

### **Tables:**
- [ ] Header background: #005EA2
- [ ] Header text: #FFFFFF, 11pt Semibold
- [ ] Body text: #1B1B1B, 11pt Regular
- [ ] Alternate rows: #F0F0F0
- [ ] Gridlines: 1px #DFE1E2
- [ ] Row padding: 6 (if tight at 4)
- [ ] No heavy borders + heavy gridlines together

### **Section Headers:**
- [ ] 14pt Semibold, #1B1B1B
- [ ] Left aligned
- [ ] 8-12px above card group
- [ ] Optional: 3px left accent in #005EA2 (sparingly)

### **Navigation Rail:**
- [ ] Background: #FFFFFF
- [ ] Border: 1px #DFE1E2
- [ ] Radius: 4px (or consistent if full-height)
- [ ] Default icon: #005EA2
- [ ] Hover icon: #1A4480
- [ ] Selected icon: #162E51
- [ ] Selected indicator: 3-4px left bar #005EA2
- [ ] Tooltips on all icons
- [ ] Focus state visible (2px outline if needed)

### **Recommended Actions Panel:**
- [ ] Background: #FFFFFF
- [ ] Border: 1px #DFE1E2
- [ ] Left accent: 3px #005EA2
- [ ] Title: "Recommended Actions" 14-16pt Semibold
- [ ] 2-5 bullets maximum
- [ ] Each bullet: One sentence, action verb first, measurable

### **Alignment (Critical):**
- [ ] All left edges aligned to same x
- [ ] Consistent card heights within rows
- [ ] Consistent gutter spacing
- [ ] Consistent title offsets
- [ ] Gridlines enabled (View → Gridlines)
- [ ] Snap to grid enabled
- [ ] Elements locked in Selection Pane

### **No "Double Frames":**
- [ ] One container = one border
- [ ] No inner frames unless table header band
- [ ] No inset panels (use text labels above instead)
- [ ] Subtle header bands: #F9F9F9 (optional), no border

### **Export-Proofing:**
- [ ] Export to PDF - looks professional
- [ ] Export to PPT - readable
- [ ] Screenshot at 100% - readable in Teams
- [ ] No transparency-heavy overlays
- [ ] No background images (compress weirdly)

---

## 🎯 FINAL "100%" GATE CHECKLIST

**If all these are true, you're done:**

✅ Every card: 4px radius, 1px #DFE1E2 border  
✅ No shadows or inner glows anywhere  
✅ Page titles: Left-aligned, consistent size  
✅ Section headers: Exist and guide the eye  
✅ Tables: Readable at 100% on Teams  
✅ Nav: Clear selected state + tooltips  
✅ Actions panel: 2-5 crisp bullets  
✅ No double frames / inset panels (unless necessary)  
✅ All left edges: Aligned to same x  
✅ Card heights: Consistent within rows  
✅ Gutter spacing: Consistent  
✅ Title offsets: Consistent  
✅ Export PDF/PPT: Professional  
✅ Screenshot 100%: Readable in Teams  

---

## 📋 ORDER OF OPERATIONS

1. **Set radius/border/shadow rules everywhere**
2. **Remove double frames and inset containers**
3. **Normalize header/title alignment and sizes**
4. **Make nav states + tooltips perfect**
5. **Tune tables for readability**
6. **Add section headers across pages**
7. **Export tests and tiny adjustments**

---

**Quick Copy-Paste:** Keep this open while formatting for instant token reference! 🚀

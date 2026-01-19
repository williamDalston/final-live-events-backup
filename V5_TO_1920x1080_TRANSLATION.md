# V5 Mockup → 1920×1080 Power BI Translation Guide

**Source Canvas:** 1280 × 720 px (V5 Mockup)
**Target Canvas:** 1920 × 1080 px (Power BI)
**Scale Factor:** 1.5× (1920÷1280 = 1080÷720 = 1.5)

**Formula:** `Target = Source × 1.5`

---

## Quick Reference: Scale Factor Application

| V5 Value | × 1.5 | 1920×1080 Value |
|----------|-------|-----------------|
| 40 px | × 1.5 | 60 px |
| 56 px | × 1.5 | 84 px |
| 64 px | × 1.5 | 96 px |
| 100 px | × 1.5 | 150 px |
| 197 px | × 1.5 | 296 px (round to 295) |
| 267 px | × 1.5 | 400 px |
| 444 px | × 1.5 | 666 px |
| 897 px | × 1.5 | 1346 px |
| 1176 px | × 1.5 | 1764 px |

---

## MANUAL SHAPES TO CREATE

These are shapes you must manually create in Power BI to match the mockup design.

---

### 1. PAGE BACKGROUND
**Type:** Canvas setting (not a shape)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| Color | #F0F0F0 | #F0F0F0 |

**How to set:**
1. Click empty canvas
2. Format → Canvas background → Color: #F0F0F0
3. Format → Wallpaper → Color: #F0F0F0

---

### 2. NAVIGATION RAIL BACKGROUND (Shape)
**Type:** Rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 0 | 0 |
| Y | 0 | 0 |
| W | 40 | **60** |
| H | 720 | **1080** |
| Fill | #FFFFFF | #FFFFFF |
| Border | None | None |
| Radius | 0 | 0 |

---

### 3. NAVIGATION RAIL DIVIDER (Shape)
**Type:** Line or thin rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 40 | **60** |
| Y | 0 | 0 |
| W | 1 | **1** |
| H | 720 | **1080** |
| Color | #DFE1E2 | #DFE1E2 |

---

### 4. ACTIVE INDICATOR BAR (Shape - per page)
**Type:** Rectangle (no border)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 0 | 0 |
| W | 3 | **4** |
| H | 40 | **60** |
| Fill | #005EA2 | #005EA2 |

**Y Position by Page:**
| Page | V5 Y | 1920×1080 Y |
|------|------|-------------|
| 1. Command Center | 63 | **84** (matches nav button) |
| 2. Explorer | 116 | **164** |
| 3. Traffic & Acquisition | 169 | **244** |
| 4. Play Events | 222 | **324** |
| 5. External Search | 275 | **404** |
| 6. AI Insights | 328 | **484** |
| 7. Deep Dive | 381 | **564** |

---

### 5. HEADER DIVIDER LINE (Shape)
**Type:** Line or thin rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 56 | **84** |
| Y | 64 | **96** |
| W | 1176 | **1764** |
| H | 1 | **1** |
| Color | #DFE1E2 | #DFE1E2 |

**Note:** Divider spans from content start (84) to right edge of Actions panel area.

---

### 6. KPI CARD CONTAINERS (4 Shapes)
**Type:** Rounded Rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| Y | 83 | **124** |
| W | 197 | **295** |
| H | 67 | **100** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 4px | **4px** |
| Shadow | OFF | OFF |

**X Positions (with 12px gap):**
| Card | V5 X | 1920×1080 X | Right Edge |
|------|------|-------------|------------|
| KPI 1 | 56 | **84** | 379 |
| KPI 2 | 261 | **391** | 686 |
| KPI 3 | 465 | **698** | 993 |
| KPI 4 | 670 | **1005** | 1300 |

**Gap calculation:** (1300 - 84 - 4×295) ÷ 3 = 12px gaps ✓

---

### 7. SECTION HEADER LABELS (2 Text Boxes)
**Type:** Text Box

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 56 | **84** |
| W | 267 | **400** |
| H | 19 | **28** |
| Font | 14pt Semibold | 14pt Semibold |
| Color | #1B1B1B | #1B1B1B |

**Y Positions:**
| Section | V5 Y | 1920×1080 Y | Text |
|---------|------|-------------|------|
| Section 1 | 160 | **240** | "Geographic & Device Distribution" |
| Section 2 | 440 | **660** | "Content Performance" |

---

### 8. VISUAL CONTAINER BACKGROUNDS (4 Shapes)
**Type:** Rounded Rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 4px | **4px** |
| Shadow | OFF | OFF |

**Top Row (2-Up Layout, Expanded State):**
| Container | V5 X | V5 Y | V5 W | V5 H | 1920 X | 1920 Y | 1920 W | 1920 H |
|-----------|------|------|------|------|--------|--------|--------|--------|
| Top Left | 56 | 176 | 444 | 254 | **84** | **264** | **666** | **381** |
| Top Right | 508 | 176 | 445 | 254 | **762** | **264** | **668** | **381** |

**Bottom Row (2-Up Layout, Expanded State):**
| Container | V5 X | V5 Y | V5 W | V5 H | 1920 X | 1920 Y | 1920 W | 1920 H |
|-----------|------|------|------|------|--------|--------|--------|--------|
| Bottom Left | 56 | 456 | 444 | 220 | **84** | **684** | **666** | **330** |
| Bottom Right | 508 | 456 | 445 | 220 | **762** | **684** | **668** | **330** |

**⚠️ IMPORTANT: Perfect Edge Alignment Calculation:**
- Content Start: 84
- Content End (Expanded): 1430 (scaled from 953)
- Usable Width: 1346 (scaled from 897)
- 2 containers + 1 gap = (1346 - 12) ÷ 2 = 667 each
- Left: 666, Right: 668 (distribute remainder)

---

### 9. VISUAL CONTAINER INNER PLACEHOLDER (Optional Shapes)
**Type:** Rectangle (inside each container)

| Property | Offset from Container |
|----------|----------------------|
| X | Container X + 18 |
| Y | Container Y + 72 |
| W | Container W - 36 |
| H | Container H - 100 |
| Fill | #F8F9FA |
| Border | None |

**Example for Top Left Container (84, 264, 666, 381):**
- Inner: X=102, Y=336, W=630, H=281

---

### 10. ACTIONS PANEL CONTAINER (Shape)
**Type:** Rounded Rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 965 | **1448** |
| Y | 134 | **201** |
| W | 267 | **400** |
| H | 275 | **412** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 4px | **4px** |

---

### 11. ACTIONS PANEL ACCENT BAR (Shape)
**Type:** Rectangle (no border, no radius)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 965 | **1448** |
| Y | 134 | **201** |
| W | 3 | **4** |
| H | 275 | **412** |
| Fill | #005EA2 | #005EA2 |

---

### 12. ACTIONS PANEL TITLE (Text Box)
**Type:** Text Box

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 978 | **1467** |
| Y | 144 | **216** |
| W | 248 | **372** |
| H | 19 | **28** |
| Text | "Recommended Actions" | "Recommended Actions" |
| Font | 12-13pt Semibold | **13pt Semibold** |
| Color | #1B1B1B | #1B1B1B |

---

### 13. ACTION CARD CONTAINERS (3 Shapes)
**Type:** Rounded Rectangle

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 980 | **1470** |
| W | 235 | **352** |
| H | 60 | **90** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 4px | **4px** |

**Y Positions:**
| Card | V5 Y | 1920×1080 Y |
|------|------|-------------|
| Card 1 (HIGH) | 172 | **258** |
| Card 2 (MEDIUM) | 243 | **365** |
| Card 3 (INFO) | 314 | **471** |

**Card Gap:** (365 - 258 - 90) = 17px gap between cards

---

### 14. ACTION CARD INNER ELEMENTS (Per Card)

**Priority Badge (Text Box):**
| Property | Value |
|----------|-------|
| X | Card X + 12 |
| Y | Card Y + 8 |
| W | 60 |
| H | 16 |
| Font | 9pt Bold, UPPERCASE |
| Colors | HIGH: #D83B01, MEDIUM: #E5A000, INFO: #0076D6 |

**Action Title (Text Box):**
| Property | Value |
|----------|-------|
| X | Card X + 12 |
| Y | Card Y + 28 |
| W | Card W - 36 |
| H | 20 |
| Font | 11pt Semibold |
| Color | #1B1B1B |

**Action Description (Text Box):**
| Property | Value |
|----------|-------|
| X | Card X + 12 |
| Y | Card Y + 50 |
| W | Card W - 36 |
| H | 32 |
| Font | 10pt Regular |
| Color | #565C65 |

**Arrow Icon (Text or Shape):**
| Property | Value |
|----------|-------|
| X | Card X + Card W - 24 |
| Y | Card Y + 35 |
| Text | "→" or chevron icon |
| Font | 14pt |
| Color | #005EA2 |

---

### 15. DISCLAIMER TEXT (Text Box)
**Type:** Text Box

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 978 | **1467** |
| Y | 384 | **576** |
| W | 241 | **361** |
| H | 19 | **28** |
| Text | "AI-generated insights" | "AI-generated insights based on data patterns" |
| Font | 9pt Regular | 9pt Regular |
| Color | #71767A | #71767A |

---

### 16. EXPAND BUTTON (Shape + Text)
**Type:** Rounded Rectangle with text

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 990 | **1485** |
| Y | 82 | **123** |
| W | 106 | **159** |
| H | 40 | **60** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 4px | **4px** |
| Text | "Actions Expand" | "Actions ❯" |
| Text Font | 11pt Regular | 12pt Regular |
| Text Color | #005EA2 | #005EA2 |

**Hover State:**
| Property | Value |
|----------|-------|
| Fill | #E7F2F4 |
| Border | 1px #0D5C6D |

---

### 17. COLLAPSE BUTTON (Shape + Text)
**Type:** Rounded Rectangle with text

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 1102 | **1653** |
| Y | 82 | **123** |
| W | 106 | **159** |
| H | 40 | **60** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 4px | **4px** |
| Text | "Actions Collapse" | "❮ Collapse" |
| Text Font | 11pt Regular | 12pt Regular |
| Text Color | #005EA2 | #005EA2 |

**Hover State:**
| Property | Value |
|----------|-------|
| Fill | #E7F2F4 |
| Border | 1px #0D5C6D |

---

### 18. RESET BUTTON (Shape)
**Type:** Rounded Rectangle (or Circle)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 934 | **1401** |
| Y | 17 | **26** |
| W | 33 | **50** |
| H | 33 | **50** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #DFE1E2 | 1px #DFE1E2 |
| Radius | 50% (circle) or 4px | 4px or 50% |
| Text | "Reset" or ↺ icon | "Reset" |
| Text Font | 10pt | 11pt |
| Text Color | #005EA2 | #005EA2 |

---

### 19. INFO BUTTON (Shape)
**Type:** Rounded Rectangle (or Circle)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| X | 974 | **1461** |
| Y | 17 | **26** |
| W | 33 | **50** |
| H | 33 | **50** |
| Fill | #FFFFFF | #FFFFFF |
| Border | 1px #005EA2 | 1px #005EA2 |
| Radius | 50% (circle) or 4px | 4px or 50% |
| Text | "i" | "i" |
| Text Font | 12pt Semibold | 12pt Semibold |
| Text Color | #005EA2 | #005EA2 |

---

## CONTENT BOUNDARIES SUMMARY

### Expanded State (Actions Panel Visible)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| Content Start X | 56 | **84** |
| Content End X | 953 | **1430** |
| Usable Width | 897 | **1346** |
| Gutter (to panel) | 12 | **18** |
| Panel Start X | 965 | **1448** |
| Panel End X | 1232 | **1848** |

### Collapsed State (Actions Panel Hidden)

| Property | V5 (1280×720) | 1920×1080 |
|----------|---------------|-----------|
| Content Start X | 56 | **84** |
| Content End X | 1232 | **1848** |
| Usable Width | 1176 | **1764** |

**Width Gained When Collapsed:** +418 px (400 panel + 18 gutter)

---

## LAYOUT TEMPLATES (1920×1080)

### Template A: Full-Width Visual
**Use for:** Matrix, large tables, timelines

**Expanded:**
| Visual | X | Y | W | H |
|--------|---|---|---|---|
| Main | 84 | 264 | 1346 | 381 |

**Collapsed:**
| Visual | X | Y | W | H |
|--------|---|---|---|---|
| Main | 84 | 264 | 1764 | 381 |

### Template B: 2-Up Layout
**Use for:** Map + Chart, two complementary visuals

**Expanded (gap=12):**
| Container | X | Y | W | H |
|-----------|---|---|---|---|
| Left | 84 | 264 | 667 | 381 |
| Right | 763 | 264 | 667 | 381 |

**Collapsed (gap=12):**
| Container | X | Y | W | H |
|-----------|---|---|---|---|
| Left | 84 | 264 | 876 | 381 |
| Right | 972 | 264 | 876 | 381 |

### Template C: 3-Up Layout
**Use for:** Multiple small charts (Acquisition page)

**Expanded (gap=12):**
| Container | X | Y | W | H |
|-----------|---|---|---|---|
| Left | 84 | 264 | 440 | 381 |
| Center | 536 | 264 | 440 | 381 |
| Right | 988 | 264 | 442 | 381 |

**Collapsed (gap=12):**
| Container | X | Y | W | H |
|-----------|---|---|---|---|
| Left | 84 | 264 | 580 | 381 |
| Center | 676 | 264 | 580 | 381 |
| Right | 1268 | 264 | 580 | 381 |

---

## BOOKMARK GROUPS FOR EXPAND/COLLAPSE

### Group: grp_Actions_Expanded
**Elements to include:**
1. Actions Panel Container (shape)
2. Actions Panel Accent Bar (shape)
3. Actions Panel Title (text box)
4. Action Card 1 container + content
5. Action Card 2 container + content
6. Action Card 3 container + content
7. Disclaimer text (text box)
8. Collapse Button (button)
9. HTML Visual (if using for dynamic content)

### Group: grp_Actions_Collapsed
**Elements to include:**
1. Expand Button (button)

### Bookmark: "Actions_Expanded"
| Setting | Value |
|---------|-------|
| Display | ✅ ON |
| Data | ❌ OFF |
| Current page | ✅ ON |
| Selected visuals | ✅ ON (grp_Actions_Expanded visible, grp_Actions_Collapsed hidden) |

### Bookmark: "Actions_Collapsed"
| Setting | Value |
|---------|-------|
| Display | ✅ ON |
| Data | ❌ OFF |
| Current page | ✅ ON |
| Selected visuals | ✅ ON (grp_Actions_Expanded hidden, grp_Actions_Collapsed visible) |

---

## CONTAINER INNER PADDING FORMULA

For consistent visual placement inside white containers:

```
Inner X = Container X + 18
Inner Y = Container Y + 72 (room for title + subtitle)
Inner W = Container W - 36
Inner H = Container H - 100
```

**Example:** Container at (84, 264, 667, 381)
- Title: X=96, Y=276, W=643, H=24 (12pt Semibold #1B1B1B)
- Subtitle: X=96, Y=304, W=643, H=20 (11pt Regular #565C65)
- Inner Visual: X=102, Y=336, W=631, H=281

---

## COLOR REFERENCE (Complete)

| Color | Hex | Usage |
|-------|-----|-------|
| Page Background | #F0F0F0 | Canvas, outspace |
| White | #FFFFFF | Cards, panels, nav rail, buttons |
| Border Gray | #DFE1E2 | All borders (default) |
| Inner Placeholder | #F8F9FA | Visual placeholder areas |
| Primary Blue | #005EA2 | Accent bars, active indicators, links |
| Hover Blue Fill | #E7F2F4 | Button hover background |
| Hover Blue Border | #0D5C6D | Button hover border |
| Active Blue | #162E51 | Selected nav icon |
| Hover Blue Icon | #1A4480 | Hovered nav icon |
| Dark Text | #1B1B1B | Titles, KPI values |
| Gray Text | #565C65 | Labels, subtitles |
| Tertiary Text | #71767A | Helper text, disclaimers |
| Success Green | #00A91C | Positive trend (▲) |
| Critical Red | #D83933 | Negative trend (▼) |
| Warning Amber | #FFBE2E | Warning state |
| High Priority | #D83B01 | HIGH badge |
| Medium Priority | #E5A000 | MEDIUM badge |
| Info Priority | #0076D6 | INFO badge |

---

## SHAPE COUNT SUMMARY

**Per Page (minimum):**
| Shape Type | Count | Purpose |
|------------|-------|---------|
| Nav Rail Background | 1 | White background rectangle |
| Nav Rail Divider | 1 | Vertical line |
| Active Indicator | 1 | Blue bar (changes Y per page) |
| Header Divider | 1 | Horizontal line |
| KPI Card Containers | 4 | White rounded rectangles |
| Section Headers | 2 | Text boxes |
| Visual Containers | 4 | White rounded rectangles |
| Actions Panel Container | 1 | White rounded rectangle |
| Actions Panel Accent Bar | 1 | Blue rectangle |
| Actions Panel Title | 1 | Text box |
| Action Cards | 3 | White rounded rectangles |
| Action Card Content | 12 | Text boxes (4 per card) |
| Disclaimer | 1 | Text box |
| Expand Button | 1 | Button/shape |
| Collapse Button | 1 | Button/shape |
| Reset Button | 1 | Button/shape |
| Info Button | 1 | Button/shape |

**Total shapes per page:** ~36 manual shapes + Power BI visuals

---

**Document Version:** 1.0
**Created:** 2026-01-18
**Purpose:** Precise translation guide for building Power BI dashboard from V5 mockup

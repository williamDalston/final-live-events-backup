# V5 Mockup Element Audit

## Canvas & Background
| Property | V5 Value | Notes |
|----------|----------|-------|
| Slide Width | 20.00" | Widescreen |
| Slide Height | 11.25" | 16:9 ratio |
| **Background Color** | **#F0F0F0** | Light gray - NOT white! |

## Navigation Rail
| Property | V5 Value |
|----------|----------|
| Width | 0.62" |
| Height | Full canvas (11.25") |
| Fill | #FFFFFF (white) |
| Right border | #DFE1E2, 1pt |
| Active indicator bar | 0.04" wide, #005EA2 |
| Active background | 0.62" x 0.62", #005EA2 |
| Icon size | 0.42" x 0.42" |
| Icon X position | 0.10" |
| First icon Y | 0.98" |
| Icon spacing | 0.83" vertical |

## Header Area
| Element | Position | Size | Style |
|---------|----------|------|-------|
| "HHS LIVE EVENTS" | x=0.88, y=0.19 | 3.12" x 0.21" | Gray text |
| Page Title | x=0.88, y=0.33 | 6.25" x 0.31" | Bold, dark |
| Subtitle | x=0.88, y=0.74 | 2.95" x 0.20" | Gray text |
| Divider line | x=0.88, y=1.00 | 18.38" x ~0 | #DFE1E2 border |

## Utility Bar (Top Right)
| Element | Position | Size | Style |
|---------|----------|------|-------|
| Date slicer | x=11.68, y=0.46 | 2.08" x 0.52" | Text with dropdown |
| Reset button | x=14.59, y=0.27 | 0.52" x 0.52" | Circle, white fill, #DFE1E2 border |
| Info button | x=15.21, y=0.27 | 0.52" x 0.52" | Circle, #005EA2 border, "i" text |
| Last refresh | x=16.92, y=0.49 | 2.08" x 0.15" | Small gray text |

## KPI Cards Row
| Property | V5 Value |
|----------|----------|
| Y position | 1.29" |
| Card width | 3.07" |
| Card height | 1.04" |
| Gap between | 0.12" |
| Fill | #FFFFFF |
| Border | #DFE1E2, 1pt |
| First card X | 0.88" |
| Card positions | 0.88, 4.07, 7.27, 10.47 |

## Section Labels
| Property | V5 Value |
|----------|----------|
| First section Y | 2.50" |
| Second section Y | 6.88" |
| Width | 4.00" |
| Height | 0.30" |
| Font | 14pt, bold, dark |

## Visual Containers
| Property | V5 Value |
|----------|----------|
| Top row Y | 2.75" |
| Top row height | 3.96" |
| Bottom row Y | 7.12" |
| Bottom row height | 3.44" |
| Container width | 6.27" |
| Gap between | 0.12" |
| Container fill | #FFFFFF |
| Container border | #DFE1E2, 1pt |

### Visual Container Inner Structure
| Element | Offset | Size |
|---------|--------|------|
| Title | +0.14", +0.15" | width-0.28", 0.30" |
| Subtitle | +0.14", +0.40" | width-0.28", 0.20" |
| Inner placeholder | +0.19", +0.60" | width-0.38", height-0.80" |
| Inner placeholder fill | **#F8F9FA** | Light gray |

## Actions Panel (Expanded)
| Property | V5 Value |
|----------|----------|
| X position | 15.07" |
| Y position | 2.10" |
| Width | 4.17" |
| Height | 4.29" |
| Fill | #FFFFFF |
| Border | #DFE1E2, 1pt |
| Blue accent bar | 0.04" wide, #005EA2 |

### Actions Panel Inner Elements
| Element | Position | Size |
|---------|----------|------|
| Title "Recommended Actions" | x+0.20", y+0.15" | 3.87" x 0.30" |
| Action card 1 | x+0.25", y+0.60" | 3.67" x 0.94" |
| Action card 2 | x+0.25", y+1.71" | 3.67" x 0.94" |
| Action card 3 | x+0.25", y+2.81" | 3.67" x 0.94" |
| Disclaimer | x+0.20", y+3.90" | 3.77" x 0.30" |

### Action Cards
| Property | V5 Value |
|----------|----------|
| Width | 3.67" |
| Height | 0.94" |
| Gap between | 1.11" (y spacing) |
| Fill | #FFFFFF |
| Border | #DFE1E2, 1pt |

## Expand/Collapse Buttons
| Button | Position | Size | Style |
|--------|----------|------|-------|
| "Actions Expand" | x=15.47, y=1.28 | 1.65" x 0.62" | White fill, #DFE1E2 border, text label |
| "Actions Collapse" | x=17.22, y=1.30 | 1.65" x 0.62" | White fill, #DFE1E2 border, text label |

**Note:** V5 uses TEXT BUTTONS ("Actions Expand", "Actions Collapse"), NOT chevron icons (<, >)

## Color Palette Summary
| Color | Hex | Usage |
|-------|-----|-------|
| Background | #F0F0F0 | Slide background |
| White | #FFFFFF | Cards, panels, nav rail |
| Border gray | #DFE1E2 | All borders |
| Inner placeholder | #F8F9FA | Visual placeholder areas |
| HHS Blue | #005EA2 | Active indicators, info button border, accent bars |
| Dark text | #1B1B1B | Titles, values |
| Gray text | #565C65 | Subtitles, labels |
| High/Red | #D83B01 | High priority |
| Medium/Amber | #E5A000 | Medium priority |
| Info/Blue | #0076D6 | Info priority |

## Key Corrections Needed in Script
1. **Slide background** must be #F0F0F0, not default/white
2. **Expand/Collapse buttons** use text labels, not < > chevrons
3. **Inner placeholder fill** is #F8F9FA (slightly different from #FAFAFA)
4. **Action card gap** is calculated from Y positions: 2.70 -> 3.81 -> 4.91 (gap = 1.11")
5. **Both Expand and Collapse buttons** appear on same slide (not conditional)

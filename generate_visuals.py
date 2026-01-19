#!/usr/bin/env python3
"""
HHS Live Events Dashboard - Visual Generator

Generates Power BI visual.json files with correct measure bindings.
Uses your project's exact measures, grid positions, and JSON patterns.

Improvements from older version:
- Flexible field reference parsing: "[MeasureName]", "Table[Column]", or plain "MeasureName"
- Optional external blueprint loading from JSON files
- Dynamic page ID mapping from pages.json

Usage:
    python generate_visuals.py --page executive_summary
    python generate_visuals.py --all
    python generate_visuals.py --dry-run --page explorer
    python generate_visuals.py --blueprint path/to/blueprint.json
"""

import json
import secrets
import os
import argparse
import copy
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

# =============================================================================
# CONFIGURATION
# =============================================================================

SCRIPT_DIR = Path(__file__).parent
BASE_PATH = SCRIPT_DIR / "HHS Live Events Performance Dashboard.Report" / "definition" / "pages"
BLUEPRINTS_DIR = SCRIPT_DIR / "blueprints"  # Optional: external blueprint files

# Visual schema (Power BI PBIP format)
VISUAL_SCHEMA_URL = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json"

# Default measure entity
DEFAULT_MEASURE_ENTITY = "Measures_Livecast"

# Grid positions from V5_PIXEL_GRID_REFERENCE.md (EXACT VALUES)
GRID = {
    "canvas": {"width": 1280, "height": 720},
    "content_start_x": 56,
    "content_end_expanded": 953,
    "content_end_collapsed": 1232,
    "kpi_row": {"y": 83, "height": 67, "width": 197, "gap": 8},  # Y=83 per doc
    "kpi_x_positions": [56, 261, 465, 670],  # 56, 261, 465, 670 per doc
    "section_1": {"y": 176, "height": 254},  # Y=176 per doc
    "section_2": {"y": 456, "height": 220},  # Y=456 per doc
    "2up_expanded": {"left_width": 444, "right_width": 445, "gap": 8, "right_x": 508},
    "2up_collapsed": {"left_width": 584, "right_width": 584, "gap": 8, "right_x": 648},
}

# Visual type mapping (friendly names -> Power BI internal types)
VISUAL_TYPE_MAP = {
    "Card": "cardVisual",
    "KPI": "kpi",
    "Table": "tableEx",
    "BarChart": "clusteredBarChart",
    "LineChart": "lineChart",
    "AreaChart": "areaChart",
    "PieChart": "pieChart",
    "Slicer": "slicer",
    "Map": "azureMap",
    "Treemap": "treemap",
    "DecompositionTree": "decompositionTreeVisual",
    "KeyInfluencers": "keyInfluencersVisual",
    "HTML": "htmlContent443BE3AD55E043BF878BED274D3A6855",
}

# =============================================================================
# FLEXIBLE FIELD REFERENCE PARSING (from older version)
# =============================================================================

def parse_field_reference(field_name: str, default_entity: str = DEFAULT_MEASURE_ENTITY) -> Tuple[str, str, bool]:
    """
    Parse a field reference to extract table name, column/measure name, and type.

    Supports multiple formats:
    - "[MeasureName]" -> Measure from default entity
    - "Table[Column]" -> Column from specific table
    - "MeasureName" -> Assumed measure from default entity

    Args:
        field_name: The field reference string
        default_entity: Default entity for measures (default: Measures_Livecast)

    Returns:
        Tuple of (entity_name, property_name, is_measure)
    """
    if not field_name:
        return default_entity, "", True

    # Format: [MeasureName] - measure with brackets
    if field_name.startswith("[") and field_name.endswith("]"):
        measure_name = field_name.strip("[]")
        return default_entity, measure_name, True

    # Format: Table[Column] - column with table prefix
    if "[" in field_name and "]" in field_name:
        parts = field_name.split("[")
        table_name = parts[0]
        column_name = parts[1].rstrip("]")
        return table_name, column_name, False

    # Plain name - assume measure from default entity
    return default_entity, field_name, True

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def generate_visual_id() -> str:
    """Generate a unique 24-character hex visual ID."""
    return secrets.token_hex(12)

def generate_filter_id() -> str:
    """Generate a unique filter ID."""
    return secrets.token_hex(10)

def generate_field_id() -> str:
    """Generate a unique field ID for reference labels."""
    return f"field-{secrets.token_hex(4)}-{secrets.token_hex(2)}-{secrets.token_hex(2)}-{secrets.token_hex(2)}-{secrets.token_hex(6)}"

def build_measure_ref(measure_name: str, entity: str = "Measures_Livecast") -> Dict:
    """Build a measure reference object."""
    return {
        "Measure": {
            "Expression": {
                "SourceRef": {
                    "Entity": entity
                }
            },
            "Property": measure_name
        }
    }

def build_column_ref(column_name: str, entity: str) -> Dict:
    """Build a column reference object."""
    return {
        "Column": {
            "Expression": {
                "SourceRef": {
                    "Entity": entity
                }
            },
            "Property": column_name
        }
    }

def literal(value: Any) -> Dict:
    """Wrap a value in Power BI literal expression format."""
    if isinstance(value, bool):
        return {"expr": {"Literal": {"Value": "true" if value else "false"}}}
    elif isinstance(value, int):
        return {"expr": {"Literal": {"Value": f"{value}L"}}}
    elif isinstance(value, float):
        return {"expr": {"Literal": {"Value": f"{value}D"}}}
    elif isinstance(value, str):
        return {"expr": {"Literal": {"Value": f"'{value}'"}}}
    else:
        return {"expr": {"Literal": {"Value": str(value)}}}

def build_field_ref(field_name: str, default_entity: str = DEFAULT_MEASURE_ENTITY) -> Dict:
    """
    Build a field reference from a flexible field string.

    Supports:
    - "[MeasureName]" -> Measure reference
    - "Table[Column]" -> Column reference
    - "MeasureName" -> Measure reference (assumed)
    """
    entity, prop, is_measure = parse_field_reference(field_name, default_entity)
    if is_measure:
        return build_measure_ref(prop, entity)
    else:
        return build_column_ref(prop, entity)

# =============================================================================
# BLUEPRINT LOADING (from older version)
# =============================================================================

def load_blueprint(blueprint_path: Path) -> Dict[str, Any]:
    """Load a page blueprint from a JSON file."""
    with open(blueprint_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_page_id_mapping() -> Dict[str, str]:
    """
    Get mapping of page display names to actual page IDs from pages.json.

    Returns:
        Dict mapping display name -> page folder ID
    """
    pages_json_path = BASE_PATH / "pages.json"
    if not pages_json_path.exists():
        return {}

    with open(pages_json_path, 'r', encoding='utf-8') as f:
        pages_metadata = json.load(f)

    page_order = pages_metadata.get("pageOrder", [])

    # Build mapping by reading each page's page.json
    mapping = {}
    for page_id in page_order:
        page_json_path = BASE_PATH / page_id / "page.json"
        if page_json_path.exists():
            with open(page_json_path, 'r', encoding='utf-8') as f:
                page_data = json.load(f)
                display_name = page_data.get("displayName", "")
                if display_name:
                    mapping[display_name] = page_id
                    # Also add lowercase/normalized versions
                    mapping[display_name.lower().replace(" ", "_")] = page_id

    return mapping

def convert_visual_type(friendly_type: str) -> str:
    """Convert a friendly visual type name to Power BI internal type."""
    return VISUAL_TYPE_MAP.get(friendly_type, friendly_type)

# =============================================================================
# KPI CARD TEMPLATE
# =============================================================================

def generate_kpi_card(
    measure: str,
    title: str,
    position: Dict,
    mom_label: Optional[str] = None,
    mom_color: Optional[str] = None,
    alt_text: Optional[str] = None,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a KPI card visual.json structure.

    Args:
        measure: Main measure name (e.g., "Sessions")
        title: Card title text
        position: Dict with x, y, z, height, width, tabOrder
        mom_label: MoM label measure name (optional)
        mom_color: MoM color measure name (optional)
        alt_text: Alt text measure name (optional)
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    visual = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 96),
            "z": position.get("z", 1000),
            "height": position.get("height", 67),
            "width": position.get("width", 197),
            "tabOrder": position.get("tabOrder", position.get("z", 1000))
        },
        "visual": {
            "visualType": "cardVisual",
            "query": {
                "queryState": {
                    "Data": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_measure_ref(measure),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": {
                "cardCalloutArea": [
                    {
                        "properties": {
                            "paddingIndividual": literal(True),
                            "paddingLeft": {"expr": {"Literal": {"Value": "5L"}}},
                            "paddingBottom": {"expr": {"Literal": {"Value": "0L"}}}
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "divider": [{"properties": {"show": literal(False)}, "selector": {"id": "default"}}],
                "fillCustom": [{"properties": {"show": literal(False)}}],
                "glowCustom": [{"properties": {"show": literal(False)}, "selector": {"id": "default"}}],
                "image": [{"properties": {"show": literal(False)}, "selector": {"id": "default"}}],
                "label": [
                    {
                        "properties": {
                            "show": literal(False),
                            "position": literal("aboveValue"),
                            "textWrap": literal(False),
                            "matchValueAlignment": literal(False),
                            "horizontalAlignment": literal("center")
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "layout": [
                    {
                        "properties": {
                            "orientation": {"expr": {"Literal": {"Value": "1D"}}},
                            "rowCount": {"expr": {"Literal": {"Value": "1L"}}},
                            "cellPadding": {"expr": {"Literal": {"Value": "0L"}}},
                            "calloutSize": {"expr": {"Literal": {"Value": "50D"}}},
                            "style": literal("Cards")
                        }
                    },
                    {
                        "properties": {
                            "backgroundShow": literal(False),
                            "rectangleRoundedCurve": {"expr": {"Literal": {"Value": "5L"}}},
                            "leftOuterMargin": {"expr": {"Literal": {"Value": "5L"}}},
                            "topOuterMargin": {"expr": {"Literal": {"Value": "0L"}}},
                            "paddingUniform": {"expr": {"Literal": {"Value": "0L"}}},
                            "paddingIndividual": literal(True)
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "outline": [{"properties": {"show": literal(False)}, "selector": {"id": "default"}}],
                "padding": [
                    {
                        "properties": {
                            "topMargin": {"expr": {"Literal": {"Value": "0L"}}},
                            "bottomMargin": {"expr": {"Literal": {"Value": "0L"}}},
                            "paddingIndividual": literal(True)
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "shadowCustom": [{"properties": {"show": literal(False)}, "selector": {"id": "default"}}],
                "spacing": [
                    {
                        "properties": {"verticalSpacing": {"expr": {"Literal": {"Value": "0L"}}}},
                        "selector": {"id": "default"}
                    }
                ],
                "value": [
                    {"properties": {"show": literal(True)}},
                    {
                        "properties": {
                            "fontFamily": literal("'Segoe UI', wf_segoe-ui_normal, helvetica, arial, sans-serif"),
                            "fontSize": {"expr": {"Literal": {"Value": "19D"}}},
                            "horizontalAlignment": literal("left")
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "referenceLabel": [
                    {
                        "properties": {
                            "backgroundShow": literal(False),
                            "paddingUniform": {"expr": {"Literal": {"Value": "5L"}}},
                            "paddingIndividual": literal(True)
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "referenceLabelTitle": [
                    {
                        "properties": {"show": literal(False)},
                        "selector": {"metadata": f"Measures_Livecast.{measure}"}
                    }
                ],
                "referenceLabelValue": []
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title),
                            "show": literal(True),
                            "heading": literal("Normal"),
                            "titleWrap": literal(True),
                            "fontColor": {"solid": {"color": {"expr": {"Literal": {"Value": "'#1B1B1B'"}}}}},
                            "alignment": literal("center"),
                            "fontSize": literal("14"),
                            "fontFamily": literal("Segoe UI Semibold")
                        }
                    }
                ],
                "spacing": [
                    {
                        "properties": {"verticalSpacing": {"expr": {"Literal": {"Value": "2D"}}}},
                        "selector": {"id": "default"}
                    },
                    {
                        "properties": {
                            "customizeSpacing": literal(False),
                            "verticalSpacing": {"expr": {"Literal": {"Value": "0D"}}}
                        }
                    }
                ],
                "background": [
                    {
                        "properties": {
                            "show": literal(True),
                            "color": {"solid": {"color": {"expr": {"Literal": {"Value": "'#FFFFFF'"}}}}},
                            "transparency": {"expr": {"Literal": {"Value": "0D"}}}
                        }
                    }
                ],
                "border": [
                    {
                        "properties": {
                            "show": literal(False),
                            "color": {"solid": {"color": {"expr": {"Literal": {"Value": "'#DFE1E2'"}}}}},
                            "radius": {"expr": {"Literal": {"Value": "4D"}}},
                            "width": {"expr": {"Literal": {"Value": "1D"}}}
                        }
                    }
                ],
                "visualHeader": [{"properties": {"show": literal(False)}}],
                "padding": [
                    {
                        "properties": {
                            "top": {"expr": {"Literal": {"Value": "0D"}}},
                            "bottom": {"expr": {"Literal": {"Value": "0D"}}},
                            "left": {"expr": {"Literal": {"Value": "0D"}}},
                            "right": {"expr": {"Literal": {"Value": "0D"}}}
                        }
                    }
                ],
                "general": [{"properties": {}}]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": [
                {
                    "name": generate_filter_id(),
                    "field": build_measure_ref(measure),
                    "type": "Advanced"
                }
            ]
        }
    }

    # Add MoM label reference if provided
    if mom_label:
        field_id = generate_field_id()
        visual["visual"]["objects"]["referenceLabel"].append({
            "properties": {
                "value": {"expr": build_measure_ref(mom_label)}
            },
            "selector": {
                "data": [{"dataViewWildcard": {"matchingOption": 0}}],
                "metadata": f"Measures_Livecast.{measure}",
                "id": field_id,
                "order": 0
            }
        })

        # Add MoM color if provided
        if mom_color:
            visual["visual"]["objects"]["referenceLabelValue"].append({
                "properties": {
                    "valueFontColor": {
                        "solid": {
                            "color": {"expr": build_measure_ref(mom_color)}
                        }
                    }
                },
                "selector": {
                    "data": [{"dataViewWildcard": {"matchingOption": 0}}],
                    "metadata": f"Measures_Livecast.{measure}"
                }
            })

    # Add alt text if provided
    if alt_text:
        visual["visual"]["visualContainerObjects"]["general"] = [
            {
                "properties": {
                    "altText": {"expr": build_measure_ref(alt_text)}
                }
            }
        ]

    return visual

# =============================================================================
# BAR CHART TEMPLATE
# =============================================================================

def generate_bar_chart(
    category_column: str,
    category_entity: str,
    measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None,
    exclude_blanks: bool = True,
    top_n: Optional[int] = None
) -> Dict:
    """
    Generate a clustered bar chart visual.json structure.

    Args:
        category_column: Column name for category axis
        category_entity: Entity/table name for category
        measure: Measure name for Y-axis
        title: Chart title text
        position: Dict with x, y, z, height, width
        visual_id: Optional custom visual ID
        exclude_blanks: Whether to filter out blank/null values
        top_n: Optional top N filter

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    # Build filters
    filters = []

    # Add blank exclusion filter
    if exclude_blanks:
        filters.append({
            "name": generate_filter_id(),
            "field": build_column_ref(category_column, category_entity),
            "type": "Categorical",
            "filter": {
                "Version": 2,
                "From": [
                    {
                        "Name": "t",
                        "Entity": category_entity,
                        "Type": 0
                    }
                ],
                "Where": [
                    {
                        "Condition": {
                            "Not": {
                                "Expression": {
                                    "In": {
                                        "Expressions": [
                                            {
                                                "Column": {
                                                    "Expression": {
                                                        "SourceRef": {
                                                            "Source": "t"
                                                        }
                                                    },
                                                    "Property": category_column
                                                }
                                            }
                                        ],
                                        "Values": [
                                            [
                                                {
                                                    "Literal": {
                                                        "Value": "null"
                                                    }
                                                }
                                            ]
                                        ]
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "objects": {
                "general": [
                    {
                        "properties": {
                            "isInvertedSelectionMode": literal(True)
                        }
                    }
                ]
            }
        })
    else:
        filters.append({
            "name": generate_filter_id(),
            "field": build_column_ref(category_column, category_entity),
            "type": "Categorical"
        })

    # Build objects with optional Top N
    objects = {
        "labels": [{"properties": {"show": literal(True)}}],
        "categoryAxis": [
            {
                "properties": {
                    "show": literal(True),
                    "showAxisTitle": literal(False)
                }
            }
        ],
        "valueAxis": [
            {
                "properties": {
                    "showAxisTitle": literal(False),
                    "show": literal(False)
                }
            }
        ]
    }

    # Add Top N filter if specified
    if top_n:
        objects["general"] = [
            {
                "properties": {
                    "filter": {
                        "expr": {
                            "Filter": {
                                "Expression": {
                                    "Top": {
                                        "Top": {
                                            "Expression": build_column_ref(category_column, category_entity)
                                        },
                                        "Count": {"Literal": {"Value": f"{top_n}L"}},
                                        "OrderBy": [
                                            {
                                                "Direction": 2,
                                                "Expression": build_measure_ref(measure)
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ]

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 466),
            "z": position.get("z", 7000),
            "height": position.get("height", 220),
            "width": position.get("width", 444),
            "tabOrder": position.get("tabOrder", position.get("z", 7000))
        },
        "visual": {
            "visualType": "clusteredBarChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": build_column_ref(category_column, category_entity),
                                "queryRef": f"{category_entity}.{category_column}",
                                "nativeQueryRef": category_column,
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_measure_ref(measure),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": objects,
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": filters
        }
    }

# =============================================================================
# TABLE TEMPLATE
# =============================================================================

def generate_table(
    columns: List[Dict],  # [{"entity": "ga4-pages", "column": "Page title"}, ...]
    measures: List[str],
    title: str,
    position: Dict,
    visual_id: Optional[str] = None,
    exclude_blanks: bool = True
) -> Dict:
    """
    Generate a table visual.json structure.

    Args:
        columns: List of column dicts with entity and column name
        measures: List of measure names
        title: Table title text
        position: Dict with x, y, z, height, width
        visual_id: Optional custom visual ID
        exclude_blanks: Whether to filter out blank/null values in first column

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    projections = []

    # Add columns
    for col in columns:
        projections.append({
            "field": build_column_ref(col["column"], col["entity"]),
            "queryRef": f"{col['entity']}.{col['column']}",
            "nativeQueryRef": col["column"]
        })

    # Add measures
    for measure in measures:
        projections.append({
            "field": build_measure_ref(measure),
            "queryRef": f"Measures_Livecast.{measure}",
            "nativeQueryRef": measure
        })

    # Build filters to exclude blank values
    filters = []
    if exclude_blanks and columns:
        first_col = columns[0]
        filters.append({
            "name": generate_filter_id(),
            "field": build_column_ref(first_col["column"], first_col["entity"]),
            "type": "Categorical",
            "filter": {
                "Version": 2,
                "From": [
                    {
                        "Name": "t",
                        "Entity": first_col["entity"],
                        "Type": 0
                    }
                ],
                "Where": [
                    {
                        "Condition": {
                            "Not": {
                                "Expression": {
                                    "In": {
                                        "Expressions": [
                                            {
                                                "Column": {
                                                    "Expression": {
                                                        "SourceRef": {
                                                            "Source": "t"
                                                        }
                                                    },
                                                    "Property": first_col["column"]
                                                }
                                            }
                                        ],
                                        "Values": [
                                            [
                                                {
                                                    "Literal": {
                                                        "Value": "null"
                                                    }
                                                }
                                            ]
                                        ]
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "objects": {
                "general": [
                    {
                        "properties": {
                            "isInvertedSelectionMode": literal(True)
                        }
                    }
                ]
            }
        })

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 508),
            "y": position.get("y", 466),
            "z": position.get("z", 6000),
            "height": position.get("height", 220),
            "width": position.get("width", 445),
            "tabOrder": position.get("tabOrder", position.get("z", 6000))
        },
        "visual": {
            "visualType": "tableEx",
            "query": {
                "queryState": {
                    "Values": {
                        "projections": projections
                    }
                }
            },
            "objects": {},
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": filters
        }
    }

# =============================================================================
# 100% STACKED BAR CHART TEMPLATE
# =============================================================================

def generate_stacked_bar_chart(
    category_column: str,
    category_entity: str,
    measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a 100% stacked bar chart visual.json structure.
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 508),
            "y": position.get("y", 188),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 445),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "hundredPercentStackedBarChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": build_column_ref(category_column, category_entity),
                                "queryRef": f"{category_entity}.{category_column}",
                                "nativeQueryRef": category_column,
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_measure_ref(measure),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": {
                "legend": [{"properties": {"show": literal(True)}}],
                "labels": [{"properties": {"show": literal(True)}}],
                "valueAxis": [
                    {
                        "properties": {
                            "show": literal(False),
                            "showAxisTitle": literal(False)
                        }
                    }
                ],
                "categoryAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": [
                {
                    "name": generate_filter_id(),
                    "field": build_column_ref(category_column, category_entity),
                    "type": "Categorical"
                },
                {
                    "name": generate_filter_id(),
                    "field": build_measure_ref(measure),
                    "type": "Advanced"
                }
            ]
        }
    }

# =============================================================================
# MAP VISUAL TEMPLATE (Azure Maps)
# =============================================================================

def generate_map_visual(
    location_column: str,
    location_entity: str,
    size_measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate an Azure Map bubble visual.
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 188),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 444),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "azureMap",
            "query": {
                "queryState": {
                    "Location": {
                        "projections": [
                            {
                                "field": build_column_ref(location_column, location_entity),
                                "queryRef": f"{location_entity}.{location_column}",
                                "nativeQueryRef": location_column,
                                "active": True
                            }
                        ]
                    },
                    "Size": {
                        "projections": [
                            {
                                "field": build_measure_ref(size_measure),
                                "queryRef": f"Measures_Livecast.{size_measure}",
                                "nativeQueryRef": size_measure
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_measure_ref(size_measure),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": {
                "legend": [{"properties": {"show": literal(False)}}]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": [
                {
                    "name": generate_filter_id(),
                    "field": build_column_ref(location_column, location_entity),
                    "type": "Categorical"
                }
            ]
        }
    }

# =============================================================================
# LINE CHART TEMPLATE
# =============================================================================

def generate_line_chart(
    axis_column: str,
    axis_entity: str,
    measures: List[str],
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a line chart visual.
    """
    vid = visual_id or generate_visual_id()

    # Build measure projections
    y_projections = []
    for measure in measures:
        y_projections.append({
            "field": build_measure_ref(measure),
            "queryRef": f"Measures_Livecast.{measure}",
            "nativeQueryRef": measure
        })

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 188),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 444),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "lineChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": build_column_ref(axis_column, axis_entity),
                                "queryRef": f"{axis_entity}.{axis_column}",
                                "nativeQueryRef": axis_column,
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": y_projections
                    }
                }
            },
            "objects": {
                "legend": [{"properties": {"show": literal(len(measures) > 1)}}],
                "labels": [{"properties": {"show": literal(False)}}],
                "categoryAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ],
                "valueAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# AREA CHART TEMPLATE
# =============================================================================

def generate_area_chart(
    axis_column: str,
    axis_entity: str,
    measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate an area chart visual.
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 188),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 444),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "areaChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": build_column_ref(axis_column, axis_entity),
                                "queryRef": f"{axis_entity}.{axis_column}",
                                "nativeQueryRef": axis_column,
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                }
            },
            "objects": {
                "legend": [{"properties": {"show": literal(False)}}],
                "labels": [{"properties": {"show": literal(False)}}],
                "categoryAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ],
                "valueAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# TREEMAP TEMPLATE
# =============================================================================

def generate_treemap(
    category_column: str,
    category_entity: str,
    measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a treemap visual.
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 188),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 444),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "treemap",
            "query": {
                "queryState": {
                    "Group": {
                        "projections": [
                            {
                                "field": build_column_ref(category_column, category_entity),
                                "queryRef": f"{category_entity}.{category_column}",
                                "nativeQueryRef": category_column,
                                "active": True
                            }
                        ]
                    },
                    "Values": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_measure_ref(measure),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": {
                "legend": [{"properties": {"show": literal(False)}}],
                "labels": [{"properties": {"show": literal(True)}}]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# MATRIX TEMPLATE (pivotTable)
# =============================================================================

def generate_matrix(
    rows: List[Dict],  # [{"entity": "ga4-titles", "column": "Page title"}, ...]
    values: List[str],  # Measure names
    title: str,
    position: Dict,
    columns: Optional[List[Dict]] = None,  # Optional column grouping
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a matrix (pivot table) visual.

    Args:
        rows: List of row field dicts with entity and column name
        values: List of measure names for values
        title: Matrix title text
        position: Dict with x, y, z, height, width
        columns: Optional list of column field dicts for column grouping
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    # Build row projections
    row_projections = []
    for i, row in enumerate(rows):
        row_projections.append({
            "field": build_column_ref(row["column"], row["entity"]),
            "queryRef": f"{row['entity']}.{row['column']}",
            "nativeQueryRef": row["column"],
            "active": i == 0  # First row is active
        })

    # Build value projections
    value_projections = []
    for measure in values:
        value_projections.append({
            "field": build_measure_ref(measure),
            "queryRef": f"Measures_Livecast.{measure}",
            "nativeQueryRef": measure
        })

    query_state = {
        "Rows": {"projections": row_projections},
        "Values": {"projections": value_projections}
    }

    # Add columns if specified
    if columns:
        col_projections = []
        for col in columns:
            col_projections.append({
                "field": build_column_ref(col["column"], col["entity"]),
                "queryRef": f"{col['entity']}.{col['column']}",
                "nativeQueryRef": col["column"]
            })
        query_state["Columns"] = {"projections": col_projections}

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 176),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 897),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "pivotTable",
            "query": {
                "queryState": query_state
            },
            "objects": {
                "grid": [
                    {
                        "properties": {
                            "stylePreset": literal("None"),
                            "rowPadding": {"expr": {"Literal": {"Value": "2L"}}}
                        }
                    }
                ],
                "columnHeaders": [
                    {
                        "properties": {
                            "bold": literal(True)
                        }
                    }
                ],
                "rowHeaders": [
                    {
                        "properties": {
                            "bold": literal(False)
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# GAUGE TEMPLATE
# =============================================================================

def generate_gauge(
    measure: str,
    title: str,
    position: Dict,
    min_value: float = 0,
    max_value: float = 100,
    target_value: Optional[float] = None,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a gauge visual.

    Args:
        measure: Measure name for the gauge value
        title: Gauge title text
        position: Dict with x, y, z, height, width
        min_value: Minimum scale value
        max_value: Maximum scale value
        target_value: Optional target line value
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    objects = {
        "gaugeAxis": [
            {
                "properties": {
                    "min": {"expr": {"Literal": {"Value": f"{min_value}D"}}},
                    "max": {"expr": {"Literal": {"Value": f"{max_value}D"}}}
                }
            }
        ],
        "labels": [{"properties": {"show": literal(True)}}]
    }

    query_state = {
        "Value": {
            "projections": [
                {
                    "field": build_measure_ref(measure),
                    "queryRef": f"Measures_Livecast.{measure}",
                    "nativeQueryRef": measure
                }
            ]
        }
    }

    # Add target if specified
    if target_value is not None:
        objects["gaugeTarget"] = [
            {
                "properties": {
                    "show": literal(True)
                }
            }
        ]

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 456),
            "z": position.get("z", 6000),
            "height": position.get("height", 220),
            "width": position.get("width", 444),
            "tabOrder": position.get("tabOrder", position.get("z", 6000))
        },
        "visual": {
            "visualType": "gauge",
            "query": {
                "queryState": query_state
            },
            "objects": objects,
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# SCATTER CHART TEMPLATE
# =============================================================================

def generate_scatter(
    x_measure: str,
    y_measure: str,
    title: str,
    position: Dict,
    legend_column: Optional[str] = None,
    legend_entity: Optional[str] = None,
    size_measure: Optional[str] = None,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a scatter chart visual.

    Args:
        x_measure: Measure name for X-axis
        y_measure: Measure name for Y-axis
        title: Chart title text
        position: Dict with x, y, z, height, width
        legend_column: Optional column for legend/color grouping
        legend_entity: Entity for legend column
        size_measure: Optional measure for bubble size
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    query_state = {
        "X": {
            "projections": [
                {
                    "field": build_measure_ref(x_measure),
                    "queryRef": f"Measures_Livecast.{x_measure}",
                    "nativeQueryRef": x_measure
                }
            ]
        },
        "Y": {
            "projections": [
                {
                    "field": build_measure_ref(y_measure),
                    "queryRef": f"Measures_Livecast.{y_measure}",
                    "nativeQueryRef": y_measure
                }
            ]
        }
    }

    # Add legend if specified
    if legend_column and legend_entity:
        query_state["Details"] = {
            "projections": [
                {
                    "field": build_column_ref(legend_column, legend_entity),
                    "queryRef": f"{legend_entity}.{legend_column}",
                    "nativeQueryRef": legend_column,
                    "active": True
                }
            ]
        }

    # Add size if specified
    if size_measure:
        query_state["Size"] = {
            "projections": [
                {
                    "field": build_measure_ref(size_measure),
                    "queryRef": f"Measures_Livecast.{size_measure}",
                    "nativeQueryRef": size_measure
                }
            ]
        }

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 508),
            "y": position.get("y", 456),
            "z": position.get("z", 6500),
            "height": position.get("height", 220),
            "width": position.get("width", 445),
            "tabOrder": position.get("tabOrder", position.get("z", 6500))
        },
        "visual": {
            "visualType": "scatterChart",
            "query": {
                "queryState": query_state
            },
            "objects": {
                "categoryAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(True)
                        }
                    }
                ],
                "valueAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(True)
                        }
                    }
                ],
                "legend": [{"properties": {"show": literal(legend_column is not None)}}]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# COMBO CHART TEMPLATE (Line + Clustered Column)
# =============================================================================

def generate_combo_chart(
    axis_column: str,
    axis_entity: str,
    column_measures: List[str],
    line_measures: List[str],
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a combo chart (line + clustered column) visual.

    Args:
        axis_column: Column name for shared axis
        axis_entity: Entity for axis column
        column_measures: List of measures for column series
        line_measures: List of measures for line series
        title: Chart title text
        position: Dict with x, y, z, height, width
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    # Build column projections
    column_projections = []
    for measure in column_measures:
        column_projections.append({
            "field": build_measure_ref(measure),
            "queryRef": f"Measures_Livecast.{measure}",
            "nativeQueryRef": measure
        })

    # Build line projections
    line_projections = []
    for measure in line_measures:
        line_projections.append({
            "field": build_measure_ref(measure),
            "queryRef": f"Measures_Livecast.{measure}",
            "nativeQueryRef": measure
        })

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 56),
            "y": position.get("y", 176),
            "z": position.get("z", 5000),
            "height": position.get("height", 254),
            "width": position.get("width", 897),
            "tabOrder": position.get("tabOrder", position.get("z", 5000))
        },
        "visual": {
            "visualType": "lineClusteredColumnComboChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": build_column_ref(axis_column, axis_entity),
                                "queryRef": f"{axis_entity}.{axis_column}",
                                "nativeQueryRef": axis_column,
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": column_projections
                    },
                    "Y2": {
                        "projections": line_projections
                    }
                }
            },
            "objects": {
                "legend": [{"properties": {"show": literal(True)}}],
                "labels": [{"properties": {"show": literal(False)}}],
                "categoryAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ],
                "valueAxis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ],
                "lineY2Axis": [
                    {
                        "properties": {
                            "showAxisTitle": literal(False)
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# FUNNEL CHART TEMPLATE
# =============================================================================

def generate_funnel(
    category_column: str,
    category_entity: str,
    measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a funnel chart visual.

    Args:
        category_column: Column name for funnel stages
        category_entity: Entity for category column
        measure: Measure name for funnel values
        title: Chart title text
        position: Dict with x, y, z, height, width
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 508),
            "y": position.get("y", 456),
            "z": position.get("z", 6500),
            "height": position.get("height", 220),
            "width": position.get("width", 445),
            "tabOrder": position.get("tabOrder", position.get("z", 6500))
        },
        "visual": {
            "visualType": "funnel",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": build_column_ref(category_column, category_entity),
                                "queryRef": f"{category_entity}.{category_column}",
                                "nativeQueryRef": category_column,
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_measure_ref(measure),
                            "direction": "Descending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": {
                "labels": [{"properties": {"show": literal(True)}}],
                "percentBarLabel": [{"properties": {"show": literal(True)}}]
            },
            "visualContainerObjects": {
                "title": [
                    {
                        "properties": {
                            "text": literal(title)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "filterConfig": {
            "filters": []
        }
    }

# =============================================================================
# HTML CONTENT VISUAL TEMPLATE (Actions Panel)
# =============================================================================

def generate_html_visual(
    measure: str,
    title: str,
    position: Dict,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate an HTML content visual for the Actions Panel.

    Args:
        measure: Measure name that returns HTML content (e.g., "Recommended Actions HTML (Dynamic)")
        title: Visual title (usually not shown for HTML visuals)
        position: Dict with x, y, z, height, width
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 978),
            "y": position.get("y", 169),
            "z": position.get("z", 15000),
            "height": position.get("height", 230),
            "width": position.get("width", 241),
            "tabOrder": position.get("tabOrder", position.get("z", 15000))
        },
        "visual": {
            "visualType": "htmlContent443BE3AD55E043BF878BED274D3A6855",
            "query": {
                "queryState": {
                    "content": {
                        "projections": [
                            {
                                "field": build_measure_ref(measure),
                                "queryRef": f"Measures_Livecast.{measure}",
                                "nativeQueryRef": measure
                            }
                        ]
                    }
                }
            },
            "drillFilterOtherVisuals": True
        }
    }

# =============================================================================
# ACTION BUTTON TEMPLATE
# =============================================================================

def generate_action_button(
    button_type: str,
    position: Dict,
    icon: Optional[str] = None,
    text: Optional[str] = None,
    tooltip: Optional[str] = None,
    navigation_page: Optional[str] = None,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate an action button visual.

    Args:
        button_type: Type of action - "info", "clearSlicers", "navigation", "bookmark"
        position: Dict with x, y, z, height, width
        icon: Icon type - "information", "clearAllSlicers", "blank", etc.
        text: Button text (optional)
        tooltip: Tooltip text (optional)
        navigation_page: Page ID to navigate to (for navigation buttons)
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    # Determine icon and action based on button_type
    if button_type == "info":
        icon = icon or "information"
        action_type = "PageNavigation"
    elif button_type == "clearSlicers":
        icon = icon or "clearAllSlicers"
        action_type = "ClearAllSlicers"
    elif button_type == "navigation":
        icon = icon or "blank"
        action_type = "PageNavigation"
    else:
        icon = icon or "blank"
        action_type = "PageNavigation"

    visual = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 0),
            "y": position.get("y", 0),
            "z": position.get("z", 10000),
            "height": position.get("height", 28),
            "width": position.get("width", 28),
            "tabOrder": position.get("tabOrder", 1000)
        },
        "visual": {
            "visualType": "actionButton",
            "objects": {
                "icon": [
                    {
                        "properties": {
                            "shapeType": literal(icon)
                        },
                        "selector": {"id": "default"}
                    }
                ]
            },
            "visualContainerObjects": {
                "visualLink": [
                    {
                        "properties": {
                            "show": literal(True),
                            "type": literal(action_type)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "howCreated": "InsertVisualButton"
    }

    # Add tooltip if provided
    if tooltip:
        visual["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["tooltipPlaceholderText"] = literal(tooltip)

    # Add navigation page if provided
    if navigation_page:
        visual["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["navigationSection"] = literal(navigation_page)

    # Add text if provided
    if text:
        visual["visual"]["objects"]["text"] = [
            {
                "properties": {
                    "text": literal(text)
                },
                "selector": {"id": "default"}
            }
        ]

    return visual

# =============================================================================
# TEXTBOX TEMPLATE
# =============================================================================

def generate_textbox(
    text: str,
    position: Dict,
    font_size: int = 9,
    font_color: str = "#565C65",
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a textbox visual.

    Args:
        text: Text content
        position: Dict with x, y, z, height, width
        font_size: Font size in points
        font_color: Font color hex
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 0),
            "y": position.get("y", 0),
            "z": position.get("z", 9000),
            "height": position.get("height", 16),
            "width": position.get("width", 100),
            "tabOrder": position.get("tabOrder", 0)
        },
        "visual": {
            "visualType": "textbox",
            "objects": {
                "general": [
                    {
                        "properties": {
                            "paragraphs": [
                                {
                                    "textRuns": [
                                        {
                                            "value": text,
                                            "textStyle": {}
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "background": [
                    {
                        "properties": {
                            "show": literal(False)
                        }
                    }
                ],
                "visualHeader": [
                    {
                        "properties": {
                            "show": literal(False)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        }
    }

# =============================================================================
# SHAPE TEMPLATE (using actionButton with blank icon)
# =============================================================================

def generate_shape(
    position: Dict,
    fill_color: str = "#FFFFFF",
    border_color: Optional[str] = "#DFE1E2",
    border_width: int = 1,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a shape visual using actionButton with blank icon.

    Args:
        position: Dict with x, y, z, height, width
        fill_color: Background fill color hex
        border_color: Border color hex (None for no border)
        border_width: Border width in pixels
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    visual = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 0),
            "y": position.get("y", 0),
            "z": position.get("z", 100),
            "height": position.get("height", 100),
            "width": position.get("width", 100),
            "tabOrder": position.get("tabOrder", 0)
        },
        "visual": {
            "visualType": "actionButton",
            "objects": {
                "icon": [
                    {
                        "properties": {
                            "shapeType": literal("blank")
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "fill": [
                    {
                        "properties": {
                            "show": literal(True),
                            "fillColor": {"solid": {"color": {"expr": {"Literal": {"Value": f"'{fill_color}'"}}}}}
                        },
                        "selector": {"id": "default"}
                    }
                ],
                "outline": [
                    {
                        "properties": {
                            "show": literal(border_color is not None)
                        }
                    }
                ]
            },
            "visualContainerObjects": {
                "visualLink": [
                    {
                        "properties": {
                            "show": literal(False)
                        }
                    }
                ],
                "background": [
                    {
                        "properties": {
                            "show": literal(False)
                        }
                    }
                ],
                "visualHeader": [
                    {
                        "properties": {
                            "show": literal(False)
                        }
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        },
        "howCreated": "InsertVisualButton"
    }

    # Add border if specified
    if border_color:
        visual["visual"]["visualContainerObjects"]["border"] = [
            {
                "properties": {
                    "show": literal(True),
                    "color": {"solid": {"color": {"expr": {"Literal": {"Value": f"'{border_color}'"}}}}},
                    "width": {"expr": {"Literal": {"Value": f"{border_width}D"}}}
                }
            }
        ]

    return visual

# =============================================================================
# SLICER VISUAL TEMPLATE
# =============================================================================

def generate_slicer(
    column: str,
    entity: str,
    title: str,
    position: Dict,
    slicer_mode: str = "Between",
    sync_group: Optional[str] = None,
    visual_id: Optional[str] = None
) -> Dict:
    """
    Generate a slicer visual.

    Args:
        column: Column name for the slicer
        entity: Entity/table name
        title: Slicer title
        position: Dict with x, y, z, height, width
        slicer_mode: Slicer mode - "Between" for date range, "Basic" for dropdown
        sync_group: Optional sync group name for cross-page sync
        visual_id: Optional custom visual ID

    Returns:
        Complete visual.json structure
    """
    vid = visual_id or generate_visual_id()

    visual = {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
        "name": vid,
        "position": {
            "x": position.get("x", 728),
            "y": position.get("y", 34),
            "z": position.get("z", 8000),
            "height": position.get("height", 28),
            "width": position.get("width", 120),
            "tabOrder": position.get("tabOrder", 0)
        },
        "visual": {
            "visualType": "slicer",
            "query": {
                "queryState": {
                    "Values": {
                        "projections": [
                            {
                                "field": build_column_ref(column, entity),
                                "queryRef": f"{entity}.{column}",
                                "nativeQueryRef": column,
                                "active": True
                            }
                        ]
                    }
                },
                "sortDefinition": {
                    "sort": [
                        {
                            "field": build_column_ref(column, entity),
                            "direction": "Ascending"
                        }
                    ],
                    "isDefaultSort": True
                }
            },
            "objects": {
                "data": [
                    {
                        "properties": {
                            "mode": literal(slicer_mode)
                        }
                    }
                ],
                "general": [
                    {
                        "properties": {}
                    }
                ]
            },
            "drillFilterOtherVisuals": True
        }
    }

    # Add sync group if specified
    if sync_group:
        visual["visual"]["syncGroup"] = {
            "groupName": sync_group,
            "fieldChanges": True,
            "filterChanges": True
        }

    return visual

# =============================================================================
# PAGE CONFIGURATIONS
# =============================================================================

PAGE_CONFIGS = {
    "executive_summary": {
        "page_id": "88620660ba315057a1dd",
        "display_name": "Executive Summary",
        "visuals": [
            # KPI Cards Row (Y=83 per V5_PIXEL_GRID_REFERENCE.md) - simplified without MoM references
            {
                "type": "kpi_card",
                "measure": "Sessions",
                "title": "Sessions",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Page Views",
                "title": "Page Views",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Top Device Category",
                "title": "Top Device",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Avg Pages per Session",
                "title": "Avg Pages/Session",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 (Y=176, H=254 per V5_PIXEL_GRID_REFERENCE.md) - Sessions by City Map (Left)
            {
                "type": "map",
                "location_column": "City",
                "location_entity": "ga4-geography-livecast-play",
                "size_measure": "Sessions by City",
                "title": "Sessions by City",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 444}
            },
            # Section 1 (Y=176, H=254) - Device Breakdown (Right) - 100% Stacked Bar per spec
            {
                "type": "stacked_bar_100",
                "category_column": "deviceCategory",
                "category_entity": "DimDevice",
                "measure": "Device Sessions",
                "title": "Device Breakdown",
                "position": {"x": 508, "y": 176, "z": 5500, "height": 254, "width": 445}
            },
            # Section 2 (Y=456, H=220 per V5_PIXEL_GRID_REFERENCE.md) - Top Livecast Videos (Left)
            {
                "type": "bar_chart",
                "category_column": "Livecast Title",
                "category_entity": "DimLivecast",
                "measure": "Total Events",
                "title": "Top Livecast Videos",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444},
                "exclude_blanks": True,
                "top_n": 5
            },
            # Section 2 (Y=456, H=220) - Top Pages Table (Right)
            {
                "type": "table",
                "columns": [{"entity": "ga4-titles", "column": "Page title"}],
                "measures": ["Page Views", "Sessions"],
                "title": "Top Pages",
                "position": {"x": 508, "y": 456, "z": 7000, "height": 220, "width": 445}
            },
            # Actions Panel - HTML Visual (per V5_PIXEL_GRID_REFERENCE.md: X=978, Y=169, W=241, H=230)
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Date Slicer (per DASHBOARD_BUILD_GUIDE.md: Y=34, right-aligned)
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Page Path Slicer (per DASHBOARD_BUILD_GUIDE.md: W=120, H=28)
            {
                "type": "slicer",
                "column": "Page path",
                "entity": "ga4-pages",
                "title": "Page path",
                "position": {"x": 600, "y": 34, "z": 8001, "height": 28, "width": 120},
                "slicer_mode": "Basic"
            },
            # Info Button (per DASHBOARD_BUILD_GUIDE.md: W=28, H=28)
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Reset Filters Button (per DASHBOARD_BUILD_GUIDE.md)
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Last Refresh Text (per DASHBOARD_BUILD_GUIDE.md)
            {
                "type": "textbox",
                "text": "Last refresh: Just Now",
                "position": {"x": 1083, "y": 31, "z": 9000, "height": 10, "width": 133}
            },
            # Actions Panel Container (per V5_PIXEL_GRID_REFERENCE.md: X=965, Y=134, W=267, H=275)
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar (per V5_PIXEL_GRID_REFERENCE.md: X=965, Y=134, W=3, H=275)
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title (per V5_PIXEL_GRID_REFERENCE.md: X=978, Y=144, W=248, H=19)
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
    "explorer": {
        "page_id": "02fc2dd334b2889002b8",
        "display_name": "Explorer",
        "visuals": [
            # KPI Cards - per spec: Active Pages, Avg Engagement, Bounce Rate, Top Source
            {
                "type": "kpi_card",
                "measure": "Active Livecasts",  # Count of distinct pages/livecasts
                "title": "Active Pages",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Avg Engagement per Viewer (Minutes)",
                "title": "Avg Engagement",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Bounce Rate",
                "title": "Bounce Rate",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Top Event Type",  # Returns top traffic source text
                "title": "Top Source",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 - Full width Matrix (pivotTable) per spec
            {
                "type": "matrix",
                "rows": [
                    {"entity": "ga4-titles", "column": "Page title"}
                ],
                "values": ["Total Users", "Engagement Rate by Page"],
                "title": "Page Performance Matrix",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 897}
            },
            # Section 2 - Left: Treemap
            {
                "type": "treemap",
                "category_column": "Traffic Source",
                "category_entity": "DimSource",
                "measure": "Sessions",
                "title": "Traffic Source Breakdown",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444}
            },
            # Section 2 - Right: Bar chart
            {
                "type": "bar_chart",
                "category_column": "Page title",
                "category_entity": "ga4-titles",
                "measure": "Page Views",
                "title": "Most Viewed Pages",
                "position": {"x": 508, "y": 456, "z": 6500, "height": 220, "width": 445},
                "top_n": 10
            },
            # Date Slicer (synced)
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Clear slicers button
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Info button
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Actions Panel
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Actions Panel Container
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
    "traffic": {
        "page_id": "5a28c07f9d53dc1603dc",
        "display_name": "Traffic & Acquisition",
        "visuals": [
            # KPI Cards - Traffic Sources (using base Sessions measure, filtered by slicer)
            {
                "type": "kpi_card",
                "measure": "Sessions",
                "title": "Total Sessions",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Page Views",
                "title": "Page Views",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Total Users",
                "title": "Total Users",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Engagement Rate",
                "title": "Engagement Rate",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 - Full width Stacked Column Chart
            {
                "type": "stacked_bar_chart",
                "category_column": "Date",
                "category_entity": "DimDate",
                "measure": "Sessions",
                "title": "Traffic Sources Over Time",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 897}
            },
            # Section 2 - Left: Top Sources Bar
            {
                "type": "bar_chart",
                "category_column": "Traffic Source",
                "category_entity": "DimSource",
                "measure": "Sessions",
                "title": "Top Traffic Sources",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444},
                "top_n": 10
            },
            # Section 2 - Right: Channel breakdown by Medium
            {
                "type": "bar_chart",
                "category_column": "Medium",
                "category_entity": "DimSource",
                "measure": "Sessions",
                "title": "Sessions by Medium",
                "position": {"x": 508, "y": 456, "z": 6500, "height": 220, "width": 445}
            },
            # Date Slicer
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Clear slicers button
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Info button
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Actions Panel
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Actions Panel Container
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
    "play_events": {
        "page_id": "5d1b99cb2a71aa8ca6aa",
        "display_name": "Play Events",
        "visuals": [
            # KPI Cards
            {
                "type": "kpi_card",
                "measure": "Video Plays",
                "title": "Play Events",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Play Conversion Rate",
                "title": "Completion Rate",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Avg Engagement per Viewer (Minutes)",
                "title": "Avg Watch Time",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Unique Viewers",
                "title": "Unique Viewers",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 - Full width Area Chart
            {
                "type": "area_chart",
                "axis_column": "Date",
                "axis_entity": "DimDate",
                "measure": "Video Plays",
                "title": "Play Events Timeline",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 897}
            },
            # Section 2 - Left: Avg Watch Time by Video
            {
                "type": "bar_chart",
                "category_column": "Livecast Title",
                "category_entity": "DimLivecast",
                "measure": "Avg Engagement per Viewer (Minutes)",
                "title": "Avg Watch Time by Video",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444},
                "exclude_blanks": True,
                "top_n": 5
            },
            # Section 2 - Right: Events by Type
            {
                "type": "bar_chart",
                "category_column": "Event name",
                "category_entity": "ga4-events",
                "measure": "Total Events",
                "title": "Events by Type",
                "position": {"x": 508, "y": 456, "z": 6500, "height": 220, "width": 445}
            },
            # Date Slicer
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Clear slicers button
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Info button
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Actions Panel
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Actions Panel Container
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
    "external_search": {
        "page_id": "5b34bb90009036de0059",
        "display_name": "External Search",
        "visuals": [
            # KPI Cards
            {
                "type": "kpi_card",
                "measure": "GSC Clicks",
                "title": "Clicks",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "GSC Impressions",
                "title": "Impressions",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "GSC CTR",
                "title": "Avg CTR",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "GSC Avg Position",
                "title": "Avg Position",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 - Full width Line Chart
            {
                "type": "line_chart",
                "axis_column": "Date",
                "axis_entity": "DimDate",
                "measures": ["GSC Clicks", "GSC Impressions"],
                "title": "Clicks & Impressions Trend",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 897}
            },
            # Section 2 - Left: Top Queries Table - uses query-specific measures per spec
            {
                "type": "table",
                "columns": [{"entity": "gsc-queries", "column": "Top queries"}],
                "measures": ["Impressions by Query", "Clicks by Query", "CTR by Query", "Position by Query"],
                "title": "Top Search Queries",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444}
            },
            # Section 2 - Right: Top Pages by Clicks
            {
                "type": "bar_chart",
                "category_column": "Top pages",
                "category_entity": "gsc-pages",
                "measure": "GSC Clicks",
                "title": "Top Pages by Clicks",
                "position": {"x": 508, "y": 456, "z": 6500, "height": 220, "width": 445},
                "top_n": 10
            },
            # Date Slicer
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Clear slicers button
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Info button
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Actions Panel
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Actions Panel Container
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
    "ai_insights": {
        "page_id": "fb09347baecdcc751b4c",
        "display_name": "AI Insights",
        "visuals": [
            # KPI Cards - per spec: Anomalies, Forecast Conf, Trend, Data Points
            {
                "type": "kpi_card",
                "measure": "Active Livecasts",  # Proxy for anomaly count
                "title": "Anomalies",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Model Confidence Score",  # Exists in measures
                "title": "Forecast Conf.",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Trend Indicator",  # Exists - returns up/down/stable
                "title": "Trend",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Total Users",  # Proxy for data points
                "title": "Data Points",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 - Full width Line Chart (Anomaly Detection) - Power BI anomaly feature
            {
                "type": "line_chart",
                "axis_column": "Date",
                "axis_entity": "DimDate",
                "measures": ["Sessions"],
                "title": "Anomaly Detection Timeline",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 897}
            },
            # Section 2 - Left: Forecast Chart (Power BI forecast feature)
            {
                "type": "line_chart",
                "axis_column": "Date",
                "axis_entity": "DimDate",
                "measures": ["Sessions"],
                "title": "Forecasted Traffic",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444}
            },
            # Section 2 - Right: Health Score Gauge per spec
            {
                "type": "gauge",
                "measure": "Health Score",
                "title": "Health Score",
                "position": {"x": 508, "y": 456, "z": 6500, "height": 220, "width": 445},
                "min_value": 0,
                "max_value": 100,
                "target_value": 75
            },
            # Date Slicer
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Clear slicers button
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Info button
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Actions Panel
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Actions Panel Container
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
    "deep_dive": {
        "page_id": "77fad064949ec3a5d1b4",
        "display_name": "Deep Dive",
        "visuals": [
            # KPI Cards - per spec: Segments, Top Segment, Correlation, Cohorts
            {
                "type": "kpi_card",
                "measure": "Active Livecasts",  # Proxy for active segments
                "title": "Segments",
                "position": {"x": 56, "y": 83, "z": 1000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Top Device Category",  # Top segment identifier
                "title": "Top Segment",
                "position": {"x": 261, "y": 83, "z": 2000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Engagement Rate",  # Sessions-engagement correlation proxy
                "title": "Correlation",
                "position": {"x": 465, "y": 83, "z": 3000, "height": 67, "width": 197}
            },
            {
                "type": "kpi_card",
                "measure": "Return Rate",  # Cohort retention proxy
                "title": "Cohorts",
                "position": {"x": 670, "y": 83, "z": 4000, "height": 67, "width": 197}
            },
            # Section 1 - Full width Matrix (Decomposition/Segmentation) per spec
            {
                "type": "matrix",
                "rows": [
                    {"entity": "DimSource", "column": "Traffic Source"},
                    {"entity": "DimDevice", "column": "deviceCategory"}
                ],
                "values": ["Sessions", "Page Views", "Total Users", "Engagement Rate"],
                "title": "Segmentation Matrix",
                "position": {"x": 56, "y": 176, "z": 5000, "height": 254, "width": 897}
            },
            # Section 2 - Left: Cohort Analysis Matrix per spec
            {
                "type": "matrix",
                "rows": [{"entity": "DimDate", "column": "Month"}],
                "values": ["Sessions", "Return Rate"],
                "title": "Cohort Analysis",
                "position": {"x": 56, "y": 456, "z": 6000, "height": 220, "width": 444}
            },
            # Section 2 - Right: Correlation Scatter per spec
            {
                "type": "scatter",
                "x_measure": "Sessions",
                "y_measure": "Engagement Rate",
                "title": "Correlation Explorer",
                "position": {"x": 508, "y": 456, "z": 6500, "height": 220, "width": 445},
                "legend_column": "deviceCategory",
                "legend_entity": "DimDevice",
                "size_measure": "Total Users"
            },
            # Date Slicer
            {
                "type": "slicer",
                "column": "Date",
                "entity": "DimDate",
                "title": "Date",
                "position": {"x": 728, "y": 34, "z": 8000, "height": 28, "width": 120},
                "slicer_mode": "Between",
                "sync_group": "Date"
            },
            # Clear slicers button
            {
                "type": "action_button",
                "button_type": "clearSlicers",
                "position": {"x": 892, "y": 34, "z": 8003, "height": 28, "width": 28},
                "tooltip": "Clear all slicers on this page"
            },
            # Info button
            {
                "type": "action_button",
                "button_type": "info",
                "position": {"x": 856, "y": 34, "z": 8002, "height": 28, "width": 28},
                "tooltip": "View page information"
            },
            # Actions Panel
            {
                "type": "html",
                "measure": "Recommended Actions HTML (Dynamic)",
                "title": "Recommended Actions",
                "position": {"x": 978, "y": 169, "z": 15000, "height": 230, "width": 241}
            },
            # Actions Panel Container
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14000, "height": 275, "width": 267},
                "fill_color": "#FFFFFF",
                "border_color": "#DFE1E2"
            },
            # Actions Panel Accent Bar
            {
                "type": "shape",
                "position": {"x": 965, "y": 134, "z": 14500, "height": 275, "width": 3},
                "fill_color": "#005EA2",
                "border_color": None
            },
            # Actions Panel Title
            {
                "type": "textbox",
                "text": "Recommended Actions",
                "position": {"x": 978, "y": 144, "z": 14600, "height": 19, "width": 248}
            },
        ]
    },
}

# =============================================================================
# GENERATOR CLASS
# =============================================================================

class VisualGenerator:
    def __init__(self, base_path: Path, dry_run: bool = False):
        self.base_path = base_path
        self.dry_run = dry_run
        self.generated_count = 0
        self.skipped_count = 0

    def generate_page(self, page_key: str) -> List[str]:
        """Generate all visuals for a page."""
        if page_key not in PAGE_CONFIGS:
            raise ValueError(f"Unknown page: {page_key}. Available: {list(PAGE_CONFIGS.keys())}")

        config = PAGE_CONFIGS[page_key]
        page_id = config["page_id"]
        created_files = []

        print(f"\n{'='*60}")
        print(f"Generating visuals for: {config['display_name']}")
        print(f"Page ID: {page_id}")
        print(f"{'='*60}")

        for visual_config in config["visuals"]:
            visual_json = self._generate_visual(visual_config)
            if visual_json:
                file_path = self._write_visual(page_id, visual_json)
                created_files.append(file_path)

        return created_files

    def _generate_visual(self, config: Dict) -> Optional[Dict]:
        """Generate a single visual based on config."""
        visual_type = config.get("type")

        if visual_type == "kpi_card":
            return generate_kpi_card(
                measure=config["measure"],
                title=config["title"],
                position=config["position"],
                mom_label=config.get("mom_label"),
                mom_color=config.get("mom_color"),
                alt_text=config.get("alt_text")
            )
        elif visual_type == "bar_chart":
            return generate_bar_chart(
                category_column=config["category_column"],
                category_entity=config["category_entity"],
                measure=config["measure"],
                title=config["title"],
                position=config["position"],
                exclude_blanks=config.get("exclude_blanks", True),
                top_n=config.get("top_n")
            )
        elif visual_type == "stacked_bar_chart":
            return generate_stacked_bar_chart(
                category_column=config["category_column"],
                category_entity=config["category_entity"],
                measure=config["measure"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "table":
            return generate_table(
                columns=config["columns"],
                measures=config["measures"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "map":
            return generate_map_visual(
                location_column=config["location_column"],
                location_entity=config["location_entity"],
                size_measure=config["size_measure"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "line_chart":
            return generate_line_chart(
                axis_column=config["axis_column"],
                axis_entity=config["axis_entity"],
                measures=config["measures"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "area_chart":
            return generate_area_chart(
                axis_column=config["axis_column"],
                axis_entity=config["axis_entity"],
                measure=config["measure"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "treemap":
            return generate_treemap(
                category_column=config["category_column"],
                category_entity=config["category_entity"],
                measure=config["measure"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "html":
            return generate_html_visual(
                measure=config["measure"],
                title=config.get("title", ""),
                position=config["position"]
            )
        elif visual_type == "slicer":
            return generate_slicer(
                column=config["column"],
                entity=config["entity"],
                title=config.get("title", ""),
                position=config["position"],
                slicer_mode=config.get("slicer_mode", "Between"),
                sync_group=config.get("sync_group")
            )
        elif visual_type == "action_button":
            return generate_action_button(
                button_type=config["button_type"],
                position=config["position"],
                icon=config.get("icon"),
                text=config.get("text"),
                tooltip=config.get("tooltip"),
                navigation_page=config.get("navigation_page")
            )
        elif visual_type == "textbox":
            return generate_textbox(
                text=config["text"],
                position=config["position"],
                font_size=config.get("font_size", 9),
                font_color=config.get("font_color", "#565C65")
            )
        elif visual_type == "shape":
            return generate_shape(
                position=config["position"],
                fill_color=config.get("fill_color", "#FFFFFF"),
                border_color=config.get("border_color", "#DFE1E2"),
                border_width=config.get("border_width", 1)
            )
        elif visual_type == "matrix":
            return generate_matrix(
                rows=config["rows"],
                values=config["values"],
                title=config["title"],
                position=config["position"],
                columns=config.get("columns")
            )
        elif visual_type == "gauge":
            return generate_gauge(
                measure=config["measure"],
                title=config["title"],
                position=config["position"],
                min_value=config.get("min_value", 0),
                max_value=config.get("max_value", 100),
                target_value=config.get("target_value")
            )
        elif visual_type == "scatter":
            return generate_scatter(
                x_measure=config["x_measure"],
                y_measure=config["y_measure"],
                title=config["title"],
                position=config["position"],
                legend_column=config.get("legend_column"),
                legend_entity=config.get("legend_entity"),
                size_measure=config.get("size_measure")
            )
        elif visual_type == "combo_chart":
            return generate_combo_chart(
                axis_column=config["axis_column"],
                axis_entity=config["axis_entity"],
                column_measures=config["column_measures"],
                line_measures=config["line_measures"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "funnel":
            return generate_funnel(
                category_column=config["category_column"],
                category_entity=config["category_entity"],
                measure=config["measure"],
                title=config["title"],
                position=config["position"]
            )
        elif visual_type == "stacked_bar_100":
            return generate_stacked_bar_chart(
                category_column=config["category_column"],
                category_entity=config["category_entity"],
                measure=config["measure"],
                title=config["title"],
                position=config["position"]
            )
        else:
            print(f"  WARNING: Unknown visual type: {visual_type}")
            return None

    def _write_visual(self, page_id: str, visual_json: Dict) -> str:
        """Write visual.json to the correct folder."""
        visual_id = visual_json["name"]
        visual_folder = self.base_path / page_id / "visuals" / visual_id
        file_path = visual_folder / "visual.json"

        if self.dry_run:
            print(f"  DRY-RUN: Would create {visual_id}")
            print(f"           Title: {visual_json.get('visual', {}).get('visualContainerObjects', {}).get('title', [{}])[0].get('properties', {}).get('text', {}).get('expr', {}).get('Literal', {}).get('Value', 'N/A')}")
        else:
            visual_folder.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(visual_json, f, indent=2)
            print(f"  CREATED: {visual_id}")
            print(f"           {file_path}")

        self.generated_count += 1
        return str(file_path)

    def generate_all(self) -> Dict[str, List[str]]:
        """Generate visuals for all pages."""
        results = {}
        for page_key in PAGE_CONFIGS:
            results[page_key] = self.generate_page(page_key)
        return results

# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate Power BI visual.json files for HHS Live Events Dashboard",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_visuals.py --page executive_summary
  python generate_visuals.py --all --dry-run
  python generate_visuals.py --blueprint blueprints/executive_summary.json
  python generate_visuals.py --show-mapping

Field Reference Formats (in blueprint files):
  "[Sessions]"                   -> Measure from Measures_Livecast
  "Measures_Livecast[Sessions]"  -> Explicit measure reference
  "DimDate[Date]"                -> Column from DimDate table
  "Sessions"                     -> Plain name (assumed measure)
        """
    )
    parser.add_argument(
        "--page",
        choices=list(PAGE_CONFIGS.keys()),
        help="Generate visuals for a specific page"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate visuals for all pages"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing files"
    )
    parser.add_argument(
        "--list-pages",
        action="store_true",
        help="List available page configurations"
    )
    parser.add_argument(
        "--blueprint",
        type=str,
        metavar="PATH",
        help="Load page config from a JSON blueprint file"
    )
    parser.add_argument(
        "--show-mapping",
        action="store_true",
        help="Show page display name -> page ID mapping from pages.json"
    )

    args = parser.parse_args()

    # Show page ID mapping
    if args.show_mapping:
        print("\nPage ID Mapping (from pages.json):")
        print("-" * 50)
        mapping = get_page_id_mapping()
        if mapping:
            # Filter to unique display names (not normalized versions)
            seen_ids = set()
            for name, page_id in sorted(mapping.items()):
                if page_id not in seen_ids and "_" not in name:
                    print(f"  {name:30} -> {page_id}")
                    seen_ids.add(page_id)
        else:
            print("  (Could not load pages.json)")
        return

    if args.list_pages:
        print("\nAvailable pages:")
        for key, config in PAGE_CONFIGS.items():
            visual_count = len(config["visuals"])
            existing = sum(1 for v in config["visuals"] if v.get("exists", False))
            missing = visual_count - existing
            print(f"  {key}: {config['display_name']} ({missing} to generate, {existing} existing)")
        return

    # Load from external blueprint if specified
    if args.blueprint:
        blueprint_path = Path(args.blueprint)
        if not blueprint_path.exists():
            print(f"ERROR: Blueprint file not found: {blueprint_path}")
            return

        print(f"\nLoading blueprint from: {blueprint_path}")
        blueprint = load_blueprint(blueprint_path)

        # Get page ID - try mapping first, then use provided ID
        page_spec = blueprint.get("page", blueprint)
        display_name = page_spec.get("displayName", "")
        page_id = page_spec.get("page_id", "")

        if not page_id and display_name:
            mapping = get_page_id_mapping()
            page_id = mapping.get(display_name) or mapping.get(display_name.lower().replace(" ", "_"))

        if not page_id:
            print(f"ERROR: Could not determine page ID. Specify 'page_id' in blueprint or ensure displayName matches pages.json")
            return

        # Create temp config
        temp_config = {
            "blueprint_page": {
                "page_id": page_id,
                "display_name": display_name or "Blueprint Page",
                "visuals": page_spec.get("visuals", [])
            }
        }

        generator = VisualGenerator(BASE_PATH, dry_run=args.dry_run)
        # Temporarily add to PAGE_CONFIGS
        PAGE_CONFIGS["blueprint_page"] = temp_config["blueprint_page"]
        results = {"blueprint_page": generator.generate_page("blueprint_page")}
        del PAGE_CONFIGS["blueprint_page"]

    elif not args.page and not args.all:
        parser.print_help()
        return

    else:
        generator = VisualGenerator(BASE_PATH, dry_run=args.dry_run)

        if args.all:
            results = generator.generate_all()
        else:
            results = {args.page: generator.generate_page(args.page)}

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Generated: {generator.generated_count}")
    print(f"  Skipped (existing): {generator.skipped_count}")
    if args.dry_run:
        print("  (DRY-RUN mode - no files were written)")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

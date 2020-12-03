from plotly.graph_objects.layout import Template
import plotly.io as pio


nord0 = "#2E3440"
nord1 = "#3B4252"
nord2 = "#434C5E"
nord3 = "#4C566A"

nord4 = "#D8DEE9"
nord5 = "#E5E9F0"
nord6 = "#ECEFF4"

nord7 = "#8FBCBB"
nord8 = "#88C0D0"
nord9 = "#81A1C1"
nord10 = "#5E81AC"

nord11 = "#BF616A"
nord12 = "#D08770"
nord13 = "#EBCB8B"
nord14 = "#A3BE8C"
nord15 = "#B48EAD"

back = nord0
text = nord4


colorway = [
    "#B48EAD",
    "#5E81AC",
    "#81A1C1",
    "#88C0D0",
    # "#8FBCBB",
    "#A3BE8C",
    "#EBCB8B",
    "#D08770",
    "#BF616A",
]

pio.templates["nord"] = Template({
    "annotationdefaults": {"arrowcolor": text, "arrowhead": 0, "arrowwidth": 1},
    "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
    "colorscale": {
        "diverging": [
            [0, "#8e0152"],
            [0.1, "#c51b7d"],
            [0.2, "#de77ae"],
            [0.3, "#f1b6da"],
            [0.4, "#fde0ef"],
            [0.5, "#f7f7f7"],
            [0.6, "#e6f5d0"],
            [0.7, "#b8e186"],
            [0.8, "#7fbc41"],
            [0.9, "#4d9221"],
            [1, "#276419"],
        ],
        "sequential": [
            [0.0, "#0d0887"],
            [0.1111111111111111, "#46039f"],
            [0.2222222222222222, "#7201a8"],
            [0.3333333333333333, "#9c179e"],
            [0.4444444444444444, "#bd3786"],
            [0.5555555555555556, "#d8576b"],
            [0.6666666666666666, "#ed7953"],
            [0.7777777777777778, "#fb9f3a"],
            [0.8888888888888888, "#fdca26"],
            [1.0, "#f0f921"],
        ],
        "sequentialminus": [
            [0.0, "#0d0887"],
            [0.1111111111111111, "#46039f"],
            [0.2222222222222222, "#7201a8"],
            [0.3333333333333333, "#9c179e"],
            [0.4444444444444444, "#bd3786"],
            [0.5555555555555556, "#d8576b"],
            [0.6666666666666666, "#ed7953"],
            [0.7777777777777778, "#fb9f3a"],
            [0.8888888888888888, "#fdca26"],
            [1.0, "#f0f921"],
        ],
    },
    "colorway": colorway,
    "font": {"color": text},
    "geo": {
        "bgcolor": back,
        "lakecolor": nord10,
        "landcolor": "rgb(17,17,17)",
        "showlakes": True,
        "showland": True,
        "subunitcolor": "#506784",
    },
    "hoverlabel": {"align": "left"},
    "hovermode": "closest",
    "mapbox": {"style": "dark"},
    "paper_bgcolor": back,
    "plot_bgcolor": nord1,
    "polar": {
        "angularaxis": {"gridcolor": "#506784", "linecolor": "#506784", "ticks": ""},
        "bgcolor": "rgb(17,17,17)",
        "radialaxis": {"gridcolor": "#506784", "linecolor": "#506784", "ticks": ""},
    },
    "scene": {
        "xaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": "#C8D4E3",
        },
        "yaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": "#C8D4E3",
        },
        "zaxis": {
            "backgroundcolor": "rgb(17,17,17)",
            "gridcolor": "#506784",
            "gridwidth": 2,
            "linecolor": "#506784",
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": "#C8D4E3",
        },
    },
    "shapedefaults": {"line": {"color": "#f2f5fa"}},
    "sliderdefaults": {
        "bgcolor": "#C8D4E3",
        "bordercolor": "rgb(17,17,17)",
        "borderwidth": 1,
        "tickwidth": 0,
    },
    "ternary": {
        "aaxis": {"gridcolor": "#506784", "linecolor": "#506784", "ticks": ""},
        "baxis": {"gridcolor": "#506784", "linecolor": "#506784", "ticks": ""},
        "bgcolor": "rgb(17,17,17)",
        "caxis": {"gridcolor": "#506784", "linecolor": "#506784", "ticks": ""},
    },
    "title": {"x": 0.05},
    "updatemenudefaults": {"bgcolor": "#506784", "borderwidth": 0},
    "xaxis": {
        "automargin": True,
        "gridcolor": "#283442",
        "linecolor": "#506784",
        "ticks": "",
        "title": {"standoff": 15},
        "zerolinecolor": "#283442",
        "zerolinewidth": 2,
    },
    "yaxis": {
        "automargin": True,
        "gridcolor": "#283442",
        "linecolor": "#506784",
        "ticks": "",
        "title": {"standoff": 15},
        "zerolinecolor": "#283442",
        "zerolinewidth": 2,
    },
})
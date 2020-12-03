import plotly.graph_objects as go
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


nord_colorway = [
    "#B48EAD",
    "#5E81AC",
    # "#81A1C1",
    "#88C0D0",
    # "#8FBCBB",
    "#A3BE8C",
    "#EBCB8B",
    "#D08770",
    "#BF616A",
]

nord_sequential = [
    (0, "#B48EAD"),
    (0.125, "#5E81AC"),
    (0.25, "#81A1C1"),
    (0.375, "#88C0D0"),
    (0.5, "#8FBCBB"),
    (0.625, "#A3BE8C"),
    (0.75, "#EBCB8B"),
    (0.875, "#D08770"),
    (1, "#BF616A"),
]

nord_sequentialminus = nord_sequential

pio.templates["nord"] = go.layout.Template(layout={
    "annotationdefaults": {"arrowcolor": text, "arrowhead": 0, "arrowwidth": 1},
    "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
    "colorscale": {
        "diverging": [
            [0, "#8e0152"],
            [0.1, "#c51b7d"],
            [0.2, "#de77ae"],
            [0.3, "#f1b6da"],
            [0.4, "#fde0ef"],
            [0.5, "#f7f7f7"],  # TODO: convert to Nord
            [0.6, "#e6f5d0"],
            [0.7, "#b8e186"],
            [0.8, "#7fbc41"],
            [0.9, "#4d9221"],
            [1, "#276419"],
        ],
        "sequentialminus": nord_sequentialminus,
        "sequential": nord_sequential
    },
    "colorway": nord_colorway,
    "font": {"color": text},
    "geo": {
        "bgcolor": back,
        "lakecolor": nord10,
        "landcolor": nord1,
        "showlakes": True,
        "showland": True,
        "subunitcolor": nord9,
    },
    "hoverlabel": {"align": "left"},
    "hovermode": "closest",
    "mapbox": {"style": "dark"},
    "paper_bgcolor": back,
    "plot_bgcolor": nord1,
    "polar": {
        "angularaxis": {"gridcolor": nord2, "linecolor": nord2, "ticks": ""},
        "bgcolor": nord1,
        "radialaxis": {"gridcolor": nord2, "linecolor": nord2, "ticks": ""},
    },
    "scene": {
        "xaxis": {
            "backgroundcolor": nord1,
            "gridcolor": nord2,
            "gridwidth": 2,
            "linecolor": nord2,
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": nord3,
        },
        "yaxis": {
            "backgroundcolor": nord1,
            "gridcolor": nord2,
            "gridwidth": 2,
            "linecolor": nord2,
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": nord3,
        },
        "zaxis": {
            "backgroundcolor": nord1,
            "gridcolor": nord2,
            "gridwidth": 2,
            "linecolor": nord2,
            "showbackground": True,
            "ticks": "",
            "zerolinecolor": nord3,
        },
    },
    "shapedefaults": {"line": {"color": text}},
    "sliderdefaults": {
        "bgcolor": nord1,
        "bordercolor": nord6,
        "borderwidth": 1,
        "tickwidth": 0,
    },
    "ternary": {
        "aaxis": {"gridcolor": nord2, "linecolor": nord2, "ticks": ""},
        "baxis": {"gridcolor": nord2, "linecolor": nord2, "ticks": ""},
        "bgcolor": nord2,
        "caxis": {"gridcolor": nord2, "linecolor": nord2, "ticks": ""},
    },
    "title": {"x": 0.05},
    "updatemenudefaults": {"bgcolor": nord1, "borderwidth": 0},
    "xaxis": {
        "automargin": True,
        "gridcolor": nord2,
        "linecolor": nord2,
        "ticks": "",
        "title": {"standoff": 15},
        "zerolinecolor": nord3,
        "zerolinewidth": 2,
    },
    "yaxis": {
        "automargin": True,
        "gridcolor": nord2,
        "linecolor": nord2,
        "ticks": "",
        "title": {"standoff": 15},
        "zerolinecolor": nord3,
        "zerolinewidth": 2,
    },
})

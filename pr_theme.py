import matplotlib.pyplot as plt

#  theme colours
theme_colours: dict = {
    "dark_grey": "#435562",
    "light_grey": "#C6CFD3",
    "rust": "#f14f30",
    "whitet": "#FFFFFF",
}

#  Categorical colours
theme_categorical: list = [
    "#E14B4B",  # Red
    "#ca4be1",  # Purple
    "#da2fdc",  # Pink
    "#4b62e1",  # Blue 
    "#2fb0dc",  # Cyan
    "#4be17f",  # Green
    "#3cda8c",  # Aqua
    "#E1964B",  # Orange
    "#f01500",  # Red
    "#edc81e",  # Yellow
    "#a66e58",  # Grey
]  

def setup_matplotlib_environment(self) -> None:
    """Set up the matplotlib plotting environment
    to use a default style.
    """

    plt.rc("lines", linewidth=4)
    # plt.rc('axes', prop_cycle=(plt.cycler('linestyle', ['-', '--', ':', '-.'])))

    # Font
    plt.rcParams["text.usetex"] = False
    plt.rcParams["font.size"] = 18
    plt.rcParams["legend.fontsize"] = 18

    # Ticks
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.size"] = 5.0
    plt.rcParams["xtick.minor.size"] = 3.0
    plt.rcParams["ytick.major.size"] = 5.0
    plt.rcParams["ytick.minor.size"] = 3.0
    plt.rcParams["ytick.right"] = True
    plt.rcParams["xtick.top"] = True

    # Axes
    plt.rcParams["axes.edgecolor"] = self.theme_colours["theme_dark_grey"]
    plt.rcParams["axes.titlecolor"] = self.theme_colours["theme_dark_grey"]
    plt.rcParams["axes.labelcolor"] = self.theme_colours["theme_dark_grey"]
    plt.rcParams["xtick.color"] = self.theme_colours["theme_dark_grey"]
    plt.rcParams["ytick.color"] = self.theme_colours["theme_dark_grey"]

    # Line width
    plt.rcParams["xtick.major.width"] = 3.0
    plt.rcParams["xtick.minor.width"] = 3.0
    plt.rcParams["ytick.major.width"] = 3.0
    plt.rcParams["ytick.minor.width"] = 3.0
    plt.rcParams["axes.linewidth"] = 3.0

    # Line Colours
    plt.rcParams["axes.prop_cycle"] = plt.cycler("color", self.theme_categorical)

    # Markers
    plt.rcParams["lines.markersize"] = 10
    plt.rcParams["lines.markeredgewidth"] = 2

    # Legend
    plt.rcParams["legend.handlelength"] = 3.0

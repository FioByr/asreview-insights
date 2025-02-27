from asreview import open_state
import matplotlib.pyplot as plt

from asreviewcontrib.insights.plot import plot_wss

with open_state("tests/asreview_files/sim_van_de_schoot_2017_1.asreview") as s:

    fig, ax = plt.subplots()

    plot_wss(ax, s)

    plt.title("WSS with custom title")

    fig.savefig("docs/example_custom_title.png")

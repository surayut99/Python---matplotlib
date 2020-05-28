import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter


def change_fmt(val, pos):
    return "{:.2f}%".format(100 * val)


def step():
    mounths = np.array(["Jan", "feb", "Mar", "Apr", "May"])
    x = np.arange(mounths.size)
    y = np.random.randint(1, 8, x.size) / 100

    fig, ax = plt.subplots(1, 3)

    for i in range(ax.shape[0]):
        ax[i].yaxis.set_major_formatter(FuncFormatter(change_fmt))

    plt.sca(ax[0])
    plt.plot(x, y, marker="o")
    plt.xticks(x, mounths)
    plt.title("Line")

    plt.sca(ax[1])
    plt.step(x, y, marker="o", color="green", where="pre")
    plt.xticks(x, mounths)
    plt.title("Step (pre)")

    # illustrate stablility
    plt.sca(ax[2])
    plt.step(x, y, marker="o", color="red", where="post")
    plt.xticks(x, mounths)
    plt.title("Step (post)")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    step()

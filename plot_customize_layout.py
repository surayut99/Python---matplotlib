import matplotlib.pyplot as plt
import numpy as np


def using_subplots():
    fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
    n = 1

    for r in range(ax.shape[0]):
        for c in range(ax.shape[1]):
            ax[r, c].scatter(np.arange(5), np.random.randint(1, 11, 5))
            ax[r, c].set_title("Graph: " + str(n))
            n += 1

    plt.tight_layout()
    plt.show()


def using_subplot2grid():
    fig = plt.figure()
    ax1 = plt.subplot2grid((3, 6), (0, 0), rowspan=2, colspan=3)
    ax2 = plt.subplot2grid((3, 6), (0, 3), rowspan=2, colspan=3)
    ax3 = plt.subplot2grid((3, 6), (2, 0), rowspan=1, colspan=6)

    x = np.arange(6)
    ax1.plot(x, np.random.randint(1, 11, x.size))
    ax2.bar(x, np.random.randint(1, 11, x.size), color="red")
    ax3.scatter(x, np.random.randint(1, 11, x.size), color="green")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    # using_subplots()
    using_subplot2grid()

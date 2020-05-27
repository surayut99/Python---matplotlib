import numpy as np
import matplotlib.pyplot as plt


def quality_control():
    n = 100
    x = np.arange(n)
    data = np.random.normal(150, 5, n)
    m, sd = np.mean(data), np.std(data)

    # create title by format
    t = "n = {}, mean = {:.2f}, sd = {:.2f}".format(n, m, sd)

    # calculate upper and lower control values
    ucl = 2 * sd
    lcl = -ucl

    # find data excluding control
    f = np.where((data > m + ucl) | (data < m + lcl))

    # plot normal chart
    plt.plot(x, data, marker="o", color=".7", alpha=.7)

    # plot data excluding control line
    plt.plot(x[f], data[f], marker="o", color="brown", linestyle="")

    # fill color in range data excluding control line
    # params >> x, start_point, end_point
    plt.fill_between(x, m + ucl, m + 5 * sd, color="red", alpha=.2)
    plt.fill_between(x, m + lcl, m - 5 * sd, color="red", alpha=.2)

    # average line
    plt.axhline(m, color="green", linestyle="--")

    # create upper and lower control line.
    plt.axhline(m + ucl, color="red", linestyle="--")
    plt.axhline(m + lcl, color="red", linestyle="--")

    plt.title(t)
    plt.ylabel("weight (gram)")
    plt.show()


if __name__ == "__main__":
    quality_control()

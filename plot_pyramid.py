# data source: http://popcensus.nso.go.th/pop_data/2553/3/whole_kingdom/Table3.xls

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


def fmt_million(val, pos):
    return "{:.1f}M".format(np.abs(val) / 1000000)


def pyramid():
    # sample data
    age = np.array(["0 - 4", "5 - 9", "10 - 14", "15 - 19", "20 - 24", "25 - 29", "30 - 34", "35 - 39",
                    "40 - 44", "45 - 49", "50 - 54", "55 - 59", "60 - 64", "65 - 69", "70 - 74",
                    "75 - 79", "80 - 84", "85 - 89", "90 - 94", "95 - 99", "> 100"])
    male = np.array([1915887, 2100931, 2494484, 2464805, 2361297, 2529633, 2669927, 2754129, 2753282,
                     2552531, 2211649, 1697221, 1311024, 902675, 722246, 482686, 273915, 108639, 35867,
                     10965, 1238])
    female = np.array([1823981, 1980712, 2369795, 2435784, 2330223, 2562964, 2724990, 2860720, 2918730,
                       2713534, 2376384, 1869867, 1454373, 1030677, 885393, 640698, 388748, 172302, 64170,
                       19868, 2711])

    y = np.arange(age.size)

    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(FuncFormatter(fmt_million))
    ax.set_xlim(-3e6, 3e6)
    female_total = sum(female)
    male_total = sum(male)

    for i in range(male.size):
        plt.text(1e5, i, "{:.1f}M ({:.2f}%)".format(
            female[i] / 1e6, female[i] * 100 / female_total), fontsize=10, verticalalignment="center")
        plt.text(-1e5, i, "{:.1f}M ({:.2f}%)".format(
            male[i] / 1e6, male[i] * 100 / male_total), fontsize=10, verticalalignment="center", horizontalalignment="right")

    plt.barh(y, -male, alpha=.5, color="blue", label="male")
    plt.barh(y, female, alpha=.5, color="pink", label="female")
    plt.yticks(y, age)
    plt.title("Population by age group and gender")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    pyramid()

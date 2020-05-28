import matplotlib.pyplot as plt
from scipy import stats


def scatter_plot():
    x = [170, 168, 166, 159, 172, 162, 155]
    y = [78, 75, 69, 71, 80, 81, 69]

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    line = slope * min(x) + intercept, slope * max(x) + intercept

    title = r"${} = {:.2f} + {:.2f}x, r^2 = {:.2f}, p = {:.2f}$".format(
        "\^y", intercept, slope, r_value ** 2, p_value)

    plt.scatter(x, y)
    plt.plot([min(x), max(x)], line, linestyle="--", color="green")
    plt.xlabel("Height (cm.)")
    plt.ylabel("Weight (kg.)")
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    scatter_plot()
    x = 5

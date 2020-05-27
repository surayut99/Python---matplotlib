import matplotlib.pyplot as plt
import numpy as np


def mix_graph():
    labels = np.array(["Jan", "Feb", "Mar", "Apr", "May"])

    # np.arange(size of range); to create range by numpy
    x = np.arange(labels.size)

    # np.random.normal(mean, sd, size of array to create); to create an array by random value
    y1 = np.random.normal(80, 10, x.size)
    y2 = np.random.normal(95, 15, x.size)
    plt.bar(x, y1, color="purple", label="We")
    plt.plot(x, y2, color="orange", label="them", marker="o")
    plt.xticks(x, labels)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    mix_graph()

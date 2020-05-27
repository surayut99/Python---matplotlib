import matplotlib.pyplot as plt


def demo1():
    # include color, marker and linestyle
    plt.plot([20, 15, 32], color="red", marker="o")
    plt.plot([12, 32, 28], color="blue", linestyle="--")
    plt.show()


def demo2():
    # pass parameter as range
    plt.plot(range(1999, 2005), [13, 23, 43, 22, 12, 44])
    plt.show()


def demo3():
    # pass parameter as range and list
    x = range(2000, 2006)
    y = [15, 12, 16, 34, 22, 20]
    plt.plot(x, y)
    plt.show()


def demo4():
    # make each graph different
    x = range(2000, 2010)
    y = [12, 23, 32, 11, 33, 27, 19, 18, 13, 20]
    plt.plot(x[:5], y[:5], color="violet", marker="o", label="actual")
    plt.plot(x[4:], y[4:], color="orange", linestyle="--", label="forecast")

    # include detail
    plt.title("Sample graph")
    plt.ylabel("Y Label")
    plt.xlabel("X Label")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    demo4()

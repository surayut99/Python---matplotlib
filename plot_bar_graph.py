import matplotlib.pyplot as plt


def bar_graph():

    x = range(4)
    y = (15, 20, 25, 30)
    avg = sum(y) / 4

    # insert title graph
    plt.title("Ordered By Menu (Beverages)", color="red", fontsize=16)

    # inset detail of each bar
    xTicks = ["Coco", "Late", "Tea", "Green" "Tea"]
    plt.xticks(x, xTicks, color="green")

    # insert label to axis
    plt.ylabel("Number of Orders", color="blue")

    # insert line
    plt.axhline(avg, color="brown", linestyle="--")

    # plot graph
    plt.bar(x, y, color="#4d1a7f")
    plt.show()


if __name__ == "__main__":
    bar_graph()

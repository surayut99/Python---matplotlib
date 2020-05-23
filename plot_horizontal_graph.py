import matplotlib.pyplot as plt

def vertical_graph():
    x = range(4)
    y = (10, 15, 20, 22)

    yticks = ["Green", "Blue", "Red", "Yellow"]
    plt.yticks(x, yticks)

    plt.barh(x, y)
    plt.show()

def horizontal_graph():
    x = range(4)
    y = (10, 15, 20, 22)

    xticks = ["Green", "Blue", "Red", "Yellow"]

    # plt.subplots(row, col); to create sub graph
    fig, ax = plt.subplots(1, 2)

    # config layout of each graph
    fig.tight_layout()
    
    # ax is tuple of graph
    ax[0].bar(x, y, color = "blue")
    ax[1].barh(x, y, color = "brown")

    # sca = set current area
    plt.sca(ax[0])
    plt.xticks(x, xticks)
    
    plt.sca(ax[1])
    plt.yticks(x, xticks)

    plt.show()

if __name__ == "__main__":
    # vertical_graph()
    horizontal_graph()
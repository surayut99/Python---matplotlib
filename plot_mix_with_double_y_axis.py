import matplotlib.pyplot as plt
import numpy as np

def plot_double_y_axis():
    labels = np.array(["Jan", "Feb", "Mar", "Apr", "May"])
    x = np.arange(labels.size)
    y1 = np.random.normal(800, 90, labels.size)
    y2 = np.random.normal(80, 10, labels.size)

    fig, ax1 = plt.subplots()
    ax1.bar(x, y1, color = "orange")
    # tick_params to set detial of number on axis
    ax1.tick_params("y", colors = "orange")
    
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("Sale", color="orange", fontsize=14)

    # twinx(); to create another axis using the same x axis
    ax2 = ax1.twinx()

    ax2.plot(x, y2, color = "green", marker = "o") 
    ax2.tick_params("y", colors = "green")
    ax2.set_ylabel("Profit", color="green", fontsize=14)

    # set start y value
    ax2.set_ylim(ymin = 0)

    plt.show()

if __name__ == "__main__":
    plot_double_y_axis()
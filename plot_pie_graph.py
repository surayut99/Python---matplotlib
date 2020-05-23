import matplotlib.pyplot as plt
import numpy as np
 
def basic_pie():
    label = ["USA", "Russia", "Japan", "China", "Korea"]
    n = [0.9, 1, 0.6, 1.6, 0.4]

    plt.pie(n, labels=label, startangle=90, autopct="%.2f%%", explode=(0,0,0,0.1,0))
    plt.axis("equal")
    plt.show()

def advanced_pie():
    label = np.array(["USA", "Russia", "Japan", "China", "Korea"])
    n = [0.9, 1, 0.6, 1.6, 0.4]

    # explode: to pull part from the center
    # use np (numpy) to create an array 
    # np.<number ending with 's'>(size of array) e.g. np.zeros(label.size)
    # create an array containing all of zeros is the same size as label size.
    explode = np.zeros(label.size)

    # can config with e.g.
    # - explode[3] = 0.1
    # - explode[np.where(label == 'China')] = .1

    explode[np.where(label == 'China')] = .1

    # config colors of ecah part, orderd by label array
    colors = ["red", "green", "yellow", "brown", "purple"]

    plt.pie(n, labels=label, startangle=90, autopct="%.2f%%", explode=explode, colors=colors, shadow=True)
    

    plt.axis("equal")
    plt.title("The number of tourists of various nations", fontsize=16)
    plt.show()

if __name__ == "__main__":
    advanced_pie()
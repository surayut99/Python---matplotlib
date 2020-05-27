import matplotlib.pyplot as plt

# parameter is data on Y
# plt.plot([1 ,3 ,4, 7])

# first list is data on X, second list is data on Y.
# plt.plot([1 ,3 , 4, 7], [25, 24 ,12, 13])

# dot graph
# including third parameter as "o", it will show a dot graph.

# pre-fix e.g. r, g, k etc. (r is red, g is green, k is black)
# post-fix e.g. -, (- is including line connecting between two dots)
# can plot one more than a graph

plt.plot([1, 3, 4, 7], [25, 24, 12, 13], "ro-")
plt.plot([1, 3, 4, 7], [11, 4, 23, 16], "bo-")
plt.plot([1, 3, 4, 7], [22, 7, 13, 18], "go-")

plt.show()

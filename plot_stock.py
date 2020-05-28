import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data


def call_stocks():
    s = ["SCC.BK", "PTT.BK", "bbl.bk", "aot.bk", "bh.bk", "kbank.bk"]
    fig, ax = plt.subplots(3, 2)
    stocks = np.array(s).reshape(ax.shape)

    start_dt = "2017-1-1"
    end_dt = "2017-1-31"

    for r in range(ax.shape[0]):
        for c in range(ax.shape[1]):
            df = data.DataReader(
                stocks[r, c], data_source="yahoo", start=start_dt, end=end_dt)
            # print(df)

            ax[r, c].set_title(stocks[r, c])
            ax[r, c].plot(df["Adj Close"])
            ax[r, c].tick_params(axis="both", which="major", labelsize=8)

            # spines are border of frame
            ax[r, c].spines["left"].set_color(".8")
            ax[r, c].spines["bottom"].set_color(".8")
            ax[r, c].spines["right"].set_color("1")
            ax[r, c].spines["top"].set_color("1")

    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()


if __name__ == "__main__":
    call_stocks()

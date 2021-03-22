import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

data = pd.read_csv("statistics.csv")

for fl in tqdm(range(285,375,10)):
    plt.figure()
    plt.hist(data.Altitude / 100, bins=[0, fl, 660])
    plt.xlabel('Cruising Level [FL]')
    plt.ylabel('Number of flight plans')
    plt.title("F{}".format(fl))
    plt.savefig("F{}.png".format(fl))

#plt.show()
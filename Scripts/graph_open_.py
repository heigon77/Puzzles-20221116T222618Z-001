# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv('Puzzles/MinimixaxClassicalDepth3.csv')

data = {}

for idx, row in df.iterrows():
    if row['Solved'] is True and row['OpeningFamily'] != "nan":
        print(row['OpeningFamily'], "nan")
        if row['OpeningFamily'] in data :
            data[row['OpeningFamily'] ] += 1
        else:
            data[row['OpeningFamily'] ] = 1
        
print(data)
def addlabels(x,y,axs):
    for i in range(len(x)):
        axs.text(i, y[i], y[i], ha = 'center', fontsize=20)


names = list(data.keys())
values = list(data.values())
plt.bar(range(len(data)), values, tick_label=names)
plt.title('2500+', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(names, values, plt)


# Chamamos o método show() para mostrar o gráfico na tela
# plt.show()

def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()

filename = "LichessBars.pdf"
save_multi_image(filename)
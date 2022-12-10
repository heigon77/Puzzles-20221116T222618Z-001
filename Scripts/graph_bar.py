# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

# Minimax
solved = [47.13,34.27,46.72,30.66,21.72,45.27,23.85,11.80,64.16]
solved_1200 = [89.62,74.00,84.89,66.35,59.41,84.03,45.37,20.00,93.88]
solved_1800 = [77.48,62.14,65.28,43.55,37.86,63.78,30.28,24.00,86.08]
solved_2200 = [33.98,22.73,44.72,31.06,17.89,35.65,25.00,11.30,56.36]
solved_2500 = [19.80,14.02,17.46,14.57,7.19,16.50,11.01,6.14,32.00]
solved_high = [9.90,3.60,9.26,9.42,1.99,7.77,8.62,0.82,12.00]

# Lichess
# solved = [27.39,19.02,27.97,15.10,10.21,32.43,19.26,12.52,42.47]
# solved_1200 = [49.06,43.00,55.40,44.23,37.62,65.97,45.37,34.00,61.22]
# solved_1800 = [46.85,27.18,29.86,20.16,13.59,47.24,28.44,22.00,62.03]
# solved_2200 = [17.48,18.18,25.20,9.09,4.07,16.52,11.29,7.83,36.36]
# solved_2500 = [13.86,7.48,17.46,5.30,2.88,11.65,5.50,1.75,14.00]
# solved_high = [6.93,1.80,5.56,5.07,1.32,5.83,7.76,1.64,10.00]

# Computer
# solved = [20.69,13.37,25.63,15.87,9.56,33.45,17.31,11.07,32.53]
# solved_1200 = [39.62,25.00,53.96,34.62,33.66,57.64,40.74,32.00,46.94]
# solved_1800 = [34.23,20.39,29.86,25.81,9.71,40.94,21.10,19.00,48.10]
# solved_2200 = [13.59,12.73,17.07,16.67,4.88,28.70,12.90,5.22,21.82]
# solved_2500 = [6.93,3.74,14.29,5.96,5.04,14.56,11.01,2.63,14.00]
# solved_high = [6.93,6.31,6.48,2.90,1.32,14.56,2.59,0.82,10.00]


temas = ["A.cur",
        "A.med",
        "M.cur",
        "M.med",
        "M.lon",
        "F.cur",
        "F.med",
        "F.lon",
        "Mate"
        ]

"""
    Chamamos o método bar que criará o gráfico de barra 
    passamos os argumentos que são: 
        - faixaEtaria como eixo x 
        - rende como eixo y
        - color para as cores das barras como red ( vermelho )
"""

def addlabels(x,y,axs):
    for i in range(len(x)):
        axs.text(i, y[i], str(y[i])+' %', ha = 'center', fontsize=20)


sizex = 14
sizey = 8

fig1 = plt.figure()
fig1.set_size_inches(sizex, sizey)
plt.bar(temas, solved, color='red')
plt.title('Todos os problemas', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved, plt)
# plt.savefig("Imagens/MinimaxBarsTotal.pdf")

fig2 = plt.figure()
fig2.set_size_inches(sizex, sizey)
plt.bar(temas, solved_1200, color='cyan')
plt.title('0 a 1200', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_1200, plt)
# plt.savefig("Imagens/MinimaxBars1200.pdf")

fig3 = plt.figure()
fig3.set_size_inches(sizex, sizey)
plt.bar(temas, solved_1800, color='green')
plt.title('1200 a 1800', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_1800, plt)

fig4 = plt.figure()
fig4.set_size_inches(sizex, sizey)
plt.bar(temas, solved_2200, color='magenta')
plt.title('1800 a 2200', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_2200, plt)

fig5 = plt.figure()
fig5.set_size_inches(sizex, sizey)
plt.bar(temas, solved_2500, color='blue')
plt.title('2200 a 2500', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_2500, plt)

fig6 = plt.figure()
fig6.set_size_inches(sizex, sizey)
plt.bar(temas, solved_high, color='yellow')
plt.title('Acima de 2500', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_high, plt)


# Chamamos o método show() para mostrar o gráfico na tela
# plt.show()

def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()

# filename = "Imagens\ComputerBars.pdf"
# filename = "Imagens\LichessBars.pdf"
filename = "Imagens\MinimaxClassicalBars.pdf"
save_multi_image(filename)
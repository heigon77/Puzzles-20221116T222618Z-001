# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv('Puzzles/DeepChessLichessDepth3_200.csv')

solved = [0] * 12
solved_1200 = [0] * 12
solved_1800 = [0] * 12
solved_2200 = [0] * 12
solved_2500 = [0] * 12
solved_high = [0] * 12

for idx, row in df.iterrows():
    if row['Solved'] is True:
        if 'opening' in row['Themes']  and 'short' in row['Themes']:
            solved[0] += 1
            aux = 0

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'opening' in row['Themes']  and 'long' in row['Themes']:
            solved[1] += 1
            aux = 1

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'middlegame' in row['Themes']  and 'short' in row['Themes']:
            solved[2] += 1
            aux = 2

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'middlegame' in row['Themes']  and 'long' in row['Themes']:
            solved[3] += 1
            aux = 3

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'middlegame' in row['Themes']  and 'veryLong' in row['Themes']:
            solved[4] += 1
            aux = 4

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1


        if 'endgame' in row['Themes']  and 'short' in row['Themes']:
            solved[5] += 1
            aux = 5

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'endgame' in row['Themes']  and 'long' in row['Themes']:
            solved[6] += 1
            aux = 6

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'endgame' in row['Themes']  and 'veryLong' in row['Themes']:
            solved[7] += 1
            aux = 7

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1
        
        if 'mate' in row['Themes']:
            solved[8] += 1
            aux = 8

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'sacrifice' in row['Themes']:
            solved[9] += 1
            aux = 9

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'discoveredAttack' in row['Themes']:
            solved[10] += 1
            aux = 10

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1

        if 'fork' in row['Themes']:
            solved[11] += 1
            aux = 11

            if int(row['Rating']) <= 1200:
                solved_1200[aux] += 1
            elif int(row['Rating']) <= 1800:
                solved_1800[aux] += 1
            elif int(row['Rating']) <= 2200:
                solved_2200[aux] += 1
            elif int(row['Rating']) <= 2500:
                solved_2500[aux] += 1
            else:
                solved_high[aux] += 1




# Um gráfico com a renda média por faixa etária será nosso Hello World, vamos definir alguns valores fictícios
temas = ["Ab.cur",
        "Ab.med",
        "Mj.cur",
        "Mj.med",
        "Mj.lon",
        "Fj.cur",
        "Fj.med",
        "Fj.lon",

        "Mate",
        "Sac",
        "At.des",
        "At.dup"
        ]

# legenda = ["os: opening short",
#         "ol: opening long",
#         "ms: middlegame short",
#         "ml: middlegame long",
#         "mv: middlegame veryLong",
#         "es: endgame short",
#         "el: endgame long",
#         "ev: engame veryLong",

#         "mate: checkmate",
#         "sacr: sacrifice",
#         "disc: discoveredAtack",
#         "fork: fork"
#         ]

"""
    Chamamos o método bar que criará o gráfico de barra 
    passamos os argumentos que são: 
        - faixaEtaria como eixo x 
        - rende como eixo y
        - color para as cores das barras como red ( vermelho )
"""

def addlabels(x,y,axs):
    for i in range(len(x)):
        axs.text(i, y[i], y[i], ha = 'center', fontsize=20)

# fig, axs = plt.subplots(3, 2)

# axs[0, 0].bar(temas, solved, color='red')
# axs[0, 0].set_title('Total', fontsize=24)
# axs[0, 0].tick_params(labelsize=16)
# addlabels(temas, solved, axs[0, 0])

# axs[0, 1].bar(temas, solved_1200, color='cyan')
# axs[0, 1].set_title('1200', fontsize=20)
# axs[0, 1].tick_params(labelsize=16)
# addlabels(temas, solved_1200, axs[0, 1])

# axs[1, 0].bar(temas, solved_1800, color='green')
# axs[1, 0].set_title('1800', fontsize=20)
# axs[1, 0].tick_params(labelsize=16)
# addlabels(temas, solved_1800, axs[1, 0])

# axs[1, 1].bar(temas, solved_2200, color='magenta')
# axs[1, 1].set_title('2200', fontsize=20)
# axs[1, 1].tick_params(labelsize=16)
# addlabels(temas, solved_2200, axs[1, 1])

# axs[2, 0].bar(temas, solved_2500, color='blue')
# axs[2, 0].set_title('2500', fontsize=20)
# axs[2, 0].tick_params(labelsize=16)
# addlabels(temas, solved_2500, axs[2, 0])

# axs[2, 1].bar(temas, solved_high, color='yellow')
# axs[2, 1].set_title('2500+', fontsize=20)
# axs[2, 1].tick_params(labelsize=16)
# addlabels(temas, solved_high, axs[2, 1])


# fig.legend(legenda)
# fig.set_size_inches(30.0, 30.0)

fig1 = plt.figure()
fig1.set_size_inches(18.5, 10.5)
plt.bar(temas, solved, color='red')
plt.title('Total', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved, plt)
# plt.savefig("Imagens/MinimaxBarsTotal.pdf")

fig2 = plt.figure()
fig2.set_size_inches(18.5, 10.5)
plt.bar(temas, solved_1200, color='cyan')
plt.title('1200', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_1200, plt)
# plt.savefig("Imagens/MinimaxBars1200.pdf")

fig3 = plt.figure()
fig3.set_size_inches(18.5, 10.5)
plt.bar(temas, solved_1800, color='green')
plt.title('1800', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_1800, plt)

fig4 = plt.figure()
fig4.set_size_inches(18.5, 10.5)
plt.bar(temas, solved_2200, color='magenta')
plt.title('2200', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_2200, plt)

fig5 = plt.figure()
fig5.set_size_inches(18.5, 10.5)
plt.bar(temas, solved_2500, color='blue')
plt.title('2500', fontsize=32)
plt.tick_params(labelsize=22)
addlabels(temas, solved_2500, plt)

fig6 = plt.figure()
fig6.set_size_inches(18.5, 10.5)
plt.bar(temas, solved_high, color='yellow')
plt.title('2500+', fontsize=32)
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

filename = "LichessBars.pdf"
save_multi_image(filename)
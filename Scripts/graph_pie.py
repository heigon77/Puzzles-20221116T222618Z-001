# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Puzzles/DeepChessLichessDepth3.csv')

solved = [0] * 20
solved_1200 = [0] * 20
solved_1800 = [0] * 20
solved_2200 = [0] * 20
solved_2500 = [0] * 20
solved_high = [0] * 20

for idx, row in df.iterrows():
    if row['Solved'] is True:
        if 'crushing' in row['Themes'] and 'opening' in row['Themes']  and 'short' in row['Themes']:
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

        if 'crushing' in row['Themes'] and 'opening' in row['Themes']  and 'long' in row['Themes']:
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

        if 'crushing' in row['Themes'] and 'middlegame' in row['Themes']  and 'short' in row['Themes']:
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

        if 'crushing' in row['Themes'] and 'middlegame' in row['Themes']  and 'long' in row['Themes']:
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

        if 'crushing' in row['Themes'] and 'middlegame' in row['Themes']  and 'veryLong' in row['Themes']:
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


        if 'crushing' in row['Themes'] and 'endgame' in row['Themes']  and 'short' in row['Themes']:
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

        if 'crushing' in row['Themes'] and 'endgame' in row['Themes']  and 'long' in row['Themes']:
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

        if 'crushing' in row['Themes'] and 'endgame' in row['Themes']  and 'veryLong' in row['Themes']:
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

        ##

        if 'advantage' in row['Themes'] and 'opening' in row['Themes']  and 'short' in row['Themes']:
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

        if 'advantage' in row['Themes'] and 'opening' in row['Themes']  and 'long' in row['Themes']:
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

        if 'advantage' in row['Themes'] and 'middlegame' in row['Themes']  and 'short' in row['Themes']:
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

        if 'advantage' in row['Themes'] and 'middlegame' in row['Themes']  and 'long' in row['Themes']:
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

        if 'advantage' in row['Themes'] and 'middlegame' in row['Themes']  and 'veryLong' in row['Themes']:
            solved[12] += 1
            aux = 12

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


        if 'advantage' in row['Themes'] and 'endgame' in row['Themes']  and 'short' in row['Themes']:
            solved[13] += 1
            aux = 13

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

        if 'advantage' in row['Themes'] and 'endgame' in row['Themes']  and 'long' in row['Themes']:
            solved[14] += 1
            aux = 14

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

        if 'advantage' in row['Themes'] and 'endgame' in row['Themes']  and 'veryLong' in row['Themes']:
            solved[15] += 1
            aux = 15

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
            solved[16] += 1
            aux = 16

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
            solved[17] += 1
            aux = 17

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
            solved[18] += 1
            aux = 18

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
            solved[19] += 1
            aux = 19

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
temas = ["cos",
        "col",
        "cms",
        "cml",
        "cmv",
        "ces",
        "cel",
        "cev",

        "aos",
        "aol",
        "ams",
        "aml",
        "amv",
        "aes",
        "ael",
        "aev",

        "mate",
        "sacr",
        "disc",
        "fork"
        ]


renda = solved_high

"""
    Chamamos o método bar que criará o gráfico de barra 
    passamos os argumentos que são: 
        - faixaEtaria como eixo x 
        - rende como eixo y
        - color para as cores das barras como red ( vermelho )
"""

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct

fig, axs = plt.subplots(3, 2)

axs[0, 0].pie(solved, labels=temas, autopct=make_autopct(solved), radius=1)
axs[0, 0].set_title('Total')
axs[0, 0].axes.xaxis.set_ticklabels([])

axs[0, 1].pie(solved_1200, labels=temas, autopct=make_autopct(solved_1200), radius=1)
axs[0, 1].set_title('1200')
axs[0, 1].axes.xaxis.set_ticklabels([])

axs[1, 0].pie(solved_1800, labels=temas, autopct=make_autopct(solved_1800), radius=1)
axs[1, 0].set_title('1800')
axs[1, 0].axes.xaxis.set_ticklabels([])

axs[1, 1].pie(solved_2200, labels=temas, autopct=make_autopct(solved_2200), radius=1)
axs[1, 1].set_title('2200')
axs[1, 1].axes.xaxis.set_ticklabels([])

axs[2, 0].pie(solved_2500, labels=temas, autopct=make_autopct(solved_2500), radius=1)
axs[2, 0].set_title('2500')

axs[2, 1].pie(solved_high, labels=temas, autopct=make_autopct(solved_high), radius=1)
axs[2, 1].set_title('2500+')

legenda = ["cos: crushing opening short",
        "col: crushing opening long",
        "cms: crushing middlegame short",
        "cml: crushing middlegame long",
        "cmv: crushing middlegame veryLong",
        "ces: crushing endgame short",
        "cel: crushing endgame long",
        "cev: crushing engame veryLong",

        "aos: advantage opening short",
        "aol: advantage opening long",
        "ams: advantage middlegame short",
        "aml: advantage middlegame long",
        "amv: advantage middlegame veryLong",
        "aes: advantage endgame short",
        "ael: advantage endgame long",
        "aev: advantage endgame veryLong",

        "mate: checkmate",
        "sacr: sacrifice",
        "disc: discoveredAtack",
        "fork: fork"
        ]

fig.legend(legenda, loc="upper right")
# Chamamos o método show() para mostrar o gráfico na tela
plt.show()
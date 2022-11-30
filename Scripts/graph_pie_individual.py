# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Puzzles/DeepChessLichessDepth3.csv')

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
temas = ["os",
        "ol",
        "ms",
        "ml",
        "mv",
        "es",
        "el",
        "ev",

        "mate",
        "sacr",
        "disc",
        "fork"
        ]

legenda = ["os: opening short",
        "ol: opening long",
        "ms: middlegame short",
        "ml: middlegame long",
        "mv: middlegame veryLong",
        "es: endgame short",
        "el: endgame long",
        "ev: engame veryLong",

        "mate: checkmate",
        "sacr: sacrifice",
        "disc: discoveredAtack",
        "fork: fork"
        ]

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

plt.figure(0)
plt.pie(solved, labels=temas, autopct=make_autopct(solved))
plt.title('Total')
plt.legend(legenda, loc="upper right", bbox_to_anchor=(1.42, 1), fontsize=10)

plt.figure(1)
plt.pie(solved_1200, labels=temas, autopct=make_autopct(solved_1200))
plt.title('1200')
plt.legend(legenda, loc="upper right", bbox_to_anchor=(1.42, 1), fontsize=10)

plt.figure(2)
plt.pie(solved_1800, labels=temas, autopct=make_autopct(solved_1800))
plt.title('1800')
plt.legend(legenda, loc="upper right", bbox_to_anchor=(1.42, 1), fontsize=10)

plt.figure(3)
plt.pie(solved_2200, labels=temas, autopct=make_autopct(solved_2200))
plt.title('2200')
plt.legend(legenda, loc="upper right", bbox_to_anchor=(1.42, 1), fontsize=10)

plt.figure(4)
plt.pie(solved_2500, labels=temas, autopct=make_autopct(solved_2500))
plt.title('2500')
plt.legend(legenda, loc="upper right", bbox_to_anchor=(1.42, 1), fontsize=10)


plt.figure(5)
plt.pie(solved_high, labels=temas, autopct=make_autopct(solved_high))
plt.title('2500+')
plt.legend(legenda, loc="upper right", bbox_to_anchor=(1.42, 1), fontsize=10)



# Chamamos o método show() para mostrar o gráfico na tela
plt.show()
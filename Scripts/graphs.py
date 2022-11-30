# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt

def addlabels(x,y, bar):
    for i in range(len(x)):
        plt.text(i+bar, y[i], y[i], ha = 'center')

# Gráfico sobre notas de 3 alunos nas provas do semestre
deepchess_computer = [343, 645, 971]
deepchess_lichess = [313, 703, 1096]
minimax  = [487, 920, 1741]
 

# Definindo a largura das barras
barWidth = 0.2

# Aumentando o gráfico
plt.figure(figsize=(10,5))

# Definindo a posição das barras
r1 = np.arange(len(deepchess_computer))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Criando as barras
plt.bar(r1, deepchess_computer, color='yellow', width=barWidth, label='DeepChess Computer Chess')
addlabels(r1,deepchess_computer,0)
plt.bar(r2, deepchess_lichess, color='red', width=barWidth, label='DeepChess Lichess')
addlabels(r2,deepchess_lichess,barWidth)
plt.bar(r3, minimax, color='blue', width=barWidth, label='MiniMax')
addlabels(r3,minimax, 2*barWidth)
 
# Adiciando legendas as barras
plt.xlabel('Profundidades')
plt.xticks([r + barWidth for r in range(len(deepchess_computer))], ['Profundidade 1', 'Profundidade 2', 'Profundidade 3'])
plt.ylabel('Problemas solucionados')
plt.title('Representação das soluções das 3 ferramentas computacionais em 3 profundidades')
 
# Criando a legenda e exibindo o gráfico
plt.legend()
plt.savefig("Imagens/Comparacao.pdf")
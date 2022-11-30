# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Puzzles/outputsDBNlichessnormal.csv')

epoch = df['Epoch'].to_numpy()
loss = df['Loss'].to_numpy()


plt.plot(epoch, loss)
plt.title('MSE Loss x Epoch : Deep Belief Network')
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")


# fig.legend(legenda)
 
# Chamamos o método show() para mostrar o gráfico na tela
plt.show()
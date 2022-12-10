# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

# df = pd.read_csv('Puzzles\DeepChessComputerChessDepth3_200.csv')
# df = pd.read_csv('Puzzles\DeepChessLichessDepth3_200.csv')
df = pd.read_csv('Puzzles\MinimixaxClassicalDepth3.csv')


temas = {"Ab.cur":0,
        "Ab.med":0,
        "Mj.cur":0,
        "Mj.med":0,
        "Mj.lon":0,
        "Fj.cur":0,
        "Fj.med":0,
        "Fj.lon":0,
        "Mate":0
        }

sol = {"Ab.cur":0,
        "Ab.med":0,
        "Mj.cur":0,
        "Mj.med":0,
        "Mj.lon":0,
        "Fj.cur":0,
        "Fj.med":0,
        "Fj.lon":0,
        "Mate":0
        }

for idx, row in df.iterrows():
    if row['Rating'] > 1200 and row['Rating'] <= 1800 :
        if 'opening' in row['Themes']  and 'short' in row['Themes'] and 'mate' not in row['Themes']:
                temas["Ab.cur"] += 1

        elif 'opening' in row['Themes']  and 'mate' not in row['Themes']:
            temas["Ab.med"] += 1

        elif 'middlegame' in row['Themes']  and 'short' in row['Themes'] and 'mate' not in row['Themes']:
            temas["Mj.cur"] += 1 

        elif 'middlegame' in row['Themes']  and 'long' in row['Themes'] and 'mate' not in row['Themes']:
            temas["Mj.med"] += 1

        elif 'middlegame' in row['Themes']  and 'veryLong' in row['Themes'] and 'mate' not in row['Themes']:
            temas["Mj.lon"] += 1


        elif 'endgame' in row['Themes']  and 'short' in row['Themes'] and 'mate' not in row['Themes']:
            temas["Fj.cur"] += 1

        elif 'endgame' in row['Themes']  and 'long' in row['Themes'] and 'mate' not in row['Themes']:
            temas["Fj.med"] += 1

        elif 'endgame' in row['Themes']  and 'veryLong' in row['Themes'] and 'mate' not in row['Themes']:
            temas["Fj.lon"] += 1
        
        elif 'mate' in row['Themes']:
            temas["Mate"] += 1

        if row['Solved'] is True:
            if 'opening' in row['Themes']  and 'short' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Ab.cur"] += 1

            elif 'opening' in row['Themes']  and 'long' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Ab.med"] += 1

            elif 'middlegame' in row['Themes']  and 'short' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Mj.cur"] += 1 

            elif 'middlegame' in row['Themes']  and 'long' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Mj.med"] += 1

            elif 'middlegame' in row['Themes']  and 'veryLong' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Mj.lon"] += 1


            elif 'endgame' in row['Themes']  and 'short' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Fj.cur"] += 1

            elif 'endgame' in row['Themes']  and 'long' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Fj.med"] += 1

            elif 'endgame' in row['Themes']  and 'veryLong' in row['Themes'] and 'mate' not in row['Themes']:
                sol["Fj.lon"] += 1
            
            elif 'mate' in row['Themes']:
                sol["Mate"] += 1

print("Temas")
print(temas)

print("Resolvidos")
print(sol)
# Primeiramente importamos as libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv('Puzzles/MinimixaxClassicalDepth3.csv')

rat = {"1200":0,
        "1800":0,
        "2200":0,
        "2500":0,
        "2500+":0,
        }

sol = {"1200":0,
        "1800":0,
        "2200":0,
        "2500":0,
        "2500+":0,
        }

for idx, row in df.iterrows():
    if row['Rating'] <= 1200:
        rat["1200"] += 1
    elif row['Rating'] <= 1800:
        rat["1800"] += 1
    elif row['Rating'] <= 2200:
        rat["2200"] += 1
    elif row['Rating'] <= 2500:
        rat["2500"] += 1
    else:
        rat["2500+"] += 1

    if row['Solved'] is True:
        if row['Rating'] <= 1200:
            sol["1200"] += 1
        elif row['Rating'] <= 1800:
            sol["1800"] += 1
        elif row['Rating'] <= 2200:
            sol["2200"] += 1
        elif row['Rating'] <= 2500:
            sol["2500"] += 1
        else:
            sol["2500+"] += 1



print("Temas")
print(rat)

print("Resolvidos")
print(sol)
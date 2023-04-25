import os
import pandas as pd

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'enemies.csv')
df = pd.read_csv(filename)
print(df.dropna().to_string()) 
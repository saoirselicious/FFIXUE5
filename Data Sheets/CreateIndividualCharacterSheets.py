import json
import pandas as pd
import glob
import os
 
def my_function(char):
    df = pd.read_csv(filename, index_col=None, header=0);
    currentStat = filename.replace("C:\\Users\\Saoirse\\Documents\\Unreal Projects\\Final_Fantasy_IX\\Data Sheets\\",'').replace(" Growth.csv", "")
    charExport[currentStat] = df[char]


ospath = r'C:\Users\Saoirse\Documents\Unreal Projects\Final_Fantasy_IX\Data Sheets' # use your path
all_files = glob.glob(os.path.join(ospath , "*.csv"))

allChar = ["Zidane", "Dagger", "Steiner", "Amarant", "Quina", "Eiko", "Vivi", "Freya"]

for sel in allChar:
    print(sel)
    charExport = pd.DataFrame()
    charExport["---"] = list(range(1,100))
    for filename in all_files:
        my_function(sel)
    
    newFileName  = ""
    newFileName = ospath + "\\CharacterStats\\" + sel + "Statsheet.csv"
    charExport.to_csv(newFileName, index=False)
    



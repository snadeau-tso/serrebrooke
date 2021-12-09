# @file ClientSerrePi_JSON.py
# @date Octobre 2021
# @brief Fichier de code le Client 

## importations des librairies
import json
from ttLecture_ds18b20 import data
from atlas.tempAtlasOEM_C_DO import adrPH

def main():    
        while True: 
                filename = '/home/serrepi/src/serrebrooke/test/json/dataCapteurs.json'
                with open(filename,'w') as outfile:
                        json.dump(data, outfile)

if __name__ == '__main__':
    main()  

# @file ClientSerrePi_JSON.py
# @date Octobre 2021
# @brief Fichier de code le Client 

## importations des librairies
import json
import ttLecture_ds18b20

data = ttLecture_ds18b20.stringExport

filename = '/home/serrepi/src/test/dataCapteurs.json'

with open(filename,'w') as outfile:
    json.dumps(data, outfile)
    

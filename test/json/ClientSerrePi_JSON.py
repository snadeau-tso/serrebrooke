# @file ClientSerrePi_JSON.py
# @date Octobre 2021
# @brief Fichier de code le Client 

## importations des librairies
import json
import ttLecture_ds18b20

print(ttLecture_ds18b20.data)  

filename = 'dataCapteurs.json'

with open(filename,'w') as outfile:
    json.dumps(ttLecture_ds18b20.data, outfile)
    

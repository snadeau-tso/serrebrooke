# @file ClientSerrePi_JSON.py
# @date Octobre 2021
# @brief Fichier de code le Client 

## importations des librairies
import json
from test.atlas import testAtlasOEM
from ttLecture_ds18b20 import data

#data2 = testAtlasOEM.lecturePH


filename = '/home/serrepi/src/serrebrooke/test/json/dataCapteurs.json'

with open(filename,'w') as outfile:
    json.dump(data, outfile)    

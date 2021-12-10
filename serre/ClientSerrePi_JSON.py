# @file ClientSerrePi_JSON.py
# @date Octobre 2021
# @brief Fichier de code le Client 

## importations des librairies
import json
from lecture_ds18b20 import m_data


def dumpJSON():
        filename = '/home/serrepi/src/serrebrooke/serre/dataCapteurs.json'
        with open(filename,'w') as outfile:
                json.dump(m_data, outfile)        
        
        
def main():    
        while True: 
                filename = '/home/serrepi/src/serrebrooke/serre/dataCapteurs.json'
                with open(filename,'w') as outfile:
                        json.dump(m_data, outfile)

if __name__ == '__main__':
    main()  

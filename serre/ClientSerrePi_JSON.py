# @file ClientSerrePi_JSON.py
# @date Octobre 2021
# @brief Client pour populer un fichier JSON avec les valeurs des capteurs. L'envoie des données sur le web reste à être fait.    

## importations des librairies
import json
from lecture_ds18b20 import m_dataDS18B20

m_filename = '/home/serrepi/src/serrebrooke/serre/dataCapteurs.json'#Chemin du fichier JSON

def dumpJSON():
        with open(m_filename,'w') as outfile: 
                json.dump(m_dataDS18B20, outfile) #Écriture des données dans le fichier JSON       
        
        
def main():    
        while True: 
                with open(m_filename,'w') as outfile:
                        json.dump(m_dataDS18B20, outfile)

if __name__ == '__main__':
    main()  

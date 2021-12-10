""" @file   lecture_ds18b20.py
    @date   Décembre 2021
    @brief  Fichier pour la lecture des capteurs DS18B20. Les données
"""

## importations des librairies
import os
import glob
import time
 
## initialiation des pins GPIO
os.system('modprobe w1-gpio') # active le module GPIO
os.system('modprobe w1-therm') # active le module température
 
## définitions des fichiers qui contiennent les valeurs de température
m_devicesPath = '/sys/bus/w1/devices/' # répertoire pour les id des capteurs
m_lstDevicesFolder = glob.glob(m_devicesPath + '28*') # liste tous les capteurs DS18B20
m_dataDS18B20 = {}
m_dataDS18B20['CapteurDS18B20'] = []
# liste un seul capteur (pour debug)
#m_deviceFile = m_lstDevicesFolder[0] + '/w1_slave' # fichier slave du capteur ciblé avec la valeur de température

# liste tous les chemins compatibles au directory (dossiers des capteurs DS18B20)
m_lstDevicesFile = [] # liste dynamique pour les capteurs 
# pour chaque capteur de disponible...
for device in m_lstDevicesFolder:
    m_lstDevicesFile.append(device + '/w1_slave')   # ajoute à la liste le fichier slave du capteur
                                                    # fichier avec les éléments de température et ...


def read_temp_raw(capteur:str):
    ''' @brief  Permet d'ouvrir un fichier ciblé et de lire son contenu.
        @param  capteur : (string) Chemin du fichier ciblé
        @return Retourne les lignes extraites du fichier.
    '''
    # récupère les valeurs du fichier slave du capteur
    f = open(capteur, 'r') # ouvre le fichier
    lines = f.readlines() # récupère les lignes du fichier ouvert
    f.close() # ferme le fichier
    return lines
 
def read_temp(capteur:str):
    ''' @brief  Permet de lire la valeur de température du capteur DS18B20 ciblé.
        @param  capteur : (string) Chemin du fichier ciblé
        @return Retourne la température en degrés celcius
    '''
    lines = read_temp_raw(capteur) # lecture du fichier, appel la fonction

    # pendant que le crc est différent de YES??
    while lines[0].strip()[-3:] != 'YES': 
        time.sleep(0.2)
        lines = read_temp_raw() # relit la valeur slave

    # trouve la position de la température
    equals_pos = lines[1].find('t=') # find() retourne -1 si inexistant
    
    if equals_pos != -1: # si trouvé?
        # lit le reste de la ligne à partir de la suite de la position
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0    # conversion des degrés en celcius
        return temp_c

def pollLectureDS18B20():
    ''' Permet de faire la lecture des capteurs DS18B20 à partir d'une
        classe.
    '''
    
    # pour chaque capteur de disponible, on prend sa mesure
    # et on l'affiche au terminal.
    for device in m_lstDevicesFile:
        posID:int = str(device).find('28')
        # affiche le id du capteur et sa valeur
        print("Capteur " + str(device[posID:-9]) + ": " + str(read_temp(device)))
        m_dataDS18B20['CapteurDS18B20'].append({
        'ID': str(device[posID:-9]),
        'Temperature': str(read_temp(device)),
        }) 
    
    # formatte la sorie au terminal et boucle à l'infinie (pour debug)
    print("--------------------------------\n")
    #time.sleep(2)

def main():
    # Boucle princiaple
    data = {}
    data['CapteurDS18B20'] = []
    
    while True:
        # pour chaque capteur de disponible, on prend sa mesure
        # et on l'affiche au terminal.
        for device in m_lstDevicesFile:
            posID:int = str(device).find('28')
            # affiche le id du capteur et sa valeur
            print("Capteur " + str(device[posID:-9]) + ": " + str(read_temp(device)))
            m_dataDS18B20['CapteurDS18B20'].append({
                'ID': str(device[posID:-9]),
                 'Temperature': str(read_temp(device)),
             })       
    
        # formatte la sorie au terminal et boucle à l'infinie (pour debug)
        print("\n--------------------------------\n")
        time.sleep(2)

# Point d'entrée du programme 
if __name__ == '__main__':
    main()

    
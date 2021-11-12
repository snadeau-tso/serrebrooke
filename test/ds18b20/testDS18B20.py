# @file testDS18B20.py
# @date Octobre 2021
# @brief Fichier de code pour un exemple de lecture des capteurs DS18B20.

# importations des librairies
import os
import glob
import time
 
# initialiation des pins GPIO
os.system('modprobe w1-gpio') # active le module GPIO
os.system('modprobe w1-therm') # active le module température
 
# définitions des fichiers qui contiennent les valeurs de température
base_dir = '/sys/bus/w1/devices/' # dir pour les id des capteurs
device_folder = glob.glob(base_dir + '28*')[0] # dossier du capteur
device_file = device_folder + '/w1_slave' # fichier du capteur

# @fonction read_temp_raw
# @brief Permet d'ouvrir un fichier ciblé et de lire son contenu.
def read_temp_raw():
    f = open(device_file, 'r') # ouvre le fichier
    lines = f.readlines() # récupère les lignes du fichier ouvert
    f.close() # ferme le fichier
    return lines
 
# @fonction read_temp 
# @brief Permet de lire la valeur de température du capteur DS18B20
#        ciblé.
def read_temp():
    lines = read_temp_raw() # lecture du fichier
    
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    # trouve la position de la température
    equals_pos = lines[1].find('t=')
    # si existe?
    if equals_pos != -1:
        # lit le reste de la ligne à partir de la suite des caractères trouvés
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0    # conversion des degrés en celcius
        #temp_f = temp_c * 9.0 / 5.0 + 32.0     # conversion des degrés en farahneit
        # retourne la valeur de/des température(s)
        return temp_c # , temp_f #(Température oF)
	
# point d'entrée du programme
while True:
	print(read_temp()) # affiche la valeur de température au terminal	
	time.sleep(1) # loop aux secondes
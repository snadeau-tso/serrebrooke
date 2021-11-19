'''
@file   tempAtlasOEM_C_DO.py
@name   Samuel Nadeau
@date   Novembre 2021
@brief  Fichier python pour exécuter le code source pour la lecture des capteurs OEM
        Atlas Scientific. Les capteurs sont pour les mesures du PH, Oxygène dissout
        et Conductivité. Le protocole utilisé pour la lecture est le I2C. On utilise
        les fichiers de librairie Atlas <python_AtlasOEM_lib> récupéré sur github. Le
        code est basé sur l'exemple source d'Atlas. Une copie de la licence doit 
        être présente avec les librairies pour respecter les droits.
'''

# importation des librairies Atlas OEM pour la création des objets capteurs.
from lib.AtlasOEM_PH import AtlasOEM_PH 
from lib.AtlasOEM_DO import AtlasOEM_DO 
from lib.AtlasOEM_EC import AtlasOEM_EC 

import time # lib pour fonction sleep

# constantes adresses i2c pour les capteurs OEM Atlas
adrPH = 0x63 # adresse pour le module PH
adrDO = 0x64 # adresse pour le module DO
adrEC = 0x65 # adresse pour le module EC

def lecturePH(objPH:AtlasOEM_PH):
    ''' Permet de récupérer la valeur du capteur OEM de PH.
        Retourne l'objet pour récupérer les données
    '''
    pH_reading = objPH.read_PH_reading()            # get it from the circuit
    print("OEM pH reading: " + str(pH_reading))  # print the reading
    objPH.write_new_reading_available(0)   # then clear the new reading register 
                                        # so the circuit can set the register
                                        # high again when it acquires a new reading
    return objPH

def lectureDO(objDO:AtlasOEM_DO):
    ''' Permet de récupérer la valeur du capteur OEM de PH.
        Retourne l'objet pour récupérer les données
    '''
    do_reading = objDO.read_DO_reading()            # get it from the circuit
    print("OEM do reading: " + str(do_reading))  # print the reading
    objDO.write_new_reading_available(0)   # then clear the new reading register 
                                        # so the circuit can set the register
                                        # high again when it acquires a new reading
    return objDO

'''
def lectureEC(objPH:AtlasOEM_PH):
    ''' '''Permet de récupérer la valeur du capteur OEM de PH.
        Retourne l'objet pour récupérer les données
    ''' '''
    pH_reading = objPH.read_PH_reading()            # get it from the circuit
    print("OEM pH reading: " + str(pH_reading))  # print the reading
    objPH.write_new_reading_available(0)   # then clear the new reading register 
                                        # so the circuit can set the register
                                        # high again when it acquires a new reading
    return objPH
'''


def main():
    ''' Fonction main qui permet d'effectuer des lectures des capteurs OEM.
        Crée aussi les objets requis.
    ''' 
    
    ''' Passe en paramètre l'adresse du capteur et un nom pour l'identifier.
        Sinon, ce sont les valeurs prises par défaut qui sont configurées.  ''' 
    PH = AtlasOEM_PH(adrPH, 'OEM PH') # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

    while True:
        if PH.read_new_reading_available():              # if we have a new PH reading
            lecturePH(PH)   # lit la valeur du capteur
                            # passe en référence l'objet PH
        else:
            print("waiting for reading...")
            time.sleep(.5)                      #if theres no reading, wait some time to not poll excessively
        
        time.sleep(2) # délai pour ralentir la requête des lectures (pour debug)
        
''' Point d'entrée principale du fichier. Vérifie si c'est le fichier main, sinon défini seulement 
    les fonctions requises.
'''
if __name__ == '__main__':
    main()
'''
@file   testAtlasOEM.py
@name   Samuel Nadeau
@date   Novembre 2021
@brief  Fichier python pour exécuter le code source pour la lecture des capteurs OEM
        Atlas Scientific. Les capteurs sont pour les mesures du PH, Oxygène dissout
        et Conductivité. Le protocole utilisé pour la lecture est le I2C. On utilise
        les fichiers de librairie Atlas <python_AtlasOEM_lib> récupéré sur github.
'''

from lib.AtlasOEM_PH import AtlasOEM_PH

import time

def main(): 
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

    while True:
        if PH.read_new_reading_available():              # if we have a new reading
            pH_reading = PH.read_PH_reading()            # get it from the circuit
            print("OEM pH reading: " + str(pH_reading))  # print the reading
            PH.write_new_reading_available(0)   # then clear the new reading register 
                                                # so the circuit can set the register
                                                # high again when it acquires a new reading
        else:
            print("waiting for reading...")
            time.sleep(.5)                      #if theres no reading, wait some time to not poll excessively
        
if __name__ == '__main__':
    main()
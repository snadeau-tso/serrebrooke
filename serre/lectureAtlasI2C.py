#!/usr/bin/python

''' @file   lectureAtlasI2C.py
    @date   Décembre 2021
    @brief  Fichier pour la lecture des capteurs Atlas(DO,ORP,PH)
'''

import io
import sys
import fcntl
import time
import copy
import string
from lib.AtlasI2C import (AtlasI2C) # librairie pour les focntions des capteurs Atlas.

DELAYTIME = float(2) # const pour gérer le délai des lectures en des capteurs

def print_devices(device_list, device):
    ''' @brief  Permet d'afficher les capteurs connectés au terminal.
        @param  device_list (Liste des capteurs récupérés)
        @param  device (Pointeur de début pour la liste)
    '''
    # Boucle pour les afficher au terminal
    for i in device_list:
        if(i == device):
            print("--> " + i.get_device_info())
        else:
            print(" - " + i.get_device_info())
    #print("")
    
def get_devices():
    ''' @brief  Permet de récupérer tous les capteurs connectés sur bus I2C
                et les liste dans la variable liste.
    '''
    device = AtlasI2C()
    device_address_list = device.list_i2c_devices()
    device_list = []
    
    for i in device_address_list:
        device.set_i2c_address(i)
        response = device.query("I")
        moduletype = response.split(",")[1] 
        response = device.query("name,?").split(",")[1]
        device_list.append(AtlasI2C(address = i, moduletype = moduletype, name = response))
    return device_list 

def pollAtlas():
    ''' Permet d'effectuer les lectures des capteurs Atlas 
        à partir d'une autre classe.
    '''
    lstJSON:str = []
    device_list = get_devices()
    
    # liste la commande de lecture pour tous les capteurs
    for dev in device_list:
        dev.write("R")
    
    time.sleep(DELAYTIME) # délai pour attente
    
    # liste les lectures pour tous les capteurs
    # et les ajoutent à la liste JSON
    for dev in device_list:
        print(dev.read())
        #lstJSON.append()
        
    return lstJSON

def main():
    
    device_list = get_devices()
        
    device = device_list[0]
    
    print_devices(device_list, device)
    
    delaytime = float(2)
    
    # test fonction pollAtlas()
    print("Test pollAtlas()\n" + str(pollAtlas()))
    
    try:
        while True:
            print("-------press ctrl-c to stop the polling")
            for dev in device_list:
                dev.write("R")
            time.sleep(delaytime)
            for dev in device_list:
                print(dev.read())
        
    except KeyboardInterrupt:       # catches the ctrl-c command, which breaks the loop above
        print("Continuous polling stopped")
        print_devices(device_list, device)
    
        
if __name__ == '__main__':
    main()
''' @file   lectureCapteurs.py
    @date   Décembre 2021
    @brief  Fichier pour la lecture des capteurs Atlas et 1-Wire, on les affiche 
            sur le terminal.
'''

import lecture_ds18b20
import lectureAtlasI2C


def main():
    # Boucle principale
    while(1):
        lecture_ds18b20.pollLectureDS18B20() # lecture des capteurs 1-Wire et print au terminal
        lectureAtlasI2C.pollAtlas() # lecture des capteurs Atlas et print au terminal

# Point d'entrée du programme
if __name__ == '__main__':
    main()
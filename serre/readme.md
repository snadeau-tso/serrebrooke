# Serrebrooke
Système d'acquisitions qui permet la lecture des différents capteurs (DS18B20, Atlas Scientific) et l'écriture dans un fichier JSON (DS18B20).

Les capteurs Atlas présents sont :
- PH
- DO (Oxygène dissout) 
- ORP (Potentiel oxydo-réduction)

On utilise un Rasperry Pi 3B+ comme système.

## Configurations RPI
Le Raspberry Pi est configuré en mode RaspbianOS Headless. La connexion se fait donc principalement
à l'aide d'un écran et d'un clavier pour une connexion directe, sinon la méthode principale est par
connexion à distance SSH.

L'édition des codes se fait par l'IDE VS Code par l'extension Remote-SSH.

Les packages installés pour la configuration du pi sont :
- activation du I2C tools
- configuration du timesync NTP
- packages :
    - i2c-tools;
    - python-smbus;
    - python3-smbus;
    - python-dev;
    - python3-dev.

### Connexion SSH
Pour accéder au pi, il faut utiliser les informations suivantes:
- Hostname : serrepi
- User : serrepi
- Password : serrebrooke

## L'exécution du code
Pour exécuter le code, il faut exécuter le fichier lectureCapteurs.py. C'est le fichier principal qui permet la 
lecture des différents types de capteurs et l'écriture des données dans le fichier JSON par l'appel de fonctions.

## Description des fichiers sources
- lectureCapteurs.py :    Permet la lecture des différents types de capteurs.
- lecture_ds18b20.py :    Permet de faire la lecture des capteurs de type DS18B20 disponibles. Écrit les valeurs dans 
                          une liste (data) pour la récupération vers le fichier JSON.
- lectureAtlasI2C.py :    Permet la lecture des capteurs EZO d'Atlas Scientific. Utilise les librairies officielles
                          d'Atlas (IMPORTANT : il doit y avoir la licence).
- ClientSerrePiJSON.py :  Permet la récupération de la liste data pour écrite les données dans le fichier JSON dataCapteurs.json.
- dataCapteurs.json :     Fichier des données JSON.

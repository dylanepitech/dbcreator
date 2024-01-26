import os   
import mysql.connector
import time

os.system('clear')

# Définition des codes de couleur
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BOLD = "\033[1m"

#fonction creation de db si fichier non créer
def creator():
    print(YELLOW+ BOLD+ 'Bonjour, bienvenu dans le creator de database')
    print('')
    print("Je vais vous poser quelques question concernant votre base de donner. (Rien ne seras enregistrer)")

    # Récupération des information
    DB_HOST = input(YELLOW + BOLD +'Quelle est votre Host ? (127.0.0.1 ou localhost par default):' + RESET)
    DB_NAME = input(YELLOW + BOLD + 'Quelle est votre Identifiant (root par défault):' + RESET)
    DB_PASSWORD = input(YELLOW + BOLD + 'Quell est votre mot de passe ? (aucun ou root par default): ' + RESET)
    DB_PORT = input(YELLOW + BOLD + 'Quell est votre PORT ? (8889 ou 3000 par default): ' + RESET)
    #Connection a la base de donner
    try:
        con = mysql.connector.connect(host=DB_HOST,user=DB_NAME,password=DB_PASSWORD,port=DB_PORT)
        cursor = con.cursor()
        print(GREEN + BOLD+ 'Connexion avec succès !' + RESET)
    except mysql.connector.Error as err:
        print(RED + BOLD +"Erreur lors de la connexion à la base de données MySQL :" + RESET)
        print(RED+ BOLD +"Merci d'avoir utiliser creatordb" + RESET)
        time.sleep(3)
        os.system('clear')
        exit(1)

    with open('.bd.txt', 'w') as f:
        f.write(DB_HOST)
        f.write("\n")
        f.write(DB_NAME)
        f.write("\n")
        f.write(DB_PASSWORD)
        f.write("\n")
        f.write(DB_PORT)
        f.write("\n")
    exit(1)



try:
    with open('.bd.txt', 'r') as r:
       contenu =  r.readlines()
       DB_HOST = contenu[0].strip()
       DB_NAME = contenu[1].strip()
       DB_PASSWORD = contenu[2].strip()
       DB_PORT = contenu[3].strip()
except FileNotFoundError:
    creator()
    exit(1)
    
try:
    con = mysql.connector.connect(host=DB_HOST,user=DB_NAME,password=DB_PASSWORD,port=DB_PORT)
    cursor = con.cursor()
    print(GREEN + BOLD+ 'Connexion avec succès !' + RESET)
except mysql.connector.Error as err:
    print('erreur de connexion')
    exit(1)
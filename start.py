import time
import sys
import os

os.system("cls")

print("Chargement...")

os.system("cls")

yes = input("Vous êtes sûr de vouloir continuer ? (y/n) : ")
if yes == "y":
  print("Installation / Vérification des modules...")
  os.system("pip install -r requirement.txt")
  os.system("npm install mineflayer")
  os.system("cd Files")
  os.system("python main.py")
elif yes=="n":
  print("Veuillez fermez le programme !")
else:
  print("Choix invalide !")

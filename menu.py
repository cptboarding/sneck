# -*- coding: utf-8 -*-
"""Exemple d'utilisation de curses.
 menu du jeu sneck  qui permet d'afficher les differentes options play ,quitter et options. 
"""
""" Installation :
pip install windows-curses 
pip install curses-menu
lancer prog : python J:\Informatique\infoOC\sneck\menu.py """

from jeu_snake import programme 
import subprocess
import sys
import curses

def play_game():
    curses.wrapper(programme)
    """ chemin_script = r"J:\Informatique\infoOC\sneck\jeu_snake.py"
    print(">>> Lancement du jeu en externe...")
    result = subprocess.run([sys.executable, chemin_script])
    print(">>> Jeu terminé avec code retour:", result.returncode)
    input("Appuyez sur Entrée pour revenir au menu...")"""

def show_options():
    print("Options du jeu :")
    print("1. Mode de base jeu sneck classique avec pomme")
    print("2. Mode medium (mur en mouvement)")
    print("3. Mode hardcore (mur en mouvement et pomme qui se tp en touchant le mur)")
    input("Appuyez sur Entrée pour continuer...")

def quit_game():
    print("Quitter le jeu...")
    sys.exit()

def main():
    while True:
        print("\n--- Menu Sneck Game ---")
        print("1. Jouer")
        print("2. Options")
        print("3. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            play_game()
        elif choix == "2":
            show_options()
        elif choix == "3":
            quit_game()
        else:
            print("Choix invalide, réessayez.")

if __name__ == "__main__":
    main()




















# -*- coding: utf-8 -*-
"""Exemple d'utilisation de curses.
jeu snake 
"""
""" Installation :
pip install windows-curses 
pip install curses-menu
lancer prog : python J:\Documents\infoOC\snake.py """


from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem

def play_game():
    print("Le jeu commence...")
    input("Appuyez sur Entrée pour continuer...")  # Pour éviter la fermeture immédiate

def show_options():
    print("Options du jeu :")
    print("1. Mode de jeu")
    print("2. Commandes")
    print("3. Retour au menu principal")
    input("Appuyez sur Entrée pour continuer...")

def quit_game():
    print("Quitter le jeu...")
    exit()

def main():
    menu = CursesMenu("Snake Game", "Utilisez les flèches pour naviguer")
    
    # Création des items avec la méthode correcte
    play_item = FunctionItem("Jouer", play_game, menu)
    options_item = FunctionItem("Options", show_options, menu)
    quit_item = FunctionItem("Quitter", quit_game, menu)
    
    # Ajout des items au menu
    menu.items.append(play_item)
    menu.items.append(options_item)
    menu.items.append(quit_item)
    
    menu.show()

if __name__ == "__main__":
    main()
























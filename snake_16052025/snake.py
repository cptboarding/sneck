"""
python "J:\Documents\Informatique\3ème année\Projet 2ème semestre\snake.py"
hauteur, longueur = console.getmaxyx()
"""

import curses
import random
import time

from coordonnees_snake import personnage

RIEN = " "
PERSONNAGE = "@"
CLONE = "#"
BORDER = "-"


def debut(console):
    console.clear()
    curses.curs_set(False)
    console.refresh()


def afficher(console, texte, y_texte, x_texte, temps=5):
    """Affiche du texte"""
    for lettre in texte:
        console.addstr(y_texte, x_texte, lettre)
        x_texte = x_texte+1
    console.getkey()
    for lettre in texte:
        x_texte = x_texte-1
    for lettre in texte:
        console.addstr(y_texte, x_texte, RIEN)
        x_texte = x_texte+1


def border(console, caractere, x_min, y_min, x_max, y_max):
    """Dessine les bords"""
    for y in range(y_min, y_max+1):
        console.addstr(y, x_min, caractere)
        console.addstr(y, x_max, caractere)
    for x in range(x_min, x_max+1):
        console.addstr(y_max, x, caractere)
        console.addstr(y_min, x, caractere)


def game_over(console, y, x, clones, pommes, x_min, y_min, x_max, y_max):
    """Supprime tout et affiche "tu es nul" """
    console.addstr(y, x, RIEN)
    for coordonnees in clones:
        console.addstr(coordonnees[0], coordonnees[1], RIEN)
    for coordonnees in pommes:
        console.addstr(coordonnees[0], coordonnees[1], RIEN)
    for y in range(y_min, y_max+1):
        console.addstr(y, x_min, RIEN)
        console.addstr(y, x_max, RIEN)
    for x in range(x_min, x_max+1):
        console.addstr(y_max, x, RIEN)
        console.addstr(y_min, x, RIEN)
    afficher(console, "Merci à", 10, 50)
    afficher(console, "Alexis pour l'idée", 10, 40)
    afficher(console, "Alexis pour la programmation", 10, 40)
    afficher(console, "Alexis (et un peu Albert faut comme même avouer, mais juste un petit peu) pour son génie", 10, 0)
    afficher(console, "Projet dédié à notre bien-aimé", 10, 40)
    afficher(console, "Alexis Blaudszun, un homme qui était beau", 10, 40)
    afficher(console, "T'imagines même pas", 10, 40)
    afficher(console, "Va sur freerobux.com pour des free robux, offre limité, donne seulement ton code bancaire", 10, 0)


def frame(console, snake, x_min, y_min, x_max, y_max, key):
    """Affiche le snake"""
    clones = snake.clones
    
    console.addstr(snake.y, snake.x, snake.caractere_snake) #affiche la tête
    console.nodelay(True)
    try:
        newkey = console.getkey()
        if newkey == key or (newkey == 'a' and key == 'd') or (newkey == 'd' and key == 'a') or (newkey == 'w' and key == 's') or (newkey == 's' and key == 'w'):
            pass
        else:
            key = newkey
    except:
        pass
    
    if len(snake.clones) > 5:
        console.addstr(snake.clones[0][0], snake.clones[0][1], RIEN) #affiche rien au dernier clone
    clones = snake.update_clones(console, CLONE, snake, clones, 5) #change les clones
    console.addstr(snake.y, snake.x, snake.caractere_clones) #affiche le nouveau clone derrière la tête
    
    if snake.nouvelles_coordonnees(key, clones, x_min, y_min, x_max, y_max) == "nul":
        return 'c est nul'
    else:
        y, x = snake.nouvelles_coordonnees(key, clones,  x_min, y_min, x_max, y_max)
        return y, x, clones, key


def jeu(console):
    """Affiche le personnage"""
    x_min, y_min, x_max, y_max = 0, 0, 100, 20
    x, y = 10, 10
    clones = []
    pommes = []
    score = 0
    key = "d"
    
    border(console, BORDER, x_min, y_min, x_max, y_max)
    
    while True:
        snake = personnage(y, x, PERSONNAGE, clones, CLONE)
        time.sleep(0.1)
        f = frame(console, snake, x_min, y_min, x_max, y_max, key)
        if f == 'c est nul':
            break
        else:
            y, x, clones, key = f
    
    console.nodelay(False)
    game_over(console, y, x, clones, pommes, x_min, y_min, x_max, y_max)
        
        
def programme(console):
    debut(console)
    jeu(console)


if __name__ == "__main__":
    curses.wrapper(programme)
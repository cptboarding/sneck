"""
Module qui affiche un snake qui se déplace sur une fenêtre de curses.

python "J:\Documents\Informatique\3ème année\Projet 2ème semestre\snake_16052025\snake.py"
"""

import curses
import random
import time

from coordonnees_snake import personnage
from murs_qui_bougent import moving_wall

RIEN = " "
PERSONNAGE = "@"
CLONE = "#"
BORDER = "-"


def debut(console) -> None:
    console.clear()
    curses.curs_set(False)
    console.refresh()


def afficher(console, texte: str, y_texte: int, x_texte: int):
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


def border(console, caractere: int, x_min: int, y_min: int, x_max: int, y_max: int):
    """Dessine les bords"""
    for y in range(y_min, y_max+1):
        console.addstr(y, x_min, caractere)
        console.addstr(y, x_max, caractere)
    for x in range(x_min, x_max+1):
        console.addstr(y_max, x, caractere)
        console.addstr(y_min, x, caractere)


def game_over(console, snake: personnage, x_min: int, y_min: int, x_max: int, y_max: int):
    """Supprime tout et affiche "tu es nul" """
    console.addstr(snake.y, snake.x, RIEN)
    for coordonnees in snake.clones:
        console.addstr(coordonnees[0], coordonnees[1], RIEN)
    for y in range(y_min, y_max+1):
        console.addstr(y, x_min, RIEN)
        console.addstr(y, x_max, RIEN)
    for x in range(x_min, x_max+1):
        console.addstr(y_max, x, RIEN)
        console.addstr(y_min, x, RIEN)
    afficher(console, "Game over", 10, 50)


def frame(console, snake: personnage, longueur_max: int, x_min: int, y_min: int, x_max: int, y_max: int, key: str):
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

    if len(snake.clones) == longueur_max and len(snake.clones)>0:
        console.addstr(snake.clones[0][0], snake.clones[0][1], RIEN) #affiche rien au dernier clone
    clones = snake.update_clones(longueur_max) #change les clones
    if len(snake.clones)>0:
        console.addstr(snake.y, snake.x, snake.caractere_clones) #affiche le nouveau clone derrière la tête
    else:
        console.addstr(snake.y, snake.x, RIEN) #s'il n'y a pas de clones, on affiche rien derrière la tête
        
    if snake.nouvelles_coordonnees(key, x_min, y_min, x_max, y_max) == "nul":
        return 'c est nul'
    else:
        y, x = snake.nouvelles_coordonnees(key,  x_min, y_min, x_max, y_max)
        return y, x, clones, key


def jeu(console):
    """Le jeu"""
    hauteur, longueur = console.getmaxyx()
    x_min, y_min, x_max, y_max = 10, 5, longueur-10, hauteur-5
    x, y = 30, 15
    score = 0
    longueur_max = 0
    key = "d"
    vitesse_initiale = 5

    clones = []

    border(console, BORDER, x_min, y_min, x_max, y_max)

    while True:
        longueur_max = score//5
        vitesse = vitesse_initiale + score/10
        snake = personnage(y, x, PERSONNAGE, clones, CLONE)
        time.sleep(1/vitesse)
        f = frame(console, snake, longueur_max, x_min, y_min, x_max, y_max, key)
        if f == 'c est nul':
            break
        else:
            y, x, clones, key = f

    console.nodelay(False)
    game_over(console, snake, x_min, y_min, x_max, y_max)


def programme(console):
    debut(console)
    jeu(console)


if __name__ == "__main__":
    curses.wrapper(programme)

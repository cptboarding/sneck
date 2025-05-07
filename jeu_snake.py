"""
python "J:\Documents\Informatique\3ème année\Projet 2ème semestre\snake.py"
hauteur, longueur = console.getmaxyx()
"""

import curses
import random

from clones_snake import afficher_clones
from coordonnees import nouvelles_coordonnees

RIEN = " "
PERSONNAGE = "@"
CLONE = “#”
BORDER = "-"


def debut(console):
	console.clear()
	curses.curs_set(False)
	console.refresh()


def afficher(console, texte, temps):
	"""Affiche du texte"""
	y_texte, x_texte = 0, 0
	for lettre in texte:
    		console.addstr(y_texte, x_texte, lettre)
    		x_texte = x_texte+1
   	 
 
def border(console, caractere, x_min, y_min, x_max, y_max):
	for y in range(y_min, y_max+1):
    		console.addstr(y, x_min, caractere)
    		console.addstr(y, x_max, caractere)
	for x in range(x_min, x_max+1):
    		console.addstr(y_max, x, caractere)
    		console.addstr(y_min, x, caractere)


def game_over(console, y, x, clones, x_min, y_min, x_max, y_max):
	"""Supprime tout et affiche "tu es nul" """
	console.addstr(y, x, RIEN)
	for coordonnees in clones:
    		console.addstr(coordonnees[0], coordonnees[1], RIEN)
	for y in range(y_min, y_max+1):
    		console.addstr(y, x_min, RIEN)
    		console.addstr(y, x_max, RIEN)
	for x in range(x_min, x_max+1):
    		console.addstr(y_max, x, RIEN)
    		console.addstr(y_min, x, RIEN)
	afficher(console, "Tu es nul!!!!!!!!!!!!!!!!!!!!!!!!!!!", 5)



def jeu(console):
	"""Affiche le personnage"""
	x_min, y_min, x_max, y_max = 0, 0, 100, 20
	x, y = 10, 10
	clones = []
	longueur_clones = 0
	longueur_max = 5
	pommes = []
    
	border(console, BORDER, x_min, y_min, x_max, y_max)
	while True:
    		console.addstr(y, x, PERSONNAGE)
    		key = console.getkey()
    		clones = afficher_clones(console, CLONE, y, x, clones, longueur_max)
    		if nouvelles_coordonnees(console, key, y, x, clones, x_min, y_min, x_max, y_max) == "nul":
        			break
    	else:   
        		x = nouvelles_coordonnees(console, key, y, x, clones,  x_min, y_min, x_max, y_max)[0]
        		y = nouvelles_coordonnees(console, key, y, x, clones, x_min, y_min, x_max, y_max)[1]
	game_over(console, y, x, clones, x_min, y_min, x_max, y_max)
	console.getkey()
   	 

def programme(console):
	debut(console)
	jeu(console)


if __name__ == "__main__":
	curses.wrapper(programme)

"""
alexis : python "J:\Documents\Informatique\3ème année\Projet 2ème semestre\snake.py"
hauteur, longueur = console.getmaxyx()
aurelien : python "J:\Informatique\infoOC\sneck\jeu_snake.py" 
"""

import curses
import random

from clones_snake import afficher_clones


RIEN = " "
PERSONNAGE = "@"
CLONE = "#"
BORDER = "-"
point = "."


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
            x, y = nouvelles_coordonnees(console, key, y, x, clones, x_min, y_min, x_max, y_max)
    
    game_over(console, y, x, clones, x_min, y_min, x_max, y_max)
    console.getkey()
def randompointposition(x_min, y_min, x_max, y_max)  -> tuple :
         x_min, y_min, x_max, y_max = 0, 0, 100, 20
         yp ,xp =  random.randint(y_min ,y_max )  , random.randint(x_min ,x_max )
         return tuple(yp,xp)
        
def pointsgenerateur(console , x_min , y_min , x_max , y_max  , point ) :
    x_min, y_min, x_max, y_max = 0, 0, 100, 20
    for i  in range(10):
          console.addstr(randompointposition(), point) 
def nouvelles_coordonnees(console, key, y, x, clones, x_min, y_min, x_max, y_max):
	"""Retourne les nouvelles coordonnées en fonction du key"""
	if key == "a":
    		if (y, x-1) in clones or x-1 == x_min:
        			return "nul"
    		else:
        			x = x-1
	if key == "d":
    		if (y, x+1) in clones or x+1 == x_max:
        			return "nul"
    		else:
        			x = x+1
	if key == "w":
    		if (y-1, x) in clones or y-1 == y_min:
        			return "nul"
    		else:
        			y = y-1
	if key == "s":
    		if (y+1, x) in clones or y+1 == y_max:
        			return "nul"
    		else:
        			y = y+1
	return x, y



   	 

def programme(console):
	debut(console)
	jeu(console)
	pointsgenerateur(console)


if __name__ == "__main__":
	curses.wrapper(programme)

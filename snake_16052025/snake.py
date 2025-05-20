import curses
import random
import time

from coordonnees_snake import personnage
from murs_qui_bougent import moving_wall

RIEN = " "
PERSONNAGE = "@"
CLONE = "#"
BORDER = "-"
pomme = "●"
SYMBOL_GOLDEN_POMME = "§"



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
    for y in range(y_min-1, y_max+2):
        console.addstr(y, x_min-1, caractere)
        console.addstr(y, x_max+1, caractere)
    for x in range(x_min-1, x_max+2):
        console.addstr(y_max+1, x, caractere)
        console.addstr(y_min-1, x, caractere)


def game_over(console, snake, x_min, y_min, x_max, y_max):
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


def frame(console, snake, longueur_max, x_min, y_min, x_max, y_max, key):
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
def afficher_score(console, score, x_score=105, y_score=2):
    "Affiche le score dans un encadré"
    largeur = 15
    console.addstr(y_score - 1, x_score, "+" + "-" * (largeur - 2) + "+")
    console.addstr(y_score, x_score, f"|Score : {score}|")
    console.addstr(y_score + 1, x_score, "+" + "-" * (largeur - 2) + "+")
def randompommeposition(x_min, y_min, x_max, y_max) -> tuple:
    y = random.randint(y_min,y_max )  # éviter les bords
    x = random.randint(x_min, x_max)
    return (y, x)

def pommegen(console, pomme,x_min, y_min, x_max, y_max):
    pommes = []
    for _ in range(10):
        y, x = randompommeposition(x_min, y_min, x_max, y_max)
        pommes.append((y, x))
        console.addstr(y, x, pomme)
    return pommes

def golden_pommegen(console, SYMBOL_GOLDEN_POMME,x_min, y_min, x_max, y_max):
    the_golden_pomme = []
    y_g, x_g = randompommeposition(x_min, y_min, x_max, y_max)
    the_golden_pomme.append((y_g, x_g))
    console.addstr(y_g, x_g, SYMBOL_GOLDEN_POMME)
    return the_golden_pomme
   

def jeu(console,pommes,murs=None):
    """Le jeu"""
    hauteur, longueur = console.getmaxyx()
    x_min, y_min, x_max, y_max = 10, 5, longueur-10, hauteur-5
    x, y = 30, 15
    score = 0
    longueur_max = 2
    key = "d"
    vitesse_initiale = 5
    last_golden_score = -20
    golden_pomme = []

    clones = []

    border(console, BORDER, x_min, y_min, x_max, y_max)

    while True:
        longueur_max = score//3
        vitesse = vitesse_initiale + score/10
        snake = personnage(y, x, PERSONNAGE, clones, CLONE)
        time.sleep(1/vitesse)
        #affiche et update le score
        afficher_score(console, score)

        f = frame(console, snake, longueur_max, x_min, y_min, x_max, y_max, key)
        if f == 'c est nul':
            break
        if murs:
            
            for mur in murs:
                for (mx, my) in mur.return_coordinates():
                    if 0 <= my < height and 0 <= mx < width:
                        console.addch(my, mx, RIEN)
            # Actualiser murs (déplacement)
            murs = [mur.frame() for mur in murs]
            # Redessiner murs
            for mur in murs:
                for (mx, my) in mur.return_coordinates():
                    if 0 <= my < height and 0 <= mx < width:
                        console.addch(my, mx, "█")
                # Collision avec murs
        if murs:
            for mur in murs:
                if (x, y) in mur.return_coordinates():
                    f = "c est nul"
                    break
        # Gestion pommes
        if (y, x) in pommes:
            pommes.remove((y, x))
            score += 1
            y_n, x_n = randompommeposition(x_min, y_min, x_max, y_max)
            pommes.append((y_n, x_n))
            console.addstr(y_n, x_n, pomme)

        # Golden pomme toutes les 20 pommes mangées
        if score != 0 and score % 20 == 0 and score != last_golden_score:
            golden_pomme = golden_pommegen(console, SYMBOL_GOLDEN_POMME)
            last_golden_score = score

        if (y, x) in golden_pomme:
            golden_pomme.remove((y, x))
            score += 5
        else:
            y, x, clones, key = f

    console.nodelay(False)
    game_over(console, snake, x_min, y_min, x_max, y_max)


def programme(console,murs=None):
    hauteur, longueur = console.getmaxyx()
    x_min, y_min, x_max, y_max = 10, 5, longueur-10, hauteur-5
    debut(console)
    pommes = pommegen(console, pomme,x_min, y_min, x_max, y_max)
    if murs is None:
        murs = []
    if murs:
        # Dessiner murs initiaux
        for mur in murs:
            for coord in mur.return_coordinates():
                # Attention l'ordre dans addstr/addch est (y, x)
                console.addstr(coord[1], coord[0], "█")
    jeu(console, pommes, murs)
    


if __name__ == "__main__":
    curses.wrapper(programme)

"""
python "J:\Documents\Informatique\3ème année\Projet 2ème semestre\snake.py"
hauteur, longueur = console.getmaxyx()
"""
import curses
import random
import time
from murs_qui_bougent import moving_wall
from coordonnees_snake import personnage

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
        x_texte = x_texte + 1
    console.getkey()
    for lettre in texte:
        x_texte = x_texte - 1
    for lettre in texte:
        console.addstr(y_texte, x_texte, RIEN)
        x_texte = x_texte + 1

def border(console, caractere, x_min, y_min, x_max, y_max):
    """Dessine les bords"""
    for y in range(y_min, y_max + 1):
        console.addstr(y, x_min, caractere)
        console.addstr(y, x_max, caractere)
    for x in range(x_min, x_max + 1):
        console.addstr(y_max, x, caractere)
        console.addstr(y_min, x, caractere)

def game_over(console, y, x, clones, pommes, x_min, y_min, x_max, y_max):
    """Supprime tout et affiche 'tu es nul'"""
    console.addstr(y, x, RIEN)
    for coordonnees in clones:
        console.addstr(coordonnees[0], coordonnees[1], RIEN)
    for coordonnees in pommes:
        console.addstr(coordonnees[0], coordonnees[1], RIEN)
    for y_ in range(y_min, y_max + 1):
        console.addstr(y_, x_min, RIEN)
        console.addstr(y_, x_max, RIEN)
    for x_ in range(x_min, x_max + 1):
        console.addstr(y_max, x_, RIEN)
        console.addstr(y_min, x_, RIEN)
    afficher(console, "Merci à", 10, 50)
    afficher(console, "Alexis pour l'idée", 10, 40)
    afficher(console, "Alexis pour la programmation", 10, 40)
    afficher(console, "Alexis (et un peu Albert faut comme même avouer, mais juste un petit peu) pour son génie", 10, 0)
    afficher(console, "Projet dédié à notre bien-aimé", 10, 40)
    afficher(console, "Alexis Blaudszun, un homme qui était beau", 10, 40)
    afficher(console, "T'imagines même pas", 10, 40)
    afficher(console, "Va sur freerobux.com pour des free robux, offre limité, donne seulement ton code bancaire", 10, 0)

def frame(console, snake, x_min, y_min, x_max, y_max, key):
    """Affiche le snake et gère son déplacement"""
    clones = snake.clones
    
    console.addstr(snake.y, snake.x, snake.caractere_snake)  # affiche la tête
    console.nodelay(True)
    try:
        newkey = console.getkey()
        # Empêche de faire demi-tour direct (ex: a->d interdit)
        if newkey == key or (newkey == 'a' and key == 'd') or (newkey == 'd' and key == 'a') or (newkey == 'w' and key == 's') or (newkey == 's' and key == 'w'):
            pass
        else:
            key = newkey
    except:
        pass
    
    if len(snake.clones) > 5:
        console.addstr(snake.clones[0][0], snake.clones[0][1], RIEN)  # efface le dernier clone
    
    clones = snake.update_clones(console, CLONE, snake, clones, 5)  # met à jour la liste des clones
    console.addstr(snake.y, snake.x, snake.caractere_clones)  # affiche nouveau clone
    
    coords = snake.nouvelles_coordonnees(key, clones, x_min, y_min, x_max, y_max)
    if coords == "nul":
        return "c est nul"
    else:
        y, x = coords
        return y, x, clones, key

def randompommeposition() -> tuple:
    y = random.randint(1, 19)  # éviter les bords
    x = random.randint(1, 99)
    return (y, x)

def pommegen(console, pomme):
    pommes = []
    for _ in range(10):
        y, x = randompommeposition()
        pommes.append((y, x))
        console.addstr(y, x, pomme)
    return pommes

def golden_pommegen(console, SYMBOL_GOLDEN_POMME):
    the_golden_pomme = []
    y_g, x_g = randompommeposition()
    the_golden_pomme.append((y_g, x_g))
    console.addstr(y_g, x_g, SYMBOL_GOLDEN_POMME)
    return the_golden_pomme

def afficher_score(console, score, x_score=105, y_score=2):
    "Affiche le score dans un encadré"
    largeur = 15
    console.addstr(y_score - 1, x_score, "+" + "-" * (largeur - 2) + "+")
    console.addstr(y_score, x_score, f"|Score : {score:<5}|")
    console.addstr(y_score + 1, x_score, "+" + "-" * (largeur - 2) + "+")

def jeu(console, pommes, murs=None):
    x_min, y_min, x_max, y_max = 0, 0, 100, 20
    x, y = 10, 10
    clones = []
    score = 0
    last_golden_score = -20
    golden_pomme = []
    key = "d"

    border(console, BORDER, x_min, y_min, x_max, y_max)

    height, width = console.getmaxyx()  # Taille terminal

    while True:
        snake = personnage(y, x, PERSONNAGE, clones, CLONE)
        afficher_score(console, score)

        if murs:
            # Effacer murs précédents
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

        time.sleep(0.1)

        f = frame(console, snake, x_min, y_min, x_max, y_max, key)

        # Collision avec murs
        if murs:
            for mur in murs:
                if (x, y) in mur.return_coordinates():
                    f = "c est nul"
                    break

        if f == "c est nul":
            break
        else:
            y, x, clones, key = f

        # Gestion pommes
        if (y, x) in pommes:
            pommes.remove((y, x))
            score += 1
            y_n, x_n = randompommeposition()
            pommes.append((y_n, x_n))
            if 0 <= y_n < height and 0 <= x_n < width:
                console.addstr(y_n, x_n, pomme)

        # Golden pomme toutes les 20 pommes mangées
        if score != 0 and score % 20 == 0 and score != last_golden_score:
            golden_pomme = golden_pommegen(console, SYMBOL_GOLDEN_POMME)
            last_golden_score = score

        if (y, x) in golden_pomme:
            golden_pomme.remove((y, x))
            score += 5

    console.nodelay(False)
    game_over(console, y, x, clones, pommes, x_min, y_min, x_max, y_max)

def programme(console, murs=None):
    debut(console)
    pommes = pommegen(console, pomme)
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
    # Mur horizontal de largeur 21 (x=10 à 30) et hauteur 1, départ en (10, 5), vitesse vers la droite, mouvement max 20 pas, progress initiale 0
    murs = [moving_wall((21, 1), 10, 5, (1, 0), 20, 0)]
    
    curses.wrapper(lambda stdscr: programme(stdscr, murs=murs))


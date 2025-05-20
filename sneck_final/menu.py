import subprocess
import sys
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
import curses
import jeu_snake
from murs_qui_bougent import moving_wall  

# Mode classique
def play_game_classic():
    print(">>> Lancement du jeu classique...")
    curses.wrapper(jeu_snake.programme)
    print(">>> Jeu terminé.")

# Mode medium avec murs mobiles
def play_game_medium():
    print(">>> Lancement du mode medium (murs dynamiques)...")

    def programme_medium(console):
        murs = [
            moving_wall((25, 1), 0, 0, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 25, 0, (1, 0), 25, 0, x_max=100, y_max=20),#ici que leprogramme bug avec les dimensions
            moving_wall((25, 1), 50, 0, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 75, 0, (1, 0), 25, 0, x_max=100, y_max=20),

            moving_wall((25, 1), 0, 20, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 25, 20, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 50, 20, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 75, 20, (1, 0), 25, 0, x_max=100, y_max=20),

            moving_wall((1, 5), 0, 0, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 0, 5, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 0, 10, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 0, 15, (0, 1), 20, 0, x_max=100, y_max=20),

            moving_wall((1, 5), 100, 0, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 100, 5, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 100, 10, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 100, 15, (0, 1), 20, 0, x_max=100, y_max=20),
        ]
        jeu_snake.programme(console, murs=murs)

    curses.wrapper(programme_medium)
    print(">>> Jeu terminé.")
def play_game_hardcore():
    print(">>> Lancement du mode hardcore (murs dynamiques + pommes qui se téléportent)...")

    def programme_hardcore(console):
        murs = [
            moving_wall((25, 1), 0, 0, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 25, 0, (1, 0), 25, 0, x_max=100, y_max=20),#ici que leprogramme bug avec les dimensions
            moving_wall((25, 1), 50, 0, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 75, 0, (1, 0), 25, 0, x_max=100, y_max=20),

            moving_wall((25, 1), 0, 20, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 25, 20, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 50, 20, (1, 0), 25, 0, x_max=100, y_max=20),
            moving_wall((25, 1), 75, 20, (1, 0), 25, 0, x_max=100, y_max=20),

            moving_wall((1, 5), 0, 0, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 0, 5, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 0, 10, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 0, 15, (0, 1), 20, 0, x_max=100, y_max=20),

            moving_wall((1, 5), 100, 0, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 100, 5, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 100, 10, (0, 1), 20, 0, x_max=100, y_max=20),
            moving_wall((1, 5), 100, 15, (0, 1), 20, 0, x_max=100, y_max=20),
            
        ]
        jeu_snake.programme(console, murs=murs, pomme_tp=True)  # Il faut rajouter les pommes qui tps

    curses.wrapper(programme_hardcore)
    print(">>> Jeu terminé.")




def quit_game():
    print("Quitter le jeu...")
    exit()

# Fonction principale du menu
def main():
    menu = CursesMenu("Sneck Game", "Utilisez les flèches pour naviguer")

    play_classic = FunctionItem("Jouer (Classique)", play_game_classic)
    play_medium = FunctionItem("Jouer (Medium - murs dynamiques)", play_game_medium)
    play_hardcore = FunctionItem("Jouer (Hardcore - murs + pommes dynamiques)", play_game_hardcore)
    options_item = FunctionItem("Options", show_options)
    quit_item = FunctionItem("Quitter", quit_game)

    menu.items.append(play_classic)
    menu.items.append(play_medium)
    menu.items.append(play_hardcore)
    menu.items.append(options_item)
    menu.items.append(quit_item)

    menu.show()

if __name__ == "__main__":
    main()



















"""
Module qui permet de créer des instances de la classe personnage, qui peut changer de coordonnées et
avoir des clones qui le suivent.
"""

from typing import NamedTuple


class personnage(NamedTuple):
    y: int
    x: int
    caractere_snake: str
    clones: list
    caractere_clones: str
    
    
    @staticmethod
    def verifier(y: int, x: int, clones: list,  x_min: int, y_min: int, x_max: int, y_max: int) -> str:
        """Vérifie si les coordonnées y et x sont possibles"""
        if (y, x) in clones:
            return "nul"
        elif x == x_min or x == x_max or y == y_min or y == y_max:
            return "nul"

    
    def nouvelles_coordonnees(self, key: str, x_min: int, y_min: int, x_max: int, y_max: int) -> tuple:
        """Retourne les nouvelles coordonnées en fonction du key"""
        if key == "a":
            if personnage.verifier(self.y, self.x-1, self.clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                x = self.x-1
                y = self.y
        if key == "d":
            if personnage.verifier(self.y, self.x+1, self.clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                x = self.x+1
                y = self.y
        if key == "w":
            if personnage.verifier(self.y-1, self.x, self.clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                y = self.y-1
                x = self.x
        if key == "s":
            if personnage.verifier(self.y+1, self.x, self.clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                y = self.y+1
                x = self.x
        return y, x
     
    @staticmethod
    def supprimer_premier_element(collection: list) -> list:
        """Supprime le premier élément d'une collection"""
        nouvelle_collection = []
        for i in range(len(collection)):
            if i != 0:
                nouvelle_collection.append(collection[i])
        return nouvelle_collection


    def update_clones(self, longueur_max: int) -> list:
        """Supprimme le dernier clone si la longueur_max est atteinte, et ajoute un nouveau clone"""
        clones = self.clones
        if len(clones) == longueur_max:
            clones = personnage.supprimer_premier_element(clones)
        if longueur_max > 0: #s'il y a au moins un clone à afficher
            clones.append((self.y, self.x))
        return clones


def _tests() -> None:
    snake_exemple = personnage(10, 10, "@", [(10, 7), (10, 8), (10, 9)], "#")
    assert snake_exemple.nouvelles_coordonnees("d", 0, 0, 20, 20) == (10, 11)

    nouveaux_clones = snake_exemple.update_clones(longueur_max=3)
    y, x = snake_exemple.nouvelles_coordonnees("d", 0, 0, 20, 20)
    snake_exemple_2 = personnage(y, x, "@", nouveaux_clones, "#")
    assert (snake_exemple_2.y, snake_exemple_2.x)  == (10, 11)
    assert snake_exemple_2.clones == [(10, 8), (10, 9), (10, 10)]

    print("Tests réussis")


if __name__ == "__main__":
    _tests()

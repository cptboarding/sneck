from typing import NamedTuple


class personnage(NamedTuple):
    y: int
    x: int
    caractere_snake: str
    clones: list
    caractere_clones: str
    
    
    @staticmethod
    def verifier(y, x, clones,  x_min, y_min, x_max, y_max):
        """Vérifie si les coordonnées y et x sont possibles"""
        if (y, x) in clones:
            return "nul"
        elif x == x_min or x == x_max or y == y_min or y == y_max:
            return "nul"

    
    def nouvelles_coordonnees(self, key, clones, x_min, y_min, x_max, y_max):
        """Retourne les nouvelles coordonnées en fonction du key"""
        if key == "a":
            if personnage.verifier(self.y, self.x-1, clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                x = self.x-1
                y = self.y
        if key == "d":
            if personnage.verifier(self.y, self.x+1, clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                x = self.x+1
                y = self.y
        if key == "w":
            if personnage.verifier(self.y-1, self.x, clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                y = self.y-1
                x = self.x
        if key == "s":
            if personnage.verifier(self.y+1, self.x, clones, x_min, y_min, x_max, y_max) == "nul":
                return "nul"
            else:
                y = self.y+1
                x = self.x
        return y, x
        
    @staticmethod
    def supprimer_premier_element(collection):
        """Supprime le premier élément d'une collection"""
        nouvelle_collection = []
        for i in range(len(collection)):
            if i != 0:
                nouvelle_collection.append(collection[i])
        return nouvelle_collection


    def update_clones(self, console, caractere, personnage, clones, longueur_max=5):
        """Change les coordonnées des clones, supprimme le dernier clone, et affiche le nouveaux clone"""
        clones = self.clones
        if len(self.clones) > longueur_max:
            clones = personnage.supprimer_premier_element(clones)
        clones.append((personnage.y, personnage.x))
        return clones
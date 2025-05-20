'''
ceci genere des classes abstraites de murs qui vont calculer la position d'un mur nomade
'''

from typing import NamedTuple

#la classe qui fait des murs mobiles
class moving_wall(NamedTuple):
    dimentions: tuple      
    x_start: int
    y_start: int
    vel: tuple              
    move_range: int
    progress: int = 0     

    #retourne un nouveau self
    @classmethod
    def new(cls, d, x, y, v, mr, p, x_max=100, y_max=20):
        return cls(d, x, y, v, mr, p, x_max, y_max)

    #les 2 trucs ci dessous sont pour processer le frame du mur
    def frame_x(self):
        # Calcul de la limite max pour que le mur ne dépasse pas
        max_progress = self.move_range - self.dimentions[0]
        if self.vel[0] == 1 and self.progress >= max_progress:
            return self.progress - 1, (-1, 0)
        elif self.vel[0] == -1 and self.progress <= 0:
            return self.progress + 1, (1, 0)
        else:
            return self.progress + self.vel[0], self.vel

    def frame_y(self):
        max_progress = self.move_range - self.dimentions[1]
        if self.vel[1] == 1 and self.progress >= max_progress:
            return self.progress - 1, (0, -1)
        elif self.vel[1] == -1 and self.progress <= 0:
            return self.progress + 1, (0, 1)
        else:
            return self.progress + self.vel[1], self.vel
    #regroupe les deux trucs ci dessus
    def frame(self):
        if abs(self.vel[0]) == 1:
            p, v = self.frame_x()
        else:
            p, v = self.frame_y()
        return self.new(self.dimentions, self.x_start, self.y_start, v, self.move_range, p, self.x_max, self.y_max)
    
    # retourne les coordonnees
    def return_coordinates(self):
        r = []
        for y in range(self.dimentions[1]):
            for x in range(self.dimentions[0]):
                prog = self.progress
                vx, vy = self.vel
                pos_x = self.x_start + x + prog * abs(vx)
                pos_y = self.y_start + y + prog * abs(vy)
                r.append((pos_x, pos_y))
        return r


if __name__ == "__main__":
    w = moving_wall((2, 1), 1, 1, (1, 0), 10, x_max=30, y_max=10)
    for i in range(25):
        print(w.return_coordinates())
        w = w.frame()

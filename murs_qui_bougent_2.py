

from typing import NamedTuple

class moving_wall(NamedTuple):
    dimentions: tuple      
    x_start: int
    y_start: int
    vel: tuple              
    move_range: int
    progress: int = 0
    x_max: int = 100        
    y_max: int = 20        

    @classmethod
    def new(cls, d, x, y, v, mr, p, x_max=100, y_max=20):
        return cls(d, x, y, v, mr, p, x_max, y_max)

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

    def frame(self):
        if abs(self.vel[0]) == 1:
            p, v = self.frame_x()
        else:
            p, v = self.frame_y()
        return self.new(self.dimentions, self.x_start, self.y_start, v, self.move_range, p, self.x_max, self.y_max)

    def return_coordinates(self):
        r = []
        for y in range(self.dimentions[1]):
            for x in range(self.dimentions[0]):
                prog = self.progress
                vx, vy = self.vel
                # Calcul de la position
                pos_x = self.x_start + x + prog * abs(vx)
                pos_y = self.y_start + y + prog * abs(vy)
                # Clamp dans la zone de jeu
                if pos_x < 0:
                    pos_x = 0
                elif pos_x >= self.x_max:
                    pos_x = self.x_max - 1
                if pos_y < 0:
                    pos_y = 0
                elif pos_y >= self.y_max:
                    pos_y = self.y_max - 1

                r.append((pos_x, pos_y))
        return r


if __name__ == "__main__":
    w = moving_wall((2, 1), 1, 1, (1, 0), 10, x_max=30, y_max=10)
    for i in range(25):
        print(w.return_coordinates())
        w = w.frame()

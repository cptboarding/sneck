

from typing import NamedTuple


class moving_wall(NamedTuple):
    dimentions: tuple
    x_start: int
    y_start: int
    vel: tuple
    move_range: int
    progress: int = 0

    @classmethod
    def new(cls, d, x, y, v, mr, p):
        return cls(d, x, y, v, mr, p)

    def frame_x(self):
        if self.vel[0] == 1 and self.progress == self.move_range - self.dimentions[0]:
            return self.progress - 1, (-1, 0)
        elif self.vel[0] == -1 and self.progress == 0:
            return self.progress + 1, (1, 0)
        else:
            return self.progress + self.vel[0], self.vel

    def frame_y(self):
        if self.vel[1] == 1 and self.progress == self.move_range - self.dimentions[1]:
            return self.progress - 1, (-1, 0)
        elif self.vel[1] == -1 and self.progress == 0:
            return self.progress + 1, (1, 0)
        else:
            return self.progress + self.vel[1], self.vel

    def frame(self):
        if abs(self.vel[0]) == 1:
            p, v = self.frame_x()
        else:
            p, v = self.frame_y()
        return self.new(self.dimentions, self.x_start, self.y_start, v, self.move_range, p)

    def return_coordinates(self):
        r = []
        for y in range(self.dimentions[1]):
            for x in range(self.dimentions[0]):
                prog = self.progress
                v = self.vel
                p = (self.x_start + x + prog*abs(v[0]), self.y_start + y + prog*abs(v[1]))
                r.append(p)
        return r




w = moving_wall((2, 1), 1, 1, (1, 0), 5)
for i in range(15):
    print(w.return_coordinates())
    w = w.frame()




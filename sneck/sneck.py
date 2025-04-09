
import enregistrement_carte as en
from typing import NamedTuple
from printe import printe, cancel_import, import_chatGPT


s1 = '■'
s2 = '□'



ml = 16
m = en.genere(ml, '')

sneck = []


class sneck_tile(NamedTuple):
    t: int
    x: int
    y: int
    vel: tuple
    
    @classmethod
    def new(cls, tt, xx, yy, v):
        return cls(t=tt, x=xx, y=yy, vel=v)
    
    def get_previous_coordinates(self):
        p = sneck[self.t-1]
        return p.x, p.y, p.vel
    
    def advance(self):
        xv = self.vel[0]
        yv = self.vel[1]
        if self.t == 0:
            return self.new(self.t, self.x+xv, self.y+yv, self.vel)
        else:
            xx, yy, v = self.get_previous_coordinates()
            return self.new(self.t, self.x+xv, self.y+yv, v)
    


def create_sneck_tile(xx=0, yy=0, vv=(1, 0)):
    l = len(sneck)
    if l == 0:
        n = sneck_tile(t=0, x=xx, y=yy, vel=vv)
    else:
        t2 = sneck[l-1]
        t2v = t2.vel
        n = sneck_tile(t=l, x=t2.x-t2v[0], y=t2.y-t2v[1], vel=t2v)
    sneck.append(n)
    return n

def sneck_advance():
    for i in range(len(sneck)-1, -1, -1):
        s = sneck[i]
        sneck[i] = s.advance()


def update_console(sneck=sneck):
    mm = en.genere(ml, '')
    for i in sneck:
        mm[i.y%16][i.x%16] = '1'
    return mm

def print_console(matrix):
    for i in matrix:
        r = ''
        for i2 in i:
            if i2 == '':
                r += s2+' '
            else:
                r += s1+' '
        print(r)
        
        
def update():
    m = update_console()
    print_console(m)
    print(sneck)
        
        
        
def test_reset():
    create_sneck_tile(6, 6, (0, -1))
    create_sneck_tile()
    create_sneck_tile()
    create_sneck_tile()
    create_sneck_tile()
    create_sneck_tile()
    create_sneck_tile()
    update()

def test_play():
    d = 90
    while True:
        r = input('r/l/leave nothing: ')
        if r == 'r':
            d -= 90
        elif r == 'l':
            d += 90
        d = d % 360
        
        first_tile = sneck[0]
        fdir = ()
        if d == 0:
            fdir = (1, 0)
        elif d == 90:
            fdir = (0, -1)
        elif d == 180:
            fdir = (-1, 0)
        elif d == 270:
            fdir = (0, 1)
        sneck[0] = first_tile.new(0, first_tile.x, first_tile.y, fdir)
        
        sneck_advance()
        update()
            
        

if __name__ == '__main__':
    test_reset()
    test_play()


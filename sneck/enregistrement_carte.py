# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 11:21:42 2025

@author: albert.stnsl
"""

import FileEditor as f
import printe


f1 = f.FileEditor('map.txt')


"""
matrice 32x32
"""


def genere(n, fill):
    r = []
    for i in range(n):
        l = []
        for i2 in range(n):
            l.append(str(fill))
        r.append(l)
    return r


def encode(m):
    c = ''
    for i in m:
        c += ':'
        for i2 in i:
            c += str(i2) + ','
    return c


def decode(t):
    r = []
    i = 1
    l = 0
    while True:
        ll = []
        n = ''
        while t[i] != ':':
            if t[i] == ',':
                ll.append(n)
                n = ''
            else:
                n += t[i]
            i += 1
            if i > len(t)-1:
                break
        r.append(ll)
        i += 1
        if i >= len(t)-1:
                break
    return r
      

def clean():
    if not f1.assertfile():
        f1.create()
    _t = f.FileEditor('test.txt')
    if _t.assertfile():
        _t.delete()


#user functions
def enregistrer_map(mp):
    r = encode(mp)
    f1.overwrite(r)
    
def lire_map():
    d = f1.readfile()
    return d
    

clean() #manage test files and create map file in absent

if __name__ == '__main__':
    m = genere(3, '1')
    enregistrer_map(m)
    print(lire_map())
    





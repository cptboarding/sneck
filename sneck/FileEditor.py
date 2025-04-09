# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 09:58:41 2025

@author: albert.stnsl
"""


from typing import NamedTuple
import os
import printe



class FileNonexistant(Exception):
    pass

class OverwriteError(Exception):
    pass
    
class UnknownError(Exception):
    pass

class DeleteError(Exception):
    pass

class AssertError(Exception):
    pass

'''
Creation de nouveau fileeditor:

f = FileEditor(filename=str)

'''

class FileEditor(NamedTuple):
    filename: str
    
    #lit le fichier
    def readfile(self):
        try:
            f = open(self.filename, 'r')
        except:
            raise FileNonexistant()
        else:
            file = f.read()
            if file == '':
                return None
            else:
                return file
    
    #genere le fichier
    def create(self):
        try:
            f = open(self.filename, 'x')
        except:
            pass
        else:
            f.close()
            
    #supprime le fichier
    def delete(self):
        try:
            os.remove(self.filename)
        except:
            raise FileNonexistant()
    
    #supprime le contenu et ecrit un nouveau texte
    def overwrite(self, txt):
        self.readfile()
        try:
            f = open(self.filename, 'w')
            f.write(txt)
            f.close()
        except:
            raise OverwriteError()
           
    #ajoute du texte
    def append(self, txt):
        self.readfile()
        try:
            f = open(self.filename, 'a')
            f.write(txt)
            f.close()
        except:
            raise AssertError()
            
    #supprime le contenu
    def empty(self):
        self.overwrite('')
      
    #True = existe, False = nonexistant
    def assertfile(self):
        try:
            self.readfile()
        except:
            return False
        else:
            return True



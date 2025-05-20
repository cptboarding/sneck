"""
Programme qui gère les coordonnées des clones d'une longueur maximum donnée
"""

RIEN = " "


def supprimer_premier_element(collection):
	"""Supprime le premier élément d'une collection"""
	nouvelle_collection = []
	for i in range(len(collection)):
    		if i != 0:
        			nouvelle_collection.append(collection[i])
	return nouvelle_collection


def afficher_clones(console, caractere, y, x, clones, longueur_max):
	"""Change les coordonnées des clones, supprimme le dernier clone, et affiche le nouveaux clone"""
	if len(clones) > longueur_max:
    		console.addstr(clones[0][0], clones[0][1], RIEN)
    		clones = supprimer_premier_element(clones)
	clones.append((y, x))
	console.addstr(y, x, caractere)
	return clones

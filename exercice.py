#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import turtle
import math



# TODO: Définissez vos fonction ici
def volume(a=1, b=1, c=1, mv=2):
    volume = 4/3 * math.pi * a * b * c
    weight = mv * volume
    return volume, weight

def valide(valeur):
    liste = ["a", "t", "g", "c"]
    for c in valeur:
        if c not in liste:
            return False
    return True

def saisie(valeur):
    if valide(valeur):
        return valeur

def proportion(chaine, sequence): # grace au découpage en fonctions, c'est à la fin qu'on a rentré nos valeurs
    chaine1 = saisie(chaine)
    sequence1 = saisie(sequence)
    pourcentage = round(chaine1.count(sequence1) / len(chaine1) * 100, 2)
    print(f"Il y a {pourcentage} % de \"{sequence1}\".")


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    proportion("attgcaatggtggtacatg", "ca")

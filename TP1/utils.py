def somme_recursive(liste):
    if not liste:
        return 0
    return liste[0] + somme_recursive(liste[1:])

def calculer_moyenne(liste):
    if not liste:
        return 0
    return somme_recursive(liste) / len(liste)
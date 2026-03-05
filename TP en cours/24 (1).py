class Etudiant:
    def __init__(self):
        self.__cin = "K584613"
        self._cne = "P1147101045"
    def afficher_priver(self):
        return self.__cin
    
REDA = Etudiant()
print(REDA._Etudiant__cin)

#///////////////

class Cercle:
    def __init__(self, rayon):
        self._rayon = rayon

    @property
    def rayon(self):
        """Getter pour le rayon"""
        return self._rayon

    @property
    def aire(self):
        """Calcul de l'aire à la volée"""
        return 3.14159 * self._rayon ** 2

    @property
    def circonference(self):
        """Calcul de la circonférence"""
        return 2 * 3.14159 * self._rayon

cercle = Cercle(5)
print(f"Rayon: {cercle.rayon}")
print(f"Aire: {cercle.aire}")
print(f"Circonférence: {cercle.circonference}")
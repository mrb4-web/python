class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}"

Personne1 = Personne("Reda",22)
print(Personne1.se_presenter())

Personne2 = Personne("Mohamed",20)
print(Personne2.se_presenter())

Personne3 = Personne("Safouane",21)
print(Personne3.se_presenter())
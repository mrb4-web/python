class Membre:
    def __init__(self, nom, experience_ans):
        self.nom = nom
        self._experience = experience_ans 

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, valeur):
        # Validation : On ne peut pas avoir une expérience négative ou de plus de 60 ans
        if valeur < 0 or valeur > 60:
            raise ValueError("Expérience non valide")
        self._experience = valeur

    def description(self):
        return f"Nom: {self.nom}, Expérience: {self.experience} ans"

class Client(Membre):
    def __init__(self, nom, experience, id_abonnement):
        super().__init__(nom, experience)
        self.id_abonnement = id_abonnement

    def description(self):
        return f"[Client] {super().description()}, Badge: {self.id_abonnement}"

class Coach(Membre):
    def __init__(self, nom, experience, specialite):
        super().__init__(nom, experience)
        self.specialite = specialite

    def description(self):
        return f"[Coach] {super().description()}, Spécialité: {self.specialite}"

class CoachStagiaire(Client, Coach):
    def __init__(self, nom, experience, id_abonnement, specialite, mentor):
        # Initialisation propre pour l'héritage multiple
        Client.__init__(self, nom, experience, id_abonnement)
        Coach.__init__(self, nom, experience, specialite)
        self.mentor = mentor

    def description(self):
        # Appel direct à la classe de base pour éviter les répétitions de préfixes
        return (f"[Stagiaire] {Membre.description(self)}, "
                f"Badge: {self.id_abonnement}, "
                f"Focus: {self.specialite}, Mentor: {self.mentor}")

# --- Test des nouvelles données ---
sportif = Client("Yassine", 2, "FIT-2024")
entraineur = Coach("Sami", 12, "Crossfit")
hybride = CoachStagiaire("Lina", 1, "STAGE-05", "Yoga", "Mme. Sarah")

print(sportif.description())
print(entraineur.description())
print(hybride.description())
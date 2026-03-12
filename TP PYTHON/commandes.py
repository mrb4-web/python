from abc import ABC, abstractmethod
from typing import List
from boissons import Boisson
from clients import Client

class Commande(ABC):
    def __init__(self, client: Client):
        self.client = client  
        self.boissons: List[Boisson] = []  

    def ajouter_boisson(self, boisson: Boisson):
       
        self.boissons.append(boisson)

    def calculer_prix_total(self) -> float:
        
        return sum(boisson.cout() for boisson in self.boissons)
    
    @abstractmethod
    def afficher_commande(self):
        pass

class CommandeSurPlace(Commande):
   
    def afficher_commande(self):
        print(f"\n--- COMMANDE SUR PLACE ---")
        print(f"Client: {self.client.nom} (N{self.client.numero})")
        for boisson in self.boissons:
            print(f"Commande: {boisson.description()}")  
            print(f"Prix: {boisson.cout():.2f}€")  
        print(f"Total de la commande: {self.calculer_prix_total():.2f}")

class CommandeEmporter(Commande):
    
    def afficher_commande(self):
        print(f"\n--- COMMANDE À EMPORTER ---")
        print(f"Client: {self.client.nom} (N{self.client.numero})")
        for boisson in self.boissons:
            print(f"Commande: {boisson.description()} | Prix: {boisson.cout():.2f}")
        
        total = self.calculer_prix_total() + 0.50 
        print(f"Total de la commande (avec 0.50 de frais d'emballage): {total:.2f}")

class Fidelite:
    
    def ajouter_points(self, client: Client, montant_commande: float):
        points = int(montant_commande * 2) 
        client.points_fidelite += points
        print(f"\n[Fidelite] {points} points ajoutes. Nouveau solde de {client.nom} : {client.points_fidelite} points.")

class CommandeFidele(CommandeSurPlace, Fidelite):
   
    def valider_commande(self):
        self.afficher_commande()
      
        self.ajouter_points(self.client, self.calculer_prix_total())
from clients import Client
from boissons import Cafe, The
from ingredients import Lait, Sucre, Caramel
from commandes import CommandeFidele

if __name__ == "__main__":
    
    client_test = Client(nom="Mohamed Reda ", numero=1, points_fidelite=10)

   
   
    boisson1 = Cafe()
    boisson1 = Lait(boisson1)
    boisson1 = Sucre(boisson1)

    boisson2 = The()
    boisson2 = Caramel(boisson2)

    menu_duo = boisson1 + boisson2

    
    ma_commande = CommandeFidele(client=client_test)

   
    ma_commande.ajouter_boisson(boisson1)
    ma_commande.ajouter_boisson(menu_duo)

   
    print(f"--- Solde initial de {client_test.nom} : {client_test.points_fidelite} points ---")
    ma_commande.valider_commande()
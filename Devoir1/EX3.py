mot_de_passe_coorect = ["python123"]

mot = input("Entrez votre mot de passe : ")
while mot != mot_de_passe_coorect[0]:
    print("Mot de passe incorrect ! - Réssayer encore une fois !")
    mot = input("Entrez votre mot de passe : ")
print("Mot de passe correct !")

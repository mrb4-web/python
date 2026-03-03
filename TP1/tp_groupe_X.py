from donnees import donnees
from validation import valider
from utils import calculer_moyenne

# --- PARTIE 1 & 2 : Nettoyage et Structuration ---
valides = []
erreurs = []
doublons_exact = set()
vus = set()

for eng in donnees:
    if eng in vus:
        doublons_exact.add(eng)
    vus.add(eng)
    
    statut, raison = valider(eng)
    if statut:
        valides.append((eng[0], eng[1], float(eng[2]), eng[3]))
    else:
        erreurs.append({"ligne": eng, "raison": raison})


matieres_totales = {e[1] for e in valides}
etudiants_notes = {}
for nom, mat, note, grp in valides:
    if nom not in etudiants_notes: etudiants_notes[nom] = set()
    etudiants_notes[nom].add(mat)

print("--- RÉSULTATS ---")
print(f"Lignes valides : {len(valides)}")
print(f"Doublons exacts détectés : {len(doublons_exact)}")
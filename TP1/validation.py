def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if not nom or not matiere or not groupe:
        return (False, "raison: nom/matière/groupe vides")
    try:
        n = float(note)
        if not (0 <= n <= 20):
            return (False, "raison: note hors intervalle")
    except (ValueError, TypeError):
        return (False, "raison: note non numérique")
    return (True, "") 

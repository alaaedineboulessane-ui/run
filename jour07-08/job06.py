def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_suivant = ((note // 5) + 1) * 5
            if multiple_suivant - note < 3:
                notes_arrondies.append(multiple_suivant)
            else:
                notes_arrondies.append(note)
    return notes_arrondies
liste_notes = [33, 38, 82, 84, 87]
print(arrondir_notes(liste_notes))


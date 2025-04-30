def pievienot_sarakstam(saraksts, elements):
    """
    Funkcija pievieno elementu sarakstam.
    """
    saraksts.append(elements)
    return saraksts
def izvadit_sarakstu(saraksts):
    """
    Funkcija izvada sarakstu.
    """
    for elements in saraksts:
        print(elements)
        
pievienot_sarakstam([1,2,3], 4)
izvadit_sarakstu([1,2,3,4])
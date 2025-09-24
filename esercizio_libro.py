def STAMPA_DET(libro):
    print(libro.values())


LIBRERIA = {
    'INVENTARIO': [],
    'NOME_LIB': ""
}


# Inserimento dati libro
TITOLO1 = input("Titolo: ")
AUTORE1 = input("Autore: ")
ANNO_DI_PUBBL1 = input("Anno di pubblicazione: ")
ISBN1 = input("ISBN: ")

LIBRO = {
    'TITOLO': TITOLO1,
    'AUTORE': AUTORE1,
    'ANNO DI PUBBL': ANNO_DI_PUBBL1,
    'ISBN': ISBN1
}


def AGG_LIB(libro):
    LIBRERIA['INVENTARIO'].append(libro)


def RICERCA_ISBN():
    ISBN_SEARCH = input("Cerca ISBN: ")
    trovato = False
    for libro in LIBRERIA['INVENTARIO']:
        if ISBN_SEARCH == libro['ISBN']:
            print(libro)
            trovato = True
    if not trovato:
        print("NON PRESENTE")

def STAMPA_INV():
    for libro in LIBRERIA['INVENTARIO']:
        STAMPA_DET(libro)

# Esempio di utilizzo
AGG_LIB(LIBRO)
STAMPA_INV()
RICERCA_ISBN()

    
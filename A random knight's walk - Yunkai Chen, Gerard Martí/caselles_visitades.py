import random 
import yogi 

def generar_p_possibles(p0: tuple[int, int]) -> list[tuple[int, int]]:
    """En un tauler 8 x 8, retorna una llista amb totes les posicions on pot anar a parar un cavall desde la posicio donada."""
    p_possibles: list[tuple[int, int]] = []
    x, y = p0
    moviments_y = [2, 2, 1, -1, -2, -2, -1, 1]
    moviments_x = [-1, 1, 2, 2, 1, -1, -2, -2]
    for i in range(8):
        p = x + moviments_x[i], y + moviments_y[i]
        if all(0 <= coord <= 7 for coord in p):
            p_possibles.append(p) 

    return p_possibles

def seguent_salt(p: tuple[int, int]) -> tuple[int, int]:
    """Retorna una posicio qualsevol a la que el cavall hi pot anar desde p."""
    p_possibles = generar_p_possibles(p)
    return random.choice(p_possibles)

def llegir_p_inicial() -> tuple[int, int]:
    """Llegeix al terminal una posicio inicial en format coordenades d'escacs i retorna una tupla amb les mateixes coordenades pero en format numero."""
    p = yogi.read(str)
    assert len(p) == 2, 'Entrada incorrecta.'
    lletra = p[0].lower() 
    nombre = int(p[1])
    return nombre - 1 , ord(lletra) - 97 

def main() -> None:
    "Programa principal"
    n = yogi.read(int)
    p0 = llegir_p_inicial() 
    n_visites = [[0 for _ in range(8)] for _ in range(8)]
    x, y = p0
    n_visites[x][y] += 1

    for _ in range(n):
        p_triada = seguent_salt(p0)
        x, y = p_triada
        n_visites[x][y] += 1
        p0 = p_triada
    
    for fila in reversed(n_visites):
        print(fila)

if __name__ == '__main__':
    main()
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

def escriure(p: tuple[int, int]) -> None:
    """Escriu la posicio donada en el format desitjat."""
    x, y = p
    q = 'ABCDEFGH'[x], y + 1
    print(q, end='')

def main() -> None:
    "Programa principal"
    n = yogi.read(int)
    p0 = 0, 1
    for _ in range(n):
        p_possibles = generar_p_possibles(p0)
        p_triada = random.choice(p_possibles)
        print(' -> ', end = '')
        escriure(p_triada) 
        p0 = p_triada
    

if __name__ == '__main__':
    main()
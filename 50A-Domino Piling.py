"""You are given a rectangular board of M x N squares. Also you are given an unlimited number of standard domino pieces of 2 x 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.

Input
In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).

Output
Output one number — the maximal number of dominoes, which can be placed.

Examples
Input
2 4
Output
4
"""

def most_dominoes(m: int, n: int, acum: int):
    domino_largo = 2
    domino_ancho = 1
    if m > n:
        por_largo = m // domino_largo
        por_ancho = n // domino_ancho
        resto = m / domino_largo - por_largo
    else:
        por_ancho = m // domino_ancho
        por_largo = n // domino_largo
        resto = n / domino_largo - por_largo
        
    if resto == 0 or ((por_ancho) == 1 and resto*2 == 1) :
        return int(por_largo * por_ancho + acum)
    else:
        return most_dominoes(por_ancho, resto*2, (por_largo * por_ancho))
        

m, n = map(int, input().split(" "))

print(most_dominoes(m, n, 0)) 
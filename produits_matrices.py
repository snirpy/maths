matrix1 = [
    [1, 0, 2],
    [-1, 3, 1],
    [2, 2, 1]
]

matrix2 = [
    [3, 1, 4],
    [2, 0, 1],
    [0, 1, 5]
]

produit = []
for i in range(len(matrix1)):
    ligne = []
    for j in range(len(matrix2[0])):  # Corrigé pour parcourir le nombre de colonnes de matrix2
        result = 0
        for k in range(len(matrix2)):
            result += matrix1[i][k] * matrix2[k][j]
        ligne.append(result)
    produit.append(ligne)

# Affichage du résultat final sous forme de matrice
for row in produit:
    print(row)

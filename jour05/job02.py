def calcul(x, n):
    if n == 0:
        return 1
    else:
        return x * calcul(x, n - 1)

print(calcul(2, 2))

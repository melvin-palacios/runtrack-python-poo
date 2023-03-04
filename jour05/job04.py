import random
liste = []
for i in range(0, 30):
    liste.append(random.randint(0, 100))

def calcul(liste,i, max):
    if liste[i] == liste[-1]:
        return max
    else:
        if liste[i] > max:
            max = liste[i]
        return calcul(liste, i + 1, max)

print(liste)
print(calcul(liste, 0, 0))

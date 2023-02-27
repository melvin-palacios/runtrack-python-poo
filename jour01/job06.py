import time


class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def nommer(self, nom):
        self.prenom = nom
    def viellir(self):
        self.age += 1
        return ("L'age de " + self.prenom + " est " + str(self.age) + " ans")

Animal1 = Animal()
Animal1.nommer("Bob")

while True:
    print(Animal1.viellir())
    time.sleep(3)

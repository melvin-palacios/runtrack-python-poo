class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

Operation1 = Operation(1, 2)
print("Le nombre1 est " + str(Operation1.nombre1))
print("Le nombre2 est " + str(Operation1.nombre2))
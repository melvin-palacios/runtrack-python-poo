class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        return self.nombre1 + self.nombre2

Operation1 = Operation(1, 2)
print(Operation1.addition())
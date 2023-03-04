def run(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if safe_x(field, i, j):
                field[i][j] = "X"
            else:
                field[i][j] = "O"
    display_field(field)

def field_creation():
    size = input("Enter the size of the field: ")
    size = int(size)
    field = []
    for i in range(size):
        field.append([])
        for j in range(size):
            field[i].append("O")
    return field
def safe_x(field, x, y):
    for i in range(len(field)):
        if field[x][i] == "X":
            return False
    for i in range(len(field)):
        if field[i][y] == "X":
            return False
    diagonal = x - 1
    diagonal2 = x + 1
    for i in range(y - 1, -1, -1):
        if diagonal >= 0:
            if field[diagonal][i] == "X":
                return False
        if diagonal2 < len(field):
            if field[diagonal2][i] == "X":
                return False
        diagonal -= 1
        diagonal2 += 1
    return True

def display_field(field):
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end=" ")
        print()


run(field_creation())
def fibonacci(nb):
    if nb == 0:
        return 0
    elif nb == 1:
        return 1
    else:
        return fibonacci(nb - 1) + fibonacci(nb - 2)

print(fibonacci(10))
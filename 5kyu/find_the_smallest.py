def smallest(n):
    string = list(str(n))
    resultados = []

    for num in string:
        copia = string.copy()
        resultados.append(copia.pop(num))


numero = 261235
print(numero)
print(smallest(numero))
# refazer depois
# def decomp(n):
#     primos = []
#     divisores = []
#     for i in range(1, n+1):
#         if i == 1:
#             continue
#         else:
#             for j in range(1, i+1):
#                 if i % j == 0:
#                     divisores.append(j)
#             if len(divisores) == 2:
#                 primos.append(i)
#                 divisores.clear()
# execuçao muito lenta.

def decomp(n):
    primos = []
    for i in range(2, n+1):
        é_primo = True
        for j in range(2, int(i ** 0.5) + 1):  # ate aqui ja apareceu um 
            # divisor se tiver
            if i % j == 0:
                é_primo = False
                break
            if é_primo:
                primos.append(i)
    resultado = []

    for primo in primos:
        expoente = 0
        potencia = primo

        while potencia <= n:
            expoente += n // potencia
            potencia *= primo

        if expoente == 1:
            resultado.append(str(primo))
        else:
            resultado.append(f'{primo}^{expoente}')

    return ' * '.join(resultado)

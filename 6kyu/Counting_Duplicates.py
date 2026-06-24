def duplicate_count(text):
    texto = str(text.lower())
    duplicados = set()
    lista = []
    for caractere in texto:
        if caractere not in lista:
            lista.append(caractere)
        else:
            duplicados.add(caractere)
    return len(duplicados)


# melhor solução:

# def duplicate_count(text):
#     return len([i for i in set(text.lower()) if text.lower().count(i) > 1])

# resolution day 06/24
# def duplicate_count(text):
#     resultado = []
#     repetido = []
#     for i in text.upper():
#         if i not in resultado:
#             resultado.append(i)
#         else:
#             if i not in repetido:
#                 repetido.append(i)
#     return len(repetido)

def delete_nth(order, max_e):
    lista = []
    for numero in order:
        if numero not in lista:
            lista.append(numero)
        else:
            if lista.count(numero) >= max_e:
                continue
            else:
                lista.append(numero)
    return lista


# new resolution 24/06:

# def delete_nth(order, max_e):
#     no_repeat = []
#     for i in order:
#         if no_repeat.count(i) < max_e:
#             no_repeat.append(i)
#     return no_repeat
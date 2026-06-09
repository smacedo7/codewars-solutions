def delete_nth(order,max_e):
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
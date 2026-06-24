def duplicate_count(text):
    resultado = []
    repetido = []
    for i in text.upper():
        if i not in resultado:
            resultado.append(i)
        else:
            if i not in repetido:
                repetido.append(i)
    return len(repetido)


print(duplicate_count('abcde'))
print(duplicate_count('aabbcde'))
print(duplicate_count('aabBcde'))
print(duplicate_count('Indivisibilities'))
def in_array(array1, array2):
    sety = set()
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] in array2[j]:
                sety.add(array1[i])

    return sorted(sety)


# tempo recorde!

# new solution day 06/24

# def in_array(array1, array2):
#     words = set()
#     for i in array1:
#         for j in range(len(array2)):
#             if i in array2[j]:
#                 words.add(i)
#     lista = list(words)
#     return sorted(lista)
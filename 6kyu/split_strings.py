def solution(s):
    lista = []
    for i in range(0, len(s), 2):
        if i == len(s) - 1:
            lista.append(s[i] + '_')
        else:
            lista.append(s[i:i+2])
    return lista


# new resolution day 04/24new resolution day 04/24

# def solution(s):
#     lista = []
#     for i in range(0, len(s), 2):
#         if i == len(s) - 1:
#             lista.append(s[i] + '_')
#         else:
#             lista.append(s[i:i+2])
#     return lista
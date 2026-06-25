# Complete the solution so that it splits the string into strings of two
# characters in a list/array (depending on the language you use). If the
# string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

# def solution(s):
#     lista = []
#     for i in range(0, len(s) - 1, 2):
#         if len(s) % 2 == 0:
#             lista.append(s[i:i+2])
#         else:
#             if i == s[-1]:
#                 lista.append(s[i] + '_')
#             else:
#                 lista.append(s[i:i+2])
#     return lista

def solution(s):
    lista = []
    for i in range(0, len(s), 2):
        if i == len(s) - 1:
            lista.append(s[i] + '_')
        else:
            lista.append(s[i:i+2])
    return lista


print(solution('abcd'))
print(solution('abc'))
print(solution('abcdef'))
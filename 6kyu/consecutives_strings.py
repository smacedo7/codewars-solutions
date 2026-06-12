def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr) or len(strarr) == 0:
        return ""

    lista = []

    for i in range(len(strarr) - k + 1):
        soma = ''.join(strarr[i:i+k])
        lista.append(soma)

    maior = ""

    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra

    return maior

# exemplo : strarr = ["a", "b", "c", "d"], k = 2
# len(strarr) = 4, len(strarr) - k = 2, porem da ate 3 posiçoes
# ent len(strarr) - k + 1
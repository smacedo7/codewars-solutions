def spin_words(sentence):
    frases_splitadas = sentence.split()
    lista = []
    for palavra in frases_splitadas:
        if len(palavra) >= 5:
            palavra = palavra[::-1]
        lista.append(palavra)
    return ' '.join(lista)


# nova resoluçao dia 23/06:

# def spin_words(sentence):
#     return ' '.join([i[::-1] if len(i) >= 5 else i for i in sentence.split()])

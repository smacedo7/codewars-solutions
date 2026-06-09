def spin_words(sentence):
    frases_splitadas = sentence.split()
    lista = []
    for palavra in frases_splitadas:
        if len(palavra) >= 5:
            palavra = palavra[::-1]
        lista.append(palavra)
    return ' '.join(lista)

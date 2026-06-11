def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i + 1]) - ord(chars[i]) != 1:
            return chr(ord(chars[i]) + 1)


# ord(letra)  # letra -> número
# chr(numero) # número -> letra

# melhor resolução:
# def find_missing_letter(chars):
    # n = 0
    # while ord(chars[n]) == ord(chars[n+1]) - 1:
    #     n += 1
    # return chr(1+ord(chars[n]))

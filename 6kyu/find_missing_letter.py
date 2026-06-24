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

# new resolution day 06/24
# def find_missing_letter(chars):
#     string = ''
#     for i in range(0, len(chars) - 1):
#         if ord(chars[i+1]) - ord(chars[i]) != 1:
#             string += chars[i]

#     return chr(ord(string) + 1)


# print(find_missing_letter(['a','b','c','d','f']))
# print(find_missing_letter(['O','Q','R','S']))

def create_phone_number(n):
    parte1 = ''.join(str(x) for x in n[:3])
    parte2 = ''.join(str(x) for x in n[3:6])
    parte3 = ''.join(str(x) for x in n[6:])

    return f'({parte1}) {parte2}-{parte3}'


# resoluçao dia 23/06 
# def create_phone_number(n):
#     string = ''
#     for i in n:
#         string += str(i)
#     return f'({string[0:3]}) {string[3:6]}-{string[6:]}'


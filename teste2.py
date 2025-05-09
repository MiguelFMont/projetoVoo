listaNomeVerificacao = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', ' '
    ]

nome = 'á'
for letra in listaNomeVerificacao:
    if letra == nome:
        print('letra encontrada')
        break
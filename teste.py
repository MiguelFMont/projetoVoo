dicTeste = {
    'teste1': {
        'teste2': [
            'rio de janeiro', 'São Paulo'
        ]
    },

}

input = input('').title()
for i in dicTeste:
    print(i)
    for j in dicTeste[i]:
        print(j)
        for k in dicTeste[i][j]:
            if input in k:
                print(k)
            
            
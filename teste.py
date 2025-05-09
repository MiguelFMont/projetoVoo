dicRegioesBrasil = {
    'teste1': {
        'teste2': [
            'rio de janeiro', 'São Paulo'
        ]
    },

}
origem = ''
for regiao, in dicRegioesBrasil:
    for estado in dicRegioesBrasil[regiao]:
        for nomeEstado in dicRegioesBrasil[regiao][estado]:
            if origem in nomeEstado:
                print(f'Origem: {nomeEstado}')
                print(f'Região: {regiao}')
                print(f'Companhias Aéreas:')
                for companhia in dicRegioesBrasil[regiao]['companhias_aereas']:
                    print(f'- {companhia}')
                break
            
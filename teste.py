dicRegioesBrasil = {
    'Norte': {
        'estados': [
            'Acre (AC)', 'Amapá (AP)', 'Amazonas (AM)',
            'Pará (PA)', 'Rondônia (RO)', 'Roraima (RR)', 'Tocantins (TO)'
        ],
        'companhiasAereas': [
            'Azul Linhas Aéreas',
            'GOL Linhas Aéreas',
            'LATAM Brasil'
        ]
    },
    'Nordeste': {
        'estados': [
            'Alagoas (AL)', 'Bahia (BA)', 'Ceará (CE)', 'Maranhão (MA)',
            'Paraíba (PB)', 'Pernambuco (PE)', 'Piauí (PI)',
            'Rio Grande do Norte (RN)', 'Sergipe (SE)'
        ],
        'companhiasAereas': [
            'GOL Linhas Aéreas',
            'LATAM Brasil',
            'Azul Linhas Aéreas'
        ]
    },
    'Centro-Oeste': {
        'estados': [
            'Distrito Federal (DF)', 'Goiás (GO)',
            'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)'
        ],
        'companhiasAereas': [
            'GOL Linhas Aéreas',
            'LATAM Brasil',
            'Azul Linhas Aéreas',
            'Voepass' 
        ]
    },
    'Sudeste': {
        'estados': [
            'Espírito Santo (ES)', 'Minas Gerais (MG)',
            'Rio de Janeiro (RJ)', 'São Paulo (SP)'
        ],
        'companhiasAereas': [
            'GOL Linhas Aéreas',  
            'LATAM Brasil',       
            'Azul Linhas Aéreas',
            'Voepass'
        ]
    },
    'Sul': {
        'estados': [
            'Paraná (PR)', 'Rio Grande do Sul (RS)', 'Santa Catarina (SC)'
        ],
        'companhiasAereas': [
            'LATAM Brasil',
            'GOL Linhas Aéreas'
        ]
    }
}

origem = input('Origem: ')
destino = input('Destino: ')

for i in dicRegioesBrasil:
    if dicRegioesBrasil[i]['estados'].count(origem) == 1:
        companhiasOrigem = dicRegioesBrasil[i]['companhiasAereas']
    if dicRegioesBrasil[i]['estados'].count(destino) == 1:
        companhiasDestino = dicRegioesBrasil[i]['companhiasAereas']
if companhiasOrigem == companhiasDestino:
    print(f'Companhias aéreas disponíveis: {companhiasOrigem}')
    
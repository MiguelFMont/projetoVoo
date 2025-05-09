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
print(dicRegioesBrasil.values())
while True:
    origem = input("Digite o estado de origem (ou 'sair' para encerrar): ")
    if origem.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Normaliza a entrada do usuário (remove espaços extras e coloca em maiúsculas)
    origem = origem.strip()

    # Verifica se o estado está presente em alguma região
    estado_encontrado = False
    for regiao in dicRegioesBrasil.values():
        for estado in regiao['estados']:
            # Verifica se a entrada é exatamente igual ao estado ou à UF
            if origem.lower() == estado.lower() or origem.upper() in estado:
                estado_encontrado = True
                origem = estado  # Atualiza para o nome completo do estado
                break
        if estado_encontrado:
            break

    if not estado_encontrado:
        print("Estado inválido. Tente novamente.")
    else:
        print(f"Estado válido: {origem}.")
    
dicRegioesBrasil = {
    "Norte": {
        "estados": [
            "Acre (AC)", "Amapá (AP)", "Amazonas (AM)",
            "Pará (PA)", "Rondônia (RO)", "Roraima (RR)", "Tocantins (TO)"
        ],
        "companhias_aereas": [
            "Azul Linhas Aéreas",
            "GOL Linhas Aéreas",
            "LATAM Brasil"
        ]
    },
    "Nordeste": {
        "estados": [
            "Alagoas (AL)", "Bahia (BA)", "Ceará (CE)", "Maranhão (MA)",
            "Paraíba (PB)", "Pernambuco (PE)", "Piauí (PI)",
            "Rio Grande do Norte (RN)", "Sergipe (SE)"
        ],
        "companhias_aereas": [
            "GOL Linhas Aéreas",
            "LATAM Brasil",
            "Azul Linhas Aéreas"
        ]
    },
    "Centro-Oeste": {
        "estados": [
            "Distrito Federal (DF)", "Goiás (GO)",
            "Mato Grosso (MT)", "Mato Grosso do Sul (MS)"
        ],
        "companhias_aereas": [
            "GOL Linhas Aéreas",
            "LATAM Brasil",
            "Azul Linhas Aéreas",
            "Voepass" 
        ]
    },
    "Sudeste": {
        "estados": [
            "Espírito Santo (ES)", "Minas Gerais (MG)",
            "Rio de Janeiro (RJ)", "São Paulo (SP)"
        ],
        "companhias_aereas": [
            "GOL Linhas Aéreas",  
            "LATAM Brasil",       
            "Azul Linhas Aéreas",
            "Voepass"
        ]
    },
    "Sul": {
        "estados": [
            "Paraná (PR)", "Rio Grande do Sul (RS)", "Santa Catarina (SC)"
        ],
        "companhias_aereas": [
            "LATAM Brasil",
            "GOL Linhas Aéreas"
        ]
    }
}

origem = input('Digite a origem do voo: ').title()

encontrado = False  # flag para controle

for i in dicRegioesBrasil:
    for j in dicRegioesBrasil[i]:
        for k in dicRegioesBrasil[i][j]:
            if origem in k:
                print(f'Origem: {k}')
                print(f'Região: {i}')
                print(f'Companhias Aéreas: {dicRegioesBrasil[i]["companhias_aereas"]}')
                encontrado = True
                break


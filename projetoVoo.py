import os

passageiros = dict()
voos = dict()

listCaracteresEspeciais = ['.', '-', '(', ')',] 
listNumVerificacaoOptions = ['1', '2', '3', '4', '5']

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

dicAeroportos = {
    'norte': {
        'Acre': [
            'Aeroporto Internacional de Rio Branco - Plácido de Castro (RBR)',
            'Aeroporto Internacional de Cruzeiro do Sul (CZS)',
        ],
        'Amapá': [
            'Aeroporto Internacional de Macapá - Alberto Alcolumbre (MCP)',
            'Aeroporto de Oiapoque (Oiapoque)',
        ],
        'Amazonas': [
            'Aeroporto Internacional de Manaus - Eduardo Gomes (MAO)',
            'Aeroporto de Tabatinga (TBT)',
        ],
        'Pará': [
            'Aeroporto Internacional de Belém - Val de Cans (BEL)',
            'Aeroporto Internacional de Carajás (CKS)',
        ],
        'Rondônia': [
            'Aeroporto Internacional de Porto Velho - Governador Jorge Teixeira (PVH)',
            'Aeroporto de Ji-Paraná (JPR)',
        ],
        'Roraima': [
            'Aeroporto Internacional de Boa Vista - Atlas Brasil Cantanhede (BVB)',
            'Aeroporto de Bonfim (BON)',
        ],
        'Tocantins': [
            'Aeroporto Internacional de Palmas - Brigadeiro Lysias Rodrigues (PMW)',
            'Aeroporto de Araguaína (AXT)',
        ]
    },
    'nordeste': {
        'Alagoas': [
            'Aeroporto Internacional de Maceió - Zumbi dos Palmares (MCZ)',
            'Aeroporto de Arapiraca (APX)',
        ],
        'Bahia': [
            'Aeroporto Internacional de Salvador - Deputado Luís Eduardo Magalhães (SSA)',
            'Aeroporto de Porto Seguro (BPS)',
        ],
        'Ceará': [
            'Aeroporto Internacional de Fortaleza - Pinto Martins (FOR)',
            'Aeroporto de Juazeiro do Norte (JDO)',
        ],
        'Maranhão': [
            'Aeroporto Internacional de São Luís - Marechal Cunha Machado (SLZ)',
            'Aeroporto de Imperatriz (IMP)',
        ],
        'Paraíba': [
            'Aeroporto Internacional de João Pessoa - Presidente Castro Pinto (JPA)',
            'Aeroporto de Campina Grande (CPV)',
        ],
        'Pernambuco': [
            'Aeroporto Internacional do Recife - Gilberto Freyre (REC)',
            'Aeroporto de Caruaru (CAU)',
        ],
        'Piauí': [
            'Aeroporto Internacional de Teresina - Senador Petrônio Portella (THE)',
            'Aeroporto de Parnaíba (PHB)',
        ],
        'Rio Grande do Norte': [
            'Aeroporto Internacional de Natal - Governador Aluízio Alves (NAT)',
            'Aeroporto de Mossoró (MVF)',
        ],
        'Sergipe': [
            'Aeroporto Internacional de Aracaju - Santa Maria (AJU)',
            'Aeroporto de Estância (EST)'
        ]
    },
    'centro-oeste': {
        'Distrito Federal': [
            'Aeroporto Internacional de Brasília - Presidente Juscelino Kubitschek (BSB)',
            'Aeroporto de Luziânia (LUZ)',
        ],
        'Goiás': [
            'Aeroporto Internacional de Goiânia - Santa Genoveva (GYN)',
            'Aeroporto de Anápolis (ANP)',
        ],
        'Mato Grosso': [
            'Aeroporto Internacional de Cuiabá - Marechal Rondon (CGB)',
            'Aeroporto de Sinop (OPS)',
        ],
        'Mato Grosso do Sul': [
            'Aeroporto Internacional de Campo Grande - Antônio João (CGR)',
            'Aeroporto de Dourados (DOU)',
        ]
    },
    'sudeste': {
        'Espírito Santo': [
            'Aeroporto Internacional de Vitória - Eurico de Aguiar Salles (VIX)',
            'Aeroporto de Linhares (LHS)',
        ],
        'Minas Gerais': [
            'Aeroporto Internacional de Belo Horizonte - Tancredo Neves (CNF)',
            'Aeroporto de Uberlândia (UDI)',
        ],
        'Rio de Janeiro': [
            'Aeroporto Internacional do Rio de Janeiro - Galeão (GIG)',
            'Aeroporto Santos Dumont (SDU)',
        ],
        'São Paulo': [
            'Aeroporto Internacional de São Paulo - Guarulhos (GRU)',
            'Aeroporto de Congonhas (CGH)',
        ]
    },
    'sul': {
        'Paraná': [
            'Aeroporto Internacional de Curitiba - Afonso Pena (CWB)',
            'Aeroporto de Foz do Iguaçu (IGU)',
        ],
        'Rio Grande do Sul': [
            'Aeroporto Internacional de Porto Alegre - Salgado Filho (POA)',
            'Aeroporto de Caxias do Sul (CXJ)',
        ],
        'Santa Catarina': [
            'Aeroporto Internacional de Florianópolis - Hercílio Luz (FLN)',
            'Aeroporto de Navegantes (NVT)',
        ]
    }
}

contPessoas = 0
contVoo = 0

while True:
    print('''Escolha uma das opções a baixo:

1 - Cadastrar um passageiro
2 - Passageiros cadastrados
3 - Voos
4 - sair''')
    option = input('\n--> ')
    os.system('cls' if os.name == 'nt' else 'clear')

    while len(option) != 1 or option not in listNumVerificacaoOptions[0:4]:
        print('Opção inválida, por favor digite uma opção válida!')
        option = input('--> ')
    else:
        if option == '1':
            verifNumPessoas = False
            while verifNumPessoas == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                numPessoas = (input('Número de pessoas que deseja cadastrar: '))
                if numPessoas.isdigit() == False or int(numPessoas) < 1 or int(numPessoas) > 10:
                    print('Número inválido! É possível cadastrar até 10 pessoas por vez!')
                    input('Pressione ENTER para continuar...')
                    continue
                else:
                    verifNumPessoas = True
                    numPessoas = int(numPessoas)
                
            pessoas = 0

            while pessoas < numPessoas:
                print(f'\n{pessoas + 1}° Pessoa')

                verifNome = False

                while verifNome == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    nome = input('Digite seu nome: ').title()

                    contEspacosVazios = 0
                    contInvalido = 0

                    for caracter in nome:
                        if not caracter.isalpha() and not caracter.isspace():
                            contInvalido += 1
                        
                    if contInvalido > 0:
                        os.system('cls')
                        print(f'O nome não pode conter números ou caracteres especiais, por favor, digite novamente!\n')
                        input('Pressione ENTER para continuar...')
                        continue

                    if len(nome) < 10:
                        print('O nome deve conter ao menos 10 caracteres.')
                    elif contEspacosVazios > 5:
                        print('O nome não pode conter mais de 5 espaços.')
                        contEspacosVazios = 0
                        continue

                    if nome == '':
                        os.system('cls')
                        print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                        input('Pressione ENTER para continuar...')
                        continue
        
                    for i in nome:  
                        if i == ' ':
                            contEspacosVazios += 1

                    if len(nome) == (contEspacosVazios):
                            os.system('cls')
                            print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                            input('Pressione ENTER para continuar...')
                            contEspacosVazios = 0
                            continue
                    verifNome = True

                verifCpf = False

                while verifCpf == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cpf = input('Digite seu CPF: ')

                    if len(cpf) == 14:
                        contNumCpf = 0
                        contCarCpf = 0
                        for i in cpf:
                            if i.isdigit() == True:
                                contNumCpf += 1
                            if listCaracteresEspeciais.count(i) == 1:
                                contCarCpf += 1
                        if contNumCpf == 11 and contCarCpf == 3 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
                            if cpf in passageiros.keys():
                                print('\nCPF já cadastrado! Por favor, digite outro CPF!')
                                input('Pressione ENTER para continuar...')
                                continue
                            else:
                                verifCpf = True
                                continue
                        else:
                            print('CPF inválido, por favor digite o seu CPF!')
                            input('Pressione ENTER para continuar...')
                            continue

                    if len(cpf) == 11 and cpf.isdigit() == True:
                        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
                        if cpf in passageiros.keys():
                            print('\nCPF já cadastrado! Por favor, digite outro CPF!')
                            input('Pressione ENTER para continuar...')
                            continue
                        else:
                            verifCpf = True
                            continue
                    else:   
                        print('CPF inválido, por favor digite o seu CPF!')
                        input('Pressione ENTER para continuar...')
                        continue
                
                verifIdade = False

                while verifIdade == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    idade = input('Digite sua idade: ')
                    if idade.isdigit() == False or int(idade) < 0 or int(idade) > 120:
                        print('Idade inválida, por favor digite a sua idade!')
                        continue
                    else:
                        verifIdade = True

                verifTelefone = False
                while verifTelefone == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telefone = input('Digite telefone: ')
                    contTelefone = 0

                    if len(telefone) == 14:
                        contNumTel = 0
                        contCarTel = 0
                        for i in telefone:
                            if i.isdigit() == True:
                                contNumTel += 1
                            if listCaracteresEspeciais.count(i) == 1:
                                contCarTel += 1
                        if contNumTel == 11 and contCarTel == 3 and telefone[0] == '(' and telefone[3] == ')' and telefone[9] == '-':
                            for c in passageiros:
                                if telefone in passageiros[c]['telefone']:
                                    contTelefone += 1
                            if contTelefone > 0:
                                print('Telefone já cadastrado! Por favor, digite outro telefone!')
                                input('Pressione ENTER para continuar...')
                                continue
                            else:
                                verifTelefone = True
                                continue
                        else:
                            print('Telefone inválido, por favor digite o seu telefone!')
                            continue

                    if telefone.isdigit() and len(telefone) == 11:
                        telefone = '(' + telefone[0:2] + ')' + telefone[2:7] + '-' + telefone[7:11]
                        for c in passageiros:
                            if telefone in passageiros[c]['telefone']:
                                contTelefone += 1
                        if contTelefone > 0:
                            print('Telefone já cadastrado! Por favor, digite outro telefone!')
                            input('Pressione ENTER para continuar...')
                            continue
                        else:
                            verifTelefone = True
                            continue
                            
                    else:
                        print('Telefone inválido, por favor digite o seu telefone!')
                        input('Pressione ENTER para continuar...')
                        continue

                    
                passageiros[cpf] = {
                    'nome': nome,
                    'idade': idade,
                    'telefone': telefone
                }
                pessoas += 1
                contPessoas += 1
                ##input('Para onde vão: ')
        elif option == '2':
            if contPessoas == 0:
                print('\nNão há passageiros cadastrados, por favor cadastre um!')
                input('\nTecle enter para voltar!\n')
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                for c, dados in passageiros.items():
                    print('------------------')
                    print(f'cpf: {c}')
                    print(f'nome: {dados['nome']}')
                    print(f'idade: {dados['idade']}')
                    print(f'telefone: {dados['telefone']}')
                    print('------------------')
        elif option == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print('''Escolha uma das opções a baixo:
                    
1- Cadastrar um voo  
2- Consultar voos cadastrados
3- listar passageiros de um voo
4- 
                    ''')
                optionVoo = input('--> ')
                while len(optionVoo) != 1 or option not in listNumVerificacaoOptions[0:4]:
                    print('Opção inválida, por favor digite uma opção válida!')
                    optionVoo = input('--> ')
                else:

                    if optionVoo == '1':
                        print('CADASTRO DE VOO\n')
                        verifOrigem = False
                        while verifOrigem == False:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            origem = input('Digite a origem do voo: ').title()

                            if origem.isalpha() and len(origem) == 2:
                                origem = origem.upper()

                            if origem == '' or origem.isdigit() == True or len(origem) < 2 or len(origem) > 50:
                                print('Origem inválida, por favor, digite a origem do voo!')
                                input('Pressione ENTER para continuar...')
                                continue

                            else:
                                estadoNaoEncontrado = 0
                                os.system('cls' if os.name == 'nt' else 'clear')
                                for regiao in dicRegioesBrasil:
                                    for estado in dicRegioesBrasil[regiao]:
                                        for nomeEstado in dicRegioesBrasil[regiao][estado]:
                                            if nomeEstado.find(origem) != -1:
                                                print('------------------')
                                                print(f'Origem: {nomeEstado}')
                                                print(f'Região: {regiao}')
                                                print(f'Companhias Aéreas:')
                                                for companhia in dicRegioesBrasil[regiao]['companhiasAereas']:
                                                    print(f'- {companhia}')
                                                print('------------------')
                                                origem = nomeEstado
                                                verifOrigem = True
                                                break
                            if verifOrigem == False:
                                print('Origem não encontrada, por favor, digite a origem do voo!')
                                input('Pressione ENTER para continuar...')
                                continue
                        destino = input('Digite o destino do voo: ').title()
                        voos[destino] = {
                            'origem': origem,
                            'destino': destino,
                            'Companhia Aérea': companhia
                        }
                        contVoo += 1
                    elif optionVoo == '2':
                        if contVoo == 0:
                            print("\nNão há voos cadastrados, por favor cadastre um!")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Voos cadastrados:')
                            for c, dados in voos.items():
                                print('------------------')
                                print(f'Voo: {c}')
                                print(f'Origem: {dados['origem']}')
                                print(f'Destino: {dados['destino']}')
                                print(f'Companhia Aérea: {dados['companhiaAerea']}')
                                print('------------------')

        elif option == '4':
            print('Finalizando app...')
            break
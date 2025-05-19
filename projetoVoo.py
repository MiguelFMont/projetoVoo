import os

passageiros = dict()
voos = {}
lugares = 40
listaNumeroVerificacao = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.']
listCaracteresEspeciais = ['.', '-', '(', ')',] 
dicPassagensVoos = dict()

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
            
        ]
    },
    'Sul': {
        'estados': [
            'Paraná (PR)', 'Rio Grande do Sul (RS)', 'Santa Catarina (SC)'
        ],
        'companhiasAereas': [
            'GOL Linhas Aéreas',  
            'LATAM Brasil',       
            'Azul Linhas Aéreas',
        ]
    }
}

dicAeroportos = {
    'norte': {
        'Acre (AC)': [
            'Aeroporto Internacional de Rio Branco - Plácido de Castro (RBR)',
            'Aeroporto Internacional de Cruzeiro do Sul (CZS)',
        ],
        'Amapá (AP)': [
            'Aeroporto Internacional de Macapá - Alberto Alcolumbre (MCP)',
            'Aeroporto de Oiapoque (Oiapoque)',
        ],
        'Amazonas (AM)': [
            'Aeroporto Internacional de Manaus - Eduardo Gomes (MAO)',
            'Aeroporto de Tabatinga (TBT)',
        ],
        'Pará (PA)': [
            'Aeroporto Internacional de Belém - Val de Cans (BEL)',
            'Aeroporto Internacional de Carajás (CKS)',
        ],
        'Rondônia (RO)': [
            'Aeroporto Internacional de Porto Velho - Governador Jorge Teixeira (PVH)',
            'Aeroporto de Ji-Paraná (JPR)',
        ],
        'Roraima (RR)': [
            'Aeroporto Internacional de Boa Vista - Atlas Brasil Cantanhede (BVB)',
            'Aeroporto de Bonfim (BON)',
        ],
        'Tocantins (TO)': [
            'Aeroporto Internacional de Palmas - Brigadeiro Lysias Rodrigues (PMW)',
            'Aeroporto de Araguaína (AXT)',
        ]
    },
    'nordeste': {
        'Alagoas (AL)': [
            'Aeroporto Internacional de Maceió - Zumbi dos Palmares (MCZ)',
            'Aeroporto de Arapiraca (APX)',
        ],
        'Bahia (BA)': [
            'Aeroporto Internacional de Salvador - Deputado Luís Eduardo Magalhães (SSA)',
            'Aeroporto de Porto Seguro (BPS)',
        ],
        'Ceará (CE)': [
            'Aeroporto Internacional de Fortaleza - Pinto Martins (FOR)',
            'Aeroporto de Juazeiro do Norte (JDO)',
        ],
        'Maranhão (MA)': [
            'Aeroporto Internacional de São Luís - Marechal Cunha Machado (SLZ)',
            'Aeroporto de Imperatriz (IMP)',
        ],
        'Paraíba (PB)': [
            'Aeroporto Internacional de João Pessoa - Presidente Castro Pinto (JPA)',
            'Aeroporto de Campina Grande (CPV)',
        ],
        'Pernambuco (PE)': [
            'Aeroporto Internacional do Recife - Gilberto Freyre (REC)',
            'Aeroporto de Caruaru (CAU)',
        ],
        'Piauí (PI)': [
            'Aeroporto Internacional de Teresina - Senador Petrônio Portella (THE)',
            'Aeroporto de Parnaíba (PHB)',
        ],
        'Rio Grande do Norte (RN)': [
            'Aeroporto Internacional de Natal - Governador Aluízio Alves (NAT)',
            'Aeroporto de Mossoró (MVF)',
        ],
        'Sergipe (SE)': [
            'Aeroporto Internacional de Aracaju - Santa Maria (AJU)',
            'Aeroporto de Estância (EST)'
        ]
    },
    'centro-oeste': {
        'Distrito Federal (DF)': [
            'Aeroporto Internacional de Brasília - Presidente Juscelino Kubitschek (BSB)',
            'Aeroporto de Luziânia (LUZ)',
        ],
        'Goiás (GO)': [
            'Aeroporto Internacional de Goiânia - Santa Genoveva (GYN)',
            'Aeroporto de Anápolis (ANP)',
        ],
        'Mato Grosso (MT)': [
            'Aeroporto Internacional de Cuiabá - Marechal Rondon (CGB)',
            'Aeroporto de Sinop (OPS)',
        ],
        'Mato Grosso do Sul (MS)': [
            'Aeroporto Internacional de Campo Grande - Antônio João (CGR)',
            'Aeroporto de Dourados (DOU)',
        ]
    },
    'sudeste': {
        'Espírito Santo (ES)': [
            'Aeroporto Internacional de Vitória - Eurico de Aguiar Salles (VIX)',
            'Aeroporto de Linhares (LHS)',
        ],
        'Minas Gerais (MG)': [
            'Aeroporto Internacional de Belo Horizonte - Tancredo Neves (CNF)',
            'Aeroporto de Uberlândia (UDI)',
        ],
        'Rio de Janeiro (RJ)': [
            'Aeroporto Internacional do Rio de Janeiro - Galeão (GIG)',
            'Aeroporto Santos Dumont (SDU)',
        ],
        'São Paulo (SP)': [
            'Aeroporto Internacional de São Paulo - Guarulhos (GRU)',
            'Aeroporto de Congonhas (CGH)',
        ]
    },
    'sul': {
        'Paraná (PR)': [
            'Aeroporto Internacional de Curitiba - Afonso Pena (CWB)',
            'Aeroporto de Foz do Iguaçu (IGU)',
        ],
        'Rio Grande do Sul (RS)': [
            'Aeroporto Internacional de Porto Alegre - Salgado Filho (POA)',
            'Aeroporto de Caxias do Sul (CXJ)',
        ],
        'Santa Catarina (SC)': [
            'Aeroporto Internacional de Florianópolis - Hercílio Luz (FLN)',
            'Aeroporto de Navegantes (NVT)',
        ]
    }
}

contPessoas = 0
contVoo = 0

verifOption = False
while verifOption == False:


    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
        === MENU PRINCIPAL ===
          
Escolha uma das opções a baixo:

1 - Cadastrar um passageiro
2 - Passageiros cadastrados
3 - Voos
4 - Sair
        
        >>> Digite "-" caso queira voltar ao menu principal <<<''')
    
    option = input('\n--> ')

    os.system('cls' if os.name == 'nt' else 'clear')

    if len(option) != 1 or option not in listaNumeroVerificacao[0:4]:
        print('Opção inválida, por favor digite uma opção válida!')
        input('Pressione ENTER para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        if option == '1':
            verifNumPessoas = False
            while verifNumPessoas == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                numPessoas = (input('Número de pessoas que deseja cadastrar: '))
                if numPessoas == '-':
                    break

                if numPessoas.isdigit() == False or int(numPessoas) < 1 or int(numPessoas) > 10:
                    print('Número inválido! É possível cadastrar até 10 pessoas por vez!')
                    input('Pressione ENTER para continuar...')
                    continue
                else:
                    verifNumPessoas = True
                    numPessoas = int(numPessoas)
            
            if numPessoas == '-':
                continue
                
            pessoas = 0

            while pessoas < numPessoas:
                print(f'\n{pessoas + 1}° Pessoa')

                verifNome = False

                while verifNome == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    nome = input('Digite seu nome: ').title()

                    if nome == '-':
                        break

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

                if nome == '-':
                    break

                verifCpf = False
                while verifCpf == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cpf = input('Digite seu CPF: ')

                    if cpf == '-':
                        break

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

                if cpf == '-':
                    break
                
                verifIdade = False
                while verifIdade == False:
                    os.system('cls' if os.name == 'nt' else 'clear')

                    idade = input('Digite sua idade: ')

                    if idade == '-':
                        break

                    if idade.isdigit() == False or int(idade) < 0 or int(idade) > 120:
                        print('Idade inválida, por favor digite a sua idade!')
                        continue
                    else:
                        verifIdade = True

                if idade == '-':
                        break

                verifTelefone = False
                while verifTelefone == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telefone = input('Digite telefone: ')
                    contTelefone = 0

                    if telefone == '-':
                        break

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
                
                if telefone == '-':
                    break
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==================')
                print(f'Passageiro cadastrado com sucesso!')
                print(f'CPF: {cpf}')
                print(f'Nome: {nome}')
                print(f'Idade: {idade}')
                print(f'Telefone: {telefone}')
                print('==================')
                input('Pressione ENTER para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')

                passageiros[cpf] = {
                    'nome': nome,
                    'idade': idade,
                    'telefone': telefone
                }
                pessoas += 1
                contPessoas += 1
                
        elif option == '2':
            if contPessoas == 0:
                print('\nNão há passageiros cadastrados, por favor cadastre um!')
                input('\nTecle enter para voltar!\n')
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Listando de passageiros cadastrados ({contPessoas}):\n')
                for c, dados in passageiros.items():
                    print('==================')
                    print(f'CPF: {c}')
                    print(f'Nome: {dados['nome']}')
                    print(f'Idade: {dados['idade']}')
                    print(f'Telefone: {dados['telefone']}')
                    print('==================')
                input('Pressione ENTER para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')
        
        elif option == '3':
            os.system('cls' if os.name == 'nt' else 'clear')

            print('''
        == MENU DE VOOS ==

Escolha uma das opções a baixo:
            
1- Cadastrar um voo  
2- Consultar voos
3- Consultar passageiros de um voo
4- Passagens
5- Voltar ao menu principal
                    ''')
            verifOptionVoo = False
            while verifOptionVoo == False:
                optionVoo = input('--> ')

                if optionVoo == '-':
                    break

                if len(optionVoo) != 1 or option not in listaNumeroVerificacao[0:5]:
                    print('Opção inválida, por favor digite uma opção válida!')
                    continue
                else:
                    verifOptionVoo = True
            else:

                if optionVoo == '1':
                    print('CADASTRO DE VOO\n')

                    verifOrigem = False
                    while verifOrigem == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        origem = input('Digite o estado origem do voo: ').title()

                        if origem == '-':
                            break

                        if origem.isalpha() and len(origem) == 2:
                            origem = origem.upper()

                        if origem == '' or origem.isdigit() == True or len(origem) < 2 or len(origem) > 50:
                            print('Origem inválida, por favor, digite a origem do voo!')
                            input('Pressione ENTER para continuar...')
                            continue

                        else:
                        
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for regiao in dicRegioesBrasil:
                                for estado in dicRegioesBrasil[regiao]:
                                    for nomeEstado in dicRegioesBrasil[regiao][estado]:
                                        if nomeEstado.find(origem) != -1:
                                            print('==================')
                                            print(f'Origem: {nomeEstado}')
                                            print(f'Região: {regiao}')
                                            print(f'Companhias Aéreas:')
                                            for companhia in dicRegioesBrasil[regiao]['companhiasAereas']:
                                                print(f'- {companhia}')
                                            print('==================')
                                            origem = nomeEstado
                                            regiaoOrigem = regiao
                                            verifOrigem = True

                                            
                        if verifOrigem == False:
                            print('Origem não encontrada, por favor, digite a origem do voo!')
                            input('Pressione ENTER para continuar...')
                            continue
                        input('Pressione ENTER para continuar...')
                    
                    if origem == '-':
                        continue

                    verifDestino = False
                    while verifDestino == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        destino = input('Digite o estado destino do voo: ').title()

                        if destino == '-':
                            break

                        if destino.isalpha() and len(destino) == 2:
                            destino = destino.upper()

                        if destino == '' or destino.isdigit() or len(destino) < 2 or len(destino) > 50:
                            print('Destino inválido, por favor, digite o destino do voo!')
                            input('Pressione ENTER para continuar...')
                            continue

                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for regiao in dicRegioesBrasil:
                                for estado in dicRegioesBrasil[regiao]:
                                    for nomeEstado in dicRegioesBrasil[regiao][estado]:
                                        if nomeEstado.find(destino) != -1:
                                            print('==================')
                                            print(f'Destino: {nomeEstado}')
                                            print(f'Região: {regiao}')
                                            print(f'Companhias Aéreas:')
                                            for companhia in dicRegioesBrasil[regiao]['companhiasAereas']:
                                                print(f'- {companhia}')
                                            print('==================')
                                            destino = nomeEstado
                                            regiaoDestino =  regiao
                                            verifDestino = True

                        if verifDestino == False:
                            print('Destino não encontrado, por favor, digite o destino do voo!')
                            input('Pressione ENTER para continuar...')
                            continue
                        input('Pressione ENTER para continuar...')
                    
                    if destino == '-':
                            continue
                    
                    verifAeroportoOrigem = False
                    while verifAeroportoOrigem == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for regiao in dicAeroportos:
                            for estado in dicAeroportos[regiao]:
                                if estado == origem:
                                    print('==================')
                                    print(f'Origem: {estado}')
                                    print(f'Região: {regiao}')
                                    print('Aeroportos:')
                                    contAerosportos = 1
                                    for aeroportosEstados in dicAeroportos[regiao][estado]:
                                        aeroportos = aeroportosEstados
                                        print(f'{contAerosportos} - {aeroportos}')
                                        contAerosportos += 1
                                    print('==================')
                                    selectAeroportoOrigem = input('\nSelecione o aeroporto de origem: ')

                                    if selectAeroportoOrigem == '-':
                                        verifAeroportoOrigem = True
                                        break

                                    if selectAeroportoOrigem.isdigit() == False or int(selectAeroportoOrigem) > contAerosportos or int(selectAeroportoOrigem) < 0 or selectAeroportoOrigem == '' or selectAeroportoOrigem not in listaNumeroVerificacao[0:2]:
                                        print('Aeroporto inválido, por favor digite o aeroporto de origem!')
                                        input('Pressione ENTER para continuar...')
                                        continue
                                    else:
                                        verifAeroportoOrigem = True
                                        if selectAeroportoOrigem == '1':
                                            selectAeroportoOrigem = dicAeroportos[regiao][estado][0]
                                        elif selectAeroportoOrigem == '2':
                                            selectAeroportoOrigem = dicAeroportos[regiao][estado][1]
                                        elif selectAeroportoOrigem == '3':
                                            selectAeroportoOrigem = dicAeroportos[regiao][estado][2]
                                        print(f'Aeroporto de origem escolhido: {selectAeroportoOrigem}')
                                        input('Pressione ENTER para continuar...')
                    
                    if selectAeroportoOrigem == '-':
                        continue

                    verifAeroportoDestino = False
                    while verifAeroportoDestino == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for regiao in dicAeroportos:
                            for estado in dicAeroportos[regiao]:
                                if estado == destino:
                                    print('==================')
                                    print(f'Destino: {estado}')
                                    print(f'Região: {regiao}')
                                    print('Aeroportos:')
                                    contAerosportos = 1
                                    for aeroportosEstados in dicAeroportos[regiao][estado]:
                                        aeroportos = aeroportosEstados
                                        print(f'{contAerosportos} - {aeroportos}')
                                        contAerosportos += 1
                                    print('==================')
                                    selectAeroportoDestino = input('\nSelecione o aeroporto de Destino: ').title()

                                    if selectAeroportoDestino == '-':
                                        verifAeroportoDestino = True
                                        break

                                    if selectAeroportoDestino.isdigit() == False or int(selectAeroportoDestino) > contAerosportos or int(selectAeroportoDestino) < 0 or selectAeroportoDestino == '' or selectAeroportoDestino not in listaNumeroVerificacao[0:2]:
                                        print('Aeroporto inválido, por favor digite o aeroporto de destino!')
                                        input('Pressione ENTER para continuar...')
                                        continue
                                    else:
                                        verifAeroportoDestino = True
                                        if selectAeroportoDestino == '1':
                                            selectAeroportoDestino = dicAeroportos[regiao][estado][0]
                                        elif selectAeroportoDestino == '2':
                                            selectAeroportoDestino = dicAeroportos[regiao][estado][1]
                                        print(f'Aeroporto de destino escolhido: {selectAeroportoDestino}')
                                        input('Pressione ENTER para continuar...')

                    if selectAeroportoDestino == '-':
                        continue

                    verifDataHora = False
                    while verifDataHora == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        dataHora = input('Informe a data e hora (formato: DD/MM/AAAA HH:MM): ')

                        if dataHora == '-':
                            break

                        if len(dataHora) > 16:
                            print(f'Data inválida!')
                            input(f'Pressione ENTER para continuar...')
                            continue

                        if dataHora == '':
                            print(f'Data e horas são obrigatórias!\n')
                            continue

                        if ' ' in dataHora:
                            data, hora = dataHora.split(' ')

                            if '/' in data and ':' in hora:
                                dia, mes, ano = data.split('/')
                                hora, minuto = hora.split(':')

                                if dia.isdigit() and mes.isdigit() and ano.isdigit() and hora.isdigit() and minuto.isdigit():
                                    dia = int(dia)
                                    mes = int(mes)
                                    ano = int(ano)
                                    hora = int(hora)
                                    minuto = int(minuto)

                                    if 1 <= dia <= 31 and 1 <= mes <= 12 and 0 <= hora <= 23 and 0 <= minuto <= 59:
                                        if mes in [4, 6, 9, 11] and dia > 30:
                                            print('Este mês tem no máximo 30 dias.')
                                        elif mes == 2 and dia > 28:
                                            if ano % 4 == 0 and dia > 29:
                                                print('Fevereiro tem no máximo 29 dias.')
                                            else:
                                                print('Fevereiro tem no máximo 28 dias.')

                                        
                                        else:
                                            verifDataHora = True

                                    else:
                                        print('Algum valor está fora dos limites permitidos.')
                                else:
                                    print('Todos os campos devem ser números.')
                            else:
                                print('Formato incorreto. Use DD/MM/AAAA HH:MM.')
                        else:
                            print('Formato incorreto. Use DD/MM/AAAA HH:MM.')

                    if dataHora == '-':
                            continue
                    
                    verifCompanhia = False
                    while verifCompanhia == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Companhias Aéreas diponíveis para a origem e destino escolhidos:')
                        contCompanhia = 1
                        for regiao in dicRegioesBrasil:
                            for estado in dicRegioesBrasil[regiao]:
                                for nomeEstado in dicRegioesBrasil[regiao][estado]:
                                    if nomeEstado.find(origem) != -1:
                                        print('==================')
                                        for companhia in dicRegioesBrasil[regiao]['companhiasAereas']:
                                            print(f'{contCompanhia} - {companhia}')
                                            contCompanhia += 1
                                        print('==================')
                                        companhia = input('Digite a companhia aérea: ').title()

                                        if companhia == '-':
                                            verifCompanhia = True
                                            break

                                        if companhia.isdigit() == False or int(companhia) > contCompanhia or int(companhia) < 0 or companhia == '' :
                                            print('Companhia inválida, por favor digite a companhia do voo!')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        else:
                                            verifCompanhia = True
                                            if companhia == '1':
                                                companhia = dicRegioesBrasil[regiao]['companhiasAereas'][0]
                                            elif companhia == '2':
                                                companhia = dicRegioesBrasil[regiao]['companhiasAereas'][1]
                                            elif companhia == '3':
                                                companhia = dicRegioesBrasil[regiao]['companhiasAereas'][2]
                                            print(f'Companhia escolhida: {companhia}')
                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')

                    if companhia == '-':
                        continue

                    print('==================')
                    print(f'Voo cadastrado com sucesso!')
                    print(f'Código do voo: v-{contVoo + 1}\n')
                    print(f'Origem: {origem}')
                    print(f'Destino: {destino}\n')
                    print(f'Aeroporto de origem: {selectAeroportoOrigem}')
                    print(f'Aeroporto de destino: {selectAeroportoDestino}\n')

                    if origem == destino:
                        print('Número de escalas: 0')
                        escalas = 0
                    else:
                        if regiaoOrigem == regiaoDestino:
                            print('Número de escalas: 1')
                            escalas = 1
                        else:
                            print('Número de escalas: 2')
                            escalas = 2

                    if origem == destino:
                        print(f'Preço da passagem: R$ 1.500,00')
                        precoPassagem = 'R$ 1.500,00'
                    else:
                        
                        if regiaoOrigem == regiaoDestino:
                            print(f'Preço da passagem: R$ 2.000,00')
                            precoPassagem = 'R$ 2.000,00'
                        else:
                            print(f'Preço da passagem: R$ 2.500,00')
                            precoPassagem = 'R$ 2.500,00'
                        
                    print(f'Número de lugares disponíveis: {lugares}')
                    print(f'Data e hora do voo: {dataHora}\n')
                    print(f'Companhia Aérea: {companhia}')
                    print('==================')
                    input('Pressione ENTER para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    contVoo += 1
                    voos['v-' + str(contVoo)] = {
                        'origem': origem,
                        'destino': destino,
                        'aeroportoDeOrigem': selectAeroportoOrigem,
                        'aeroportoDeDestino': selectAeroportoDestino,
                        'escalas': escalas,
                        'precoPassagem': precoPassagem,
                        'lugares': lugares,
                        'dataHora': dataHora,
                        'companhiaAerea': companhia
                    }

                elif optionVoo == '2':
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    if contVoo == 0:
                        print('\nNão há voos cadastrados, por favor cadastre um!')
                        input(f'Pressione ENTER para continuar...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    else:
                        verifSelectConsultaVoo = False
                        while verifSelectConsultaVoo == False:
                            print('Selecione uma opção de consulta por:')
                            print('''
1 - Código do voo
2 - Origem
3 - Destino
4 - Listar voos com menor escala (até 1 escala)
5 - Listar todos os voos''')
                            selectConsultaVoo = input('--> ')

                            if selectConsultaVoo == '-':
                                break

                            if selectConsultaVoo == '' or selectConsultaVoo not in listaNumeroVerificacao[0:5]:
                                print(f'Opção inválida! Por favor, digite somente uma das opções disponíveis (1, 2, 3, 4 ou 5)')
                                input(f'Pressione ENTER para continuar...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                                continue

                            else:
                                verifSelectConsultaVoo = True

                                if selectConsultaVoo == '1':

                                    verifVooConsulta = False
                                    while verifVooConsulta == False:
                                        vooConsulta = input('Digite o código do voo que deseja consultar. Ex: v-1: ')

                                        if vooConsulta == '-':
                                            break

                                        if vooConsulta == '' or vooConsulta[0] != 'v' or vooConsulta[1] != '-' or vooConsulta[2:].isdigit() == False:
                                            print('Código inválido, por favor digite o código do voo!')
                                            continue
                                        else:
                                            print('Voos cadastrados:')
                                            if vooConsulta in voos.keys():
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                print('\n\n==================')
                                                print(f'Código do voo: {vooConsulta}\n')
                                                print(f'Origem: {voos[vooConsulta]['origem']}')
                                                print(f'Destino: {voos[vooConsulta]['destino']}\n')
                                                print(f'Aeroporto de origem: {voos[vooConsulta]['aeroportoDeOrigem']}')
                                                print(f'Aeroporto de destino: {voos[vooConsulta]['aeroportoDeDestino']}\n')
                                                print(f'Número de escalas: {voos[vooConsulta]['escalas']}')
                                                print(f'Preço da passagem:  {voos[vooConsulta]['precoPassagem']}')
                                                print(f'Número de lugares disponíveis: {voos[vooConsulta]['lugares']}')
                                                print(f'Data e hora do voo: {voos[vooConsulta]['dataHora']}\n')
                                                print(f'Companhia Aérea: {voos[vooConsulta]['companhiaAerea']}')
                                                print('==================\n')
                                                verifVooConsulta = True    
                                            else:
                                                print(f'Código não encontrado! Digite novamente.\n')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue

                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                

                                elif selectConsultaVoo == '2':
                                    verifConsultaOrigem = False
                                    while verifConsultaOrigem == False:
                                        print(f'Consultar voos pela origem..\n')
                                        consultaOrigem = input(f'Digite a origem:  ').title()

                                        if consultaOrigem == '-':
                                            break

                                        if consultaOrigem.isalpha() and len(consultaOrigem) == 2:
                                            consultaOrigem = consultaOrigem.upper()

                                        if consultaOrigem == '' or consultaOrigem.isdigit() == True or len(consultaOrigem) < 2 or len(consultaOrigem) > 50:
                                            print('Origem inválida, por favor, digite a Origem do voo!')
                                            input('Pressione ENTER para continuar...')
                                            continue

                                        else:
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            for cod in voos:
                                                if consultaOrigem in voos[cod]['origem']:
                                                    print('==================')
                                                    print(f'Código do voo: {cod}\n')
                                                    print(f'Origem: {voos[cod]['origem']}')
                                                    print(f'Destino: {voos[cod]['destino']}\n')
                                                    print(f'Aeroporto de origem: {voos[cod]['aeroportoDeOrigem']}')
                                                    print(f'Aeroporto de destino: {voos[cod]['aeroportoDeDestino']}\n')
                                                    print(f'Número de escalas: {voos[cod]['escalas']}')
                                                    print(f'Preço da passagem:  {voos[cod]['precoPassagem']}')
                                                    print(f'Número de lugares disponíveis: {voos[cod]['lugares']}')
                                                    print(f'Data e hora do voo: {voos[cod]['dataHora']}\n')
                                                    print(f'Companhia Aérea: {voos[cod]['companhiaAerea']}')
                                                    print('==================\n')
                                                    verifConsultaOrigem = True  

                                            if verifConsultaOrigem:
                                                input(f'Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                    
                                        if not verifConsultaOrigem:
                                            print(f'Origem não encontrada! Por favor, digite novamente.')
                                            input(f'Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                                

                                elif selectConsultaVoo == '3':
                                    verifConsultaDestino = False
                                    while verifConsultaDestino == False:
                                        print(f'Consultar voos pelo Destino..\n')
                                        consultaDestino = input(f'Digite o destino:  ').title()

                                        if consultaDestino == '-':
                                            break

                                        if consultaDestino.isalpha() and len(consultaDestino) == 2:
                                            consultaDestino = consultaDestino.upper()

                                        if consultaDestino == '' or consultaDestino.isdigit() == True or len(consultaDestino) < 2 or len(consultaDestino) > 50:
                                            print('Destino inválido, por favor, digite o destino do voo!')
                                            input(f'Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue
                                        else:
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            for cod in voos:
                                                if consultaDestino in voos[cod]['destino']:
                                                    print('==================')
                                                    print(f'Código do voo: {cod}\n')
                                                    print(f'Origem: {voos[cod]['origem']}')
                                                    print(f'Destino: {voos[cod]['destino']}\n')
                                                    print(f'Aeroporto de origem: {voos[cod]['aeroportoDeOrigem']}')
                                                    print(f'Aeroporto de destino: {voos[cod]['aeroportoDeDestino']}\n')
                                                    print(f'Número de escalas: {voos[cod]['escalas']}')
                                                    print(f'Preço da passagem:  {voos[cod]['precoPassagem']}')
                                                    print(f'Número de lugares disponíveis: {voos[cod]['lugares']}')
                                                    print(f'Data e hora do voo: {voos[cod]['dataHora']}\n')
                                                    print(f'Companhia Aérea: {voos[cod]['companhiaAerea']}')
                                                    print('==================\n')
                                                    verifConsultaDestino = True
                                            if verifConsultaDestino:
                                                input(f'Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')

                                        if not verifConsultaDestino:
                                            print(f'Origem não encontrada! Por favor, digite novamente.')
                                            input(f'Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')

                                elif selectConsultaVoo == '4':
                                    verifConsultaEscala = False
                                    while verifConsultaEscala == False:
                                        print('''Consultar voos com menor escala pelo(a):
1 - Origem
2 - Destino
''')   
                                        consultaEscala = input('--> ')

                                        if consultaEscala == '-':
                                            break

                                        if consultaEscala == '' or consultaEscala not in listaNumeroVerificacao[0:3]:
                                            print('Opção inválida! Por favor, digite somente uma das opções disponíveis (1, 2)')
                                            input(f'Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue
                                        else:
                                            verifConsultaEscala = True
                                            if consultaEscala == '1':
                                                verifConsultaEscalaOrigem = False
                                                while verifConsultaEscalaOrigem == False:
                                                    consultaEscalaOrigem = input(f'Digite a origem:  ').title()

                                                    if consultaEscalaOrigem == '-':
                                                        break

                                                    if consultaEscalaOrigem.isalpha() and len(consultaEscalaOrigem) == 2:
                                                        consultaEscalaOrigem = consultaEscalaOrigem.upper()

                                                    if consultaEscalaOrigem == '' or consultaEscalaOrigem.isdigit() == True or len(consultaEscalaOrigem) < 2 or len(consultaEscalaOrigem) > 50:
                                                        print('Origem inválida, por favor, digite a origem do voo!')
                                                        input(f'Pressione ENTER para continuar...')
                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                                        continue
                                                    else:
                                                        
                                                        for cod in voos:
                                                            if consultaEscalaOrigem in voos[cod]['origem']:
                                                                if voos[cod]['escalas'] < 2:

                                                                    print('==================')
                                                                    print(f'Código do voo: {cod}\n')
                                                                    print(f'Origem: {voos[cod]['origem']}')
                                                                    print(f'Destino: {voos[cod]['destino']}\n')
                                                                    print(f'Aeroporto de origem: {voos[cod]['aeroportoDeOrigem']}')
                                                                    print(f'Aeroporto de destino: {voos[cod]['aeroportoDeDestino']}\n')
                                                                    print(f'Número de escalas: {voos[cod]['escalas']}')
                                                                    print(f'Preço da passagem:  {voos[cod]['precoPassagem']}')
                                                                    print(f'Número de lugares disponíveis: {voos[cod]['lugares']}')
                                                                    print(f'Data e hora do voo: {voos[cod]['dataHora']}\n')
                                                                    print(f'Companhia Aérea: {voos[cod]['companhiaAerea']}')
                                                                    print('==================\n')
                                                                    verifConsultaEscalaOrigem = True
                                                    
                                                    if not verifConsultaEscalaOrigem:
                                                        print(f'Origem não encontrada ou voo possuí mais de uma escala! Por favor, digite novamente.')
                                                        input(f'Pressione ENTER para continuar...')
                                                        os.system('cls' if os.name == 'nt' else 'clear')

                                            elif consultaEscala == '2':
                                                verifConsultaEscalaDestino = False
                                                while verifConsultaEscalaDestino == False:
                                                    consultaEscalaDestino = input(f'Digite o Destino:  ').title()

                                                    if consultaEscalaDestino == '-':
                                                        break

                                                    if consultaEscalaDestino.isalpha() and len(consultaEscalaDestino) == 2:
                                                        consultaEscalaDestino = consultaEscalaDestino.upper()

                                                    if consultaEscalaDestino == '' or consultaEscalaDestino.isdigit() == True or len(consultaEscalaDestino) < 2 or len(consultaEscalaDestino) > 50:
                                                        print('Destino inválido, por favor, digite o destino do voo!')
                                                        input(f'Pressione ENTER para continuar...')
                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                                        continue
                                                    else:
                                                        
                                                        for cod in voos:
                                                            if consultaEscalaDestino in voos[cod]['destino']:
                                                                if voos[cod]['escalas'] < 2:
                                                                    print('==================')
                                                                    print(f'Código do voo: {cod}\n')
                                                                    print(f'Origem: {voos[cod]['origem']}')
                                                                    print(f'Destino: {voos[cod]['destino']}\n')
                                                                    print(f'Aeroporto de origem: {voos[cod]['aeroportoDeOrigem']}')
                                                                    print(f'Aeroporto de destino: {voos[cod]['aeroportoDeDestino']}\n')
                                                                    print(f'Número de escalas: {voos[cod]['escalas']}')
                                                                    print(f'Preço da passagem:  {voos[cod]['precoPassagem']}')
                                                                    print(f'Número de lugares disponíveis: {voos[cod]['lugares']}')
                                                                    print(f'Data e hora do voo: {voos[cod]['dataHora']}\n')
                                                                    print(f'Companhia Aérea: {voos[cod]['companhiaAerea']}')
                                                                    print('==================\n')
                                                                    verifConsultaEscalaDestino = True
                                                    
                                                    if not verifConsultaEscalaDestino:
                                                        print(f'Destino não encontrado! Por favor, digite novamente.')
                                                        input(f'Pressione ENTER para continuar...')
                                                        os.system('cls' if os.name == 'nt' else 'clear')

                                        input(f'Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')

                                elif selectConsultaVoo == '5':
                                    print(f'Listando todos os voos..')
                                    for cod, dados in voos.items():
                                        print('==================')
                                        print(f'Código do voo: {cod}\n')
                                        print(f'Origem: {dados['origem']}')
                                        print(f'Destino: {dados['destino']}\n')
                                        print(f'Aeroporto de origem: {dados['aeroportoDeOrigem']}')
                                        print(f'Aeroporto de destino: {dados['aeroportoDeDestino']}\n')
                                        print(f'Número de escalas: {dados['escalas']}')
                                        print(f'Preço da passagem:  {dados['precoPassagem']}')
                                        print(f'Número de lugares disponíveis: {dados['lugares']}')
                                        print(f'Data e hora do voo: {dados['dataHora']}\n')
                                        print(f'Companhia Aérea: {dados['companhiaAerea']}')
                                        print('==================\n')
                                    input(f'Pressione ENTER para continua...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                
                elif optionVoo == '3':
                    if contVoo == 0:
                        print('\nAinda não há voos cadastrados!')
                        input('Pressione ENTER para continuar...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        verifOptionPassageirosVoo = False
                        while verifOptionPassageirosVoo == False:
                            print(f'Deseja listar todos os voos?')
                            print('''
1 - Sim
2 - Não''')
                            optionListarVoos = input('--> ')

                            if optionListarVoos == '-':
                                break

                            if len(optionListarVoos) != 1 or optionListarVoos not in listaNumeroVerificacao[0:2]:
                                print('Opção inválida, por favor digite uma opção válida!')
                                continue
                            else:
                                if optionListarVoos == '1':
                                    contVooLotado = 0
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('Listando voos com passageiros...')
                                    if len(dicPassagensVoos) > 0:
                                        for voo in dicPassagensVoos:
                                            print(f'{voo}: {len(dicPassagensVoos[voo])} passageiros')
                                            optionListarVoos = '2'
                                            verifOptionPassageirosVoo = True
                                    else:
                                        print(f'Não há voos com passageiros cadastrados!')
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        break                  
                                if optionListarVoos == '2':

                                    verifCodVoo = False
                                    while verifCodVoo == False:

                                        codVoo = input('Digite o código do voo que deseja exibir os passageiros. Ex: v-1: ')

                                        if codVoo == '-':
                                            break

                                        if codVoo == '' or codVoo not in voos.keys():
                                            print('Código inválido, por favor digite o código do voo!')
                                            continue
                                        else:
                                            verifOptionPassageirosVoo = True
                                            if codVoo in dicPassagensVoos.keys():
                                                for codigo in dicPassagensVoos:
                                                    if codVoo == codigo:
                                                        print('==================')
                                                        print(f'Código do voo: {codVoo}\n')
                                                        print(f'Número de passageiros: {len(dicPassagensVoos[codigo])}')
                                                        print('==================\n')
                                                        for c, dados in dicPassagensVoos[codigo].items():
                                                            print('==================')
                                                            print(f'CPF: {c}')
                                                            print(f'Nome: {dados}')
                                                            print('==================')
                                                        verifCodVoo = True
                                            else:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                print('Código do voo inválido, por favor digite o código do voo!')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                elif optionVoo == '4':

                    if contVoo == 0:
                        print('\nAinda não há voos cadastrados!')
                        input('Pressione ENTER para continuar...')
                    else:
                        
                        verifMenuPassagem = False
                        while verifMenuPassagem == False:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('''
        === MENU DE PASSAGENS ===
1 - Comprar passagem
2 - Cancelar passagem
3 - Voltar ao menu principal
                            ''')
                            opcaoPassagem = input('--> ')

                            if opcaoPassagem == '-':
                                break

                            if len(opcaoPassagem) != 1 or opcaoPassagem not in ['1', '2', '3']:
                                print('Opção inválida, por favor digite uma opção válida!')
                                input('Pressione ENTER para continuar...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                                continue

                            if opcaoPassagem == '1':
                                
                                verifCodVoo = False
                                while verifCodVoo == False:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('Voos disponíveis:')
                                    for codVoo, dadosVoo in voos.items():
                                        print(f'{codVoo}: {dadosVoo['origem']} -> {dadosVoo['destino']} | Lugares: {dadosVoo['lugares']}')
                                
                                    codVoo = input('Digite o código do voo desejado: ')

                                    if codVoo == '-':
                                        break

                                    if codVoo not in voos or codVoo == '':
                                        print('Código de voo inválido!')
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        continue

                                    if voos[codVoo]['lugares'] <= 0:
                                        print('Não há lugares disponíveis neste voo!')
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        continue

                                    verifCodVoo = True

                                verifCpfVenda = False
                                while verifCpfVenda == False:
                                    cpfVenda = input('Digite o CPF do passageiro: ')

                                    if cpfVenda == '-':
                                        break
                                    
                                    if len(cpfVenda) == 14:
                                        contNumCpf = 0
                                        contCarCpf = 0
                                        for i in cpfVenda:
                                            if i.isdigit():
                                                contNumCpf += 1
                                            if listCaracteresEspeciais.count(i) == 1:
                                                contCarCpf += 1

                                        if contNumCpf == 11 and contCarCpf == 3 and cpfVenda[3] == '.' and cpfVenda[7] == '.' and cpfVenda[11] == '-':
                                            cpfVendaFormatado = cpfVenda
                                            verifCpfVenda = True
                                        else:
                                            print('CPF inválido, por favor digite novamente!')
                                            input('Pressione ENTER para continuar...')
                                            continue

                                    elif len(cpfVenda) == 11 and cpfVenda.isdigit():
                                        cpfVendaFormatado = cpfVenda[0:3] + '.' + cpfVenda[3:6] + '.' + cpfVenda[6:9] + '-' + cpfVenda[9:11]
                                        verifCpfVenda = True
                                    else:
                                        print('CPF inválido, por favor digite novamente!')
                                        input('Pressione ENTER para continuar...')
                                        continue

                                if cpfVenda == '-':
                                        break

                                if cpfVendaFormatado not in passageiros:
                                    print('Passageiro não cadastrado! Cadastre o passageiro antes de comprar a passagem.')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                                
                                if cpfVendaFormatado in dicPassagensVoos:
                                    print('Este passageiro já possui uma passagem!')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue
                                
                                voos[codVoo]['lugares'] -= 1
                                dicPassagensVoos[codVoo] = {
                                    cpfVendaFormatado : passageiros[cpfVendaFormatado]['nome']
                                                        }
                                print('==================')
                                print(f'{passageiros[cpfVendaFormatado]['nome']} incluído na lista de passageiros do voo {codVoo}!')
                                print('==================')
                                input('Pressione ENTER para continuar...')
                                os.system('cls' if os.name == 'nt' else 'clear')

                            elif opcaoPassagem == '2':

                                verifCpfCancelamento = False
                                while verifCpfCancelamento == False:

                                    cpfCancelar = input('Digite o CPF do passageiro para cancelar a passagem: ')

                                    if cpfCancelar == '-':
                                        break

                                    if len(cpfCancelar) == 14:

                                        contNumCpf = 0
                                        contCarCpf = 0

                                        for i in cpfCancelar:
                                            if i.isdigit():
                                                contNumCpf += 1
                                            if listCaracteresEspeciais.count(i) == 1:
                                                contCarCpf += 1

                                        if contNumCpf == 11 and contCarCpf == 3 and cpfCancelar[3] == '.' and cpfCancelar[7] == '.' and cpfCancelar[11] == '-':
                                            cpfCancelarFormatado = cpfCancelar
                                            verifCpfCancelamento = True
                                        else:
                                            print('CPF inválido, por favor digite novamente!')
                                            input('Pressione ENTER para continuar...')
                                            continue

                                    elif len(cpfCancelar) == 11 and cpfCancelar.isdigit():
                                        cpfCancelarFormatado = cpfCancelar[0:3] + '.' + cpfCancelar[3:6] + '.' + cpfCancelar[6:9] + '-' + cpfCancelar[9:11]
                                        verifCpfCancelamento = True
                                    else:
                                        print('CPF inválido, por favor digite novamente!')
                                        input('Pressione ENTER para continuar...')
                                        continue
                                
                                if cpfCancelar == '-':
                                        break
                                
                                for codVoo in dicPassagensVoos:

                                        verifcodigoVooCancelar = False
                                        while not verifcodigoVooCancelar:
                                            if cpfCancelarFormatado in dicPassagensVoos[codVoo]:
                                                print(f'Voos em que {passageiros[cpfCancelarFormatado]['nome']} tem passagens:')

                                                for codVoo, dados in voos.items():
                                                    print(f'{codVoo}: Origem - {dados['origem']}, destino - {dados['destino']}')
                                                codigoVooCancelar = input(f'Digite o código do voo que deseja cancelar: ')

                                                if codigoVooCancelar == '-':
                                                    break

                                                if codigoVooCancelar == '' or codigoVooCancelar not in dicPassagensVoos:
                                                    print(f'Código inválido! Por favor, digite novamente.')
                                                    input(f'Pressione ENTER para continuar..')
                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                else:   
                                                    del dicPassagensVoos[codVoo][cpfCancelarFormatado]
                                                    print('Passagem cancelada com sucesso!')
                                                    voos[codVoo]['lugares'] += 1
                                                    verifcodigoVooCancelar = True
                                            else:
                                                print('Nenhuma passagem encontrada para esse CPF.')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')

                            elif opcaoPassagem == '3':
                                verifMenuPassagem = True
                                os.system('cls' if os.name == 'nt' else 'clear')

                elif optionVoo == '5':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue                                       


        elif option == '4':
            print('Finalizando app...')
            break
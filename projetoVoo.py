import os

cadastrosPessoa = dict()
voos = dict()

listCaracteresEspeciais = ['.', '-', '(', ')',] 
listNumVerificacaoOptions = ['1', '2', '3', '4', '5']

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
            numPessoas = int(input('Número de pessoas que deseja cadastrar: '))

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
                        if not caracter.isalpha() or caracter.isspace():
                            contInvalido += 1

                    if contInvalido > 0:
                        os.system('cls')
                        print(f'O nome não pode conter números ou caracteres especiais, por favor, digite novamente!\n')
                        continue

                    if len(nome) < 15:
                        os.system('cls')
                        print(f'O nome não pode conter mais de 5 espaços nem conter menos que 10 caracteres!\n')
                        contEspacosVazios = 0
                        continue

                    if nome == '':
                        os.system('cls')
                        print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                        continue
        
                    for i in nome:  
                        if i == ' ':
                            contEspacosVazios += 1

                    if len(nome) == (contEspacosVazios):
                            os.system('cls')
                            print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
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
                            if cpf in cadastrosPessoa.keys():
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
                        if cpf in cadastrosPessoa.keys():
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

                    if telefone.isdigit() == True and len(telefone) == 11:
                        telefone = '(' + telefone[0:2] + ')' + telefone[2:7] + '-' + telefone[7:11]
                        verifTelefone = True
                    else:
                        print('Telefone inválido, por favor digite o seu telefone!')
                        continue
                    
                cadastrosPessoa[cpf] = {
                    'nome': nome,
                    'idade': idade,
                    'telefone': telefone
                }
                pessoas += 1
                ##input('Para onde vão: ')
        elif option == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                for c, dados in cadastrosPessoa.items():
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

                        origem = input('Digite a origem do voo: ').title()

                        while origem == '' or origem.isdigit() == True or len(origem) < 2 or len(origem) > 50:

                            print('Origem inválida, por favor digite a origem do voo!')
                            origem = input('Digite a origem do voo: ').title()
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for regiao in dicRegioesBrasil:
                                for estado in dicRegioesBrasil[regiao]:
                                    for nomeEstado in dicRegioesBrasil[regiao][estado]:
                                        if origem in nomeEstado:
                                            print(f'Origem: {nomeEstado}')
                                            print(f'Região: {regiao}')
                                            print(f'Companhias Aéreas:')
                                            for companhia in dicRegioesBrasil[regiao]['companhias_aereas']:
                                                print(f'- {companhia}')
                                            break
                                        
                            destino = input('Digite o destino do voo: ').title()
                            
                            

        elif option == '4':
            print('Finalizando app...')
            break
import os

passageiros = {
    '466.156.648-36':{
        'nome': 'Miguel Fernandes Monteiro',
        'idade': 18,
        'telefone': '(19)98228-5101',
        'acompanhante' : {},
        'passagens' : {}
    },
    '416.769.548-05':{
        'nome': 'Cezar Rull',
        'idade': 18,
        'telefone': '(19)99944-0521',
        'acompanhante' : {},
        'passagens' : {}
    },

    }
voos = {
    'v-1':{
        'origem': 'São Paulo (SP)',
        'destino': 'Rio de Janeiro (RJ)',
        'aeroportoDeOrigem': 'Aeroporto de Congonhas (CGH)',
        'aeroportoDeDestino': 'Aeroporto Santos Dumont (SDU)',
        'escalas': 1,
        'precoPassagem': 'R$ 2.000,00',
        'lugares': 40,
        'dataHora': '15/05/2025 22:26',
        'companhiaAerea': 'Azul Linhas Aéreas'
    }
}


listaNumeroVerificacao = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.']
listCaracteresEspeciais = ['.', '-', '(', ')',] 
dicPassagensVoos = {}

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

listaPassagens = []

contPessoas = 0
lugares = 40
contVoo = 1

verifOption = False
while verifOption == False:


    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
        === MENU PRINCIPAL ===
          
Escolha uma das opções a baixo:

1 - Cadastrar passageiros
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

                verifCpf = False
                while verifCpf == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{pessoas + 1}° Pessoa')
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
                                passageiroEncontrado = False
                                for auxCpf in passageiros:
                                    if cpf in passageiros[auxCpf]['acompanhante'].keys():
                                        passageiroEncontrado = True
                                        
                                if passageiroEncontrado == True:
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
                            passageiroEncontrado = False
                            for auxCpf in passageiros:
                                if cpf in passageiros[auxCpf]['acompanhante'].keys():
                                    passageiroEncontrado = True
                                    
                            if passageiroEncontrado == True:
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
                        input('Pressione ENTER para continuar...')
                        continue
                    elif contEspacosVazios > 5:
                        print('O nome não pode conter mais de 5 espaços.')
                        input('Pressione ENTER para continuar...')
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
                verifIdade = False
                while verifIdade == False:
                    os.system('cls' if os.name == 'nt' else 'clear')

                    idade = input('Digite sua idade: ')

                    if idade == '-':
                        break

                    if idade.isdigit() == False: 
                        print(f'Idade inválida! Por favor, digite novamente.')
                        input(f'Pressione ENTER para continuar..')
                        continue

                    verifCpfResponsavel = False
                    if int(idade) < 18:

                        while verifCpfResponsavel == False:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Passageiros menores de idade precisam estar ligados a um responsável!')

                            cpfResponsavel = input('Digite o CPF do responsável: ')

                            if cpfResponsavel == '-':
                                break

                            if len(cpfResponsavel) == 14:
                                contNumCpfResponsavel = 0
                                contCarCpfResponsavel = 0
                                for i in cpfResponsavel:
                                    if i.isdigit() == True:
                                        contNumCpfResponsavel += 1
                                    if listCaracteresEspeciais.count(i) == 1:
                                        contCarCpfResponsavel += 1
                                if contNumCpfResponsavel == 11 and contCarCpfResponsavel == 3 and cpfResponsavel[3] == '.' and cpfResponsavel[7] == '.' and cpfResponsavel[11] == '-':
                                    if cpfResponsavel in passageiros.keys():
                                        if int(passageiros[cpfResponsavel]['idade']) >= 18:
                                            passageiros[cpfResponsavel]['acompanhante'][cpf] = {
                                                'nome': nome,
                                                'idade': idade,
                                                'telefoneResponsavel': passageiros[cpfResponsavel]['telefone'],
                                                'cpfResponsavel' : cpfResponsavel,
                                                'nomeResponsavel' : passageiros[cpfResponsavel]['nome'],
                                                'passagens' : {}
                                            }   

                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print('==================')
                                            print(f'Passageiro cadastrado com sucesso!')
                                            print(f'CPF: {cpf}')
                                            print(f'Nome: {nome}')
                                            print(f'Idade: {idade}')
                                            print(f'Telefone do Responsável: {passageiros[cpf]['telefoneResponsavel']}')
                                            print(f'CPF do responsável: {passageiros[cpf]['cpfResponsavel']}')
                                            print(f'Nome do responsável: {passageiros[cpf]['nomeResponsavel']}')
                                            print('==================')
                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')

                                            pessoas += 1
                                            contPessoas += 1
                                            verifIdade = True
                                            verifCpfResponsavel = True
                                            continue
                                        
                                        else:
                                            print(f'O passageiro responsável precisa ser maior de idade')
                                            continue
                                    else:
                                        print(f'Não há passageiros cadastrados com esse CPF ({cpfResponsavel})')
                                        continue
                                    
                                else:
                                    print('CPF inválido, por favor digite o CPF do responsável!')
                                    input('Pressione ENTER para continuar...')
                                    continue

                            if len(cpfResponsavel) == 11 and cpfResponsavel.isdigit() == True:
                                cpfResponsavel = cpfResponsavel[0:3] + '.' + cpfResponsavel[3:6] + '.' + cpfResponsavel[6:9] + '-' + cpfResponsavel[9:11]
                                if cpfResponsavel in passageiros.keys():
                                    
                                    passageiros[cpfResponsavel]['acompanhante'][cpf] = {
                                        'nome': nome,
                                        'idade': idade,
                                        'telefoneResponsavel': passageiros[cpfResponsavel]['telefone'],
                                        'cpfResponsavel' : cpfResponsavel,
                                        'nomeResponsavel' : passageiros[cpfResponsavel]['nome'],
                                        'passagens' : {}
                                    }   

                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('==================')
                                    print(f'Passageiro cadastrado com sucesso!')
                                    print(f'CPF: {cpf}')
                                    print(f'Nome: {nome}')
                                    print(f'Idade: {idade}')
                                    print(f'Telefone do Responsável: {passageiros[cpfResponsavel]['telefone']}')
                                    print(f'CPF do responsável: {cpfResponsavel}')
                                    print(f'Nome do responsável: {passageiros[cpfResponsavel]['nome']}')
                                    print('==================')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')

                                    pessoas += 1
                                    contPessoas += 1
                                    verifCpfResponsavel = True
                                    verifIdade = True
                                    continue
                                else:
                                    print(f'Não há passageiros cadastrados com esse CPF ({cpfResponsavel}) ou o passageiro também é menor de idade')
                                    continue
                            else:   
                                print('CPF inválido, por favor digite o seu cpfResponsavel!')
                                input('Pressione ENTER para continuar...')
                                continue

                        if cpfResponsavel == '-':
                                break

                    elif int(idade) > 120:
                        print('Idade inválida, por favor digite novamnete!')
                        input('Pressione ENTER para continuar...')
                        continue
                    else:
                        verifIdade = True

                if idade == '-':
                        break
                
                if verifCpfResponsavel == True:
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
                    'telefone': telefone,
                    'acompanhante' : {},
                    'passagens' : {}
                }
                pessoas += 1
                contPessoas += 1
                
        elif option == '2':
            if len(passageiros) == 0:
                print('\nNão há passageiros cadastrados, por favor cadastre um!')
                input('\nTecle enter para voltar!\n')
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                verifOptionPassageiros = False
                while not verifOptionPassageiros:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('''        == MENU DE PASSAGEIROS ==
1 - Listar passageiros cadastrados
2 - Alterar dados de um passageiro
3 - Voltar ao menu principal''')
                    optionPassageiros = input('--> ')

                    if optionPassageiros == '-':
                        break
                    if len(optionPassageiros) != 1 or optionPassageiros not in listaNumeroVerificacao[0:5]:
                        print('Opção inválida, por favor digite uma opção válida!')
                        input('Pressione ENTER para continuar...')
                        continue

                    if optionPassageiros == '1':
                        print(f'1 - Listar todos os passageiros cadastrados')
                        print(f'2 - Listar passageiro especifico')

                        verifListarPassageiros = False
                        while verifListarPassageiros == False:
                            listarPassageiros = input('--> ')

                            if listarPassageiros == '-':
                                break

                            if listarPassageiros not in ['1', '2']:
                                print('Opção inválida, por favor digite 1 ou 2!')
                                continue
                            else:
                                verifListarPassageiros = True

                        if listarPassageiros == '1':

                                contPassageiros = 0
                                for cpf in passageiros:
                                    contPassageiros += 1 + len(passageiros[cpf]['acompanhante'])
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f'Listando de passageiros cadastrados ({contPassageiros}):\n')
                                for cpf, dados in passageiros.items():
                                    print('==================')
                                    print(f'CPF: {cpf}')
                                    print(f'Nome: {dados['nome']}')
                                    print(f'Idade: {dados['idade']}')
                                    print(f'Telefone: {dados['telefone']}')
                                    if passageiros[cpf]['passagens'] != {}:
                                        print('Passagens: ')
                                        for passagens in passageiros[cpf]['passagens']:
                                            print(f'{passagens} - pagador: {passageiros[cpf]['passagens'][passagens]['pagador']}')
                                    if passageiros[cpf]['acompanhante'] != {}:
                                        print(f'\nAcompanhantes: ')
                                        for cpfAcompanhante, dados in passageiros[cpf]['acompanhante'].items():
                                            print(f'CPF: {cpfAcompanhante}')
                                            print(f'Nome: {dados['nome']}')
                                            print(f'Idade: {dados['idade']}')
                                            if passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens'] != {}:
                                                print(f'Passagens:')
                                                for passagens in passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens']:
                                                    print(f'{passagens} - pagador: {passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens'][passagens]['pagador']}')
                                    print('==================')
                                input('Pressione ENTER para continuar...')
                                os.system('cls' if os.name == 'nt' else 'clear')

                        elif listarPassageiros == '2':
                            verifCpfListar = False
                            while verifCpfListar == False:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                cpfListar = input('Digite o CPF do passageiro que deseja listar: ')

                                if cpfListar == '-':
                                    break

                                if len(cpfListar) == 14:
                                    contNumCpf = 0
                                    contCarCpf = 0
                                    for i in cpfListar:
                                        if i.isdigit() == True:
                                            contNumCpf += 1
                                        if listCaracteresEspeciais.count(i) == 1:
                                            contCarCpf += 1
                                    if contNumCpf == 11 and contCarCpf == 3 and cpfListar[3] == '.' and cpfListar[7] == '.' and cpfListar[11] == '-':
                                        verifCpfListar = True
                                        continue

                                    else:
                                        print('CPF inválido, por favor digite o seu CPF!')
                                        input('Pressione ENTER para continuar...')
                                        continue

                                if len(cpfListar) == 11 and cpfListar.isdigit() == True:
                                    cpfListar = cpfListar[0:3] + '.' + cpfListar[3:6] + '.' + cpfListar[6:9] + '-' + cpfListar[9:11]
                                    verifCpfListar = True
                                    continue
                                else:   
                                    print('CPF inválido, por favor digite o seu CPF!')
                                    input('Pressione ENTER para continuar...')
                                    continue

                            if cpfListar == '-':
                                break
                            
                            if cpfListar in passageiros.keys():
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f'Passageiro encontrado!\n')
                                print('==================')
                                print(f'CPF: {cpfListar}')
                                print(f'Nome: {passageiros[cpfListar]['nome']}')
                                print(f'Idade: {passageiros[cpfListar]['idade']}')
                                print(f'Telefone: {passageiros[cpfListar]['telefone']}')
                                if passageiros[cpfListar]['passagens'] != {}:
                                    print('Passagens: ')
                                    for passagens in passageiros[cpfListar]['passagens']:
                                        print(f'{passagens} - pagador: {passageiros[cpfListar]['passagens'][passagens]['pagador']}')
                                if passageiros[cpfListar]['acompanhante'] != {}:
                                    print(f'\nAcompanhantes: ')
                                    for cpfAcompanhante, dados in passageiros[cpfListar]['acompanhante'].items():
                                        print(f'CPF: {cpfAcompanhante}')
                                        print(f'Nome: {dados['nome']}')
                                        print(f'Idade: {dados['idade']}')
                                        if passageiros[cpfListar]['acompanhante'][cpfAcompanhante]['passagens'] != {}:
                                            print(f'Passagens:')
                                            for passagens in passageiros[cpfListar]['acompanhante'][cpfAcompanhante]['passagens']:
                                                print(f'{passagens} - pagador: {passageiros[cpfListar]['acompanhante'][cpfAcompanhante]['passagens'][passagens]['pagador']}')
                                print('==================')
                                input('Pressione ENTER para continuar...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                for cpf in passageiros:
                                    if cpfListar in passageiros[cpf]['acompanhante'].keys():
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(f'Passageiro encontrado!\n')
                                        print('==================')
                                        print(f'CPF: {cpfListar}')
                                        print(f'Nome: {passageiros[cpf]['acompanhante'][cpfListar]['nome']}')
                                        print(f'Idade: {passageiros[cpf]['acompanhante'][cpfListar]['idade']}')
                                        print(f'Telefone do responsável: {passageiros[cpf]['telefone']}')
                                        print(f'CPF do responsável: {cpf}')
                                        print(f'Nome do responsável: {passageiros[cpf]['nome']}')
                                        if passageiros[cpf]['acompanhante'][cpfListar]['passagens'] != {}:
                                            print('Passagens:')
                                            for passagens in passageiros[cpf]['acompanhante'][cpfListar]['passagens']:
                                                print(f'{passagens} - pagador: {passageiros[cpf]['acompanhante'][cpfListar]['passagens'][passagens]['pagador']}')
                                        print('==================')
                                        break
                                else:
                                    print(f'Passageiro não encontrado!')
                                input('Pressione ENTER para continuar...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break

                    elif optionPassageiros == '2':
                        verifCpfAlterar = False
                        while verifCpfAlterar == False:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            cpfAlterar = input('Digite o CPF do passageiro que deseja alterar: ')

                            if cpfAlterar == '-':
                                break

                            if len(cpfAlterar) == 14:
                                contNumCpf = 0
                                contCarCpf = 0
                                for i in cpfAlterar:
                                    if i.isdigit() == True:
                                        contNumCpf += 1
                                    if listCaracteresEspeciais.count(i) == 1:
                                        contCarCpf += 1
                                if contNumCpf == 11 and contCarCpf == 3 and cpfAlterar[3] == '.' and cpfAlterar[7] == '.' and cpfAlterar[11] == '-':
                                    verifCpfAlterar = True
                                    continue
                                    
                                else:
                                    print('CPF inválido, por favor digite o seu CPF!')
                                    input('Pressione ENTER para continuar...')
                                    continue

                            if len(cpfAlterar) == 11 and cpfAlterar.isdigit() == True:
                                cpfAlterar = cpfAlterar[0:3] + '.' + cpfAlterar[3:6] + '.' + cpfAlterar[6:9] + '-' + cpfAlterar[9:11]
                                verifCpfAlterar = True
                                continue
                            
                            else:   
                                print('CPF inválido, por favor digite o seu CPF!')
                                input('Pressione ENTER para continuar...')
                                continue

                        if cpfAlterar == '-':
                            break

                        verifOptionDados = False
                        while not verifOptionDados:
                            if cpfAlterar in passageiros.keys():
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f'Passageiro encontrado!\n')
                                print('==================')
                                print(f'CPF: {cpfAlterar}')
                                print(f'Nome: {passageiros[cpfAlterar]['nome']}')
                                print(f'Idade: {passageiros[cpfAlterar]['idade']}')
                                print(f'Telefone: {passageiros[cpfAlterar]['telefone']}')
                                print('==================')

                                print('''Escolha uma das opções a baixo:
    1 - Alterar nome
    2 - Alterar idade
    3 - Alterar telefone
    4 - Excluir passageiro
    5 - Voltar ao menu de passageiros''')
                                
                                optionDados = input('--> ')
                                if optionDados == '-':
                                    break
                                if len(optionDados) != 1 or optionDados not in listaNumeroVerificacao[0:6]:
                                    print('Opção inválida, por favor digite uma opção válida!')
                                    input('Pressione ENTER para continuar...')
                                    continue
                                if optionDados == '1':
                                    verifNomeAlterar = False
                                    while verifNomeAlterar == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        nomeAlterar = input('Digite o novo nome: ').title()

                                        if nomeAlterar == '-':
                                            break

                                        contEspacosVazios = 0
                                        contInvalido = 0

                                        for caracter in nomeAlterar:
                                            if not caracter.isalpha() and not caracter.isspace():
                                                contInvalido += 1
                                            
                                        if contInvalido > 0:
                                            os.system('cls')
                                            print(f'O nome não pode conter números ou caracteres especiais, por favor, digite novamente!\n')
                                            input('Pressione ENTER para continuar...')
                                            continue

                                        if len(nomeAlterar) < 10:
                                            print('O nome deve conter ao menos 10 caracteres.')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        elif contEspacosVazios > 5:
                                            print('O nome não pode conter mais de 5 espaços.')
                                            input('Pressione ENTER para continuar...')
                                            contEspacosVazios = 0
                                            continue

                                        if nomeAlterar == '':
                                            os.system('cls')
                                            print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        
                                        for i in nomeAlterar:  
                                            if i == ' ':
                                                contEspacosVazios += 1

                                        if len(nomeAlterar) == (contEspacosVazios):
                                                os.system('cls')
                                                print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                                                input('Pressione ENTER para continuar...')
                                                contEspacosVazios = 0
                                                continue
                                        verifNomeAlterar = True

                                    if nomeAlterar == '-':
                                        break

                                    passageiros[cpfAlterar]['nome'] = nomeAlterar
                                    for codVoo in dicPassagensVoos:
                                        if cpfAlterar in dicPassagensVoos[codVoo].keys():
                                            dicPassagensVoos[codVoo][cpfAlterar]['nome'] = nomeAlterar
                                    print(f'Nome alterado com sucesso!')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')

                                elif optionDados == '2':
                                    verifIdadeAlterar = False
                                    while verifIdadeAlterar == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        idadeAlterar = input('Digite a nova idade: ')

                                        if idadeAlterar == '-':
                                            break

                                        if idadeAlterar < passageiros[cpfAlterar]['idade']:
                                            print('Não é possível diminuir a idade do passageiro!')
                                            input('Pressione ENTER para continuar...')
                                            continue


                                        if idadeAlterar.isdigit() == False: 
                                            print(f'Idade inválida! Por favor, digite novamente.')
                                            input(f'Pressione ENTER para continuar..')
                                            continue

                                        if int(idadeAlterar) < 0 or int(idadeAlterar) > 120:
                                            print('Idade inválida, por favor digite novamnete!')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        else:
                                            verifIdadeAlterar = True

                                    if idadeAlterar == '-':
                                        break

                                    passageiros[cpfAlterar]['idade'] = idadeAlterar
                                    for codVoo in dicPassagensVoos:
                                        if cpfAlterar in dicPassagensVoos[codVoo].keys():
                                            dicPassagensVoos[codVoo][cpfAlterar]['idade'] = idadeAlterar
                                    print(f'Idade alterada com sucesso!')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')

                                elif optionDados == '3':
                                    verifTelefoneAlterar = False
                                    while verifTelefoneAlterar == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        telefoneAlterar = input('Digite o novo telefone: ')
                                        contTelefone = 0

                                        if telefoneAlterar == '-':
                                            break

                                        if len(telefoneAlterar) == 14:
                                            contNumTel = 0
                                            contCarTel = 0
                                            for i in telefoneAlterar:
                                                if i.isdigit() == True:
                                                    contNumTel += 1
                                                if listCaracteresEspeciais.count(i) == 1:
                                                    contCarTel += 1
                                            if contNumTel == 11 and contCarTel == 3 and telefoneAlterar[0] == '(' and telefoneAlterar[3] == ')' and telefoneAlterar[9] == '-':
                                                for c in passageiros:
                                                    if telefoneAlterar in passageiros[c]['telefone']:
                                                        contTelefone += 1
                                                if contTelefone > 0:
                                                    print('Telefone já cadastrado! Por favor, digite outro telefone!')
                                                    input('Pressione ENTER para continuar...')
                                                    continue
                                                else:
                                                    verifTelefoneAlterar = True
                                                    continue
                                            else:
                                                print('Telefone inválido, por favor digite o seu telefone!')
                                                continue

                                        if telefoneAlterar.isdigit() and len(telefoneAlterar) == 11:
                                            telefoneAlterar = '(' + telefoneAlterar[0:2] + ')' + telefoneAlterar[2:7] + '-' + telefoneAlterar[7:11]
                                            for c in passageiros:
                                                if telefoneAlterar in passageiros[c]['telefone']:
                                                    contTelefone += 1
                                            if contTelefone > 0:
                                                print('Telefone já cadastrado! Por favor, digite outro telefone!')
                                                input('Pressione ENTER para continuar...')
                                                continue
                                            else:
                                                verifTelefoneAlterar = True
                                                continue
                                                
                                        else:
                                            print('Telefone inválido, por favor digite o seu telefone!')
                                            input('Pressione ENTER para continuar...')
                                            continue

                                    if telefoneAlterar == '-':
                                        break

                                    passageiros[cpfAlterar]['telefone'] = telefoneAlterar
                                    for codVoo in dicPassagensVoos:
                                        if cpfAlterar in dicPassagensVoos[codVoo].keys():
                                            dicPassagensVoos[codVoo][cpfAlterar]['telefone'] = telefoneAlterar
                                    print(f'Telefone alterado com sucesso!')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                elif optionDados == '4':
                                    verifExcluir = False
                                    while verifExcluir == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        excluir = input(f'Deseja realmente excluir o passageiro {passageiros[cpfAlterar]['nome']}? (S/N): ').upper()

                                        if excluir == '-':
                                            break

                                        if excluir not in ['S', 'N']:
                                            print('Opção inválida, por favor digite S ou N!')
                                            continue
                                        else:
                                            verifExcluir = True

                                    if excluir == 'S':
                                        listaCpfApagar = []
                                        del passageiros[cpfAlterar]
                                        for codVoo in dicPassagensVoos:
                                            if cpfAlterar in dicPassagensVoos[codVoo].keys():
                                                listaCpfApagar.append(codVoo)
                                        for codVoo in listaCpfApagar:
                                            del dicPassagensVoos[codVoo][cpfAlterar]
                                            voos[codVoo]['passageiros'] += 1
                                        print(f'Passageiro excluído com sucesso!')
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        break
                                    elif excluir == 'N':
                                        continue

                                elif optionDados == '5':
                                    verifOptionDados = True
                                    continue
                            else:
                                for cpf in passageiros:
                                    if cpfAlterar in passageiros[cpf]['acompanhante'].keys():
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print(f'Passageiro encontrado!\n')
                                        print('==================')
                                        print(f'CPF: {cpfAlterar}')
                                        print(f'Nome: {passageiros[cpf]['acompanhante'][cpfAlterar]['nome']}')
                                        print(f'Idade: {passageiros[cpf]['acompanhante'][cpfAlterar]['idade']}')
                                        print(f'Telefone do responsável: {passageiros[cpf]['telefone']}')
                                        print(f'CPF do responsável: {cpf}')
                                        print(f'Nome do responsável: {passageiros[cpf]['nome']}')
                                        print('==================')
                                        break
                                else:
                                    print('Passageiro não encontrado, por favor digite um CPF válido!')
                                    input('Pressione ENTER para continuar...')
                                    continue

                                print('''Escolha uma das opções a baixo:
1 - Alterar nome
2 - Alterar idade
3 - Excluir passageiro
4 - Voltar ao menu de passageiros''')
                                optionDados = input('--> ')
                                if optionDados == '-':
                                    break
                                if len(optionDados) != 1 or optionDados not in listaNumeroVerificacao[0:3]:
                                    print('Opção inválida, por favor digite uma opção válida!')
                                    input('Pressione ENTER para continuar...')
                                    continue
                                if optionDados == '1':
                                    verifNomeAlterar = False
                                    while verifNomeAlterar == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        nomeAlterar = input('Digite o novo nome: ').title()

                                        if nomeAlterar == '-':
                                            break

                                        contEspacosVazios = 0
                                        contInvalido = 0

                                        for caracter in nomeAlterar:
                                            if not caracter.isalpha() and not caracter.isspace():
                                                contInvalido += 1
                                            
                                        if contInvalido > 0:
                                            os.system('cls')
                                            print(f'O nome não pode conter números ou caracteres especiais, por favor, digite novamente!\n')
                                            input('Pressione ENTER para continuar...')
                                            continue

                                        if len(nomeAlterar) < 10:
                                            print('O nome deve conter ao menos 10 caracteres.')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        elif contEspacosVazios > 5:
                                            print('O nome não pode conter mais de 5 espaços.')
                                            input('Pressione ENTER para continuar...')
                                            contEspacosVazios = 0
                                            continue

                                        if nomeAlterar == '':
                                            os.system('cls')
                                            print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        
                                        for i in nomeAlterar:  
                                            if i == ' ':
                                                contEspacosVazios += 1

                                        if len(nomeAlterar) == (contEspacosVazios):
                                                os.system('cls')
                                                print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                                                input('Pressione ENTER para continuar...')
                                                contEspacosVazios = 0
                                                continue
                                        verifNomeAlterar = True

                                    if nomeAlterar == '-':
                                        break
                                    
                                    for cpf in passageiros:
                                        if cpfAlterar in passageiros[cpf]['acompanhante'].keys():
                                            passageiros[cpf]['acompanhante'][cpfAlterar]['nome'] = nomeAlterar
                                    for codVoo in dicPassagensVoos:
                                        for cpf in dicPassagensVoos[codVoo].keys():
                                            if cpfAlterar in dicPassagensVoos[codVoo][cpf]['acompanhante'].keys():
                                                dicPassagensVoos[codVoo][cpf]['acompanhante'][cpfAlterar]['nome'] = nomeAlterar

                                    print(f'Nome alterado com sucesso!')
                                    input('Pressione ENTER para continuar...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    

                                elif optionDados == '2':
                                    verifIdadeAlterar = False
                                    while verifIdadeAlterar == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        idadeAlterar = input('Digite a nova idade: ')

                                        if idadeAlterar == '-':
                                            break
                                        idadeMenor = False
                                        for cpf in passageiros:
                                            if cpfAlterar in passageiros[cpf]['acompanhante'].keys():
                                                if idadeAlterar < passageiros[cpf]['acompanhante'][cpfAlterar]['idade']:
                                                    idadeMenor = True
                                        
                                        if idadeMenor == True:
                                            print('Não é possível diminuir a idade do passageiro!')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                           
                                        if idadeAlterar.isdigit() == False: 
                                            print(f'Idade inválida! Por favor, digite novamente.')
                                            input(f'Pressione ENTER para continuar..')
                                            continue

                                        if int(idadeAlterar) < 0 or int(idadeAlterar) > 120:
                                            print('Idade inválida, por favor digite novamnete!')
                                            input('Pressione ENTER para continuar...')
                                            continue
                                        else:
                                            verifIdadeAlterar = True

                                    if idadeAlterar == '-':
                                        break

                                    if int(idadeAlterar) >= 18:
                                        verifTelefoneAlterar = False
                                        while verifTelefoneAlterar == False:
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            print(f'O cadastro do telefone para passageiros a partir de 18 anos é obrigatório!')
                                            telefoneAlterar = input('Digite o telefone: ')
                                            contTelefone = 0

                                            if telefoneAlterar == '-':
                                                break

                                            if len(telefoneAlterar) == 14:
                                                contNumTel = 0
                                                contCarTel = 0
                                                for i in telefoneAlterar:
                                                    if i.isdigit() == True:
                                                        contNumTel += 1
                                                    if listCaracteresEspeciais.count(i) == 1:
                                                        contCarTel += 1
                                                if contNumTel == 11 and contCarTel == 3 and telefoneAlterar[0] == '(' and telefoneAlterar[3] == ')' and telefoneAlterar[9] == '-':
                                                    for c in passageiros:
                                                        if telefoneAlterar in passageiros[c]['telefone']:
                                                            contTelefone += 1
                                                    if contTelefone > 0:
                                                        print('Telefone já cadastrado! Por favor, digite outro telefone!')
                                                        input('Pressione ENTER para continuar...')
                                                        continue
                                                    else:
                                                        verifTelefoneAlterar = True
                                                        continue
                                                else:
                                                    print('Telefone inválido, por favor digite o seu telefone!')
                                                    continue

                                            if telefoneAlterar.isdigit() and len(telefoneAlterar) == 11:
                                                telefoneAlterar = '(' + telefoneAlterar[0:2] + ')' + telefoneAlterar[2:7] + '-' + telefoneAlterar[7:11]
                                                for c in passageiros:
                                                    if telefoneAlterar in passageiros[c]['telefone']:
                                                        contTelefone += 1
                                                if contTelefone > 0:
                                                    print('Telefone já cadastrado! Por favor, digite outro telefone!')
                                                    input('Pressione ENTER para continuar...')
                                                    continue
                                                else:
                                                    verifTelefoneAlterar = True
                                                    continue
                                                    
                                            else:
                                                print('Telefone inválido, por favor digite o seu telefone!')
                                                input('Pressione ENTER para continuar...')
                                                continue

                                        for cpf in passageiros:
                                            if cpfAlterar in passageiros[cpf]['acompanhante'].keys():
                                                listaCpfApagar.append(cpf)
                                        for cpf in listaCpfApagar:
                                            passageiros[cpfAlterar] = {
                                                'nome': passageiros[cpf]['acompanhante'][cpfAlterar]['nome'],
                                                'idade': idadeAlterar,
                                                'telefone': telefoneAlterar,
                                                'passagens': passageiros[cpf]['acompanhante'][cpfAlterar]['passagens'],
                                                'acompanhante': {}
                                            }
                                            del passageiros[cpf]['acompanhante'][cpfAlterar]

                                        dicCpfVooApagar = {}
                                        for codVoo in dicPassagensVoos:
                                            for cpf in dicPassagensVoos[codVoo].keys():
                                                if cpfAlterar in dicPassagensVoos[codVoo][cpf]['acompanhante'].keys():
                                                    dicCpfVooApagar[codVoo] = {cpf}

                                        for codVoo in dicCpfVooApagar:
                                            for cpf in dicCpfVooApagar[codVoo]:
                                                del dicPassagensVoos[codVoo][cpf]['acompanhante'][cpfAlterar]
                                                dicPassagensVoos[codVoo][cpfAlterar] = {
                                                    'nome': passageiros[cpfAlterar]['nome'],
                                                    'idade': passageiros[cpfAlterar]['idade'],
                                                    'telefone': passageiros[cpfAlterar]['telefone'],
                                                    'passagens': passageiros[cpfAlterar]['passagens'],
                                                    'acompanhante': {}
                                                }
                                        
                                    else:
                                        for cpf in passageiros:   
                                            passageiros[cpf]['acompanhante'][cpfAlterar]['idade'] = idadeAlterar
                                        for codVoo in dicPassagensVoos:
                                            for cpf in dicPassagensVoos[codVoo].keys():
                                                if cpfAlterar in dicPassagensVoos[codVoo][cpf]['acompanhante'].keys():
                                                    dicPassagensVoos[codVoo][cpf]['acompanhante'][cpfAlterar]['idade'] = idadeAlterar

                                            print(f'Idade alterada com sucesso!')
                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                elif optionDados == '3':
                                    verifExcluir = False
                                    while verifExcluir == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        excluir = input(f'Deseja realmente excluir o passageiro {passageiros[cpfAlterar]['acompanhante'][cpfAlterar]['nome']}? (S/N): ').upper()

                                        if excluir == '-':
                                            break

                                        if excluir not in ['S', 'N']:
                                            print('Opção inválida, por favor digite S ou N!')
                                            continue
                                        else:
                                            verifExcluir = True

                                    if excluir == 'S':
                                        for cpf in passageiros:
                                            if cpfAlterar in passageiros[cpf]['acompanhante'].keys():
                                                listaCpfApagar.append(cpf)

                                        for cpf in listaCpfApagar:
                                            del passageiros[cpf]['acompanhante'][cpfAlterar]
                                            
                                        dicCpfVooApagar = {}
                                        for codVoo in dicPassagensVoos:
                                            for cpf in dicPassagensVoos[codVoo].keys():
                                                if cpfAlterar in dicPassagensVoos[codVoo][cpf]['acompanhante'].keys():
                                                    dicCpfVooApagar[codVoo] = {cpf}
                                        for codVoo in dicCpfVooApagar:
                                            for cpf in dicCpfVooApagar[codVoo]:
                                                del dicPassagensVoos[codVoo][cpf]['acompanhante'][cpfAlterar]
                                                voos[codVoo]['passageiros'] += 1
                                                
                                        print(f'Passageiro excluído com sucesso!')
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        break
                                    elif excluir == 'N':
                                        continue

                                elif optionDados == '4':
                                    break

                    elif optionPassageiros == '3':
                        verifOptionPassageiros = True
                        continue
                            
        elif option == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
        
            menuVoos = True
            while menuVoos == True:
                print('''
        == MENU DE VOOS ==

Escolha uma das opções a baixo:
            
1- Cadastrar um voo  
2- Consultar voos
3- Consultar passageiros de um voo
4- Menu passagens
5- Cancelar voo
6- Voltar ao menu principal
                    ''')
                verifOptionVoo = False
                while verifOptionVoo == False:
                    optionVoo = input('--> ')

                    if optionVoo == '-':
                        menuVoos = False
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
                                menuVoos = False
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
                            menuVoos = False
                            continue

                        verifDestino = False
                        while verifDestino == False:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            destino = input('Digite o estado destino do voo: ').title()

                            if destino == '-':
                                menuVoos = False
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
                                menuVoos = False
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
                                            menuVoos = False
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

                                            print(f'Aeroporto de origem escolhido: {selectAeroportoOrigem}')
                                            input('Pressione ENTER para continuar...')
                        
                        if selectAeroportoOrigem == '-':
                            menuVoos = False
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
                                            menuVoos = False
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
                            menuVoos = False
                            continue

                        verifDataHora = False
                        while verifDataHora == False:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            dataHora = input('Informe a data e hora (formato: DD/MM/AAAA HH:MM): ')

                            if dataHora == '-':
                                menuVoos = False
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
                                menuVoos = False
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
                                                menuVoos = False
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
                            menuVoos = False
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
                                    menuVoos = False
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
                                                menuVoos = False
                                                break

                                            if vooConsulta == '' or vooConsulta[0] != 'v' or vooConsulta[1] != '-' or vooConsulta[2:].isdigit() == False:
                                                print('Código inválido, por favor digite o código do voo!')
                                                continue
                                            else:
                                                print('Voo cadastrado:')
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
                                                menuVoos = False
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
                                                menuVoos = False
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
                                                menuVoos = False
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
                                                            menuVoos = False
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
                                                            menuVoos = False
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
                                        if not voos == {}:
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
                                        else:  
                                            print(f'Não há voos cadastrados!')
                                            input(f'Pressione ENTER para continuar...')
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
                                    menuVoos = False
                                    break

                                if len(optionListarVoos) != 1 or optionListarVoos not in listaNumeroVerificacao[0:2]:
                                    print('Opção inválida, por favor digite uma opção válida!')
                                    continue
                                else:
                                    if optionListarVoos == '1':
                                        
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print('Listando voos com passageiros...')
                                        
                                        if len(dicPassagensVoos) > 0:

                                            for voo in dicPassagensVoos:
                                                contPassageirosVoo = 0
                                                for cpf in dicPassagensVoos[voo]:
                                                    if dicPassagensVoos[voo][cpf]['acompanhante'] != {''}:
                                                        contPassageirosVoo += len(dicPassagensVoos[voo][cpf]['acompanhante'].keys())+1
                                                    else:
                                                        contPassageirosVoo += 1
                                                print(f'{voo}: {contPassageirosVoo:.0f} passageiros | Origem: {voos[voo]['origem']} -> Destino: {voos[voo]['destino']} | Lugares: {voos[voo]['lugares']} | Data/Hora: {voos[voo]['dataHora']} | Companhia: {voos[voo]['companhiaAerea']}')
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
                                                menuVoos = False
                                                break

                                            if codVoo == '' or codVoo not in voos.keys():
                                                print('Código inválido, por favor digite o código do voo!')
                                                continue
                                            else:
                                                verifOptionPassageirosVoo = True
                                                if codVoo in dicPassagensVoos.keys():
                                                            print('==================')
                                                            print(f'Código do voo: {codVoo} | Origem: {voos[codVoo]['origem']} -> Destino: {voos[codVoo]['destino']} | Data/Hora: {voos[codVoo]['dataHora']} | Companhia: {voos[codVoo]['companhiaAerea']}')
                                                            print(f'Número de passageiros: {contPassageirosVoo:.0f}')
                                                            print(f'Lugares disponíveis: {voos[codVoo]['lugares']}')
                                                            print('==================\n')
                                                            for cpf, dados in dicPassagensVoos[codVoo].items():
                                                                print('==================')
                                                                print(f'CPF: {cpf}')
                                                                print(f'Nome: {dados['nome']}')
                                                                for cpfAcompanhante in dicPassagensVoos[codVoo][cpf]['acompanhante']:
                                                                    print(f'Acompanhantes:\n - CPF: {cpfAcompanhante}\n - Nome: {dicPassagensVoos[codVoo][cpf]['acompanhante'][cpfAcompanhante]['nome']}' 
                                                                        if dicPassagensVoos[codVoo][cpf]['acompanhante'] != ''
                                                                        else '')
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
    1 - Vender passagem
    2 - Cancelar passagem
    3 - Voltar ao menu principal
                                ''')
                                opcaoPassagem = input('--> ')

                                if opcaoPassagem == '-':
                                    menuVoos = False
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
                                            print(f'{codVoo}: {dadosVoo['origem']} -> {dadosVoo['destino']} | Lugares: {dadosVoo['lugares']} | Data/Hora: {dadosVoo['dataHora']} | Companhia: {dadosVoo['companhiaAerea']}')
                                    
                                        codVoo = input('Digite o código do voo desejado: ')
                                        contPassageirosVoo = 0
                                        passagem = ''

                                        if codVoo == '-':
                                            menuVoos = False
                                            break

                                        if codVoo not in voos or codVoo == '':
                                            print('Código de voo inválido!')
                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue

                                        if voos[codVoo]['lugares'] == 0:
                                            print('Não há lugares disponíveis neste voo!')
                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue

                                        verifCodVoo = True

                                    if codVoo not in dicPassagensVoos:
                                        dicPassagensVoos[codVoo] = {}
                                    
                                    if codVoo == '-':
                                            menuVoos = False
                                            continue
                                    verifCpfVenda = False
                                    while verifCpfVenda == False:
                                        cpfVenda = input('Digite o CPF do passageiro: ')

                                        if cpfVenda == '-':
                                            menuVoos = False
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
                                            menuVoos = False
                                            break

                                    if cpfVendaFormatado not in passageiros:
                                        print('Passageiro não cadastrado! Cadastre o passageiro antes de comprar a passagem.')
                                        input('Pressione ENTER para continuar...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        continue

                                    if int(passageiros[cpfVendaFormatado]['idade']) < 18:
                                        print(f'{passageiros[cpfVendaFormatado]['nome']} não possui idade suficiente para comprar passagens aéreas')
                                        continue

                                    if cpfVendaFormatado in dicPassagensVoos[codVoo]:
                                        print(f'Este passageiro ({passageiros[cpfVendaFormatado]['nome']}) já possui uma ou mais passagens compradas!')
                                        print(f'Deseja incluir uma nova passagem? \n\n1-SIM\n\n2-NÃO')
                                        print(f'obs: Passageiros menores de idade são incluidos como acompanhantes.')

                                        verifOpcaoVendaPassagem = False
                                        while not verifOpcaoVendaPassagem:

                                            opcaoVendaPassagem = input('--> ')

                                            if opcaoVendaPassagem == '-':
                                                menuVoos = False
                                                break
                                            
                                            if opcaoVendaPassagem == '' or opcaoVendaPassagem not in ['1', '2']:
                                                print(f'Opção inválida! Digite somente 1 ou 2.')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')

                                            else:
                                                verifOpcaoVendaPassagem = True
                                                if opcaoVendaPassagem == '1':
                                                    verifQtdPassagens = False
                                                    while not verifQtdPassagens:

                                                        qtdPassagens = input(f'Digite o número de passagens que deseja incluir: ')
                                                        
                                                        if qtdPassagens == '-':
                                                            menuVoos = False
                                                            break
                                                        
                                                        elif qtdPassagens == '' or not qtdPassagens.isdigit() or int(qtdPassagens) > voos[codVoo]['lugares'] or int(qtdPassagens) < 1 :
                                                            print(f'Quantidade ínvalida! Por favor, digite novamente.')
                                                            input(f'Pressione ENTER para continuar..')
                                                            os.system('cls' if os.name == 'nt' else 'clear')
                                                            
                                                        else:
                                                            verifQtdPassagens = True
                                                            qtdPassagens = int(qtdPassagens)
                                                            listaPassageirosIncluidos = []

                                                            if qtdPassagens >= 1:
                                                                contCadastroViagem = 1
                                                                while contCadastroViagem <= qtdPassagens:

                                                                    if len(dicPassagensVoos[codVoo].keys()) > 0:
                                                                        for cpf in dicPassagensVoos[codVoo]:
                                                                            if dicPassagensVoos[codVoo][cpf]['acompanhante'] != {''}:
                                                                                contPassageirosVoo += 1 + len(dicPassagensVoos[codVoo][cpf]['acompanhante'].keys())
                                                                            else:
                                                                                contPassageirosVoo += 1

                                                                    passagem = f'p{contPassageirosVoo+1}_{codVoo}'

                                                                    auxContPassageirosVoo = contPassageirosVoo

                                                                    passagemUtilizada = True
                                                                    while passagemUtilizada:
                                                                        if passagem in listaPassagens:
                                                                            auxContPassageirosVoo += 1
                                                                            passagem = f'p{auxContPassageirosVoo+1}_{codVoo}'
                                                                        else:
                                                                            passagemUtilizada = False

                                                                    auxContPassageirosVoo = 0

                                                                    print(f'Digite os dados do {contCadastroViagem+1}º passageiro: ')
                                                                    verifCpfPassageiro = False
                                                                    while verifCpfPassageiro == False:
                                                                        cpfPassageiro = input('Digite o CPF do passageiro: ')

                                                                        if cpfPassageiro == '-':
                                                                            menuVoos = False
                                                                            break
                                                                        
                                                                        if len(cpfPassageiro) == 14:
                                                                            contNumCpf = 0
                                                                            contCarCpf = 0
                                                                            for i in cpfPassageiro:
                                                                                if i.isdigit():
                                                                                    contNumCpf += 1
                                                                                if listCaracteresEspeciais.count(i) == 1:
                                                                                    contCarCpf += 1

                                                                            if contNumCpf == 11 and contCarCpf == 3 and cpfPassageiro[3] == '.' and cpfPassageiro[7] == '.' and cpfPassageiro[11] == '-':
                                                                                cpfAcompanhanteFormatado = cpfPassageiro
                                                                                verifCpfPassageiro = True
                                                                            else:
                                                                                print('CPF inválido, por favor digite novamente!')
                                                                                input('Pressione ENTER para continuar...')
                                                                                continue

                                                                        elif len(cpfPassageiro) == 11 and cpfPassageiro.isdigit():
                                                                            cpfAcompanhanteFormatado = cpfPassageiro[0:3] + '.' + cpfPassageiro[3:6] + '.' + cpfPassageiro[6:9] + '-' + cpfPassageiro[9:11]
                                                                            verifCpfPassageiro = True
                                                                        else:
                                                                            print('CPF inválido, por favor digite novamente!')
                                                                            input('Pressione ENTER para continuar...')
                                                                            continue

                                                                    if cpfPassageiro == '-':
                                                                            menuVoos = False
                                                                            break
                                                                    
                                                                    if cpfAcompanhanteFormatado in passageiros or cpfAcompanhanteFormatado in passageiros[cpfVendaFormatado]['acompanhante']:
                                                                        if cpfAcompanhanteFormatado not in passageiros[cpfVendaFormatado]['acompanhante']:
                                                                            if cpfAcompanhanteFormatado not in dicPassagensVoos[codVoo]:
                                                                                voos[codVoo]['lugares'] -= 1
                                                                                dicPassagensVoos[codVoo][cpfAcompanhanteFormatado] = {
                                                                                'nome' : passageiros[cpfAcompanhanteFormatado]['nome'],
                                                                                'idade' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                                'telefone' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                                'passagem' : {
                                                                                    passagem : {'pagador' : cpfVendaFormatado}
                                                                                    }
                                                                                }
                                                                                listaPassagens.append(passagem)
                                                                                listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                                                contCadastroViagem += 1
                                                                                continue
                                                                            else:
                                                                                print(f'Passageiro já possui uma passagem comprada no voo: {codVoo}')
                                                                                input('Pressione ENTER para continuar...')
                                                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                                                continue

                                                                        else:

                                                                            if cpfAcompanhanteFormatado not in dicPassagensVoos[codVoo][cpfVendaFormatado]['acompanhante']:

                                                                                print(f'Passageiro encontrado: \nCPF: {cpfAcompanhanteFormatado}\nNome: {passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['nome']}\nSerá incluido como acompanhante de {passageiros[cpfVendaFormatado]['nome']}')

                                                                                voos[codVoo]['lugares'] -= 1
                                                                                dicPassagensVoos[codVoo][cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado] = {
                                                                                'nome' : passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['nome'],
                                                                                'idade' : passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['idade'],
                                                                                'telefoneResponsavel' : passageiros[cpfVendaFormatado]['telefone'],
                                                                                'cpfResponsavel' : cpfVendaFormatado,
                                                                                'passagem' : {
                                                                                    passagem : {'pagador' : cpfVendaFormatado}
                                                                                    }
                                                                                }

                                                                                passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                                    'pagador' : cpfVendaFormatado
                                                                                }
                                                                                listaPassagens.append(passagem)
                                                                                listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                                                contCadastroViagem += 1
                                                                                continue

                                                                            else:
                                                                                print(f'Passageiro já possui uma passagem comprada no voo: {codVoo}')
                                                                                input('Pressione ENTER para continuar...')
                                                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                                                continue

                                                                    else:
                                                                    
                                                                        verifNome = False
                                                                        while verifNome == False:
                                                                            os.system('cls' if os.name == 'nt' else 'clear')

                                                                            nome = input('Digite o nome do(a) acompanhante: ').title()

                                                                            if nome == '-':
                                                                                menuVoos = False
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
                                                                                input('Pressione ENTER para continuar...')
                                                                                continue
                                                                            elif contEspacosVazios > 5:
                                                                                print('O nome não pode conter mais de 5 espaços.')
                                                                                input('Pressione ENTER para continuar...')
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
                                                                            menuVoos = False
                                                                            break
                                                                        
                                                                        verifIdade = False
                                                                        while verifIdade == False:
                                                                            os.system('cls' if os.name == 'nt' else 'clear')

                                                                            idade = input('Digite a idade do(a) acompanhante: ')

                                                                            if idade == '-':
                                                                                menuVoos = False
                                                                                break

                                                                            if idade.isdigit() == False or int(idade) < 1 or int(idade) > 120:
                                                                                print('Idade inválida, por favor digite a sua idade!')
                                                                                input('Pressione ENTER para continuar...')
                                                                                continue
                                                                            else:
                                                                                verifIdade = True

                                                                        if idade == '-':
                                                                                menuVoos = False
                                                                                break
                                                                        
                                                                        if int(idade) >= 18:
                                                                            verifTelefone = False
                                                                            while verifTelefone == False:
                                                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                                                telefone = input('Digite telefone: ')
                                                                                contTelefone = 0

                                                                                if telefone == '-':
                                                                                    menuVoos = False
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
                                                                                menuVoos = False
                                                                                break
                                                                            passageiros[cpfAcompanhanteFormatado] = {
                                                                            'nome' : passageiros[cpfAcompanhanteFormatado]['nome'],
                                                                            'idade' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                            'telefone' : passageiros[cpfAcompanhanteFormatado]['telefone'],
                                                                            'acompanhante' : {},
                                                                            'passagens' : {}
                                                                            }

                                                                            voos[codVoo]['lugares'] -= 1
                                                                            dicPassagensVoos[codVoo][cpfAcompanhanteFormatado] = {
                                                                            'nome' : passageiros[cpfAcompanhanteFormatado]['nome'],
                                                                            'idade' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                            'telefone' : passageiros[cpfAcompanhanteFormatado]['telefone'],
                                                                            'acompanhante' : {},
                                                                            'passagem' : {
                                                                                passagem : {'pagador' : cpfVendaFormatado}
                                                                                } 
                                                                            }
                                                                            passageiros[cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                                'pagador' : cpfVendaFormatado
                                                                            }
                                                                            listaPassagens.append(passagem)
                                                                            listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                                            
                                                                        else:
                                                                            passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado] = {
                                                                                'nome': nome,
                                                                                'idade': idade,
                                                                                'telefoneResponsavel' : passageiros[cpfVendaFormatado]['telefone'],
                                                                                'cpfResponsavel' : cpfVendaFormatado,
                                                                                'nomeResponsavel' : passageiros[cpfVendaFormatado]['nome'],
                                                                                'passagens' : {}
                                                                            }
                                                                            voos[codVoo]['lugares'] -= 1
                                                                            dicPassagensVoos[codVoo][cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado] = {
                                                                                'nome' : nome,
                                                                                'idade' : idade,
                                                                                'telefoneResponsavel' : passageiros[cpfVendaFormatado]['telefone'],
                                                                                'cpfResponsavel' : cpfVendaFormatado,
                                                                                'nomeResponsavel' : passageiros[cpfVendaFormatado]['nome'],
                                                                                'passagem' : {
                                                                                    passagem : {'pagador' : cpfVendaFormatado}
                                                                                }
                                                                            }
                                                                            passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                                'pagador' : cpfVendaFormatado
                                                                            }
                                                                            listaPassagens.append(passagem)
                                                                            listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)

                                                                        contCadastroViagem += 1

                                                                print(f'===================')
                                                                for cpf in listaPassageirosIncluidos:
                                                                    if cpf in passageiros[cpfVendaFormatado]['acompanhante']:
                                                                        print(f'{passageiros[cpfVendaFormatado]['acompanhante'][cpf]['nome']} foi incluido no voo: {codVoo}, como acompanhante de {passageiros[cpfVendaFormatado]['nome']}')     
                                                                    else:                                                           
                                                                        print(f'{passageiros[cpf]['nome']} foi incluido no voo: {codVoo}')
                                                                print(f'===================') 
                                                                input(f'Pressione ENTER para continuar..')
                                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                                listaPassageirosIncluidos = []
                                                                listaPassagens.append(passagem)
                                                                break
                                                else:                       
                                                    break

                                        if opcaoVendaPassagem == '-':
                                            menuVoos = False
                                            continue
                                    else:       
                                        print(f'Passageiro encontrado:\nCPF: {cpfVendaFormatado} \nNome: {passageiros[cpfVendaFormatado]['nome']}')   
                                        
                                        verifQtdPassagens = False
                                        while not verifQtdPassagens:

                                            qtdPassagens = input(f'Digite o número de passagens que deseja incluir: ')
                                            
                                            if qtdPassagens == '-':
                                                menuVoos = False
                                                break
                                            
                                            elif qtdPassagens == '' or not qtdPassagens.isdigit() or int(qtdPassagens) > voos[codVoo]['lugares'] or int(qtdPassagens) < 1 :
                                                print(f'Quantidade ínvalida! Por favor, digite novamente.')
                                                input(f'Pressione ENTER para continuar..')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                
                                            else:
                                                if len(dicPassagensVoos[codVoo].keys()) > 0:
                                                    for cpf in dicPassagensVoos[codVoo]:
                                                        if dicPassagensVoos[codVoo][cpf]['acompanhante'] != {''}:
                                                            contPassageirosVoo += 1 + len(dicPassagensVoos[codVoo][cpf]['acompanhante'].keys())
                                                        else:
                                                            contPassageirosVoo += 1

                                                passagem = f'p{contPassageirosVoo+1}_{codVoo}'

                                                auxContPassageirosVoo = contPassageirosVoo

                                                passagemUtilizada = True
                                                while passagemUtilizada:
                                                    if passagem in listaPassagens:
                                                        auxContPassageirosVoo += 1
                                                        passagem = f'p{auxContPassageirosVoo+1}_{codVoo}'
                                                    else:
                                                        passagemUtilizada = False

                                                verifQtdPassagens = True
                                                qtdPassagens = int(qtdPassagens)

                                                voos[codVoo]['lugares'] -= 1
                                                dicPassagensVoos[codVoo][cpfVendaFormatado] = {
                                                    'nome' : passageiros[cpfVendaFormatado]['nome'],
                                                    'idade' : passageiros[cpfVendaFormatado]['idade'],
                                                    'telefone' : passageiros[cpfVendaFormatado]['telefone'],
                                                    'acompanhante' : {},
                                                    'passagem' : {
                                                        passagem : {'pagador' : cpfVendaFormatado}
                                                    }
                                                }
                                                passageiros[cpfVendaFormatado]['passagens'][passagem] = {
                                                    'pagador' : cpfVendaFormatado
                                                }
                                                listaPassagens.append(passagem)

                                                listaPassageirosIncluidos = []

                                                if qtdPassagens > 1:
                                                    contCadastroViagem = 1
                                                    while contCadastroViagem < qtdPassagens:
                                                        if len(dicPassagensVoos[codVoo].keys()) > 0:
                                                            for cpf in dicPassagensVoos[codVoo]:
                                                                if dicPassagensVoos[codVoo][cpf]['acompanhante'] != {''}:
                                                                    contPassageirosVoo += 1 + len(dicPassagensVoos[codVoo][cpf]['acompanhante'].keys())
                                                                else:
                                                                    contPassageirosVoo += 1

                                                        passagem = f'p{contPassageirosVoo+1}_{codVoo}'

                                                        auxContPassageirosVoo = contPassageirosVoo

                                                        passagemUtilizada = True
                                                        while passagemUtilizada:
                                                            if passagem in listaPassagens:
                                                                auxContPassageirosVoo += 1
                                                                passagem = f'p{auxContPassageirosVoo+1}_{codVoo}'
                                                            else:
                                                                passagemUtilizada = False

                                                        print(f'Digite os dados do {contCadastroViagem+1}º passageiro: ')
                                                        verifCpfPassageiro = False
                                                        while verifCpfPassageiro == False:
                                                            cpfPassageiro = input('Digite o CPF do passageiro: ')

                                                            if cpfPassageiro == '-':
                                                                menuVoos = False
                                                                break
                                                            
                                                            if len(cpfPassageiro) == 14:
                                                                contNumCpf = 0
                                                                contCarCpf = 0
                                                                for i in cpfPassageiro:
                                                                    if i.isdigit():
                                                                        contNumCpf += 1
                                                                    if listCaracteresEspeciais.count(i) == 1:
                                                                        contCarCpf += 1

                                                                if contNumCpf == 11 and contCarCpf == 3 and cpfPassageiro[3] == '.' and cpfPassageiro[7] == '.' and cpfPassageiro[11] == '-':
                                                                    cpfAcompanhanteFormatado = cpfPassageiro
                                                                    verifCpfPassageiro = True
                                                                else:
                                                                    print('CPF inválido, por favor digite novamente!')
                                                                    input('Pressione ENTER para continuar...')
                                                                    continue

                                                            elif len(cpfPassageiro) == 11 and cpfPassageiro.isdigit():
                                                                cpfAcompanhanteFormatado = cpfPassageiro[0:3] + '.' + cpfPassageiro[3:6] + '.' + cpfPassageiro[6:9] + '-' + cpfPassageiro[9:11]
                                                                verifCpfPassageiro = True
                                                            else:
                                                                print('CPF inválido, por favor digite novamente!')
                                                                input('Pressione ENTER para continuar...')
                                                                continue

                                                        if cpfPassageiro == '-':
                                                                menuVoos = False
                                                                break
                                                        
                                                        if cpfAcompanhanteFormatado in passageiros or cpfAcompanhanteFormatado in passageiros[cpfVendaFormatado]['acompanhante']:
                                                            if cpfAcompanhanteFormatado not in passageiros[cpfVendaFormatado]['acompanhante']:
                                                                if cpfAcompanhanteFormatado not in dicPassagensVoos[codVoo]:
                                                                    voos[codVoo]['lugares'] -= 1
                                                                    dicPassagensVoos[codVoo][cpfAcompanhanteFormatado] = {
                                                                    'nome' : passageiros[cpfAcompanhanteFormatado]['nome'],
                                                                    'idade' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                    'telefone' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                    'acompanhante' : {},
                                                                    'passagem' : {
                                                                        passagem : {'pagador' : cpfVendaFormatado}
                                                                        }
                                                                    }

                                                                    passageiros[cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                        'pagador' : cpfVendaFormatado
                                                                    }
                                                                    listaPassagens.append(passagem)
                                                                    listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                                    contCadastroViagem += 1
                                                                    continue
                                                                else:
                                                                    print(f'Passageiro já possui uma passagem comprada no voo: {codVoo}')
                                                                    input('Pressione ENTER para continuar...')
                                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                                    continue
                                                            else:
                                                                if cpfAcompanhanteFormatado not in dicPassagensVoos[codVoo][cpfVendaFormatado]['acompanhante']:
                                                                    print(f'Passageiro encontrado: \nCPF: {cpfAcompanhanteFormatado}\nNome: {passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['nome']}\nSerá incluido como acompanhante de {passageiros[cpfVendaFormatado]['nome']}')

                                                                    voos[codVoo]['lugares'] -= 1
                                                                    dicPassagensVoos[codVoo][cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado] = {
                                                                    'nome': nome,
                                                                    'idade': idade,
                                                                    'telefoneResponsavel' : passageiros[cpfVendaFormatado]['telefone'],
                                                                    'cpfResponsavel' : cpfVendaFormatado,
                                                                    'nomeResponsavel' : passageiros[cpfVendaFormatado]['nome'],
                                                                    'passagem' : {
                                                                        passagem : {'pagador' : cpfVendaFormatado}
                                                                        }
                                                                    }
                                                                    passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                        'pagador' : cpfVendaFormatado
                                                                    }
                                                                    contCadastroViagem += 1
                                                                    listaPassagens.append(passagem)
                                                                    listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                                    continue
                                                                else:
                                                                    print(f'Passageiro já possui uma passagem comprada no voo: {codVoo}')
                                                                    input('Pressione ENTER para continuar...')
                                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                                    continue

                                                        else:
                                                        
                                                            verifNome = False
                                                            while verifNome == False:
                                                                os.system('cls' if os.name == 'nt' else 'clear')

                                                                nome = input('Digite o nome do(a) acompanhante: ').title()

                                                                if nome == '-':
                                                                    menuVoos = False
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
                                                                    input('Pressione ENTER para continuar...')
                                                                    continue
                                                                elif contEspacosVazios > 5:
                                                                    print('O nome não pode conter mais de 5 espaços.')
                                                                    input('Pressione ENTER para continuar...')
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
                                                                menuVoos = False
                                                                break
                                                            
                                                            verifIdade = False
                                                            while verifIdade == False:
                                                                os.system('cls' if os.name == 'nt' else 'clear')

                                                                idade = input('Digite a idade do(a) acompanhante: ')

                                                                if idade == '-':
                                                                    menuVoos = False
                                                                    break

                                                                if idade.isdigit() == False or int(idade) < 1 or int(idade) > 120:
                                                                    print('Idade inválida, por favor digite a sua idade!')
                                                                    input('Pressione ENTER para continuar...')
                                                                    continue
                                                                else:
                                                                    verifIdade = True

                                                            if idade == '-':
                                                                menuVoos = False
                                                                break
                                                            
                                                            if int(idade) >= 18:
                                                                verifTelefone = False
                                                                while verifTelefone == False:
                                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                                    telefone = input('Digite telefone: ')
                                                                    contTelefone = 0

                                                                    if telefone == '-':
                                                                        menuVoos = False
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
                                                                    menuVoos = False
                                                                    break

                                                                passageiros[cpfAcompanhanteFormatado] = {
                                                                    'nome' : nome,
                                                                    'idade' : idade,
                                                                    'telefone' : telefone,
                                                                    'acompanhante' : {},
                                                                    'passagens' : {}
                                                                    }

                                                                voos[codVoo]['lugares'] -= 1
                                                                dicPassagensVoos[codVoo][cpfAcompanhanteFormatado] = {
                                                                    'nome' : passageiros[cpfAcompanhanteFormatado]['nome'],
                                                                    'idade' : passageiros[cpfAcompanhanteFormatado]['idade'],
                                                                    'telefone' : passageiros[cpfAcompanhanteFormatado]['telefone'],
                                                                    'passagem' : {
                                                                        passagem : {'pagador' : cpfVendaFormatado}
                                                                        }
                                                                    }
                                                                passageiros[cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                    'pagador' : cpfVendaFormatado
                                                                }
                                                                contCadastroViagem += 1
                                                                listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                                listaPassagens.append(passagem)
                                                                
                                                            else:
                                                                passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado] = {
                                                                    'nome': nome,
                                                                    'idade': idade,
                                                                    'telefoneResponsavel' : passageiros[cpfVendaFormatado]['telefone'],
                                                                    'cpfResponsavel' : cpfVendaFormatado,
                                                                    'nomeResponsavel' : passageiros[cpfVendaFormatado]['nome'],
                                                                    'passagens' : {}
                                                                    }
                                                            
                                                                voos[codVoo]['lugares'] -= 1
                                                                dicPassagensVoos[codVoo][cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado] = {
                                                                    'nome' :  passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['nome'],
                                                                    'idade' :  passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['idade'],
                                                                    'telefoneResponsavel' : passageiros[cpfVendaFormatado]['telefone'],
                                                                    'cpfResponsavel' : cpfVendaFormatado,
                                                                    'nomeResponsavel' : passageiros[cpfVendaFormatado]['nome'],
                                                                    'passagem' : {
                                                                        passagem : {'pagador' : cpfVendaFormatado}
                                                                        }
                                                                    }
                                                                passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['passagens'][passagem] = {
                                                                    'pagador' : cpfVendaFormatado
                                                                }
                                                                contCadastroViagem += 1
                                                                listaPassagens.append(passagem)
                                                                listaPassageirosIncluidos.append(cpfAcompanhanteFormatado)
                                                        contCadastroViagem += 1
                                                    print(f'===================')       
                                                    for cpf in listaPassageirosIncluidos:
                                                        print(f'{passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['nome']} foi incluido no voo ({codVoo}) como acompanhante de {passageiros[cpfVendaFormatado]['nome']}' 
                                                                if int(passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['idade']) < 18 else f'{passageiros[cpfVendaFormatado]['acompanhante'][cpfAcompanhanteFormatado]['nome']} foi incluido no voo ({codVoo})')
                                                    print(f'===================')
                                                    input(f'Pressione ENTER para continuar..')
                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                    
                                                    listaPassageirosIncluidos = []

                                                else:

                                                    print(f'{passageiros[cpfVendaFormatado]['nome']} foi incluido(a) no voo: {codVoo}!')
                                                    input(f'Pressione ENTER para continuar..')
                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                    
                                elif opcaoPassagem == '2':

                                    verifCpfCancelamento = False
                                    while verifCpfCancelamento == False:

                                        cpfCancelar = input('Digite o CPF do passageiro para cancelar a passagem: ')

                                        if cpfCancelar == '-':
                                            menuVoos = False
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
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue

                                        elif len(cpfCancelar) == 11 and cpfCancelar.isdigit():
                                            cpfCancelarFormatado = cpfCancelar[0:3] + '.' + cpfCancelar[3:6] + '.' + cpfCancelar[6:9] + '-' + cpfCancelar[9:11]
                                            verifCpfCancelamento = True
                                        else:
                                            print('CPF inválido, por favor digite novamente!')
                                            input('Pressione ENTER para continuar...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue
                                    
                                    if cpfCancelar == '-':
                                        menuVoos = False
                                        break
                                    
                                    verifcodigoVooCancelar = False
                                    while not verifcodigoVooCancelar:
                                        contNaoEncontrado = 0
                                        if cpfCancelarFormatado in passageiros:
                                            print(f'Voos em que {passageiros[cpfCancelarFormatado]['nome']} tem passagens:')
                                            print(f'obs: Passageiros acompanhantes (menores de 18) ligados as este CPF são excluídos automaticamente')

                                            for codVoo in dicPassagensVoos:
                                                if cpfCancelarFormatado in dicPassagensVoos[codVoo]:
                                                    print(f'{codVoo}: Origem - {voos[codVoo]['origem']}, destino - {voos[codVoo]['destino']}')
                                                else:
                                                    contNaoEncontrado += 1
                                            if contNaoEncontrado == len(dicPassagensVoos):
                                                print('\nNenhuma passagem encontrada para esse CPF.')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                break
                                            
                                            print(f'Para cancelar a passagem, digite o código do voo (ex: "v-1"): ')
                                            codigoVooCancelar = input(f'--> ')

                                            if codigoVooCancelar == '-':
                                                menuVoos = False
                                                break

                                            if codigoVooCancelar == '' or codigoVooCancelar not in dicPassagensVoos:
                                                print(f'Código inválido! Por favor, digite novamente.')
                                                input(f'Pressione ENTER para continuar..')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                            else:   
                                                verifcodigoVooCancelar = True
                                                print('Passagem cancelada com sucesso!')
                                                contPassageirosVoo = 0
                                                contPassageirosVoo += len(dicPassagensVoos[codVoo][cpfCancelarFormatado]['acompanhante'])+1
                                                voos[codVoo]['lugares'] += contPassageirosVoo
                                                del dicPassagensVoos[codVoo][cpfCancelarFormatado]

                                                for passagem in passageiros[cpfCancelarFormatado]['passagens']:
                                                    if passagem.find(codigoVooCancelar) != -1:
                                                        cancelarPassagem = passagem
                                                del passageiros[cpfCancelarFormatado]['passagens'][cancelarPassagem]

                                                for cpfAcompanhante in passageiros[cpfCancelarFormatado]['acompanhante']:
                                                    for passagemAcompanhante in passageiros[cpfCancelarFormatado]['acompanhante'][cpfAcompanhante]['passagens'].keys():
                                                        if passagemAcompanhante.find(codigoVooCancelar) != -1:
                                                            cancelarPassagemAcompanhante = passagemAcompanhante
                                                            auxiliarCpfAcompanhante = cpfAcompanhante
                                                        del passageiros[cpfCancelarFormatado]['acompanhante'][auxiliarCpfAcompanhante]['passagens'][cancelarPassagemAcompanhante]
                                                input(f'Pressione ENTER para continuar..')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue
                                        else:
                                            passageirosNaoEncontrados = False
                                            for cpf in passageiros:
                                                if cpfCancelarFormatado in passageiros[cpf]['acompanhante']:
                                                    auxCpf = cpf
                                                    passageirosNaoEncontrados = False
                                                    break
                                                else:
                                                    passageirosNaoEncontrados = True

                                            if passageirosNaoEncontrados:
                                                print(f'Nenhum passageiro encontrado com o CPF: {cpfCancelarFormatado}')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                break

                                            print(f'Passageiro encontrado: \nCPF: {cpfCancelarFormatado}\nNome: {passageiros[auxCpf]['acompanhante'][cpfCancelarFormatado]['nome']}')
                                            print(f'obs: Este passageiro é acompanhante de: ')
                                            
                                            for cpf in passageiros:
                                                if cpfCancelarFormatado in passageiros[cpf]['acompanhante']:
                                                    print(f'- {passageiros[cpf]['nome']}')

                                            print(f'\nVoos em que {passageiros[auxCpf]['acompanhante'][cpfCancelarFormatado]['nome']} tem passagens:')
                                            listaCpfCancelarAcompanhante = []
                                            for codVoo in dicPassagensVoos:
                                                for cpf in dicPassagensVoos[codVoo]:
                                                    if cpfCancelarFormatado in dicPassagensVoos[codVoo][cpf]['acompanhante']:
                                                        print(f'{codVoo}: Origem - {voos[codVoo]['origem']}, destino - {voos[codVoo]['destino']}')
                                                        listaCpfCancelarAcompanhante.append(cpf)
                                                    else:
                                                        contNaoEncontrado += 1
                                            if contNaoEncontrado == len(dicPassagensVoos):
                                                print('\nNenhuma passagem encontrada para esse CPF.')
                                                input('Pressione ENTER para continuar...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                break
                                            print(f'Para cancelar a passagem, digite o código do voo (ex: "v-1"): ')
                                            codigoVooCancelar = input(f'--> ')

                                            if codigoVooCancelar == '-':
                                                menuVoos = False
                                                break
                                            
                                            if codigoVooCancelar == '' or codigoVooCancelar not in dicPassagensVoos:
                                                print(f'Código inválido! Por favor, digite novamente.')
                                                input(f'Pressione ENTER para continuar..')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue
                                            else:
                                                verifcodigoVooCancelar = True
                                                print('Passagem cancelada com sucesso!')
                                                voos[codVoo]['lugares'] += 1
                                                for cpf in listaCpfCancelarAcompanhante:
                                                    del dicPassagensVoos[codVoo][cpf]['acompanhante'][cpfCancelarFormatado]

                                                for passagem in passageiros[cpf]['acompanhante'][cpfCancelarFormatado]['passagens']:
                                                    if passagem.find(codigoVooCancelar) != -1:
                                                        cancelarPassagem = passagem
                                                del passageiros[cpf]['acompanhante'][cpfCancelarFormatado]['passagens'][cancelarPassagem]
                                                input(f'Pressione ENTER para continuar..')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue

                                elif opcaoPassagem == '3':
                                    verifMenuPassagem = True
                                    menuVoos = False
                                    os.system('cls' if os.name == 'nt' else 'clear')
                    elif optionVoo == '5':
                        verifCodVooCancelar = False
                        while not verifCodVooCancelar:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Digite o código do voo que deseja cancelar (ex: "v-1"): ')
                            print(f'obs: Todos os passageiros e acompanhantes deste voo serão excluídos automaticamente')
                            codVooCancelar = input(f'--> ')
                            if codVooCancelar == '-':
                                menuVoos = False
                                break
                            if codVooCancelar == '' or codVooCancelar not in voos:
                                print(f'Código inválido ou voo não cadastrado! Por favor, digite novamente.')
                                input(f'Pressione ENTER para continuar..')
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                verifCodVooCancelar = True
                                print(f'Voo encontrado: \nCódigo: {codVooCancelar}\nOrigem: {voos[codVooCancelar]['origem']}\nDestino: {voos[codVooCancelar]['destino']}\nData/Hora: {voos[codVooCancelar]['dataHora']}')
                                print(f'Voo {codVooCancelar} cancelado com sucesso!')
                                if passageiros != {}:
                                    dicCpfPassagemCancelar = {}
                                    listaAuxPassagensCancelar = []
                                    dicPassagensAcompanhantesCancelar = {}
                                    listaAuxPassagensAcompanhantesCancelar = []
                                    for cpf in passageiros:
                                        if passageiros[cpf]['passagens'] != {}:
                                            for passagem in passageiros[cpf]['passagens']:
                                                if passagem.find(codVooCancelar) != -1:
                                                    listaAuxPassagensCancelar.append(passagem)
                                                    dicCpfPassagemCancelar[cpf] = listaAuxPassagensCancelar
                                    
                                    for cpf in dicCpfPassagemCancelar:
                                        for passagem in listaAuxPassagensCancelar:
                                            if passagem in passageiros[cpf]['passagens']:   
                                                del passageiros[cpf]['passagens'][passagem]
                                            if passagem in listaPassagens:
                                                listaPassagens.remove(passagem)

                                    for cpf in passageiros:
                                        if passageiros[cpf]['acompanhante'] != {}:
                                            for cpfAcompanhante in passageiros[cpf]['acompanhante']:
                                                if passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens'] != {}:
                                                    dicPassagensAcompanhantesCancelar[cpf] = {}
                                                    for passagemAcompanhante in passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens']:
                                                        if passagemAcompanhante.find(codVooCancelar) != -1:
                                                            listaAuxPassagensAcompanhantesCancelar.append(passagemAcompanhante)
                                                            dicPassagensAcompanhantesCancelar[cpf][cpfAcompanhante] = listaAuxPassagensAcompanhantesCancelar

                                    for cpf in dicPassagensAcompanhantesCancelar:
                                        for cpfAcompanhante in dicPassagensAcompanhantesCancelar[cpf]:
                                            for passagemAcompanhante in listaAuxPassagensAcompanhantesCancelar:
                                                if passagemAcompanhante in passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens']:
                                                    del passageiros[cpf]['acompanhante'][cpfAcompanhante]['passagens'][passagemAcompanhante]
                                                if passagem in listaPassagens:
                                                    listaPassagens.remove(passagem)
                                if codVooCancelar in dicPassagensVoos:
                                    del dicPassagensVoos[codVooCancelar]
                                del voos[codVooCancelar]
                                contVoo -= 1

                                input(f'Pressione ENTER para continuar..')
                                os.system('cls' if os.name == 'nt' else 'clear')

                    elif optionVoo == '6':
                        break                                     

        elif option == '4':
            print('Finalizando app...')
            break
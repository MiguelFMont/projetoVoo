cadastrosPessoa = dict()
voos = dict()

listCaracteresEspeciais = ['.', '-', '(', ')',] 
listNumVerificacaoOption = ['1', '2', '3', '4']
listNumVerificacaoOptionVoo = ['1', '2', '3', '4', '5']

companhiasAereasBrasil = ['Gol', 'Latam', 'Azul', 'TAM']

estadosParaRegião = {
    'Acre(AC)': 'Norte',
    'Alagoas(AL)': 'Nordeste',
    'Amapá(AP)': 'Norte',
    'Amazonas(AM)': 'Norte',
    'Bahia(BA)': 'Nordeste',
    'Ceará(CE)': 'Nordeste',
    'Distrito Federal(DF)': 'Centro-Oeste',
    'Espírito Santo(ES)': 'Sudeste',
    'Goiás(GO)': 'Centro-Oeste',
    'Maranhão(MA)': 'Nordeste',
    'Mato Grosso do Sul(MS)': 'Centro-Oeste',
    'Mato Grosso(MT)': 'Centro-Oeste',
    'Minas Gerais(MG)': 'Sudeste',
    'Pará(PA)': 'Norte',
    'Paraíba(PB)': 'Nordeste',
    'Paraná(PR)': 'Sul',
    'Pernambuco(PE)': 'Nordeste',
    'Piauí(PI)': 'Nordeste',
    'Rio de Janeiro(RJ)': 'Sudeste',
    'Rio Grande do Norte(RN)': 'Nordeste',
    'Rio Grande do Sul(RS)': 'Sul',
    'Rondônia(RO)': 'Norte',
    'Roraima(RR)': 'Norte',
    'Santa Catarina(SC)': 'Sul',
    'São Paulo(SP)': 'Sudeste',
    'Sergipe(SE)': 'Nordeste',
    'Tocantins(TO)': 	'Norte'
}

while True:
    print('''Escolha uma das opções a baixo:
1 - Cadastrar um passageiro
2 - Passageiros cadastrados
3 - Voos
4 - sair''')
    option = input('\n--> ')
    while len(option) != 1 or listNumVerificacaoOption.count(option) == 0:
        print('Opção inválida, por favor digite uma opção válida!')
        option = input('--> ')
    else:
        if option == '1':
            numPessoas = int(input('Número de pessoas que deseja cadastrar: '))

            pessoas = 0

            while pessoas < numPessoas:
                print(f'\n{pessoas + 1}° Pessoa')

                nome = input('Digite seu nome: ').title()

                while nome == '' or nome.isalpha() == False or len(nome) < 3 or len(nome) > 50:
                    print('Nome inválido, por favor digite o seu nome!')
                    nome = input('Digite seu nome: ').title()

                cpf = input('Digite seu CPF: ')

                listCpf = []

                while len(cpf) == 14:
                    contNumCpf = 0
                    contCarCpf = 0
                    for i in cpf:
                        if i.isdigit() == True:
                            contNumCpf += 1
                        if listCaracteresEspeciais.count(i) == 1:
                            contNumCpf += 1
                    if contNumCpf == 11 and contCarCpf == 3 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
                        break
                    else:
                        print('CPF inválido, por favor digite o seu CPF!')
                        cpf = input('Digite seu CPF: ')

                while len(cpf) == 11 and cpf.isdigit() == True:
                    cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
                    listCpf.append(cpf)
                    break
                else:   
                    print('CPF inválido, por favor digite o seu CPF!')
                    cpf = input('Digite seu CPF: ')

                if cpf in cadastrosPessoa.keys():
                    print('\nCPF inválido, por favor digite o seu CPF!')
                else:
                    idade = input('Digite sua idade: ')

                    while idade.isdigit() == False or int(idade) < 0 or int(idade) > 120:
                        print('Idade inválida, por favor digite a sua idade!')
                        idade = input('Digite sua idade: ')

                    telefone = input('Digite telefone: ')

                    listTelefone = []

                    while telefone.isdigit() == True and len(telefone) == 11:
                        telefone = '(' + telefone[0:2] + ')' + telefone[2:7] + '-' + telefone[7:11]
                        listTelefone.append(telefone)
                        break
                    
                    cadastrosPessoa[cpf] = {
                        'nome': nome,
                        'idade': idade,
                        'telefone': telefone
                    }
                    pessoas += 1
                ##input('Para onde vão: ')
        elif option == '2':
            while True:
                for c, dados in cadastrosPessoa.items():
                    print('------------------')
                    print(f'cpf: {c}')
                    print(f'\ncpf: {c}')
                    print(f'nome: {dados['nome']}')
                    print(f'idade: {dados['idade']}')
                    print(f'telefone: {dados['telefone']}')
                    print('------------------')
        elif option == '3':
            while True:
                print('''Escolha uma das opções a baixo:
                    
1- Cadastrar um voo  
2- Consultar voos cadastrados
3- listar passageiros de um voo
4- 
                    ''')
                optionVoo = input('--> ')
                while len(optionVoo) != 1 or listNumVerificacaoOptionVoo.count(optionVoo) == 0:
                    print('Opção inválida, por favor digite uma opção válida!')
                    optionVoo = input('--> ')
                else:

                    if optionVoo == '1':
                        print('CADASTRO DE VOO\n')
                        origem = input('Digite a origem do voo: ').title()
                        while origem == '' or origem.isalpha() == False or len(origem) < 2 or len(origem) > 50:
                            print('Origem inválida, por favor digite a origem do voo!')
                            origem = input('Digite a origem do voo: ').title()

                        destino = input('Digite o destino do voo: ').title()
                        if destino == origem:
                            print('Origem e destino não podem ser iguais!')
                            destino = input('Digite o destino do voo: ').title()
                        if destino  == estadosParaRegião.keys():
                            print('oi')
                            if estadosParaRegião[destino] == estadosParaRegião.values('Sul'):
                                print('A região Sul não possui voos diretos!')
                                destino = input('Digite o destino do voo: ').title()





        elif option == '4':
            print('Finalizando app...')
            break
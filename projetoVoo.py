cadastrosPessoa = dict()
listCaracteresEspeciais = ['.', '-', '(', ')',] 

while True:
    print('''Escolha uma das opções a baixo:
1 - cadastrar
2 - informações''')
    option = input('\n--> ')
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
            optionInfo = input('\n1 - cadastros de clientes'
            '\n2 - voos'
            '\n3 - sair'
            '\nopcão: ')
            if optionInfo == '1':
                for c, dados in cadastrosPessoa.items():
                    print(f'\ncpf: {c}')
                    print(f'nome: {dados['nome']}')
                    print(f'idade: {dados['idade']}')
                    print(f'telefone: {dados['telefone']}')
            elif optionInfo == '2':
                print('voos**')
            elif optionInfo == '3':
                break
            else:
                print('Digite somente as opções 1, 2 ou 3')
                input('Tecle enter para continuar')
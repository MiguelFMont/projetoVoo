cadastrosPessoa = dict()

pessoas = 0

while True:
    print('\nEscolha uma das opções a baixo: \n'
    '\n1 - cadastrar'
    '\n2 - informações')
    option = input('\n--> ')
    if option == '1':
        numPessoas = int(input('Número de pessoas que deseja cadastrar: '))

        while pessoas < numPessoas:
            print(f'\n{pessoas + 1}° Pessoa')
            nome = input('Digite seu nome: ').title()
            cpf = input('Digite seu CPF: ')
            while cpf.count('.') == 0 or cpf.count('-') == 0:
                listCpf = []
                cont = 0
                for c in cpf:
                    cont+=1
                    listCpf.append(c)
                    if cont == 3 or cont == 6:
                        listCpf.append('.')
                    elif cont == 9:
                        listCpf.append('-')
                break
            x = ''
            for i in listCpf:
                x = x + i
                cpf = x

            if cpf in cadastrosPessoa.keys():
                print('\nCPF inválido, por favor digite o seu CPF!')
            else:
                idade = input('Digite sua idade: ')
                cidade = input('Digite sua cidade: ')

                cadastrosPessoa[cpf] = {
                    'nome': nome,
                    'idade': idade,
                    'cidade origem': cidade
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
                    print(f'cidade origem: {dados['cidade origem']}')
            elif optionInfo == '2':
                print('voos**')
            elif optionInfo == '3':
                break
            else:
                print('Digite somente as opções 1, 2 ou 3')
                input('Tecle enter para continuar')
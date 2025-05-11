listaNumeroVerificacao = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.']

import os

verifPrecoPassagem = False
while verifPrecoPassagem == False:

    precoPassagem = input('Preço da passagem: ')

    if precoPassagem == '':
        os.system('cls')
        print(f'Preço inválido, por favor, digite novamente!\n')
        input('Pressione ENTER para continuar...')
        continue
    else:
        contNumInvalido = 0
        contNum = 0

        for n in precoPassagem:
            if listaNumeroVerificacao.count(n) == 0:
                contNumInvalido += 1
            if n.isdigit() == True:
                contNum += 1
        if contNumInvalido > 0 or contNum == 0:
            os.system('cls')
            print(f'Preço inválido, por favor, digite novamente!\n')
            input('Pressione ENTER para continuar...')                 
            continue

        if precoPassagem.count(',') > 1:
            os.system('cls')
            print(f'Preço inválido, por favor, digite novamente!\n')
            input('Pressione ENTER para continuar...')
            continue
        else:
            precoPassagem = precoPassagem.replace(',', '.')

            precoPassagem = float(precoPassagem)
            
        print(f'Preço da passagem: {precoPassagem:.2f}')
cadastrosPessoa = {}

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
dic = {}
x = ''
for i in listCpf:
    x = x + i
    cpf = x

print(cpf)
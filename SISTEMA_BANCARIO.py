from datetime import date

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
hoje = date.today()
# Formatar a data no formato dd/mm/aaaa
data_formatada = hoje.strftime("%d/%m/%Y")

while True:

    opcao = input (menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'depósito: R$ {valor: .2f}\n'

        else:
            print('Operação falhou! Valor informado é invalido.')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print ('Operação falhou! Você não tem limite suficiente.')  

        elif excedeu_saques:
            print ('Operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print ('Operação falhou! O valor informado é invalido.')

    elif opcao == 'e':
        print ('\n=========EXTRATO=========')
        print ('========BANCO DO BRASIL======')
        print ('Não foram realizado movimentações.' if not extrato else extrato)
        print (f'\nSaldo: R$ {saldo: .2f}')
        print (f'Data: {data_formatada}')
        print ('===========================')

    elif opcao == 'q':
        break

    else:
        print ('Operação invalida, por favor selecione novamete a operação desejada.')
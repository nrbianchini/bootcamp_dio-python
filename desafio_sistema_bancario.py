menu = """
[d] - depositar
[s] - sacar
[e] - extrato
[q] - sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        #criação de variável 'valor' que é pnt flutuante, recebida como entrada
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            #soma-se o valor depositado ao saldo
            saldo += valor
            #adiciona-se ao extrato a seguinte informação:
            extrato += f"depósito: R${valor:.2f}\n"

        else:
            print("operação falhou! o valor informádo é inválido")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        #valor de saque é maior que o saldo
        excedeu_saldo = valor > saldo
        #valor de saque é maior que o limite
        excedeu_limite = valor > limite
        #número de saques excedeu o limite diário
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou! você não tem saldo suficiente.")

        elif excedeu_limite:
            print("operação falhou! o valor do saque excede o limite.")

        elif excedeu_saques:
            print("operação falhou! número máximo de saques excedido.")

        elif valor > 0:
            #diminui-se o valor sacado do saldo
            saldo -= valor
            #adiciona-se ao extrato a seguinte informação:
            extrato += f"saque: R${valor:.2f}\n"
            #aumenta o número de saques para controlar o limite
            numero_saques += 1

        else:
            print("operação falhou! o valor informado é inválido.")

    elif opcao == "e":
        print("\n-------- EXTRATO --------")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"saldo: R${saldo:.2f}")
        print("---------------------------")

    elif opcao == "q":
        break

    else:
        print("operação inválida, por favor selecione novamente a operação desejada.")
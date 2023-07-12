menu_boas_vindas = """
===Banco Bem Vindo===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=====================
=>
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    entrada = input(menu_boas_vindas)

    # Depositar
    if entrada == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("!!!Valor informado informado incorreto.!!!")

    # Sacar
    elif entrada == "s":
        valor = float(input("Informe o valor do saque: "))

        exceder_saldo = valor > saldo
        exceder_limite = valor > limite
        exceder_saques = numero_saques >= LIMITE_SAQUES

        # Filtro de entrada
        if exceder_saldo:
            print("Saldo insuficiente.")
        elif exceder_limite:
            print("Excedeu o limite do saque.")
        elif exceder_saques:
            print("Número máximo de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("!!!Valor inválido!!!")
    
    # Extrato
    elif entrada == "e":
        print("\n=== EXTRATO ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================")

    # Sair
    elif entrada == "q":
        break

    # No caso de não ser nenhuma das opções
    else:
        print("Operação inválida, informe novamente a operação desejada")
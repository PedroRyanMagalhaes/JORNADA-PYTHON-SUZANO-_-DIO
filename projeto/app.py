from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0 
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor_do_deposito):
    global saldo
    global extrato
    if valor_do_deposito > 0:
        saldo = saldo + valor_do_deposito
        print("Depósito realizado com sucesso.")
        extrato.append(f"Depósito: R$ {valor_do_deposito:.2f} no dia {datetime.now():%d/%m/%Y %H:%M:%S}")
    else:
        print("Operação falhou! O valor informado é inválido.")

def saque(valor_do_saque):
    global saldo
    global extrato
    global numero_saques
    if valor_do_saque > 0 and valor_do_saque <= 500:
        if valor_do_saque <= saldo:
            if numero_saques < LIMITE_SAQUES:
                saldo = saldo - valor_do_saque
                print("Saque realizado com sucesso.")
                extrato.append(f"Saque: R$ {valor_do_saque:.2f} no dia {datetime.now():%d/%m/%Y %H:%M:%S}")
                numero_saques += 1
            else:
                print("Operação falhou! Número máximo de saques diários excedido.")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")
    else:
        print("Operação falhou! O valor informado é inválido.")


def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")


while True:
    opcao = input(menu)

    if opcao == "d":
        valor_do_deposito = float(input("Informe o valor do depósito: "))
        deposito(valor_do_deposito)
        print("deposito")

    elif opcao == "s":
        valor_do_saque = float(input("Informe o valor do saque: "))
        saque(valor_do_saque)
        print("saque")

    elif opcao == "e":
        exibir_extrato()
        print("extrato")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



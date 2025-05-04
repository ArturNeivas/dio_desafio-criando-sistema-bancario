saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
BANCO DO PROGRAMADOR
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

### Funções
def func_deposito(dep):
    global saldo
    global extrato
    
    if dep > 0:
        saldo += dep
        extrato.append(f"Depósito: R${dep:.2f}")
    
        print(f"Você realizou o deposito no valor de R${dep:.2f} reais.")
        print(f"Seu saldo é de R${saldo:.2f} reais.")
    
    else:
        print("Depósito invalido.")


def func_sacar(sac):
    global saldo
    global extrato
    global numero_saques
    global limite
    
    if sac < 0:
        print("Saque invalido.")
    
    elif sac > saldo:
        print(f"Saldo indisponivel, seu saldo é de R${saldo:.2f}.")

    elif sac > limite:
        print("Saque é superior ao limite de R${limite}.")
    
    elif numero_saques > LIMITE_SAQUES:
        print(f"Você usou seus limites de saques diarios.")
    
    else:
        saldo -= sac
        extrato.append(f"Saque: R${sac:.2f}")
    
        print(f"Você realizou o saque no valor de R${sac:.2f} reais.")
        print(f"Seu saldo é de R${saldo:.2f} reais.")
        
        numero_saques += 1
        print(f"NUMERO DE SAQUE: {numero_saques} ||LIMITE DE SAQUE: {LIMITE_SAQUES}")

def mostrar_extrato():
    print("Extrato")
    for item in extrato:
        print(item)

while True:

    opcao = input(menu)

    if opcao == "d":
        print ("Depósito")
        valor_deposito = float(input("Quanto gostaria de depositar: "))
        func_deposito(valor_deposito)

    elif opcao == "s":
        print ("Saque")
        valor_saque = float(input("Quanto gostaria de sacar: "))
        func_sacar(valor_saque) 
    

    elif opcao == "e":
        print(' ')
        mostrar_extrato()
        print(' ')
        print('=====')

    elif opcao == "q":
        break                        

    else:
        print("Operação inválida, por favor selecione a operação desajada.")
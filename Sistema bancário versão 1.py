# Novo Sistema Conta Bancária Para o Banco Y

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

LIMITE_DIARIO_SAQUES = 3
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Quanto você deseja depositar na sua conta bancária: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Saldo final da conta: {saldo}")

        else:
            print("Ocorreu um problema com o depósito. Tente novamente mais tarde.")

    elif opcao == "2":
        valor = float(input("Quanto você deseja sacar hoje: "))

        excedeu_limite_diario = numero_saques >= LIMITE_DIARIO_SAQUES

        excedeu_limite_saque = limite_saque > valor

        excedeu_saldo = valor > saldo

        if excedeu_limite_diario: 
                print("Não é possível realizar mais de três saques por dia. Tente novamente amanhã.")

        elif excedeu_limite_saque:
                print("Não é possível retirar mais de 500 reais por saque. Diminua o valor para a operação ser bem sucedida.")
        
        elif excedeu_saldo:
             print("Não há saldo o suficiente na sua conta para retirar o saque desejado.")

        elif valor > 0:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2f}\n"
             numero_saques += 1
             print("Saldo restante da conta: {saldo}")

        else: 
             print("Ocorreu um problema com o saque. Tente novamente mais tarde.")
    
    elif opcao == "3":
         print("O seu extrato das últimas horas é de:")
         print("Não houve movimentação na sua conta nas últimas horas." if not extrato else extrato)
         print(saldo)
    
    elif opcao == "0":
         print("Saindo da sua conta bancária. Até em breve!")
         break
    
    else:
         print("É necessário escolher uma das opções para acessar a sua conta.")








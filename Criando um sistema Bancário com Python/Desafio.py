# Dados Bancarios
menu = """
        ---------------    MENU    ---------------        

                       [1] Depositar
                       [2] Sacar
                       [3] Extrato
                       [0] Sair

        >>>>>>>>>>>>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

# Operação de Deposito
    if opcao == "1":
        print()
        valor_deposito = float(input("Digite o valor de Deposito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print("Valor Depositado com Sucesso!!")
        else:
            print()
            print("O valor de deposito é inferior a 0 e não pode ser depositado!")
    
# Operação de Saque
    elif opcao == "2":
        if numero_saques != 3:
           print()
           print("*********** Lembrando que o limite de saque é R$500.00 ***********")
           valor_saque = float(input("Digite o valor de Saque: "))
           if valor_saque <= 500.00:
               if saldo <= valor_saque:
                   print()
                   print("Saldo insuficiente para a operação!")
               else:
                   numero_saques += 1
                   saldo -= valor_saque
                   print(f"Saque de R${valor_saque}")
                   print("Faça a retirada do valor na boca do Caixa")
                   print()
           else:
               print()
               print("Valor digitado maior que o limite de saque permitido!")
               
        else:
            print()
            print("Limite de saque diario atingindo!!")

# Operação de extrato
    elif opcao == "3":
        extrato = f"R${saldo:.2f}"
        print()
        print("*********** Extrato Bancário ***********")
        print(extrato)
    
    elif opcao == "0":
        print()
        print("Obrigado por utilizar nosso sistema, volte sempre!")
        break
    else:
        print()
        print("Operação inválida, por favor selecione novamente a operação desejada.")












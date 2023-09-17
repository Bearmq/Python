# tomar cuidado pra n por mtos elifs no codigo pq isso aumenta a complexidade dele.
saldo = 5000
opcao = int(input('Escolha uma opção:\n [1] Sacar \n [2] Estrato: \n [3] Saldo:  '))
if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
    if valor > saldo:
        print("Quantia inválida!")

elif opcao == 2:
    print("Exibindo o Extrato...")

elif opcao == 3:
    print('Seu saldo é:', saldo)

else:
    print('Opção Inválida!')
#Operador and precisa que as duas partes sejam verdadeiras para dar true. Se tiver um falso, entao a resposta vai ser false
saldo = 1000
saque = 200
limite = 100

prin2 = saldo >= saque and saque <= limite
print(prin2)

#Operador ou (or), se tiver um verdadeiro então a resposta será true é vdd se apenas uma expressão já for verdadeira. Pra ser falso, tudo tem q ser falso.
saldo = 1000
saque = 200
limite = 100

prin1 = saldo >= saque or saque <= limite
print(prin1)

#Operador de negação not, a negação de falso é verdadeiro. É o inverso da vdd
contatos_emergencia = []
not 1000 > 5000
not contatos_emergencia
not "saque 1500"
not ""

#Parênteses 
saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp1)
#dessa forma é mais legivel pois ele le da esquerda para a direita e começa pelos parenteses
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)



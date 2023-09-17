# em Python podemos fazer o if/else na msm linha

saldo = 100
saque = 1000

status = "Sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")
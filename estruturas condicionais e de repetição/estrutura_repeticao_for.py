texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: #n é comum no dia a dia
    print() #adiciona uma quebra de linha
    print('Execulta no final do laço')

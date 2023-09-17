# f string esse metodo ainda é melhor q os outros dois, porém ainda tem pontos negativos
# como por exemplo, se eu quissese a variavel nome varias vezes teria q escreve-la varias vezes.
nome = "Beatriz"
idade = 22
profissao = "Programadora"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade trabalho como {profissao} e estou matriculada no curso de {linguagem}.")

PI = 3.14159
# esse .2f, é o numero de casas q quero q ele considere e de espaços
print(f"Valor de PI: {PI:.2f} ")

print(f"Valor de PI: {PI:10.2f}")



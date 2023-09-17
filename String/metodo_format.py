# Metodo Format
nome = "Beatriz"
idade = 22
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade trabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

# Aqui ele traz uma capacidade um pouco mair de costumização 
print("Olá, me chamo {3}. Eu tenho {2} anos de idade trabalho como {1} e estou matriculada no curso de {0}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade trabalho como {profissão} e estou matriculada no curso de {Python}.".format(nome, idade, profissao, linguagem))


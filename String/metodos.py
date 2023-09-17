nome = "BeAtrIz"

# Deixa todas as letras Maiúsculas
print(nome.upper())

# Deixa todas as letras minúsculas
print(nome.lower())

# Transforma em titulo
print(nome.title())

cidi = "  Bsb "

# Tira espaços em branco
print(cidi.strip() + ".")

# Põe o espaço em branco no fim da string -remove lado esquerdo
print(cidi.lstrip() + ".")

# Deixa o espaço em branco -remove espaço direito
print(cidi.rstrip() + ".")

curso = "Python"

# Junta e centraliza (poe o numero de caracteres e oq quer juntar)
# Se não informar qual caracter quer juntar "#"  ele adiciona espaço em branco
# para poder totalizar 10
print(curso.center(10, "#"))

#  Ele vai adicionar . entre cada letra
print(".".join(curso))
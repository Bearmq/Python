# esse desafio pede para que o usuario faça um tweet de ate 140 caracteres, 
# se passar disso, ele imprime MUTE
T = str(input("Faça um Tweet: "))

# len compara a string T com 140
if len(T) <= 140:
  print("TWEET")

else:
  print("MUTE")
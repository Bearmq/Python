nome = 'Beatriz'

mensagem = f'''
    Olá meu nome é {nome},
  Eu estou aprendendo Python.
      Eu estou aprendendo Python.
'''
print(mensagem)

# É mais facil usar assim
print('''

    ****************MENU****************
    1 - Depositar
    2 - Sacar
    0 - Sair

    *************************************

        Obrigado por usar nosso sistema!!!

''')

# do que ter o trabalho de fazer assim
menu = "****************MENU****************"
menu += '\n'
menu += '1 - Depositar'

print(menu)
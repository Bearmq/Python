# Esse desafio pede para que o usuario entre com um numero entre 1 e 12,
#  e reponde com o mes equivalente aquele numero
month = int(input("Digite o número do més desejado"))

# É so definir tudo aq ao inves de por varios elifs
months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
   
}
if month in months_dict:
    print(months_dict[month])
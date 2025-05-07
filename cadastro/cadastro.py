# Privacidade e Comunicação
privacy = bool(input("Autoriza? S/N: \n"))
communication = bool(input("AUtoriza S/N: \n"))

# Declaração de variáveis
nome = input("Digite o seu nome: ")
idade = float(input("Digite sua idade: "))
rua = input("Digite sua rua: ")
numero = input("Digite o número da sua rua: ")
complemento = input("Digite o complemento, se houver: ")
bairro = input("Digite o seu bairro: ")
cidade = input("Digite o nome da sua cidade: ")
estado = input("Digite o nome do seu estado: ")
cep = input("Digite seu CEP: ")

# Concatenação das variáveis de endereço e criação de variável global
endereco = f"{rua},{numero}, {complemento}, {bairro}, {cidade}, {estado}, {cep}"

print("-----------------------------------------------------------")
print("O seu nome é ", nome)
print("Sua idade é ", idade)
print("O seu endereço é ", endereco)
print("-----------------------------------------------------------")

# Inicializamos lista com zeros para definir o tamanho

NOME = [0] * 3
IDADE = [0] * 3
TELEFONE = [0] * 3
MATRICULA = [0] * 3

# A variavel 'cont' é usada como índice para percorrer as listas

cont = 0

# Loop 'for' em Python que itera de 0 até 2 (inclusive)

for cont in range(3):
    # Imprime o cabeçalho do cadastro, incrementando 'cont'
    # Para exibir o número do cadastro
    print(f"------- {cont+1}º CADASTRO -------")
    print()
    
    # Solicita e lê o nome do usuário, armazenando-o na lista NOME na posição 'cont'
    print("Digite o seu nome: ")
    NOME[cont] = input()
    
    # Solicita e lê a idade do usuário, convertendo a
    # entrada para inteiro e armazenando na lista IDADE.
    print("Digite a sua idade: ")
    IDADE[cont] = int(input())
    
    # Solicita e lê o telefone do usuário, armazenando os dados
    print("Digite o seu telefone: ")
    TELEFONE[cont] = int(input())
    
    #Solicita e lê a matrícula do usuário, armazenando os dados
    print("Digite sua matrícula: ")
    MATRICULA[cont] = int(input())
    
# Simula a limpeza da tela     
print("\n" * 20)

# print(f"1º Cadastro: {NOME[0]}, {IDADE[0]}, {TELEFONE[0]}, {MATRICULA[0]}")
# print(f"2º Cadastro: {NOME[1]}, {IDADE[1]}, {TELEFONE[1]}, {MATRICULA[1]}")
# print(f"3º Cadastro: {NOME[2]}, {IDADE[2]}, {TELEFONE[2]}, {MATRICULA[2]}")


#Outro loop 'for' para exibir os dados cadastrados
for cont in range(3):
    #Imprime os dados de cada pessoa formatadas.
    # Imprime o cabeçalho do cadastro, incrementando 'cont'
    # Para exibir o número do cadastro
    print(f"------- {cont+1}º CADASTRO -------")
    print()
    print(f"NOME: {NOME[cont]}")
    print(f"IDADE: {IDADE[cont]}")
    print(f"TELEFONE: {TELEFONE[cont]}")
    print(f"MATRÍCULA: {MATRICULA[cont]}")
print("--------------------------------------")
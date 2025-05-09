print("SEJA BEM-VINDO(A) AO PIZZA PIAZZA!\n\n VAMOS COMEÇAR O SEU PEDIDO?")
print("------------------------------------------------------------")
print("")

print("PARA COMEÇAR, DIGITE O SEU NOME:")
nome = input().upper()
print("------------------------------------------------------------")
print("")

print("DIGITE O SEU E-MAIL:")
email = input().upper()
print("------------------------------------------------------------")
print("")

print("DIGITE O SEU TELEFONE:")
telefone = input().upper()
print("------------------------------------------------------------")
print("")

print("EXCELENTE!\n AGORA, VAMOS PASSAR PARA O SEU ENDEREÇO")

print("DIGITE O NOME SEU LOGRADOURO (RUA, VIELA, AVENIDA...):")
logradouro = input().upper()
print("")

print("DIGITE O NÚMERO:")
numero_endereco = input().upper()
print("")

print("DIGITE O BAIRRO:")
bairro = input().upper()
print("")

print("DIGITE A CIDADE:")
cidade = input().upper()
print("")

print("DIGITE O CEP:")
cep = input().upper()
print("------------------------------------------------------------")
print("")

endereco = (f"{logradouro}, {numero_endereco}, {bairro}, {cidade}, {cep}")

print("EXCELENTE!\n AGORA, VAMOS PASSAR PARA O SEU PEDIDO")
print("")
print("*************************SABORES DE PIZZAS*************************")
print("CALABRESA, FRANGO COM CATUPIRY, PORTUGUESA E TRÊS QUEIJOS")
print("")

print("*************************TAMANHOS DE PIZZAS*************************")
print("* PIZZA PEQUENA - R$ 10,00 *")
print("* PIZZA MÉDIA - R$ 12,00 *")
print("* PIZZA GRANDE - R$ 20,00 *")
print("")

print("*************************REFRIGERANTES*************************")
print("* COCA-COLA - R$ 13,00 *")
print("* GUARANÁ ANTÁRTICA - R$ 10,00 *")
print("* FANTA LARANJA - R$ 7,00 *")
print("")

print("FAÇA AGORA O SEU PEDIDO")
print("")

print("QUAL SABOR DE PIZZA VOCÊ DESEJA:")
print("1 - CALABRESA")
print("2 - FRANGO COM CATUPIRY")
print("3 - PORTUGUESA")
print("4 - TRÊS QUEIJOS")
print("________________________________________________________________")
saborpizza = int(input())
print("")

print("DIGITE O TAMANHO DA PIZZA:")
print("P - PIZZA PEQUENA - R$ 10,00")
print("M - MÉDIA - R$ 12,00")
print("G - GRANDE - R$ 20,00")
print("________________________________________________________________")
tamanho_pizza = input().upper()
print("")

print("VOCÊ GOSTARIA DE REFRIGERANTE? SE SIM, ESCOLHA O NÚMERO:")
print("0 - NÃO DESEJO REFRIGERANTE")
print("1 - COCA-COLA - R$ 13,00")
print("2 - GUARANÁ ANTÁRTICA - R$ 10,00")
print("3 - FANTA LARANJA - R$ 7,00")
print("________________________________________________________________")
refrigerante = int(input())
print("")
print("")

#PEDIDOS PEQUENOS ----------------------------------------------------------------------------------------
#Pedidos de CALABRESA (1)

if(saborpizza == 1) and (tamanho_pizza == "P") and (refrigerante == 0):
    preco_pedido = 10.00
    pedido = "PIZZA DE CALABRESA PEQUENA SEM REFRIGERANTE"

elif(saborpizza == 1) and (tamanho_pizza == "P") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00  
    pedido = "PIZZA DE CALABRESA PEQUENA COM COCA-COLA"
    
elif(saborpizza == 1) and (tamanho_pizza == "P") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00   
    pedido = "PIZZA DE CALABRESA PEQUENA COM GUARANÁ ANTÁRTICA" 

elif(saborpizza == 1) and (tamanho_pizza == "P") and (refrigerante == 3):
    preco_pedido = 10.00 + 7.00   
    pedido = "PIZZA DE CALABRESA PEQUENA COM FANTA LARANJA" 
    
    
#Pedidos de FRANGO COM CATUPIRY (2)
    
elif(saborpizza == 2) and (tamanho_pizza == "P") and (refrigerante == 0):
    preco_pedido = 10.00
    pedido = "PIZZA DE FRANGO COM CATUPIRY PEQUENA SEM REFRIGERANTE" 

elif(saborpizza == 2) and (tamanho_pizza == "P") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 
    pedido = "PIZZA DE FRANGO COM CATUPIRY PEQUENA COM COCA-COLA" 
    
elif(saborpizza == 2) and (tamanho_pizza == "P") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 
    pedido = "PIZZA DE FRANGO COM CATUPIRY PEQUENA COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 2) and (tamanho_pizza == "P") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 
    pedido = "PIZZA DE FRANGO COM CATUPIRY PEQUENA COM FANTA LARANJA" 
    

#Pedidos de PORTUGUESA (3)
    
elif(saborpizza == 3) and (tamanho_pizza == "P") and (refrigerante == 0):
    preco_pedido = 10.00
    pedido = "PIZZA DE PORTUGUESA PEQUENA SEM REFRIGERANTE" 

elif(saborpizza == 3) and (tamanho_pizza == "P") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 
    pedido = "PIZZA DE PORTUGUESA PEQUENA COM COCA-COLA" 
    
elif(saborpizza == 3) and (tamanho_pizza == "P") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 
    pedido = "PIZZA DE PORTUGUESA PEQUENA COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 3) and (tamanho_pizza == "P") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 
    pedido = "PIZZA DE PORTUGUESA PEQUENA COM FANTA LARANJA" 
    
#Pedidos de TRÊS QUEIJOS (4)
    
elif(saborpizza == 4) and (tamanho_pizza == "P") and (refrigerante == 0):
    preco_pedido = 10.00
    pedido = "PIZZA DE TRÊS QUEIJOS PEQUENA SEM REFRIGERANTE" 

elif(saborpizza == 4) and (tamanho_pizza == "P") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 
    pedido = "PIZZA DE TRÊS QUEIJOS PEQUENA COM COCA-COLA" 
    
elif(saborpizza == 4) and (tamanho_pizza == "P") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 
    pedido = "PIZZA DE TRÊS QUEIJOS PEQUENA COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 4) and (tamanho_pizza == "P") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 
    pedido = "PIZZA DE TRÊS QUEIJOS PEQUENA COM FANTA LARANJA" 
    
#PEDIDOS MÉDIOS ----------------------------------------------------------------------------------------    
# Pedido de CALABRESA (1)
elif(saborpizza == 1) and (tamanho_pizza == "M") and (refrigerante == 0):
    preco_pedido = 12.00
    pedido = "PIZZA DE CALABRESA MÉDIA SEM REFRIGERANTE"
    
elif(saborpizza == 1) and (tamanho_pizza == "M") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 2.00  
    pedido = "PIZZA DE CALABRESA MÉDIA COM COCA-COLA"
    
elif(saborpizza == 1) and (tamanho_pizza == "M") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 2.00  
    pedido = "PIZZA DE CALABRESA MÉDIA COM GUARANÁ ANTÁRTICA" 

elif(saborpizza == 1) and (tamanho_pizza == "M") and (refrigerante == 3):
    preco_pedido = 10.00 + 7.00 + 2.00     
    pedido = "PIZZA DE CALABRESA MÉDIA COM FANTA LARANJA" 
    
    
#Pedidos de FRANGO COM CATUPIRY (2)
    
elif(saborpizza == 2) and (tamanho_pizza == "M") and (refrigerante == 0):
    preco_pedido = 10.00 + 2.00  
    pedido = "PIZZA DE FRANGO COM CATUPIRY MÉDIA SEM REFRIGERANTE" 

elif(saborpizza == 2) and (tamanho_pizza == "M") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 2.00  
    pedido = "PIZZA DE FRANGO COM CATUPIRY MÉDIA COM COCA-COLA" 
    
elif(saborpizza == 2) and (tamanho_pizza == "M") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 2.00   
    pedido = "PIZZA DE FRANGO COM CATUPIRY MÉDIA COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 2) and (tamanho_pizza == "M") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 + 2.00   
    pedido = "PIZZA DE FRANGO COM CATUPIRY MÉDIA COM FANTA LARANJA" 
    

#Pedidos de PORTUGUESA (3)
    
elif(saborpizza == 3) and (tamanho_pizza == "M") and (refrigerante == 0):
    preco_pedido = 10.00 + 2.00  
    pedido = "PIZZA DE PORTUGUESA MÉDIA SEM REFRIGERANTE" 

elif(saborpizza == 3) and (tamanho_pizza == "M") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 2.00  
    pedido = "PIZZA DE PORTUGUESA MÉDIA COM COCA-COLA" 
    
elif(saborpizza == 3) and (tamanho_pizza == "M") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 2.00   
    pedido = "PIZZA DE PORTUGUESA MÉDIA COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 3) and (tamanho_pizza == "M") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 + 2.00   
    pedido = "PIZZA DE PORTUGUESA MÉDIA COM FANTA LARANJA" 
    
#Pedidos de TRÊS QUEIJOS (4)
    
elif(saborpizza == 4) and (tamanho_pizza == "M") and (refrigerante == 0):
    preco_pedido = 10.00 + 2.00  
    pedido = "PIZZA DE TRÊS QUEIJOS MÉDIA SEM REFRIGERANTE" 

elif(saborpizza == 4) and (tamanho_pizza == "M") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 2.00   
    pedido = "PIZZA DE TRÊS QUEIJOS MÉDIA COM COCA-COLA" 
    
elif(saborpizza == 4) and (tamanho_pizza == "M") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 2.00   
    pedido = "PIZZA DE TRÊS QUEIJOS MÉDIA COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 4) and (tamanho_pizza == "M") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 + 2.00   
    pedido = "PIZZA DE TRÊS QUEIJOS MÉDIA COM FANTA LARANJA" 

#PEDIDOS GRANDES ----------------------------------------------------------------------------------------
    
# Pedido de CALABRESA (1)
elif(saborpizza == 1) and (tamanho_pizza == "G") and (refrigerante == 0):
    preco_pedido = 20.00
    pedido = "PIZZA DE CALABRESA GRANDE SEM REFRIGERANTE"
    
elif(saborpizza == 1) and (tamanho_pizza == "G") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 10.00  
    pedido = "PIZZA DE CALABRESA GRANDE COM COCA-COLA"
    
elif(saborpizza == 1) and (tamanho_pizza == "G") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 10.00  
    pedido = "PIZZA DE CALABRESA GRANDE COM GUARANÁ ANTÁRTICA" 

elif(saborpizza == 1) and (tamanho_pizza == "G") and (refrigerante == 3):
    preco_pedido = 10.00 + 7.00 + 10.00     
    pedido = "PIZZA DE CALABRESA GRANDE COM FANTA LARANJA" 
    
    
#Pedidos de FRANGO COM CATUPIRY (2)
    
elif(saborpizza == 2) and (tamanho_pizza == "G") and (refrigerante == 0):
    preco_pedido = 20.00
    pedido = "PIZZA DE FRANGO COM CATUPIRY GRANDE SEM REFRIGERANTE" 

elif(saborpizza == 2) and (tamanho_pizza == "G") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 10.00  
    pedido = "PIZZA DE FRANGO COM CATUPIRY GRANDE COM COCA-COLA" 
    
elif(saborpizza == 2) and (tamanho_pizza == "G") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 10.00   
    pedido = "PIZZA DE FRANGO COM CATUPIRY GRANDE COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 2) and (tamanho_pizza == "G") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 + 10.00   
    pedido = "PIZZA DE FRANGO COM CATUPIRY GRANDE COM FANTA LARANJA" 
    

#Pedidos de PORTUGUESA (3)
    
elif(saborpizza == 3) and (tamanho_pizza == "G") and (refrigerante == 0):
    preco_pedido = 10.00 + 10.00  
    pedido = "PIZZA DE PORTUGUESA GRANDE SEM REFRIGERANTE" 

elif(saborpizza == 3) and (tamanho_pizza == "G") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 10.00  
    pedido = "PIZZA DE PORTUGUESA GRANDE COM COCA-COLA" 
    
elif(saborpizza == 3) and (tamanho_pizza == "G") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 10.00   
    pedido = "PIZZA DE PORTUGUESA GRANDE COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 3) and (tamanho_pizza == "G") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 + 10.00   
    pedido = "PIZZA DE PORTUGUESA GRANDE COM FANTA LARANJA" 
    
#Pedidos de TRÊS QUEIJOS (4)
    
elif(saborpizza == 4) and (tamanho_pizza == "G") and (refrigerante == 0):
    preco_pedido = 10.00 + 10.00  
    pedido = "PIZZA DE TRÊS QUEIJOS GRANDE SEM REFRIGERANTE" 

elif(saborpizza == 4) and (tamanho_pizza == "G") and (refrigerante == 1):
    preco_pedido = 10.00 + 13.00 + 10.00   
    pedido = "PIZZA DE TRÊS QUEIJOS GRANDE COM COCA-COLA" 
    
elif(saborpizza == 4) and (tamanho_pizza == "G") and (refrigerante == 2):
    preco_pedido = 10.00 + 10.00 + 10.00   
    pedido = "PIZZA DE TRÊS QUEIJOS GRANDE COM GUARANÁ ANTÁRTICA" 
    
elif(saborpizza == 4) and (tamanho_pizza == "G") and (refrigerante == 3):
    preco_pedido = 10.00 + 10.00 + 10.00   
    pedido = "PIZZA DE TRÊS QUEIJOS GRANDE COM FANTA LARANJA"

else:
    preco_pedido = 0.0
    pedido = "PEDIDO INVÁLIDO"

print("")
print("------------------------------------------------------------")
print("************************* DESCRIÇÃO DO PEDIDO *************************")
print(f"NOME DO SOLICITANTE: {nome}")
print(f"E-MAIL DO SOLICITANTE: {email}")
print(f"CONTATO DO SOLICITANTE: {telefone}")
print(f"ENDEREÇO DO SOLICITANTE: {endereco}")
print("------------------------------------------------------------")
print(f"O TOTAL A PAGAR É: R$ {preco_pedido:.2f}")
print("------------------------------------------------------------")
print(f"SEU PEDIDIO FOI: {pedido}")
print("------------------------------------------------------------")

print("")
print("")
print("EM BREVE O PEDIDO SERÁ LIBERADO PARA ENTREGA!")
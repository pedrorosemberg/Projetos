#Calculadora simples de dois números

#       1. Solicitando os números
num1 = float(input("Digite o pimeiro número: "))
num2 = float(input("Digite o segundo número: "))

#       2. Solicitando as operações
operador = input("Digite a operação:\nSomar (+)\nSubtrair (-)\nDividir (/)\nMultiplicar (*)\nPotenciação (**)\n")

#       3. Realizando as operções
if operador == '+':
    resultado = num1+num2

elif operador == '-':
    resultado = num1-num2

elif operador == '*':
    resultado = num1*num2

elif operador == '**':
    resultado = num1**num2

elif operador == '/':
    
    if num2 != 0:
        resultado = num1/num2
    
    else: 
        resultado = "Erro: Divisão por zero!"

else: 
    resultado = "Operação inválida. Tente novamente."

#       4. Resultado
print(f"\nO resultado é: {resultado}\n")

# Outra forma de utilizar: 
# print("O resultado é: " + str(resultado))
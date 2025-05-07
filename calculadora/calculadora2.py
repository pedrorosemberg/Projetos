import tkinter as tk


# Função para calcular o resultado
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operador = operador_var.get()

        # Realizando as operações
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "**":
            resultado = num1**num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero!"
        else:
            resultado = "Operação inválida."

        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida!")


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Criando widgets
label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operador = tk.Label(root, text="Escolha a operação:")
label_operador.pack()

operador_var = tk.StringVar(value="+")

# Opções de operação
opcoes = ["+", "-", "*", "/", "**"]
for op in opcoes:
    radio = tk.Radiobutton(root, text=op, variable=operador_var, value=op)
    radio.pack()

# Botão para calcular
button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack()

# Iniciando a interface
root.mainloop()

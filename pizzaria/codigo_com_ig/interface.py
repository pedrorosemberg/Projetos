# interface.py
import tkinter as tk
from tkinter import ttk, messagebox
from logica import calcular_pedido

def iniciar_interface():
    def enviar_pedido():
        dados = {
            "nome": nome_var.get().upper(),
            "email": email_var.get().upper(),
            "telefone": telefone_var.get().upper(),
            "logradouro": logradouro_var.get().upper(),
            "numero": numero_var.get().upper(),
            "bairro": bairro_var.get().upper(),
            "cidade": cidade_var.get().upper(),
            "cep": cep_var.get().upper(),
            "sabor": sabores.index(sabor_var.get()) + 1,
            "tamanho": tamanho_var.get(),
            "refrigerante": refrigerantes.index(refri_var.get())
        }

        resultado = calcular_pedido(dados)

        if resultado["valido"]:
            messagebox.showinfo("Pedido Realizado", f"{resultado['resumo']}\nTotal: R$ {resultado['preco']:.2f}")
        else:
            messagebox.showerror("Erro", "Pedido inválido.")

    janela = tk.Tk()
    janela.title("Pizza Piazza")

    # Variáveis
    nome_var = tk.StringVar()
    email_var = tk.StringVar()
    telefone_var = tk.StringVar()
    logradouro_var = tk.StringVar()
    numero_var = tk.StringVar()
    bairro_var = tk.StringVar()
    cidade_var = tk.StringVar()
    cep_var = tk.StringVar()

    sabores = ["Calabresa", "Frango com Catupiry", "Portuguesa", "Três Queijos"]
    sabor_var = tk.StringVar(value=sabores[0])

    tamanhos = ["P", "M", "G"]
    tamanho_var = tk.StringVar(value="P")

    refrigerantes = ["Nenhum", "Coca-Cola", "Guaraná Antártica", "Fanta Laranja"]
    refri_var = tk.StringVar(value=refrigerantes[0])

    # Layout
    campos = [
        ("Nome", nome_var),
        ("Email", email_var),
        ("Telefone", telefone_var),
        ("Logradouro", logradouro_var),
        ("Número", numero_var),
        ("Bairro", bairro_var),
        ("Cidade", cidade_var),
        ("CEP", cep_var)
    ]

    for texto, var in campos:
        tk.Label(janela, text=texto).pack()
        tk.Entry(janela, textvariable=var).pack()

    tk.Label(janela, text="Sabor").pack()
    ttk.Combobox(janela, textvariable=sabor_var, values=sabores, state="readonly").pack()

    tk.Label(janela, text="Tamanho").pack()
    ttk.Combobox(janela, textvariable=tamanho_var, values=tamanhos, state="readonly").pack()

    tk.Label(janela, text="Refrigerante").pack()
    ttk.Combobox(janela, textvariable=refri_var, values=refrigerantes, state="readonly").pack()

    tk.Button(janela, text="Finalizar Pedido", command=enviar_pedido).pack(pady=10)

    janela.mainloop()

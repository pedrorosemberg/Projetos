#interface.py

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from logica import calcular_pedido, buscar_cep, historico_pedidos
import json
import re
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Piazza")
        self.root.geometry("800x600")
        
        # Configurando tema
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Variáveis
        self.nome_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.telefone_var = tk.StringVar()
        self.logradouro_var = tk.StringVar()
        self.numero_var = tk.StringVar()
        self.bairro_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.uf_var = tk.StringVar()
        self.cep_var = tk.StringVar()
        
        self.sabores = ["Calabresa", "Frango com Catupiry", "Portuguesa", "Três Queijos"]
        self.sabor_var = tk.StringVar(value=self.sabores[0])
        
        self.tamanhos = ["P", "M", "G"]
        self.tamanho_var = tk.StringVar(value="P")
        
        self.refrigerantes = ["Nenhum", "Coca-Cola", "Guaraná Antártica", "Fanta Laranja"]
        self.refri_var = tk.StringVar(value=self.refrigerantes[0])
        
        # Criando notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Aba de pedido
        self.tab_pedido = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_pedido, text="Fazer Pedido")
        
        # Aba de histórico
        self.tab_historico = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_historico, text="Histórico de Pedidos")
        
        # Configurar layout da aba de pedido
        self.setup_pedido_tab()
        
        # Configurar layout da aba de histórico
        self.setup_historico_tab()
    
    def setup_pedido_tab(self):
        frame_principal = ttk.Frame(self.tab_pedido)
        frame_principal.pack(fill="both", expand=True)
        
        # Dividir em duas colunas
        frame_esquerda = ttk.Frame(frame_principal)
        frame_esquerda.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        frame_direita = ttk.Frame(frame_principal)
        frame_direita.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        
        # Frame para dados pessoais
        frame_dados = ttk.LabelFrame(frame_esquerda, text="Dados do Cliente")
        frame_dados.pack(fill="both", expand=True, padx=5, pady=5)
        
        # CEP primeiro com botão para busca
        ttk.Label(frame_dados, text="CEP*").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        frame_cep = ttk.Frame(frame_dados)
        frame_cep.grid(row=0, column=1, sticky="we", padx=5, pady=2)
        ttk.Entry(frame_cep, textvariable=self.cep_var, width=15).pack(side="left")
        ttk.Button(frame_cep, text="Buscar", command=self.buscar_endereco).pack(side="left", padx=5)
        
        # Demais dados de endereço
        ttk.Label(frame_dados, text="Logradouro*").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.logradouro_var, width=40).grid(row=1, column=1, sticky="we", padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Número*").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.numero_var, width=10).grid(row=2, column=1, sticky="w", padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Bairro*").grid(row=3, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.bairro_var, width=30).grid(row=3, column=1, sticky="we", padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Cidade*").grid(row=4, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.cidade_var, width=30).grid(row=4, column=1, sticky="we", padx=5, pady=2)
        
        ttk.Label(frame_dados, text="UF*").grid(row=5, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.uf_var, width=5).grid(row=5, column=1, sticky="w", padx=5, pady=2)
        
        # Dados de contato
        ttk.Label(frame_dados, text="Nome*").grid(row=6, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.nome_var, width=40).grid(row=6, column=1, sticky="we", padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Email*").grid(row=7, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.email_var, width=40).grid(row=7, column=1, sticky="we", padx=5, pady=2)
        
        ttk.Label(frame_dados, text="Telefone*").grid(row=8, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(frame_dados, textvariable=self.telefone_var, width=20).grid(row=8, column=1, sticky="w", padx=5, pady=2)
        
        # Frame para pedido
        frame_pedido = ttk.LabelFrame(frame_direita, text="Seu Pedido")
        frame_pedido.pack(fill="both", expand=True, padx=5, pady=5)
        
        ttk.Label(frame_pedido, text="Sabor da Pizza*").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(frame_pedido, textvariable=self.sabor_var, values=self.sabores, state="readonly", width=25).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_pedido, text="Tamanho*").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        frame_tamanho = ttk.Frame(frame_pedido)
        frame_tamanho.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        for i, tam in enumerate(self.tamanhos):
            ttk.Radiobutton(frame_tamanho, text=f"{tam} ({self.get_tamanho_desc(tam)})", variable=self.tamanho_var, value=tam).pack(side="left", padx=3)
        
        ttk.Label(frame_pedido, text="Refrigerante").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Combobox(frame_pedido, textvariable=self.refri_var, values=self.refrigerantes, state="readonly", width=25).grid(row=2, column=1, padx=5, pady=5)
        
        # Resumo do pedido (como NF-e)
        self.frame_resumo = ttk.LabelFrame(frame_direita, text="Resumo do Pedido")
        self.frame_resumo.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.resumo_text = scrolledtext.ScrolledText(self.frame_resumo, width=40, height=10, wrap=tk.WORD, state="disabled")
        self.resumo_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Botões de ação
        frame_botoes = ttk.Frame(frame_direita)
        frame_botoes.pack(fill="x", padx=5, pady=10)
        
        ttk.Button(frame_botoes, text="Calcular Pedido", command=self.calcular).pack(side="left", padx=5)
        ttk.Button(frame_botoes, text="Finalizar Pedido", command=self.finalizar_pedido).pack(side="right", padx=5)
        
    def setup_historico_tab(self):
        frame_top = ttk.Frame(self.tab_historico)
        frame_top.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_top, text="Histórico de Pedidos", font=("Arial", 12, "bold")).pack(side="left")
        ttk.Button(frame_top, text="Exportar Selecionado (PDF)", command=self.exportar_pdf).pack(side="right", padx=5)
        
        # Tabela de pedidos
        columns = ("id", "data", "cliente", "pedido", "valor")
        self.tabela = ttk.Treeview(self.tab_historico, columns=columns, show="headings")
        
        # Definindo os cabeçalhos
        self.tabela.heading("id", text="Nº")
        self.tabela.heading("data", text="Data/Hora")
        self.tabela.heading("cliente", text="Cliente")
        self.tabela.heading("pedido", text="Pedido")
        self.tabela.heading("valor", text="Valor")
        
        # Definindo o tamanho das colunas
        self.tabela.column("id", width=50)
        self.tabela.column("data", width=150)
        self.tabela.column("cliente", width=150)
        self.tabela.column("pedido", width=250)
        self.tabela.column("valor", width=80)
        
        # Adicionando scrollbar
        scrollbar = ttk.Scrollbar(self.tab_historico, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scrollbar.set)
        
        self.tabela.pack(fill="both", expand=True, padx=10, pady=5)
        scrollbar.pack(side="right", fill="y")
        
        # Detalhes do pedido selecionado
        frame_detalhes = ttk.LabelFrame(self.tab_historico, text="Detalhes do Pedido")
        frame_detalhes.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.detalhes_text = scrolledtext.ScrolledText(frame_detalhes, width=60, height=10, wrap=tk.WORD, state="disabled")
        self.detalhes_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Vincular evento de seleção na tabela
        self.tabela.bind("<<TreeviewSelect>>", self.mostrar_detalhes_pedido)
    
    def get_tamanho_desc(self, tamanho):
        descricoes = {"P": "Pequena", "M": "Média", "G": "Grande"}
        return descricoes.get(tamanho, "")
        
    def buscar_endereco(self):
        cep = self.cep_var.get()
        if not cep:
            messagebox.showwarning("CEP Vazio", "Por favor, digite um CEP!")
            return
            
        resultado = buscar_cep(cep)
        
        if resultado.get("erro"):
            messagebox.showerror("Erro", resultado["erro"])
            return
            
        # Preencher os campos com os dados retornados
        self.logradouro_var.set(resultado["logradouro"])
        self.bairro_var.set(resultado["bairro"])
        self.cidade_var.set(resultado["cidade"])
        self.uf_var.set(resultado["uf"])
        self.cep_var.set(resultado["cep"])
        
        # Foco no campo número
        for widget in self.tab_pedido.winfo_children():
            if isinstance(widget, ttk.Frame):
                for subwidget in widget.winfo_children():
                    if isinstance(subwidget, ttk.Frame):
                        for child in subwidget.winfo_children():
                            if isinstance(child, ttk.LabelFrame) and child.cget("text") == "Dados do Cliente":
                                for grandchild in child.winfo_children():
                                    if isinstance(grandchild, ttk.Entry) and grandchild.grid_info().get("row") == 2:
                                        grandchild.focus_set()
                                        break
    
    def calcular(self):
        # Validação básica
        if not self.validar_campos():
            return
            
        dados = self.coletar_dados()
        resultado = calcular_pedido(dados)
        
        if not resultado["valido"]:
            messagebox.showerror("Erro", "Pedido inválido.")
            return
            
        # Atualizar resumo (como NF-e)
        self.atualizar_resumo(resultado["nfe"])
            
    def validar_campos(self):
        campos_obrigatorios = [
            (self.nome_var.get(), "Nome"),
            (self.email_var.get(), "Email"),
            (self.telefone_var.get(), "Telefone"),
            (self.logradouro_var.get(), "Logradouro"),
            (self.numero_var.get(), "Número"),
            (self.bairro_var.get(), "Bairro"),
            (self.cidade_var.get(), "Cidade"),
            (self.cep_var.get(), "CEP")
        ]
        
        for valor, nome in campos_obrigatorios:
            if not valor.strip():
                messagebox.showwarning("Campo Obrigatório", f"O campo {nome} é obrigatório!")
                return False
                
        # Validar e-mail
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.email_var.get()):
            messagebox.showwarning("Email Inválido", "Por favor, digite um email válido!")
            return False
            
        return True
        
    def coletar_dados(self):
        return {
            "nome": self.nome_var.get().upper(),
            "email": self.email_var.get().upper(),
            "telefone": self.telefone_var.get().upper(),
            "logradouro": self.logradouro_var.get().upper(),
            "numero": self.numero_var.get().upper(),
            "bairro": self.bairro_var.get().upper(),
            "cidade": self.cidade_var.get().upper(),
            "cep": self.cep_var.get().upper(),
            "sabor": self.sabores.index(self.sabor_var.get()) + 1,
            "tamanho": self.tamanho_var.get(),
            "refrigerante": self.refrigerantes.index(self.refri_var.get())
        }
        
    def atualizar_resumo(self, nfe):
        self.resumo_text.config(state="normal")
        self.resumo_text.delete(1.0, tk.END)
        
        # Formatar como NF-e
        resumo = f"""
NOTA FISCAL SIMPLIFICADA - PIZZA PIAZZA
Nº: {nfe['numero']}
Data: {nfe['data']}
------------------------------------------
CLIENTE: {nfe['cliente']['nome']}
ENDEREÇO: {nfe['cliente']['endereco']}
------------------------------------------
ITENS:
"""
        
        for item in nfe['itens']:
            resumo += f"{item['descricao']} - R$ {item['valor']:.2f}\n"
            
        resumo += f"""
------------------------------------------
TOTAL: R$ {nfe['total']:.2f}
"""
        
        self.resumo_text.insert(tk.END, resumo)
        self.resumo_text.config(state="disabled")
        
    def finalizar_pedido(self):
        if not self.validar_campos():
            return
            
        dados = self.coletar_dados()
        resultado = calcular_pedido(dados)
        
        if not resultado["valido"]:
            messagebox.showerror("Erro", "Pedido inválido.")
            return
            
        # Adicionar ao histórico
        historico_pedidos.append(resultado["nfe"])
        
        # Atualizar tabela de histórico
        self.atualizar_tabela_historico()
        
        # Mostrar confirmação
        messagebox.showinfo("Pedido Finalizado", "Seu pedido foi finalizado com sucesso!")
        
        # Mudar para a aba de histórico
        self.notebook.select(self.tab_historico)
        
    def atualizar_tabela_historico(self):
        # Limpar tabela
        for item in self.tabela.get_children():
            self.tabela.delete(item)
            
        # Adicionar itens
        for pedido in historico_pedidos:
            self.tabela.insert("", "end", values=(
                pedido["numero"],
                pedido["data"],
                pedido["cliente"]["nome"],
                ", ".join([item["descricao"] for item in pedido["itens"]]),
                f"R$ {pedido['total']:.2f}"
            ))
            
    def mostrar_detalhes_pedido(self, event):
        # Obter o item selecionado
        selecionado = self.tabela.selection()
        if not selecionado:
            return
            
        item = self.tabela.item(selecionado[0])
        numero_pedido = item["values"][0]
        
        # Encontrar o pedido correspondente
        pedido = None
        for p in historico_pedidos:
            if p["numero"] == numero_pedido:
                pedido = p
                break
                
        if not pedido:
            return
            
        # Exibir detalhes
        self.detalhes_text.config(state="normal")
        self.detalhes_text.delete(1.0, tk.END)
        
        detalhes = f"""
PIZZA PIAZZA - DETALHES DO PEDIDO
==================================================
Nº do Pedido: {pedido['numero']}
Data/Hora: {pedido['data']}
==================================================

DADOS DO CLIENTE:
--------------------------------------------------
Nome: {pedido['cliente']['nome']}
Email: {pedido['cliente']['email']}
Telefone: {pedido['cliente']['telefone']}
Endereço: {pedido['cliente']['endereco']}
--------------------------------------------------

ITENS DO PEDIDO:
--------------------------------------------------
"""
        
        for item in pedido['itens']:
            detalhes += f"- {item['descricao']}: R$ {item['valor']:.2f}\n"
            
        detalhes += f"""
--------------------------------------------------
TOTAL DO PEDIDO: R$ {pedido['total']:.2f}
==================================================
        """
        
        self.detalhes_text.insert(tk.END, detalhes)
        self.detalhes_text.config(state="disabled")
        
    def exportar_pdf(self):
        # Obter o item selecionado
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Seleção", "Por favor, selecione um pedido para exportar!")
            return
            
        item = self.tabela.item(selecionado[0])
        numero_pedido = item["values"][0]
        
        # Encontrar o pedido correspondente
        pedido = None
        for p in historico_pedidos:
            if p["numero"] == numero_pedido:
                pedido = p
                break
                
        if not pedido:
            return
            
        # Solicitar local para salvar
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=f"pedido_{pedido['numero']}.pdf"
        )
        
        if not filename:
            return
            
        # Gerar PDF
        self.gerar_pdf(pedido, filename)
        
        messagebox.showinfo("Exportação", f"Pedido exportado com sucesso para {filename}")
        
    def gerar_pdf(self, pedido, filename):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        
        styles = getSampleStyleSheet()
        title_style = styles["Title"]
        heading_style = styles["Heading2"]
        normal_style = styles["Normal"]
        
        # Título
        elements.append(Paragraph(f"PIZZA PIAZZA - NOTA FISCAL SIMPLIFICADA", title_style))
        elements.append(Spacer(1, 0.25*inch))
        
        # Informações do pedido
        elements.append(Paragraph(f"Pedido Nº: {pedido['numero']}", heading_style))
        elements.append(Paragraph(f"Data/Hora: {pedido['data']}", normal_style))
        elements.append(Spacer(1, 0.25*inch))
        
        # Dados do cliente
        elements.append(Paragraph("DADOS DO CLIENTE", heading_style))
        cliente_data = [
            ["Nome:", pedido['cliente']['nome']],
            ["Email:", pedido['cliente']['email']],
            ["Telefone:", pedido['cliente']['telefone']],
            ["Endereço:", pedido['cliente']['endereco']]
        ]
        
        cliente_table = Table(cliente_data, colWidths=[1.5*inch, 5*inch])
        cliente_table.setStyle(TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(cliente_table)
        elements.append(Spacer(1, 0.25*inch))
        
        # Itens do pedido
        elements.append(Paragraph("ITENS DO PEDIDO", heading_style))
        items_data = [["Item", "Valor (R$)"]]
        
        for item in pedido['itens']:
            items_data.append([item['descricao'], f"{item['valor']:.2f}"])
            
        # Adicionar linha de total
        items_data.append(["TOTAL", f"{pedido['total']:.2f}"])
        
        items_table = Table(items_data, colWidths=[5*inch, 1.5*inch])
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -2), 'Helvetica'),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ]))
        elements.append(items_table)
        
        # Nota de rodapé
        elements.append(Spacer(1, 0.5*inch))
        elements.append(Paragraph("Obrigado por escolher a Pizza Piazza!", normal_style))
        elements.append(Paragraph("Este documento não possui valor fiscal oficial.", normal_style))
        
        doc.build(elements)

def iniciar_interface():
    root = tk.Tk()
    app = PizzaApp(root)
    root.mainloop()
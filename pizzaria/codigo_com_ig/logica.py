#logica.py

import requests
import re
from datetime import datetime

class Pedido:
    def __init__(self, dados):
        self.dados = dados
        self.data_hora = datetime.now()
        self.id = int(self.data_hora.timestamp())
        self.calcular()
    
    def calcular(self):
        nome = self.dados["nome"]
        email = self.dados["email"]
        telefone = self.dados["telefone"]
        endereco = f"{self.dados['logradouro']}, {self.dados['numero']}, {self.dados['bairro']}, {self.dados['cidade']}, {self.dados['cep']}"
        saborpizza = self.dados["sabor"]
        tamanho = self.dados["tamanho"]
        refri = self.dados["refrigerante"]
        preco = 0.0
        pedido = "PEDIDO INVÁLIDO"
        valido = True
        
        # Preços
        precos_pizza = {"P": 10.0, "M": 12.0, "G": 20.0}
        precos_refri = [0, 13.0, 10.0, 7.0]
        adicionais = {"M": 2.0, "G": 10.0, "P": 0.0}
        sabores_map = {1: "CALABRESA", 2: "FRANGO COM CATUPIRY", 3: "PORTUGUESA", 4: "TRÊS QUEIJOS"}
        tamanho_nome = {"P": "PEQUENA", "M": "MÉDIA", "G": "GRANDE"}
        refri_nome = ["SEM REFRIGERANTE", "COM COCA-COLA", "COM GUARANÁ ANTÁRTICA", "COM FANTA LARANJA"]
        
        if saborpizza in sabores_map and tamanho in precos_pizza:
            preco = precos_pizza[tamanho] + precos_refri[refri] + adicionais[tamanho]
            pedido = f"PIZZA DE {sabores_map[saborpizza]} {tamanho_nome[tamanho]} {refri_nome[refri]}"
        else:
            valido = False
            
        self.preco = preco
        self.pedido_descricao = pedido
        self.valido = valido
        self.resumo = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nEndereço: {endereco}\nPedido: {pedido}"
        
        # Dados para NF-e
        self.data_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M:%S")
        self.itens = [
            {"descricao": f"PIZZA {sabores_map[saborpizza]} {tamanho_nome[tamanho]}", 
             "valor": precos_pizza[tamanho] + adicionais[tamanho]},
        ]
        
        if refri > 0:
            self.itens.append({"descricao": refri_nome[refri].replace("COM ", ""), 
                              "valor": precos_refri[refri]})
            
    def gerar_nfe(self):
        # Gera um dicionário com todas as informações para a NF-e
        return {
            "numero": self.id,
            "data": self.data_formatada,
            "cliente": {
                "nome": self.dados["nome"],
                "email": self.dados["email"],
                "telefone": self.dados["telefone"],
                "endereco": f"{self.dados['logradouro']}, {self.dados['numero']}, {self.dados['bairro']}, {self.dados['cidade']}, {self.dados['cep']}"
            },
            "itens": self.itens,
            "total": self.preco
        }

def buscar_cep(cep):
    # Remove caracteres não numéricos
    cep_limpo = re.sub(r'[^0-9]', '', cep)
    
    if len(cep_limpo) != 8:
        return {"erro": "CEP deve conter 8 dígitos"}
    
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep_limpo}/json/')
        data = response.json()
        
        if "erro" in data:
            return {"erro": "CEP não encontrado"}
            
        return {
            "cep": data["cep"],
            "logradouro": data["logradouro"],
            "bairro": data["bairro"],
            "cidade": data["localidade"],
            "uf": data["uf"],
            "erro": None
        }
    except Exception as e:
        return {"erro": f"Erro ao buscar CEP: {str(e)}"}

def calcular_pedido(dados):
    pedido = Pedido(dados)
    return {
        "preco": pedido.preco, 
        "resumo": pedido.resumo, 
        "valido": pedido.valido,
        "nfe": pedido.gerar_nfe()
    }

# Lista para armazenar o histórico de pedidos
historico_pedidos = []
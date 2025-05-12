# logica.py

def calcular_pedido(dados):
    nome = dados["nome"]
    email = dados["email"]
    telefone = dados["telefone"]
    endereco = f"{dados['logradouro']}, {dados['numero']}, {dados['bairro']}, {dados['cidade']}, {dados['cep']}"
    saborpizza = dados["sabor"]
    tamanho = dados["tamanho"]
    refri = dados["refrigerante"]

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

    resumo = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nEndereço: {endereco}\nPedido: {pedido}"

    return {"preco": preco, "resumo": resumo, "valido": valido}

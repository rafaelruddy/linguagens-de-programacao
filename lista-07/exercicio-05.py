# 5. Catálogo de Produtos
# Crie um dicionário onde as chaves representem códigos de produtos e os valores
# sejam tuplas contendo o nome do produto e seu preço. Permita que o usuário
# informe um código para buscar o nome e o preço do produto correspondente.

catalogo = {
    1: ("Camiseta", 29.99),
    2: ("Calça", 59.99),
    3: ("Tênis", 99.99)
}

codigo = int(input("Digite o código do produto: "))

if codigo in catalogo:
    produto, preco = catalogo[codigo]
    print(f"Nome: {produto}\nPreço: {preco}")
else:
    print("Código inválido.")
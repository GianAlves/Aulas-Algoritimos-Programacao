produtos = ['Refrigerante', 'Cerveja', 'Água', 'Suco', 'Vinho']
precos = [6.50, 7.0, 2.50, 3.50, 15.00]
qntProduto = [25, 22, 30, 25, 10]

def imprimirProduto(produto):
    for k, v in enumerate (produtos):
        if v == produto:
            return print(f'Produto: {v}, Preço: R${precos[k]}, Quantidade: {qntProduto[k]}')

def retirarProduto(produto):
    for k, v in enumerate(produtos):
        if v == produto:
            produtos.pop(k)
            print(f'Produto removido: {v}')


imprimirProduto('Cerveja')

retirarProduto('Suco')

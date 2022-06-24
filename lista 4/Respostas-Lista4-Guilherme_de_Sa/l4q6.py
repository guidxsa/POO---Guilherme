class Pedido:
    def __init__(self, lista_produtos):
        self.quant = 0
        self.total = 0
        self.lista = lista_produtos
        self.pagamento = None

    def fazer_pedido(self):
        item = input('Digite qual item deseja adicionar ao pedido:')

        for i in  range (len(self.lista)):
            if item == self.lista[i].nome:
                self.quant = int(input('O quanto deseja desse item? '))
                
                if self.quant >=0 and self.quant <= self.lista[i].estoque:
                    self.total = self.lista[i].preco * self.quant

                    self.pagamento = input('Digite a forma de pagamento(Dinheiro, Cheque ou Cartao): ')
                    print('\t\tPedido\n\n{} - {}\n\nTotal: {:.2f}R$\nForma de Pagamento: {}'.format(self.quant, self.lista[i].nome, self.total, self.pagamento))
                else:
                    print('Inválido!')

                break
            
            elif i == len(self.lista) - 1:
                print('Produto não cadastrado!')

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

if __name__ == '__main__':

    lista_produtos = []

    produto_1 = Produto('Arroz', 20, 20)
    lista_produtos.append(produto_1)

    produto_2 = Produto('Feijão', 25, 15)
    lista_produtos.append(produto_2)

    produto_3 = Produto('Pilha', 10, 5)
    lista_produtos.append(produto_3)

    pedido = Pedido(lista_produtos)

    pedido.fazer_pedido()
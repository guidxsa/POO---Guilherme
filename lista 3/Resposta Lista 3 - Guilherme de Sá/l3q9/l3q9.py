import pickle

with open ('arquivo.bin', 'wb') as arq:
    pass

def inserir (arq, lista_codigos, lista_produtos):
    codigo = int(input('Digite o código do produto: '))
    while codigo in lista_codigos:
        print('Codigo repetido, tente outro\n')
        codigo = int(input('Digite o código do produto: '))
    lista_codigos.append(codigo)
    nome = input('Digite o nome do produto: ')
    quant = int(input('Digite a quantidade em estoque do produto: '))
    preco = float(input('Digite o preço do produto: '))
    produto = [codigo, nome, quant, preco]
    lista_produtos.append(produto)
    
    with open ('arquivo.bin', 'ab') as arq:
        pickle.dump(produto, arq)
        
def alterar (arq, lista_codigos, lista_produtos):
    codigo = int(input('Digite o código do produto: '))
    if codigo in lista_codigos:
        for i in range (len(lista_produtos)):
            ultimo_codigo = lista_produtos[i][0]
            if ultimo_codigo == codigo:
                lista_produtos.pop(i)
                break
        nome = input('Digite o nome do produto: ')
        quant = int(input('Digite a quantidade em estoque do produto: '))
        preco = float(input('Digite o preço do produto: '))
        produto = [codigo, nome, quant, preco]
        lista_produtos.append(produto)
        
        with open ('arquivo.bin', 'wb') as arq:
            for i in range(len(lista_produtos)):
                pickle.dump(lista_produtos[i], arq)

    else:
        print('Código não encontrado\n')

def excluir (arq, lista_codigos, lista_produtos):
    codigo = int(input('Digite o código do produto: '))
    if codigo in lista_codigos:
        lista_codigos.remove(codigo)
        for i in range(len(lista_produtos)):
            ultimo_codigo = lista_produtos[i][0]
            if ultimo_codigo == codigo:
                lista_produtos.pop(i)
                break
        
        with open ('arquivo.bin', 'wb') as arq:
            for i in range(len(lista_produtos)):
                pickle.dump(lista_produtos[i], arq)
            print('Produto removido\n')
    else:
        print('Código não encontrado\n')

def consultar(arq, lista_codigos, lista_produtos):
    codigo = int(input('Digite o código do produto: '))

    if len(lista_codigos) > 0:
        lista_produtos = []
        with open ('arquivo.bin', 'rb') as arq:
            while True:
                try:
                    lista_produtos.append(pickle.load(arq))
                except EOFError:
                    break

                for i in range (len(lista_produtos)):
                    if lista_produtos[i][0] == codigo:
                        print('Código: {}\nNome: {}\nQuantidade em Estoque: {}\nPreço: R${:.2f}'.format(lista_produtos[i][0], lista_produtos[i][1], lista_produtos[i][2], lista_produtos[i][3]))
                        break
                    elif i == len(lista_produtos) - 1:
                        print('Código não encontrado\n')
    else:
        print('Arquivo sem produtos cadastrados\n')       

        

def listar(arq, lista_codigos, lista_produtos):

    if len(lista_codigos) > 0:
        lista_produtos = []
        with open ('arquivo.bin', 'rb') as arq:
            while True:
                try:
                    lista_produtos.append(pickle.load(arq))
                except EOFError:
                    break
        print('\t\tLista de Produtos\n')

        for i in range (len(lista_produtos)):
            print('Código: {}\nNome: {}\nQuantidade em Estoque: {}\nPreço: R${:.2f}\n'.format(lista_produtos[i][0], lista_produtos[i][1], lista_produtos[i][2], lista_produtos[i][3]))

    else:
        print('Arquivo sem produtos cadastrados\n')  

def estatisticas(arq, lista_codigos, lista_produtos):
    print('\t\tDados Estatísticos\n')
    print('Quantidade de Produtos Cadastrados: {}'.format(len(lista_produtos)))

    if len(lista_codigos) > 0:
        total_estoque = 0
        baixo_estoque = 0
        total_preco = 0

        for produto in lista_produtos:
            total_estoque += produto[2]
            if produto[2] < 20:
                baixo_estoque += 1
        percentual_baixo = baixo_estoque * 100 / len(lista_produtos)
        print('Quantidade de produtos com estoque baixo: {}\nPercentual de produtos com estoque baixo: {:.2f}%'.format(baixo_estoque, percentual_baixo))
        
        media = total_estoque / len(lista_produtos)
        acima_media = 0

        for produto in lista_produtos:
            if produto[2] > media:
                acima_media += 1   
        percentual_media = acima_media * 100 / len(lista_produtos)
        print('Quantidade de produtos acima da média: {}\nPercentual de produtos acima da média: {:.2f}%'.format(acima_media, percentual_media))

        for produto in lista_produtos:
            total_preco += produto[3]
        media_preco = total_preco / len(lista_produtos)
        var = 0
        for produto in lista_produtos:
            var += (produto[3] - media_preco) ** 2
        
        desvio_p = var ** 0.5

        print('Média geral dos preços: R${}\nDesvio padrão dos preços: {}'.format(media_preco, desvio_p))
    else:
        print('Quantidade de produtos com estoque baixo: 0\nPercentual de produtos com estoque baixo: 0%')
        print('Quantidade de produtos acima da média: 0\nPercentual de produtos acima da média: 0%')
        print('Média geral dos preços: R$0.00\nDesvio padrão dos preços: 0')


lista_codigos = []
lista_produtos = []

while True:
    opcao = int(input('CADASTRO DE PRODUTOS\n\n\t1 - INSERIR UM NOVO PRODUTO\n\t2 - ALTERAR UM PRODUTO\n\t3 - EXCLUIR UM PRODUTO\n\t4 - EXCLUIR TODOS OS PRODUTOS\n\t5 - CONSULTAR UM PRODUTO\n\t6 - LISTAR TODOS OS PRODUTOS\n\t7 - EXIBIR DADOS ESTATISTICOS\n\t8 - SAIR\n\nDIGITE SUA OPÇÃO:'))

    if opcao == 1:
        inserir(arq, lista_codigos, lista_produtos)
    elif opcao == 2:
        alterar(arq, lista_codigos, lista_produtos)
    elif opcao == 3:
        excluir(arq, lista_codigos, lista_produtos)
    elif opcao == 4:
        lista_codigos = []
        lista_produtos = []
        with open ('arquivo.bin', 'wb') as arq:
            pass
    elif opcao == 5:
        consultar(arq, lista_codigos, lista_produtos)
    elif opcao == 6:
        listar(arq, lista_codigos, lista_produtos)
    elif opcao == 7:
        estatisticas(arq, lista_codigos, lista_produtos)
    elif opcao == 8:
        break
    else:
        print('\n\nOPÇÃO INVÁLIDA!\n\n')
from l4q9 import Fatura

if __name__ == '__main__':

    continuar = 1

    while continuar == 1:
        num = int(input('Digite o numero do item:'))
        desc = input('Digite a descreição do item:')
        quant = int(input('Digite a quantidade que deseja:'))
        preco = float(input('Digite o preço unitário:'))

        fatura = Fatura(num, desc, quant, preco)

        fatura.set_num_item()
        fatura.set_desc_item()
        fatura.set_quant_item()
        fatura.set_preco_item()
        fatura.set_calcular_valor_fatura()

        print('\n\t\tFatura\n{}x - Item {}:{} - R${:.2f} preço unitário\n\nTotal: R${:.2f}'.format(fatura.get_quant_item(), fatura.get_num_item(), fatura.get_desc_item(), fatura.get_preco_item(), fatura.get_calcular_valor_fatura()))
        continuar = input('\nDeseja continuar? Digite 1 caso sim: ')
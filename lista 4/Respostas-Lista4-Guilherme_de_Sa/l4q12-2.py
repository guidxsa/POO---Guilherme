from l4q12 import Voo

if __name__ == '__main__':

    voo = Voo(5, 'Vitória', 'Salvador', '20/06/2022')

    while 1:
        escolha = int(input('\t1 - Próximo Livre\n\t2 - Verificar Assento\n\t3 - Marcar Assento\n\t4 - Retornar Vagas\nDigite a sua escolha:'))

        if escolha == 1:
            print('\nO número do próximo assento livre é:', voo.proximo_livre())
    
        elif escolha == 2:
            num_cadeira = int(input('Digite o número da cadeira: '))
            if num_cadeira > 0 and num_cadeira <= 200:
                if voo.verifica_assento(num_cadeira) == False:
                    print('\nAssento não foi ocupado!')
                else:
                    print('\nAssento já ocupado!')

            else:
                print('Número de cadeira inválido!') 
                
        elif escolha == 3:
            num_cadeira = int(input('Digite o número da cadeira: '))
            if num_cadeira > 0 and num_cadeira <= 200:
                if voo.marcar_assento(num_cadeira) == True:
                    print('Operação foi bem sucedida!')
                else:
                    print('Assento já ocupado!')
                
            else:
                print('Número de cadeira inválido!')


        elif escolha == 4:
            print('Assentos livres: ', voo.retornar_vagas())

    
        else:
            break
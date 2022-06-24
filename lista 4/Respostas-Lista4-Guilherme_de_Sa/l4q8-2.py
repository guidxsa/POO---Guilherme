from l4q8 import Elevador

if __name__ == '__main__':
    elevador = Elevador(5, 5)

    elevador.set_inicializar()
    elevador.get_inicializar()

    while 1:
        escolha = int(input('\t1 - Inicializar\n\t2 - Entrar\n\t3 - Sair\n\t4 - Subir\n\t5 - Descer\nDigite a sua escolha:'))

        if escolha == 1:
            elevador.set_inicializar()
            elevador.get_inicializar()
    
        elif escolha == 2:
            elevador.set_entrar()
            elevador.get_entrar()
    
        elif escolha == 3:
            elevador.set_sair()
            elevador.get_sair()

        elif escolha == 4:
            elevador.set_subir()
            elevador.get_subir()
    
        elif escolha == 5:
            elevador.set_descer()
            elevador.get_descer()
    
        else:
            break

        elevador.imprimir()
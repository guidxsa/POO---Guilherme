class Jogador:
    def __init__(self, nome, posicao, nasc, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nasc = nasc
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso
        self.__idade = 0
        self.__aposentar = 0

    def set_idade(self):
        self.__idade = 2022 - int(self.data_nasc[len(self.data_nasc) - 4:])
    
    def get_idade(self):
        return self.__idade

    def set_aposentar(self):
        if self.posicao == 'defensor':
            media = 40
            self.__aposentar = media - self.__idade
        
        elif self.posicao == 'meia':
            media = 38
            self.__aposentar = media - self.__idade
        
        elif self.posicao == 'atacante':
            media = 35
            self.__aposentar = media - self.__idade
        else:
            self.__aposentar = -500
        
    def get_aposentar(self):
        return self.__aposentar
    
    def imprimir(self):
        print('\n\nDados do Jogador:\nNome: {}\nPosição: {}\nData de Nascimento: {}\nNacionalidade: {}\nAltura: {:.2f}m\nPeso: {}kg\n'.format(self.nome, self.posicao, self.data_nasc,self.nacionalidade, self.altura, self.peso))

if __name__ == '__main__':
    nome = input('Digite o nome do jogardor:')
    posicao = input('Digite a posição do jogador (defensor, meia, atacante):')
    nasc = input('Digite a data de nascimento(11/11/1111 por exemplo):')
    nacionalidade = input('Digite a nacionalidade:')
    altura = float(input('Digite a altura (1.11 por exemplo):'))
    peso = int(input('Digite o peso:'))

    jogador = Jogador(nome,posicao,nasc,nacionalidade,altura,peso)

    jogador.imprimir()
    jogador.set_idade()
    jogador.set_aposentar()

    print('A idade do jogador é {} anos\n'.format(jogador.get_idade()))
    
    if jogador.get_aposentar() > 0:
        print('Faltam {} anos para se aposentar'.format(jogador.get_aposentar()))
    elif jogador.get_aposentar() == -500:
        print('Posição não reconhecida!')
    else:
        print('Pronto pra aposentar/aposentado')
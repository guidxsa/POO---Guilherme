class Elevador:
    def __init__(self, total_andares, capacidade):
        self.total_andares = total_andares
        self.capacidade = capacidade

    def set_inicializar(self):
        self.__andar_atual = 0
        self.__pessoas_presentes = 0
    
    def get_inicializar(self):
        return self
    
    def set_entrar(self):
        if self.__pessoas_presentes < self.capacidade:
            self.__pessoas_presentes += 1
    
    def get_entrar(self):
        return self
    
    def set_sair(self):
        if self.__pessoas_presentes > 0:
            self.__pessoas_presentes -= 1
    
    def get_sair(self):
        return self
    
    def set_subir(self):
        if self.__andar_atual < self.total_andares:
            self.__andar_atual += 1
    
    def get_subir(self):
        return self
    
    def set_descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
    
    def get_descer(self):
        return self
    
    def imprimir(self):
        print('Total andares: {}\nCapacidade: {}\nAndar atual: {}\nPessoas Presentes: {}'. format(self.total_andares, self.capacidade, self.__andar_atual, self.__pessoas_presentes))
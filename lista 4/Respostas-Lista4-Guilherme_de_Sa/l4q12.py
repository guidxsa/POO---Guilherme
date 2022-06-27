class Voo:
    def __init__(self, numero_voo, cidade_ori, cidade_dest, data):
        self.dict = {}
        self.numero_voo = numero_voo
        self.cidade_ori = cidade_ori
        self.cidade_dest = cidade_dest
        self.data = data

        for i in range (1, 201):
            self.dict[i] = 'vazio'

    def proximo_livre(self):
        for i in range (1, 201):
            if self.dict[i] == 'vazio':
                return i
            elif i == 200:
                return 'Não há assentos livres!'
    
    def verifica_assento(self, num_cadeira):
        self.num_cadeira = num_cadeira
        if self.dict[self.num_cadeira] == 'vazio':
            return False
        else:
            return True
    
    def marcar_assento(self, num_cadeira):
        self.num_cadeira = num_cadeira
        if self.dict[self.num_cadeira] == 'vazio':
            self.dict[self.num_cadeira] = 'ocupado'
            return True
        else:
            return False
    
    def retornar_vagas(self):
        list_vagas = []
        for i in range (1, 201):
            if self.dict[i] == 'vazio':
                list_vagas.append(i)
        
        return list_vagas
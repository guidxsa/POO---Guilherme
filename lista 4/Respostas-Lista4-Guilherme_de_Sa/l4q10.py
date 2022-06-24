class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print('O valor do ingresso é: R${:.2f}'.format(self.valor))

class IngressoVIP(Ingresso):
    def __init__(self, valor, acrescimo):
        super().__init__(valor)
        self.acrescimo = acrescimo

    def set_calcula_VIP(self):
        self.valor_VIP = self.acrescimo + self.valor

    def get_calcula_VIP(self):
        return self.valor_VIP 

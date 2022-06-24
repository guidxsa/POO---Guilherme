class Fatura:
    def __init__(self, num, desc, quant, preco):
        self.num_item = num
        self.desc_item = desc
        self.quant_item = quant if quant >= 0 else 0
        self.preco_item = preco if preco >= 0 else 0.0

    def set_num_item(self):
        self.__num_item = self.num_item
    
    def get_num_item(self):
        return self.__num_item
    
    def set_desc_item(self):
        self.__desc_item = self.desc_item
    
    def get_desc_item(self):
        return self.__desc_item
    
    def set_quant_item(self):
        self.__quant_item = self.quant_item
    
    def get_quant_item(self):
        return self.__quant_item
    
    def set_preco_item(self):
        self.__preco_item = self.preco_item
    
    def get_preco_item(self):
        return self.__preco_item
    
    def set_calcular_valor_fatura(self):
        self.__valor = self.__quant_item * self.__preco_item
    
    def get_calcular_valor_fatura(self):
        return self.__valor

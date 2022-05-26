from classes import Pessoa

if __name__ == '__main__':
   
   p1 = Pessoa('Guilherme','1111111111',19)

   p2 = Pessoa('Joao','wwwwww',25)

   p3 = Pessoa('Claudio','2222',31)
        
   
   print('Pessoa 1: {}'.format(p1.__dict__))

   print('\nPessoa 2: {}'.format(p2.__dict__))

   print('\nPessoa 3: {}'.format(p3.__dict__))














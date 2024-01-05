class Pessoa3:
        def __init__(self) :
            self.Sobrenome : str 
            self.Peso : float 
            self.Nome : str 
            self.idade : int

        def __str__(self) :
              return f'{self.Nome} {self.Sobrenome} {self.idade} {self.Peso}'    

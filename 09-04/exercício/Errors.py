from Categoria import Categoria

class AgeError(Exception):
    '''Exception raised for errors in the participant age.'''
    def __init__(self, idade: int):
        self.idade = idade
        if idade < 10:
            self.message = "\033[1;32;31mParticipante muito novo\033[0;0m"
        if idade > 60:
            self.message = "\033[1;32;31mParticipante muito velho\033[0;0m"
        super().__init__(self.message)
        
class CategoryError(Exception):
    '''Exception raised for errors in the participant age for its category.'''
    def __init__(self, idade: int, categoria: Categoria):

        match categoria:
            case Categoria.INFANTIL:
                if idade > 14:
                    self.message = "\033[1;32;31mParticipante muito velho para a categoria infantil\033[0;0m"
            case Categoria.JUVENIL:
                if idade > 17:
                    self.message = "\033[1;32;31mParticipante muito velho para a categoria juvenil\033[0;0m"
                else:
                    self.message = "\033[1;32;31mParticipante muito novo para a categoria juvenil\033[0;0m"
            case Categoria.ADULTO:
                if idade < 18:
                    self.message = "\033[1;32;31mParticipante muito novo para a categoria adulto\033[0;0m"

        super().__init__(self.message)
    
        
class ElapsedTimeError(Exception):
    '''Exception raised for errors in the participant conclusion time.'''
    def __init__(self, tempo: int):        
        if tempo < 30:
            self.message = "\033[1;32;31mTempo Estimado menor que 30 minutos\033[0;0m"
        elif tempo > 180:
            self.message = "\033[1;32;31mTempo Estimado maior que 180 minutos\033[0;0m"
        super().__init__(self.message)
        
class NotSignedError(Exception):
    '''Exception raised for errors in the participant registration signature.'''
    def __init__(self):
        self.message = "\033[1;32;31mCadastro não assinado\033[0;0m"
        super().__init__(self.message)
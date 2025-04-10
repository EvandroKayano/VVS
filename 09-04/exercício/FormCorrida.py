from Participante import Participante
from Categoria import Categoria
from Errors import AgeError, CategoryError, ElapsedTimeError, NotSignedError

#Participante1 = Participante("João", 25, Categoria.ADULTO, 100, False)

def verificarCadastro(pessoa: Participante):
    # idade
    if pessoa.idade < 10 or pessoa.idade > 60:
        raise AgeError(pessoa.idade)
    
    # categoria
    switch_categoria = {
        Categoria.INFANTIL: pessoa.idade >= 10 and pessoa.idade <= 14,
        Categoria.JUVENIL: pessoa.idade >= 15 and pessoa.idade <= 17,
        Categoria.ADULTO: pessoa.idade >= 18 and pessoa.idade <= 60
    }
    
    if pessoa.categoria in switch_categoria and switch_categoria[pessoa.categoria] == False:
        raise CategoryError(pessoa.idade, pessoa.categoria)
        
    # tempo estimado
    if pessoa.tempoEstimado < 30 or pessoa.tempoEstimado > 180:
        raise ElapsedTimeError(pessoa.tempoEstimado)
    
    # assinado
    if not pessoa.assinado:
        raise NotSignedError()
    
    return True
        
#verificarCadastro(Participante1)
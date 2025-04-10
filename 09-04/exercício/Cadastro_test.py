import pytest
from Categoria import Categoria
from Errors import AgeError, CategoryError, ElapsedTimeError, NotSignedError
from Participante import Participante
from FormCorrida import verificarCadastro

def test_success_registration():
    participante1 = Participante("João", 25, Categoria.ADULTO, 100, True)
    participante2 = Participante("Maria", 15, Categoria.JUVENIL, 50, True)
    participante3 = Participante("Ana", 12, Categoria.INFANTIL, 40, True)
    
    assert verificarCadastro(participante1) == True
    assert verificarCadastro(participante2) == True
    assert verificarCadastro(participante3) == True
    
def test_age_error():
    muitoNovo = Participante("João", 9, Categoria.INFANTIL, 100, True)
    muitoVelho = Participante("João", 65, Categoria.ADULTO, 100, True)
    with pytest.raises(AgeError):
        verificarCadastro(muitoNovo)
    with pytest.raises(AgeError):
        verificarCadastro(muitoVelho)
        
def test_wrong_age_for_category():
    muitoVelhoInfantil = Participante("João", 15, Categoria.INFANTIL, 100, True)
    muitoNovoJuvenil = Participante("Lucas", 13, Categoria.JUVENIL, 100, True)
    muitoVelhoJuvenil = Participante("Carla", 18, Categoria.JUVENIL, 100, True)
    muitoNovoAdulto = Participante("Julia", 16, Categoria.ADULTO, 100, True)
    with pytest.raises(CategoryError):
        verificarCadastro(muitoVelhoInfantil)
    with pytest.raises(CategoryError):
        verificarCadastro(muitoNovoJuvenil)
    with pytest.raises(CategoryError):
        verificarCadastro(muitoVelhoJuvenil)
    with pytest.raises(CategoryError):
        verificarCadastro(muitoNovoAdulto)    
    
def test_elapsed_time_error():
    tempoMenor = Participante("João", 25, Categoria.ADULTO, 20, True)
    tempoMaior = Participante("João", 25, Categoria.ADULTO, 200, True)
    with pytest.raises(ElapsedTimeError):
        verificarCadastro(tempoMenor)
    with pytest.raises(ElapsedTimeError):
        verificarCadastro(tempoMaior)
        
def test_not_signed_error():
    semAssinatura = Participante("João", 25, Categoria.ADULTO, 100, False)
    with pytest.raises(NotSignedError):
        verificarCadastro(semAssinatura)
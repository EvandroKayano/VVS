from input import validar_email
import pytest
from testExceptions.UsernameEmailError import UsernameEmailError
from testExceptions.DomainEmailError import DomainEmailError
from testExceptions.TLDEmailError import TLDEmailError
from testExceptions.TLDSizeError import TLDSizeError

def test_success_verify_email():
    email = "comeco.meio@fim.br"
    assert validar_email(email) == True, f"Email {email} deveria ser válido"
    
def test_exception_email_username():
    
    with pytest.raises(UsernameEmailError):
        validar_email("@fim.br") == False
    
def test_exception_email_domain():
    with pytest.raises(DomainEmailError):
        validar_email("comeco.meio@.br") == False
   
def test_exception_email_tld():
    with pytest.raises(TLDEmailError):
        validar_email("comeco.meio@fim.") == False

def test_exception_email_tld_size():
    with pytest.raises(TLDSizeError):
        validar_email("comeco.meio@fim.tdlsize") == False
    

import pytest
from email_validator import validate

def test_should_not_accept_null_strings():
    email = None
    assert validate(email) is False

def test_should_not_accept_empty_strings():
    email = ''
    assert validate(email) is False

def test_should_accept_valid_email():
    email = 'any@mail.com'
    assert validate(email)
    
    
    
    
    
    

def test_should_not_accept_strings_larger_than_320_chars():
    # 64+1+63+1+63+1+63+1+63 = 320
    # 64+1+255 = 320
    # limite máximo
    email1 = 'l' * 64 + '@' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63
    email2 = 'l' * 65 + '@' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63
    email3 = 'l' * 64 + '@' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 64
   
    assert validate(email1) is True
    assert validate(email2) is False
    assert validate(email3) is False
    
    
    # que porra que não ta funcionando?
    
    
    
    

def test_should_not_accept_domain_part_larger_than_255_chars():
    email = 'local@' + 'd' * 128 + '.' + 'd' * 127
    assert validate(email) is False

'''
- email_validator.py: (l: 21, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>

if len(local_part) > 64 or len(domain) > 255: -> len(domain) >= 255
    return False
        
limite máximo
'''
def test_should_accept_domain_part_with_255_chars():
    # Tem uma verificação de que cada parte do domain n pode ser maior que 63
    email = 'local@' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63 + '.' + 'd' * 63
    assert validate(email) is True

def test_should_not_accept_local_part_larger_than_64_chars():
    email = 'l' * 65 + '@mail.com'
    assert validate(email) is False
    
'''
- email_validator.py: (l: 21, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>

if len(local_part) > 64 or len(domain) > 255: -> len(local_part) >= 64
    return False
        
limite minimo
'''
def test_should_accept_local_part_with_64_chars():
    email = 'l' * 64 + '@mail.com'
    assert validate(email) is True

def test_should_not_accept_empty_local_part():
    email = '@mail.com'
    assert validate(email) is False

def test_should_not_accept_empty_domain():
    email = 'any@'
    assert validate(email) is False
    
def test_should_not_accept_empty_local_part_and_domain():
    email = '@'
    assert validate(email) is False

def test_should_not_accept_domain_with_part_larger_than_63_chars():
    email = 'any@' + 'd' * 64 + '.com'
    assert validate(email) is False

def test_should_not_accept_local_part_with_space():
    email = 'any email@mail.com'
    assert validate(email) is False

def test_should_not_accept_local_part_with_two_dots():
    email = 'any..email@mail.com'
    assert validate(email) is False

def test_should_not_accept_local_part_with_ending_dot():
    email = 'any.@mail.com'
    assert validate(email) is False

def test_should_not_accept_email_without_an_at_sign():
    email = 'anymail.com'
    assert validate(email) is False
    
def test_should_not_accept_email_with_more_than_one_at():
    email = 'any@@mail.com'
    assert validate(email) is False

def test_should_not_accept_non_strings():
    email = 2
    assert validate(email) is False

def test_should_not_accept_local_part_with_invalid_char():
    email = 'anyç@mail.com'
    assert validate(email) is False

def test_should_not_accept_domain_part_with_invalid_char():
    email = 'any@mailç.com'
    assert validate(email) is False  
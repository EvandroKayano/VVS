class DomainEmailError(Exception):
    '''Exception raised for errors in the first part of input email address.'''
    def __init__(self, message="\033[1;32;31mEmail inválido: não possui domain\033[0;0m"):
        super().__init__(message)
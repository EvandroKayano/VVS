class TLDSizeError(Exception):
    '''Exception raised when the tdl size is bigger than 3.'''
    def __init__(self, message="\033[1;32;31mtop-level domain inválido\033[0;0m"):
        super().__init__(message)
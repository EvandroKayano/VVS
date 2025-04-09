import re
from testExceptions.UsernameEmailError import UsernameEmailError
from testExceptions.DomainEmailError import DomainEmailError
from testExceptions.TLDEmailError import TLDEmailError
from testExceptions.TLDSizeError import TLDSizeError

# email = input("Digite o email: ")
email = "ek.kayano@unifesp.br"

def validar_email(endereco):
    valido = re.match('[a-zA-Z\\-\\.]+@([a-zA-Z\\-]+\\.)+[a-zA-Z\\-]{2,4}$',endereco) # [qualquerCoisa]@[qualquerCoisa].[qualquerCoisa]
    if not valido:
        username = endereco.split('@')      # comeco | meio.fim
        if username[0] == "":        # não tem username
            raise UsernameEmailError()
        elif username[1] == "":
            raise DomainEmailError()
        domains = username[1].split('.')    # meio | fim
        if len(domains) < 2 or domains[1] == "": # não tem top-level domain "fim"
            raise TLDEmailError()
        elif domains[0] == "":
            raise DomainEmailError()
        # uol.com.br
        if len(domains) >= 2: # tem .com.br por exemplo
            # domains[1] pode ser .com ou .net ou .org
            # domains[2] deve ser o domain do país, como .br ou .ar ou .uk
            if len(domains[1]) != 3 or len(domains[2]) > 2:
                raise TLDSizeError()
            
        print("Tem erro não tratado")
        
    return True
        
if(validar_email(email)):
    print("Email válido")
        
    
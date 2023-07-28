from validate_docbr import CPF
import re

def cpf_validator(cpf_n):
    cpf = CPF()
    return cpf.validate(cpf_n)
    
def name_validator(name):
    return name.isalpha()

def rg_validator(rg):
    return len(rg) == 9

def phonenumber_validator(phonenumber):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phonenumber)
    return response
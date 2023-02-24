from validate_docbr import CPF
from validate_docbr import CNPJ

cpf = CPF()
cnpj = CNPJ()

cpfs = cpf.generate_list(10, True, False)
cnpjs = cnpj.generate_list(10, True, False)

print(cpfs)
print("-------")
print(cnpjs)
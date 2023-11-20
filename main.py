from cpf_validator import CPFValidator

def main():
    cpf_fornecido = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")    
    validator = CPFValidator(cpf_fornecido)
    
    if validator.validate():
        print("CPF é válido")
    else:
        print("CPF inválido")

if __name__ == "__main__":
    main()
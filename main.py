import re

# Solicita ao usuário a entrada do CPF no formato XXX.XXX.XXX-XX
cpf_fornecido = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")

# Remove caracteres não numéricos do CPF fornecido
cpf_tratado = re.sub(r"[^0-9]", "", cpf_fornecido)

# Verifica se todos os dígitos do CPF são iguais, o que indicaria um CPF inválido
if cpf_tratado == cpf_tratado[0] * len(cpf_tratado):
    print("CPF inválido")
else:
    # Separa os primeiros nove dígitos do CPF, excluindo os dígitos verificadores
    cpf_sem_digitos_verificadores = cpf_tratado[:9]
    nr_digitos = 10

    # Inicia a variável que armazenará o total da soma para cálculo do primeiro dígito verificador
    digito_calculado = 0

    # Calcula a soma para o primeiro dígito verificador
    for cada_digito in cpf_sem_digitos_verificadores:
        digito_calculado += int(cada_digito) * nr_digitos
        nr_digitos -= 1

    # Calcula o primeiro dígito verificador
    digito_verificador_1 = (digito_calculado * 10) % 11

    # Ajusta o primeiro dígito verificador se for maior que 9
    if digito_verificador_1 <= 9:
        digito_verificador_1 = digito_verificador_1
    else:
        digito_verificador_1 = 0

    # Concatena o primeiro dígito verificador calculado ao CPF sem dígitos verificadores
    cpf_com_um_digito_verificador = cpf_sem_digitos_verificadores + str(digito_verificador_1)
    nr_digitos = 11

    # Reinicia a variável para o cálculo do segundo dígito verificador
    digito_calculado = 0

    # Calcula a soma para o segundo dígito verificador
    for cada_digito in cpf_com_um_digito_verificador:
        digito_calculado += int(cada_digito) * nr_digitos
        nr_digitos -= 1

    # Calcula o segundo dígito verificador
    digito_verificador_2 = (digito_calculado * 10) % 11

    # Ajusta o segundo dígito verificador se for maior que 9
    if digito_verificador_2 <= 9:
        digito_verificador_2 = digito_verificador_2
    else:
        digito_verificador_2 = 0

    # Verifica se os dígitos verificadores calculados são iguais aos fornecidos pelo usuário
    if (int(cpf_tratado[9]) == digito_verificador_1) and (int(cpf_tratado[10]) == digito_verificador_2):
        print("CPF é válido")
    else:
        print("CPF inválido")
import re

class CPFValidator:
    """ Classe para validação de CPF.
    
    Attributes:
        cpf (str): CPF a ser validado no formato XXX.XXX.XXX-XX.
    """
    
    def __init__(self, cpf):
        """ Inicializa o validador de CPF com o CPF fornecido.
        
        Args:
            cpf (str): CPF a ser validado no formato XXX.XXX.XXX-XX.
        """

        self.cpf = self._clean_cpf(cpf)

    def _clean_cpf(self, cpf):
        """ Remove caracteres não numéricos do CPF. 
        
        Args:
            cpf (str): CPF a ser limpo no formato XXX.XXX.XXX-XX.
        Returns:
            str: CPF limpo no formato XXXXXXXXX (apenas números).
        """
        return re.sub(r"[^0-9]", "", cpf)

    def _is_invalid_sequence(self):
        """ Verifica se a sequência do CPF é inválida (todos os números iguais). 
        
        Returns:
            bool: True se a sequência é inválida, False caso contrário.
        """
        return self.cpf == self.cpf[0] * len(self.cpf)

    def _calculate_digit(self, cpf_base):
        """ Calcula um dígito verificador do CPF. 
        
        Args:
            cpf_base (str): CPF base para o cálculo do próximo dígito verificador.
        Returns:
            int: Dígito verificador calculado.
        """

        total = 0 # Armazena a soma para cálculo do dígito verificador
        factor = len(cpf_base) + 1 # Fator de multiplicação (número de dígitos + 1)

        # Para cada dígito no CPF, calcula o produto da multiplicação e atualiza o fator
        for digit in cpf_base:
            total += int(digit) * factor
            factor -= 1

        # Computa o novo dígito verificador
        new_digit = (total * 10) % 11

        # Trunca o dígito para 0 caso o resultado seja maior que 9
        if new_digit > 9:
            new_digit = 0

        return new_digit

    def validate(self):
        """ Valida o CPF fornecido. 
        
        Returns:
            bool: True se o CPF é válido, False caso contrário.
        """
        # Checa se o CPF fornecido possui 11 dígitos e se não é uma sequência inválida (todos os dígitos iguais)
        if len(self.cpf) != 11 or self._is_invalid_sequence():
            return False

        # Separa a base do CPF e calcula os dois dígitos verificadores
        cpf_base = self.cpf[:9]
        first_digit = self._calculate_digit(cpf_base)
        second_digit = self._calculate_digit(cpf_base + str(first_digit))

        # Retorna True se o CPF fornecido é válido (os dígitos verificadores calculados correspondem com of informados), False caso contrário
        return self.cpf == cpf_base + str(first_digit) + str(second_digit)
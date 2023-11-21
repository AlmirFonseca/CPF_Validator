import unittest
from cpf_validator import CPFValidator

class TestCPFValidator(unittest.TestCase):

    ## Testes para Particionamento de Equivalência (EP)

    # Testa um CPF válido
    def test_valid_cpf(self):
        self.assertTrue(CPFValidator("529.982.247-25").validate())

    # Testa um CPF com formato inválido (sem formatação).
    def test_invalid_cpf_format(self):
        with self.assertRaises(ValueError):
            CPFValidator("52998224725").validate()

    # Testa Testa um CPF com comprimento inválido (muito curto).
    def test_invalid_cpf_shorter_length(self):
        with self.assertRaises(ValueError):
            CPFValidator("123").validate()

    # Testa um CPF com comprimento inválido (muito longo).
    def test_invalid_cpf_longer_length(self):
        with self.assertRaises(ValueError):
            CPFValidator("123.456.789-0123").validate()

    # Testa um CPF com caracteres não numéricos.
    def test_invalid_cpf_non_numeric(self):
        with self.assertRaises(ValueError):
            CPFValidator("abc.def.ghi-jk").validate()

    # Testa um CPF com todos os dígitos iguais.
    def test_invalid_cpf_all_same_digits(self):
        self.assertFalse(CPFValidator("111.111.111-11").validate())


    ## Testes para Análise de Valor Limite (BVA)

    # Testa um CPF no limite superior do intervalo válido.
    # O maior CPF corresponde ao CPF de base 999.999.999, com os dígitos verificadores 99, mas este CPF é inválido devido à regra de sequência idêntica.
    # Logo, o maior CPF válido é o CPF de base 999.999.998, com os dígitos verificadores 08.
    def test_valid_cpf_boundary(self):
        self.assertTrue(CPFValidator("999.999.998-08").validate()) 

    # Testa um CPF logo após o limite superior do intervalo válido.
    # Nesse caso, escolhemos o CPF imediatamente maior que o limite superior do intervalo válido.
    def test_invalid_cpf_boundary(self):
        self.assertFalse(CPFValidator("999.999.998-09").validate())


    ## Teste de Tabela de Decisão

    def test_cpf_with_different_digit_patterns(self):
        # Testa diferentes padrões de dígitos, que são casos válidos e inválidos.
        valid_cpf = "248.438.034-80"
        invalid_cpf_due_to_second_digit = "248.438.034-81"
        invalid_cpf_due_to_first_digit = "248.438.034-70"

        self.assertTrue(CPFValidator(valid_cpf).validate())
        self.assertFalse(CPFValidator(invalid_cpf_due_to_first_digit).validate())
        self.assertFalse(CPFValidator(invalid_cpf_due_to_second_digit).validate())


    ## Suposição de Erro

    def test_cpf_common_mistake_patterns(self):
        # Testa padrões comuns de erros que podem ser inseridos por usuários
        # Por exemplo, um usuário pode inverter dígitos, usar sequências populares como '123.456.789-09', etc.
        valid_cpf = "248.438.034-80"
        invalid_cpf_due_to_digit_inversion = "248.438.034-08"
        valid_cpf_due_to_common_sequence = "123.456.789-09"
        invalid_cpf_due_to_common_sequence = "234.567.890-12"
        invalid_cpf_due_to_inversion_of_hifen_and_dot = "248-438-034.80"

        self.assertTrue(CPFValidator(valid_cpf).validate())
        self.assertFalse(CPFValidator(invalid_cpf_due_to_digit_inversion).validate())
        self.assertTrue(CPFValidator(valid_cpf_due_to_common_sequence).validate())
        self.assertFalse(CPFValidator(invalid_cpf_due_to_common_sequence).validate())
        with self.assertRaises(ValueError):
            CPFValidator(invalid_cpf_due_to_inversion_of_hifen_and_dot).validate()

if __name__ == "__main__":
    unittest.main()

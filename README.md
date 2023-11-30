# CPF_Validator
Repositório para entrega da atividade de Eng. de Software sobre refatoração de princícpios SOLID

---

No código fornecido, os princípios SOLID de Single Responsibility (SRP) e Open/Closed (OCP) são aplicados da seguinte maneira:

### Single Responsibility Principle (SRP)

Classe ```CPFValidator```: Esta classe é responsável por uma única tarefa: validar CPFs. Ela encapsula todos os passos necessários para esta validação, como limpeza do CPF, verificação de sequências inválidas e cálculo dos dígitos verificadores. A classe não está sobrecarregada com responsabilidades adicionais, como interação com o usuário ou persistência de dados, o que está de acordo com o SRP.

Função ```main``` no arquivo principal: Esta função lida exclusivamente com a interação com o usuário, solicitando a entrada do CPF e exibindo o resultado da validação. Esta separação de responsabilidades mantém a lógica de validação do CPF isolada da lógica de interface com o usuário.

### Open/Closed Principle (OCP)

Extensibilidade da Classe ```CPFValidator```: A estrutura da classe ```CPFValidator``` permite que ela seja estendida sem a necessidade de modificar seu código-fonte. Por exemplo, se você precisar adicionar novas regras de validação de CPF, pode criar uma subclasse que estenda ```CPFValidator``` e sobrescreva o método validate ou adicione novos métodos conforme necessário.

Uso de Métodos Privados para Encapsulamento: Métodos como ```_clean_cpf```, ```_is_invalid_sequence``` e ```_calculate_digit``` são privados, o que significa que detalhes internos de implementação estão encapsulados dentro da classe. Isso permite que esses métodos sejam modificados no futuro (para aprimorar a lógica de validação, por exemplo) sem impactar as classes ou funções que utilizam ```CPFValidator```, desde que a interface pública (método ```validate```) permaneça a mesma.
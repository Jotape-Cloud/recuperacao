# Atividade — Conserte o Sistema de Locadora de Veículos

## Contexto

O sistema abaixo simula uma locadora de veículos, dividido em módulos — igual ao que vocês
fizeram no seminário: `excecoes.py`, `veiculo.py`, `cliente.py`, `locadora.py` e `main.py`.

O código **roda sem erro de sintaxe** e, em boa parte dos testes rápidos, parece funcionar.
Mas existem **8 bugs escondidos** espalhados pelos arquivos. Nenhum deles é um erro de
digitação óbvio — são erros de **lógica**, **comparação** ou **exceções mal definidas**, do
tipo que só aparece quando você testa uma situação específica com atenção.

## Sua tarefa

1. Rode o programa e teste **todos os fluxos possíveis**, não só o caminho mais óbvio:
   - Alugar um veículo
   - Alugar o **mesmo veículo duas vezes seguidas**
   - Alugar por diferentes quantidades de dias e **conferir se o valor cobrado está correto**
   - Cadastrar e movimentar **mais de um cliente**, e verificar se o histórico de cada um
     está isolado do outro
   - Buscar um veículo que **não é o primeiro da lista**
   - Consultar o histórico de um cliente
   - Provocar um erro esperado (CPF inexistente, dias inválidos) e observar o que acontece
2. Para cada comportamento estranho que encontrar, volte no código e leia com atenção —
   nem todo bug quebra o programa com um traceback. Alguns só produzem um **resultado
   errado**, silenciosamente.
3. Corrija o problema na origem, sem alterar o comportamento correto do resto do sistema.

## Como pensar sobre isso

Cada bug pertence a uma dessas categorias — pode ser útil ir checando uma por vez:

- **Comparação errada** — o código compara duas coisas, mas usa o operador ou o critério
  errado, então a comparação "quase sempre" dá o resultado certo, exceto em algum caso.
- **Fluxo de controle mal posicionado** — uma linha está no lugar errado dentro de um laço
  ou condicional, fazendo com que ela só funcione na primeira tentativa.
- **Valor mutável compartilhado** — um comportamento clássico (e traiçoeiro) do Python, que
  faz dados de um objeto vazarem para outro sem que ninguém tenha mandado isso acontecer.
- **Conta errada** — uma operação matemática está sutilmente errada, cobrando ou calculando
  um valor diferente do esperado.
- **Atributo que não existe** — uma exceção customizada referencia um dado que ela mesma
  nunca guardou.
- **Ordem de argumentos trocada** — uma função é chamada passando os parâmetros na ordem
  errada, e como os tipos "combinam" superficialmente, ninguém percebe de cara.
- **Entrada não convertida** — um dado veio do `input()` como texto e foi usado como se já
  fosse número.

## Sobre tratamento de exceções

Reparem que **nenhuma exceção está sendo tratada** neste projeto — `raise` é usado, mas não
existe nenhum `try/except`. Isso é proposital: depois de corrigir os 8 bugs, adicionem
tratamento de exceção nos pontos que fazem sentido (usando o que vocês aprenderam na aula),
para que o programa não trave e sim informe o usuário com uma mensagem clara.

## Requisitos para considerar a atividade completa

- [ ] Não é possível alugar um veículo que já está alugado
- [ ] O valor cobrado no aluguel corresponde exatamente a `valor_diaria × dias`
- [ ] Cada cliente tem seu próprio histórico de locações, sem misturar com o de outro cliente
- [ ] É possível encontrar e alugar qualquer veículo cadastrado, não só o primeiro da lista
- [ ] Buscar um cliente pelo CPF funciona corretamente
- [ ] Alugar um veículo converte a quantidade de dias para número antes de usar
- [ ] Os parâmetros são passados na ordem correta em todas as chamadas de função
- [ ] Exceções relevantes (CPF não encontrado, veículo indisponível, dias inválidos, veículo
      inexistente) têm mensagens corretas quando lançadas
- [ ] O programa trata as exceções nos pontos de entrada (menu), evitando que o usuário veja
      um traceback cru

Boa caçada!

# Desenvolvimento_calculadora_python
### Desafio de projeto sobre função em Python 

Faça uma função calculadora de dois números com três parâmetros: <br>
os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. <br>
<br>
<strong>Considere a seguinte definição:</strong>
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não existe, o resultado deverá ser 0.


## Solução para o Projeto

Função calculadora de dois números com três parâmetros:  <br>
 <br>
Calcula o resultado de uma operação aritmética entre dois números. <br>
 <br>
  Args: <br>
    numero_1: O primeiro número. <br>
    numero_2: O segundo número. <br>
    operacao: O número da operação a ser executada. <br>
 <br>
  Returns: <br>
    O resultado da operação. <br>
     <br>
 <br>
     Esta solução usa o módulo math para realizar as operações aritméticas. O código funciona da seguinte forma: <br>
 <br>
A função calculadora() recebe três parâmetros: numero_1, numero_2 e operacao. <br>
A função calculadora() valida a operação, verificando se o valor de operacao está no dicionário operacoes. <br>
Se a operação for válida, a função obtém a função correspondente do módulo math e a executa com os dois números. <br>
Se a operação não for válida, a função retorna 0. <br>
O código principal, main(), recebe a entrada do usuário e chama a função calculadora(). <br>
 <br>
### Aqui estão alguns exemplos de entrada e saída do código: <br>
<br>
>>> <strong>Desenvolv_calculadora.py</strong> <br>
Digite o primeiro número: 10 <br>
Digite o segundo número: 20 <br>
Digite o número da operação: 1 <br>
O resultado da operação soma é: 30 <br>
<br>
>>> <strong>Desenvolv_calculadora.py</strong> <br>
Digite o primeiro número: 10 <br>
Digite o segundo número: 20 <br>
Digite o número da operação: 2 <br>
O resultado da operação subtração é: -10 <br>
<br>
>>> <strong>Desenvolv_calculadora.py</strong> <br>
Digite o primeiro número: 10 <br>
Digite o segundo número: 20 <br>
Digite o número da operação: 3 <br>
O resultado da operação multiplicação é: 200 <br>
<br>
>>> <strong>Desenvolv_calculadora.py</strong> <br>
Digite o primeiro número: 10 <br>
Digite o segundo número: 0 <br>
Digite o número da operação: 4 <br>
O resultado da operação divisão é: 0 <br>
<br>

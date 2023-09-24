def calculadora(numero_1, numero_2, operacao):
  """
  Calcula o resultado de uma operação aritmética entre dois números.

  Args:
    numero_1: O primeiro número.
    numero_2: O segundo número.
    operacao: O número da operação a ser executada.

  Returns:
    O resultado da operação.
  """

  # Valida a operação

  if operacao not in [1, 2, 3, 4]:
    return 0

  # Realiza a operação

  if operacao == 1:
    return numero_1 + numero_2
  elif operacao == 2:
    return numero_1 - numero_2
  elif operacao == 3:
    return numero_1 * numero_2
  else:
    if numero_2 == 0:
      return "Não é possível dividir por zero."
    else:
      return numero_1 / numero_2


def main():
  # Entrada dos dados

  numero_1 = float(input("Digite o primeiro número: "))
  numero_2 = float(input("Digite o segundo número: "))
  operacao = int(input("Digite o número da operação: "))

  # Chamada da função

  resultado = calculadora(numero_1, numero_2, operacao)

  # Saída do resultado

  if isinstance(resultado, str):
    print(resultado)
  else:
    print(f"O resultado é: {resultado}")


if __name__ == "__main__":
  main()
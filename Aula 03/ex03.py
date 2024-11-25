# Exercício 3 - Notas de 50, 10 e 1

valor = int(input("Digite o valor da conta: "))

n50 = valor//50
resto = valor%50
n10 = resto//10
n1 = resto%10

print(f"Notas de 50: {n50}")
print(f"Notas de 10: {n10}")
print(f"Notas de 1: {n1}")

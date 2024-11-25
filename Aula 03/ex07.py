# Exercício 7 - Área de um triângulo pela fórmula de Hierão

a = float(input("Digite o valor do lado a (cm): "))
b = float(input("Digite o valor do lado b (cm): "))
c = float(input("Digite o valor do lado c (cm): "))

s = (a+b+c)/2
k = (s*(s-a)*(s-b)*(s-c))**0.5

print(f"Área do triângulo: {k} cm²")

a

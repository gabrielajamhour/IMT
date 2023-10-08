# Exercício 5 - Trocar os valores de x e y

x = float(input("Digite um valor para x: "))
y = float(input("Digite um valor para y: "))

aux = x
x = y
y = aux
# A função "aux" (variável auxiliar) serve para guardar um primeiro valor

print(f"x = {x} e y = {y}")


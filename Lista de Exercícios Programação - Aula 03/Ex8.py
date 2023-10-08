# Exercício 8 - Conversão de graus para radianos

g = float(input("Digite um ângulo em graus: "))

import math   # Para usar π, é necessário usar esse comando
r = g*(math.pi)/180
# π = math.pi

print(f"Conversão para radianos: {r} rad")

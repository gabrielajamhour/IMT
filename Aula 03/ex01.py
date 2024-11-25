# Exercício 1 - Req em série e em paralelo

R1 = float(input("Digite R1 (Ω, ohms): "))
R2 = float(input("Digite R2 (Ω, ohms): "))

serie = R1 + R2   # item a
paralelo = R1 * R2 / (R1 + R2)   # item b

print(f"Equivalente em série: {serie} Ω")
print(f"Equivalente em paralelo: {paralelo} Ω")

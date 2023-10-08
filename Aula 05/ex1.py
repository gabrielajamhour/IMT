def soma_fracoes():
    numerador_1 = int(input("Digite o numerador 1:"))
    denominador_1 = int(input("Digite o denominador 1:"))
    numerador_2 = int(input("Digite o numerador 2:"))
    denominador_2 = int(input("Digite o denominador 2:"))

    numerador_final = numerador_1*denominador_2+numerador_2*denominador_1
    denominador_final = denominador_1*denominador_2

    print(f"{numerador_final}")
    print(f"---")
    print(f"{denominador_final}")

soma_fracoes()

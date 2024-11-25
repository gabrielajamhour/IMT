import math

def Alcance():
    Vo = float(input("Digite a velocidade inicial (m/s):"))
    alfa = float(input("Digite o ângulo entre o cano do canhão e o solo (°):"))

    teta = math.pi/180*alfa
    S = Vo**2/9.81*math.sin(2*teta)

    print(f"Alcance do projétil: {S}m")

Alcance()
a

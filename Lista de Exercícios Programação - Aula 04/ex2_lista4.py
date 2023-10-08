import math

def cosseno_hiperbólico():
    x = float(input("Digite um valor para x:"))
    cosh = (math.exp(x)+math.exp(-x))/2
    print(f"{cosh}")

cosseno_hiperbólico()
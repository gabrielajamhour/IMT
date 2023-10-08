def horario():
    dias = int(input("Digite o número de dias:"))
    horas = int(input("Digite o número de horas:"))
    minutos = int(input("Digite o número de minutos:"))
    segundos = int(input("Digite o número de segundos:"))

    if dias>0:
        horas+=dias*24
    if minutos%60!=0:
        horas+=minutos//60
        minutos=minutos%60
    if segundos%60!=0:
        minutos+=segundos//60
        segundos=segundos%60

    print(f"{horas}h{minutos}m{segundos}s")

horario()
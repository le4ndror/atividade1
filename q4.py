relogio = int(input("digite o horário atual : "))
tocar = int(input("digite em quantas horas o alarme irá tocar: "))
alarme = 0

while alarme<tocar:
    relogio = relogio + 1
    alarme = alarme + 1
    if relogio == 24:
        relogio =0
    
print(f"são {relogio} horas")
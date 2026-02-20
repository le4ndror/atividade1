relogio = 9
alarme = 0

while alarme<37:
    relogio = relogio + 1
    alarme = alarme + 1
    if relogio == 24:
        relogio =0
    
print(f"são {relogio} horas")
#declamos la funcion
def signoZodiaco(d,m):
    if (m ==3 and d >= 21) or (m==4 and d <= 19):
        signo = "Aries"
    elif (m ==4 and d >= 20) or (m==5 and d <= 20):
        signo = "Tauro"
    elif (m ==5 and d >= 21) or (m==6 and d <= 21):
        signo = "Geminis"
    elif (m ==6 and d >= 22) or (m==7 and d <= 22):
        signo = "Cancer"
    elif (m ==7 and d >= 23) or (m==8 and d <= 22):
        signo = "Leo"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
        signo = "Virgo"
    elif (m ==9 and d >= 23) or (m==10 and d <= 22):
        signo = "Libra"
    elif (m ==10 and d >= 23) or (m==11 and d <= 21):
        signo = "Escorpio"
    elif (m ==12 and d >= 22) or (m==1 and d <= 19):
        signo = "Capricornio"
    elif (m ==1 and d >= 20) or (m==2 and d <= 18):
        signo = "Acuario"
    elif (m ==2 and d >= 19) or (m==3 and d <= 20):
        signo = "Picis"
    return signo


# algoritmo principal
print("a continuacion daremos su signo zodiacal dependiendo su dia y mes de nacimiento")
day = int(input("Ingrese dia de su cumpleaños: "))
month = int(input("Ingrese mes de su cumpleaños: "))

resultado = signoZodiaco(day, month)
print(f"Su signo zodiacal es: {resultado}")
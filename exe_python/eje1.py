def becomeSeconds(hour, minutes, seconds):
    return (hour * 3600) + (minutes * 60) + seconds

print("Inserta a continuación las horas, minutos y segundos que deseas convertir a segundos.")
h = int(input("Ingrese horas: "))
m = int(input("Ingrese minutos: "))
s = int(input("Ingrese segundos: "))

print("El total de segundos es:", becomeSeconds(h, m, s))

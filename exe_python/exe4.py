def juego(p1,p2):
    if p1 == "P" or "p": # jugador 1 elije piedra
        if p2 == "P" or "p":
            resultado = "empate" # jugador 2 elije piedra
        elif p2== "L" or "l":
            resultado = "Gana Jugador 2"
        elif p2 == "T" or "t": #jugador 2 elije tijera
            resultado = "Gana jugador 1"
    elif p1 == "L" or "l": #jugador 1 elije papel
        if p2 == "L" or "l": # jugador 2 elige papel
            resultado = "Empate"
        elif p2 == "T" or "t": #jugardor 2 elije tijera
            resultado = "Gana jugador 2"
        elif p2 == "p" or "P": #jugador 2 elije piedra
            resultado = "gana jugador 1"
    elif p1 == "t" or "T": #jugador 1 elije tijera
        if p2 == "t" or "T": #jugador 2 elije tijera
            resultado = "Empate"
        elif p2 == "p" or "P": #jugador 2 elige piedra
            resultado = "Gana jugador 2"
        elif p2 == "l" or "L": #jugador 2 elije papel
            resultado ="Gana jugador 1"
    return resultado

#algoritmo principal
# hacemos un bucle while que seria lo equitativo al mientras
print( "Jugaremos el tipico juego de pierdta papel o tijera")

while (p1 == "p" or "P") or (p1 == "L" or "l") or (p1 == "t" or "T"):
    p1 = input("turno jugador 1. ingresa P (piedra), L (papel) o T(tijera)")
while (p1 == "p" or "P") or (p1 == "L" or "l") or (p1 == "t" or "T"):
    p2 = input("turno jugador 2. ingresa P (piedra), L (papel) o T(tijera)")
ganador = juego(p1,p2)
print(f"el resultado es:  {ganador}")
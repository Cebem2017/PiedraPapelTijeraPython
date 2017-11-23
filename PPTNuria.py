import random

lista = ["piedra","papel","tijera"]
jugador1="piedra"
jugador2 ="piedra"

while jugador1==jugador2:
    jugador1=random.choice(lista)
    jugador2 = input("Que escoges, piedra, papel o tijera?:")
    print("Empate! Juguemos otra vez")

if jugador1 == "piedra" and jugador2=="papel" :
    print("Tu ganas! papel gana a piedra")
elif jugador1 == "piedra" and jugador2 =="tijera":
    print("Tu pierdes! piedra gana a tijera")
elif jugador1 == "papel" and jugador2 =="piedra":
    print("Tu pierdes! papel gana a piedra")
elif jugador1 == "papel" and jugador2 =="tijera":
    print("Tu ganas! tijera gana a papel")
elif jugador1 == "tijera" and jugador2 =="piedra":
    print("Tu ganas! piedra gana a tijera")
elif jugador1 == "tijera" and jugador2 =="papel":
    print("Tu pierdes! tijera gana a papel")
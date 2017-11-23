import random

piedra = "piedra" #1
papel = "papel" #2
tijeras = "tijeras" #3



def numero_aleatorio():
    return random.randrange(1,4)



def jugada(mano_jugador, numero_aleatorio):
    if(mano_jugador == tijeras and numero_aleatorio == 2):
        return "tu ganas, tu rival echa papel"
    elif mano_jugador == piedra and numero_aleatorio == 3:
        return "tu ganas, tu rival echa tijeras"
    elif mano_jugador == papel and numero_aleatorio == 1:
        return "tu ganas, tu rival echa piedra"
    elif mano_jugador == tijeras and numero_aleatorio == 1:
        return "tu pierdes, tu rival echa piedra"
    elif mano_jugador == piedra and numero_aleatorio == 2:
        return "tu pierdes, tu rival echa papel"
    elif mano_jugador == papel and numero_aleatorio == 3:
        return "tu pierdes, tu rival echa tijeras"


    elif mano_jugador == papel and numero_aleatorio == 2:
        return "empate"
    elif mano_jugador == piedra and numero_aleatorio == 1:
        return "empate"
    elif mano_jugador == tijeras and numero_aleatorio == 3:
        return "emapte"
mano_jugador = ""

while mano_jugador != "salir":
    
    print("Que echas")
    mano_jugador = input()
    print(jugada(mano_jugador, numero_aleatorio()))
import random

opcionPc = random.choice([1, 2, 3])

pc = ""


print("1 - Piedra")
print("2 - Papel")
print("3 - Tijera")


opcionUsuario = int(input("¿Piedra, papel o tijera?: "))

if opcionUsuario == 1:
    usuario = "piedra"
elif opcionUsuario == 2:
    usuario = "papel"
elif opcionUsuario == 3:
    usuario = "tijera"
print("Usuario: ", usuario)

if opcionPc == 1:
    pc = "piedra"
elif opcionPc == 2:
    pc = "papel"
elif opcionPc == 3:
    pc = "tijera"
print("PC: ", pc)

if pc == "piedra" and usuario == "papel" :
    print("Ganaste")

elif pc == "papel" and usuario == "tijera":
    print("Ganaste")
elif pc == "tijera" and usuario == "piedra":
    print("Ganaste")

if pc == "papel" and usuario == "piedra":
    print("Perdiste")
elif pc == "tijera" and usuario == "papel":
    print("Perdiste")
elif pc == "piedra" and usuario == "tijera":
    print("Perdiste")
elif pc == usuario:
    print("EMPATE")

print("FIN DEL JUEGO")
from random import randint
opciones = { 1: 'Piedra', 2: 'Papel', 3: 'Tijeras' }
rival = opciones[randint(1, 3)]
miOpcion= input()
if miOpcion=='Piedra':
    if rival=='Piedra':
        print("EMPATE, Rival: {}".format(rival))
    if rival=='Papel':
        print("GANA EL RIVAL, Rival: {}".format(rival))
    if rival=='Tijeras':
        print("GANAS TÚ, Rival: {}".format(rival))
elif miOpcion=='Papel':
    if rival=='Piedra':
        print("GANAS TÚ, Rival: {}".format(rival))
    if rival=='Papel':
        print("EMPATE, Rival: {}".format(rival))
    if rival=='Tijeras':
        print("GANA EL RIVAL, Rival: {}".format(rival))
elif miOpcion=='Tijeras':
    if rival=='Piedra':
        print("GANA EL RIVAL, Rival: {}".format(rival))
    if rival=='Papel':
        print("GANAS TÚ, Rival: {}".format(rival))
    if rival=='Tijeras':
        print("EMPATE, Rival: {}".format(rival))
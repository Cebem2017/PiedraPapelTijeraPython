import random 

 

juego = ['piedra','papel','tijera','lagarto','spock'] 

maquina = random.choice(juego) 

 

print ("Bienvenidos a piedra, papel, tijera, lagarto Spock.")

usuario = input("¿Que eliges? Piedra, papel, tijera, lagarto o Spock: ") 

 

print ("has elegido %s" %usuario)

print ("la maquina ha elegido %s" %maquina)

 

if usuario == maquina: 

    print ('Empate')

 

if usuario == 'piedra': 

    if maquina == 'papel': 

        print ('Perdiste') 

    elif maquina == 'tijera': 

        print ('Ganaste') 

    elif maquina == 'lagarto': 

        print ('Ganaste')

    elif maquina == 'spock': 

        print ('Perdiste')

         

elif usuario == 'papel': 

    if maquina == 'piedra': 

        print ('Ganaste')

    elif maquina == 'tijera': 

        print ('Perdiste ') 

    elif maquina == 'lagarto': 

        print ('Perdiste ') 

    elif maquina == 'spock': 

        print ('Ganaste') 

         

elif usuario == 'tijera': 

    if maquina == 'piedra': 

        print ('Perdiste ')

    elif maquina == 'papel': 

        print ('Ganaste ')

    elif maquina == 'lagarto': 

        print ('Ganaste ')

    elif maquina == 'spock': 

        print ('Perdiste ')

 

elif usuario == 'lagarto': 

    if maquina == 'piedra': 

        print ('Perdiste ')

    elif maquina == 'papel': 

        print ('Ganaste ')

    elif maquina == 'tijera': 

        print ('Perdiste ')

    elif maquina == 'spock': 

        print ('Ganaste ')

 

elif usuario == 'spock': 

    if maquina == 'piedra': 

        print ('Ganaste ')

    elif maquina == 'papel': 

        print ('Perdiste')

    elif maquina == 'tijera': 

        print ('Ganaste ')

    elif maquina == 'lagarto': 

        print ('Perdiste ')

else: 

    print ('Opcion erronea') 
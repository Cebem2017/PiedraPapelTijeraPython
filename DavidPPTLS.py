import os

Opciones=["Piedra","Papel","Tijeras","Lagarto","Spock"]

cont1=0
cont2=0
jug1=""
jug2=""
opcion1=0
opcion2=0
print("Jugador 1, introduzca su nombre")
jug1=input()
print("Jugador 2 introduzca su nombre")
jug2=input()

#Por mejorar el detector de errores con los numeros!!

while (cont1<3 and cont2<3):

    print(jug1+" escriba la opcion, 1 para Piedra, 2 para Papel, 3 para Tijeras, 4 para Lagarto, 5 para Spock")
    opcion1=int(input())
    os.system("cls")

  
    print(jug2+" escriba la opcion, 1 para Piedra, 2 para Papel, 3 para Tijeras, 4 para Lagarto, 5 para Spock")
    opcion2=int(input())
    os.system("cls")
    

    if(opcion1==opcion2):
        print("EMPATE, el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)      
    elif(opcion1==1):
        if(opcion2==3 or opcion2==4):
            cont1=cont1+1
            print("GANA " +jug1+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
        else:
            cont2=cont2+1
            print("GANA " +jug2+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
    elif(opcion1==2):
        if(opcion2==1 or opcion2==5):
            cont1=cont1+1
            print("GANA " +jug1+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
        else:
            cont2=cont2+1
            print("GANA " +jug2+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)
    elif(opcion1==3):
        if(opcion2==2 or opcion2==4):
            cont1=cont1+1
            print("GANA " +jug1+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
        else:
            cont2=cont2+1
            print("GANA " +jug2+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
    elif(opcion1==4):
        if(opcion2==2 or opcion2==5):
            cont1=cont1+1
            print("GANA " +jug1+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
        else:
            cont2=cont2+1
            print("GANA " +jug2+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
    elif(opcion1==5):
        if(opcion2==1 or opcion2==3):
            cont1=cont1+1
            print("GANA " +jug1+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
        else:
            cont2=cont2+1
            print("GANA " +jug2+", el marcador va "+str(cont1)+" puntos para "+jug1+" y "+str(cont2)+" puntos para "+jug2)  
if(cont1==3):
    print("HA GANADO "+jug1)
else:
    print("HA GANADO "+jug2)
import random
import os
import time

neumaticos = None
neumaticospc = None 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
x = None




print("    _______________                   ")
print("   / ____<  / ____/___ _____ ___  ___ ")
print("  / /_   / / / __/ __ `/ __ `__ \/ _ \ ")
print(" / __/  / / /_/ / /_/ / / / / / /  __/ ")
print("/_/    /_/\____/\__,_/_/ /_/ /_/\___/ \n")


input("Enter para continuar... ")
clearConsole()

print("Creado por Luis Eduardo")

time.sleep(1)

clearConsole()

print("Bienvenido, a continuación seleccione un Piloto: ")
print("\n")


while x != 1 and x != 2 and x !=3:
    print("1 --> Sergio Pérez")
    print("2 --> Max Verstappen")
    print("3 --> Lando Norris")
    x = int(input("Inserte una opción valida --> "))
    clearConsole()

if x == 1:
    name = ("Sergio Pérez")
    print("Tu piloto es: " + name ) 

elif x == 2:
    name = ("Max Verstappen")
    print("Tu piloto es: " + name ) 

else:
    name = ("Lando Norris")
    print("Tu piloto es: " + name ) 

print("\n")

print(name + " vamos a tener un duelo con otro piloto.")
print("Recuerda siempre cuidar tus neumáticos\n")

print("Generando Rival..." )

time.sleep(5)

clearConsole()

namepc = random.randint(1, 5)

if namepc == 1:
    namepc = "Latifi"

elif namepc == 2:
    namepc = "Carlos Sainz"  

elif namepc == 3:
    namepc = "Daniel Ricciardo" 

elif namepc == 4:
    namepc == "Charles Leclerc"

elif namepc ==5:
    namepc = "Lewis Hamilton"


print( name + " tu rival es {}".format(namepc))
print("\n")

time.sleep(2)
clearConsole()

print("Tus neumáticos equipados duaran 7 vueltas, con un uso promedio")
print("\n")

print("A continuación tendremos la clasificación")

time.sleep(5)


print("Los neumáticos no se desgatan durante las clasificación")

time.sleep(2)

clearConsole()

clas = random.randint(1, 2 )

if clas == 1:
    print(name + " tienes la pole felicidades")
    poss = 1
    posspc = 2

else:
    print(name + " quedaste en segundo!")
    poss = 1
    posspc = 2


print("A continuacion te dare algunos datos para la carrera")

time.sleep(4)

clearConsole()

neumaticos = "[///////]"
neumaticospc = "[///////]"
vueltas = "[#######]"


print("Neumáticos " + neumaticos)
print("Neumáticos de rival " + neumaticospc)
print("Numero de Vueltas " + vueltas + " en total hay 7 vueltas")
print("Rival {}".format(namepc))

time.sleep(4.5)
clearConsole()

print("Antes de empezar ocupas un director de carrera.")
director = input("¿Cómo quieres que se llame?")


print("Tu director de carrera es: " + director)
print("YA NO HAY MÁS, VERSION 1.O (BETA) BY LUIS EDUARDO OCEGUEDA CORTÉS")

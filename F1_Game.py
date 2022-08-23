import random
import os
import time

neumaticos = None
neumaticospc = None 
gas = None
gaspc= None
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
print("Recuerda siempre cuidar tus neumaticos y el nivel de combustible\n")

print("Generando Rival..." )

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

print("La duración de la carrera es de 5 vueltas.\n")

vueltas = ("[/////]")

print("Combustible: [//////////]")

gas = "[//////////]"
gaspc = "[//////////]"

time.sleep(4)
clearConsole()

print(name + " Preparate, faltan 3 segundos para empezar la clasificación")

print("[# # #]\n")
time.sleep(1)

print("[# # -]\n")
time.sleep(1)

print("[# - -]\n")
time.sleep(1)

print("[- - -]\n")
time.sleep(1)



print(name + " se apagan las luces, empezamos!")
clearConsole()

lugar = random.randint(1, 2)

if lugar ==1:
    print(name + " quedaste en primer lugar {} en segundo lugar ".format(namepc))
else:
    print(name + " quedaste en segundo lugar {} en primer lugar ".format(namepc))

clearConsole()

print("Empazamos la carrera.")
print("Recuerda que la duración de la carreara es de 5 Vueltas")
clearConsole()

gas = "[///////---]"
gaspc = "[///////---]"


print("Rival: {}".format(namepc))
print("Vueltas: " + vueltas)
print("Conbustible" + gas)
print("Conbustible Rival " + gaspc)




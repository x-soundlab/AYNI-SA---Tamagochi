#print Mensaje de bienvenida 
    #nombre = input("Holiwis! ₍^. .^₎⟆ ₊˚⊹♡ ¿Cómo se llama tu Miawmiaw?: ")
    #print(f"El nombre de tu Miawmiaw es {nombre}")


#importar funcion random
import random
import time

#Variables para randomizer
a=(3,4,5)
b=(3,4,5)
c=(3,4,5)

energia = random.choice(seq=a)
felicidad = random.choice(seq=b)
hambre = random.choice(seq=c)
acciones = 0



#funciones del tamagochi

#funcion mostrar estado

def mostrar_estado():
    print("ᓚ₍ ^. .^₎ " "❤️", energia, "⚡", felicidad, "🍖", hambre,)
#print (mostrar_estado())

#funcion comer
def comer():
    global hambre, felicidad, energia
    hambre -= 3
    felicidad += 1
    energia -= 1
    print("está comiendo 🍗")
#comer()
#print (mostrar_estado())

#funcion dormir
def dormir():
    global energia, felicidad
    energia += 4 
    felicidad += 1 
    print("está durmiendo (˶˃ᆺ˂˶) 😴 zzz.... ")
    time.sleep(3)
    print("Ya despertó (=^･^=) ")
#dormir()
#print (mostrar_estado())

#funcion jugar
def jugar():
    global felicidad, energia, hambre
    felicidad += 2
    energia -= 2
    hambre += 1
    print("esta jugando")
#jugar()
#print (mostrar_estado())

#funcion aburrirse
def aburrirse():
    global felicidad
    felicidad -= 2 
    print("Algo va mal, tu Miawmiaw está aburrido /ᐠ - ˕ -マ ")
#aburrirse()
#print (mostrar_estado())

#input que llame una funcion de python

acciones_disponibles = {
    "comer": comer,
    "dormir": dormir,
    "jugar": jugar,
}


#Gameplay loop 
nombre = input("Holiwis! ₍^. .^₎⟆ ₊˚⊹♡ ¿Cómo se llama tu Miawmiaw?: ")
print(f"El nombre de tu Miawmiaw es {nombre}")
print(mostrar_estado())

while True:
    acciones += 1 
    if random.random() < 0.2:
        aburrirse()
        print (mostrar_estado())
    if acciones == 10: 
        print(f"{nombre}Se murió de viejo (｡•́︿•̀｡) RIP ")
        break
    if hambre >= 10:
        print("Me he morido, deja la vida bohemia y comprame whiskas ₍⑅ᐢ..ᐢ₎ RIP ")
        break
    if energia <= 0:
        print("Jefe estoy cansado, adiosito... (｡•́︿•̀｡) RIP ")
        break
    accion = input("Que debería hacer? >⩊< (comer, dormir, jugar): " )
    if accion in acciones_disponibles:
        acciones_disponibles[accion]()
        print (mostrar_estado())
    else:
        print("Error: No se hacer esto ᓚᘏᗢ ")

#Algoritmo parfa mirar quien es mayor de edad de cada unas de las personas
#Utilizaremos los operadores de comparacion

#Variable ya definida
#edadPersonaAdulta = 18

#Entrada de datos
edadPersona= int(input("por favor digite la edad de la persona N° 1 : "))
edadPersona= int(input("por favor digite la edad de la persona N° 2: "))

#Proceso de operacion
if edadPersona >= 18:
    print(f"la persona N° 1   con la edad de {edadPersona} cumple con la mayoria de edad")
else:
    print(f"la persona N° 2 con la edad de {edadPersona} no cumple con la mayoria de edad")

#Terminacion de ejecucion de algritmo de calcular la edad mayor de edad.
print("Hemos terminado la ejecucion del programa")
"""
Instruciones del ejercicio: EL mayor de dosa numeros.

solicitar al usuario  dos valores, y determinar cual numero es mayor.
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos numeros  (la salida debe ser identica a ola que le sigue):
proporciona el numero1:
proporciona el numero2:
el numero mayor es :<numeroMayor>
"""


#Solicitar al usuario dos valores de tipo int

numero1 = int(input("Proporciona el numero1: "))
numero2 = int(input("Proporciona el numero2: "))

#Determinar cual de los dos numeros es el mayor
if numero1 > numero2:
    print(f"El numero1 es mayor y su numero es: {numero1}")
else:
    print(f"El numero2 es mayor y su numero es: {numero2}")
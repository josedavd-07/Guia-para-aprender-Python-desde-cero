#Miembro donde pedimos los datos del usuario que se usan durante el programa
#edad = int(input("Introduce tu edad: "))
"""
Forma de hacerlo con variables pero las mas recomendable es hacerlo directamente en el if
veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)
"""
#Primer resuldato forma de hacerlo directamente en el if pero con loa variables anteriores pero tampoco recomendable
'''
print("\nPrimer resultado:\n")
#condicionales if else de los valore de las variables veintes y treintas
if veintes or treintas:
    print('Dentro del ranfo (20\'s) o (30\'s)') #caracter de escape para el apostrofe no cierre la cadena.
else:
    print('Fuera del rango (20\'s) o (30\'s)')

print("--------------------------")

#Segundo resultado
print("\nSegundo resultado:\n")
#Con condicionales if y elif y else los cuales son  anidados
if edad >= 20 and edad < 30:
    print("Estás entre los  veinte años")
elif edad >= 30 and edad < 40:
    print("Estás entre los treinta años")
else:
    print("No estás en la veintena ni en la treintena")

print("\n--------------------------")
'''

#Hagamos el ejercicicio de la manera correcta.
edad = int(input("Introduce tu edad: "))

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print("Dentro del rango (20's) o (30's)")
else:
    print("Fuera del rango (20's) o (30's)")

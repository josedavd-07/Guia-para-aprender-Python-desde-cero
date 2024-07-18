#Miraremos un  ejemplo con el operador logico or
#Asistir al juego del hijo
'''
vacaciones = True
diaDescanso = True

#condicional or

if vacaciones or diaDescanso:
    print("Puede asistir al juego del hijo")
else:
    print("No puede asistir al juego del hijo")
'''
#Salida: Puede asistir al juego del hijo


#Ahora pidamos los datos al usuario

vacaciones = input("¿Estas de vacaciones? (si/no): ")
diaDescanso = input("¿Es tu dia de descanso? (si/no): ")

if vacaciones == "si" or diaDescanso == "si":
    print("Puede asistir al juego del hijo")
else:
    print("Tiene deberes por hacer")

#La salida depende de la respuesta del usuario.

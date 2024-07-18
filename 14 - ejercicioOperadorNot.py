# Ejercicio de operador not puede asisteir a ver el hijo a jugar
#Ahora pidamos los datos al usuario

vacaciones = input("¿Estas de vacaciones? (si/no): ")
diaDescanso = input("¿Es tu dia de descanso? (si/no): ")

if not vacaciones == "si" or diaDescanso == "si":

    print("Tiene deberes por hacer")
else:
    print("Puede asistir al juego del hijo")

#La salida depende de la respuesta del usuario.

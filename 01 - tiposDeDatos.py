
#resumen de tipo de datos en python.

#Tipo de dato entero.
entero = 10
print(entero)

#Tipo de dato flotante.
flotante = 10.5
print(flotante)

#Tipo de dato string.
cadena = "Hola mundo"
print(cadena)

#Tipo de dato booleano.
booleano = True
print(booleano)

#Manejo de cadenas en python. utilizamos concatenacion de cadenas de la manera
# mas sencilla posible. que es la de conm el signo +
#Estra es una forma pero no tan optima
miGrupoFavorito = "Celeste" + " el mejor grupo de musica"
print("mi grupo favorito es: " + miGrupoFavorito)

#Otra forma  mas optimna de realizar la concatenacion simple con el signo +

myName = "Jose"
carreraUniversitaria = "Ingenieria de sistemas"
print("mi nombre es: " + myName + " y estudio la carrera de " + carreraUniversitaria + "en la Unad")

#Ahora miraremos la forma de concatenar mediante el uso del signo de la coma

miNombre = "Jose"
miEdad = 20
miPais = "Colombia"

print("Hola que tal me llamo", miNombre, "tengo", miEdad, "años y soy de", miPais)

#Aca miramos como se concatenan los numeros en vez de susmarse
# ya que son de tipo string y no de tipo numerico en este caso entero

num1 = "10"
num2 = "20"  # Este string se podria convertir y daria como entero
#esto nos dara como resultado 1020
print("Concatenacion:", num1 + num2)

#Ahora miraremos como sumar los numeros en el caso que fueran enteros.
numero1 = 20
numero2 = 13
resultadoSuma = numero1 + numero2
print("el resultado de la suma entre el numero ", numero1, " y el numero ", numero2, " es: ", resultadoSuma)

#miremos como hacer la conversion de tipos de datos de cadenas
# de string a entero en este caso in t o integer

edad1 = "20"
edad2 = "13"
print("la suma de las edades es: ", int(edad1) + int(edad2))
print("la concatenacion de las edades es: ", edad1 + edad2)

#Tipos de datos(booleanos) en python.
#En python los booleanos son True y False
miVariableBooleanaT = True
miVariableBooleanaF = False
print(miVariableBooleanaT)
print(miVariableBooleanaF)

#Ejercicio de un resultado booleano
#En este caso la variable pruebaDeResultadoBooleano es True
pruebaDeResultadoBooleano = 10 > 5
pruebaDeResultadoBooleano2 = 10 < 5

print("El resultado de esta comparacion de valores numericos es: ", pruebaDeResultadoBooleano)
print("El resultado de esta comparacion de valores numericos es: ", pruebaDeResultadoBooleano2)
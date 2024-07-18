#Algoritmo numero par o impar
#usando los operadores aritmeticos y los de comparacion.

#Entrada de datos
numero = int(input("por favor digite un numero: "))

#Proceso de operacion del numero con el operador modulo
#si el residuo de la division es 0 entonces es par
#si el residuo de la division es diferente de 0 entonces es impar

#numero = numero % 2 esto se puede usar sin hacer la de abajo

#Salida de datos
if numero % 2 == 0:
    print(f"El numero de la variable {numero} es par")
else:
    print(f"El numero  de la variable {numero} es impar")

#Fin del programa
print("hemos terminado la ejecucion del programa")


#programa de ingresos mensuales

#Entrada de datos
ingresos = float(input("por favor digite sus ingresos mensuales: "))
gastos = float(input("por favor digite sus gastos mensuales: "))

#Proceso de operacion
if gastos > ingresos:
    print("Usted tiene deficit")
else:
    print("Usted es una persona responsable que administra su deinero sabiamente")
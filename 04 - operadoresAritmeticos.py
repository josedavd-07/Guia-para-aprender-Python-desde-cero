#Parte 1 de operadores en python.
#operadores aritmeticos en python
# adiccion o suma : +
#  substarcion o  resta: -
# multiplicacion : *
# division : /
# integer division : //
#exponente : **
#modulo/remainder : %
#Operadores de asignacion en python
# = : asignacion

#operadores aritmetcos de suma
operandoA = 3
operandoB = 2

suma = operandoA + operandoB
#Esto es una forma normalde imprimir datos y es una  concatenacion de cadenas
#print('Resultado de la suma: ', suma)

#Utilizemos la interpolacion de cadenas por medio de la funcion format() o f-string
#Esta es la forma mas optima de concatenar cadenas en python
print(f'Resultado de la suma: {suma}')

#Operando de restas
resta = operandoA - operandoB
print(f'Resultado de la resta: {resta}')

#Operando de multiplicacion
multiplicacion = operandoA * operandoB
print(f'Resultado de la multiplicacion: {multiplicacion}')

#Operando de division
division = operandoA / operandoB
print(f'Resultado de la division: {division}')

#Operando de division entera
divisionEntera = operandoA // operandoB
print(f'Resultado de la division entera: {divisionEntera}')

#Operando de exponente
exponente = operandoA ** operandoB
print(f'Resultado de la exponente: {exponente}')

#Operando de modulo
modulo = operandoA % operandoB
print(f'Resultado de la modulo: {modulo}')



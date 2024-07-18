#Ejercicio de and sobre el rango de los numeros
valor = int(input("Escribe el valor a comparar: "))
valorMinimo = 0
valorMaximo = 5

dentroDeRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroDeRango:
    print(f"El valor {valor} esta dentro del rango de o a 5")
else:
    print(f"El valor {valor} esta fuera del rango de 0 a 5")
#Ejercicio de tienda de libros.

#Miembros Variables
nombreLibro = input("Proporciona el nombre del libro: ")
AutorLibro = input("Proporciona el nombre del autor: ")
idLibro = int(input("Proporciona el ID del libro: "))
precioLibro = float(input("Proporciona el precio del libro: "))
envio = input("Indica si el envio es gratuito (si = True/no = False): ")

#Condiccional del envio gratuito o pago
"""
if envio == "si":
    print("El envio es: gratuito")
elif envio == "no":
    print("El envio es: pago")
else:
    print("Valor incorrecto")
"""

if envio == 'si':
    envio = True
elif envio == 'no':
    envio = False
else:
    envio = "Valor incorrecto"

#De esta manera tenemos formato de escritura con el f string y triple comillas
print(f'''
    Titulo del libro: {nombreLibro},
    Autor del libro es: {AutorLibro},
    ID del libro: {idLibro},
    Precio del libro: {precioLibro}
    El envio es: {envio}
''')

#Mostramos datos del libro
"""
print("\n--------------------------")
print("\nDatos del libro:")
print(f"Titulo del libro: {nombreLibro}")
print(f"Autor del libro es: {AutorLibro}")
print(f"ID del libro: {idLibro}")
print(f"Precio del libro: {precioLibro}")
"""

'''
if envio == "True":
    print("El envio es gratuito")
else:
    print("El envio no es gratuito")
'''
'''
if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = "Valor incorrecto"
'''
print("\n--------------------------")

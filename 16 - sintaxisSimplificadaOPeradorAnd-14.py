#Hagamos el ejercicicio de la manera correcta.
'''
edad = int(input("Introduce tu edad: "))

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print("Dentro del rango (20's) o (30's)")
else:
    print("Fuera del rango (20's) o (30's)")
'''

#Hagamos el ejercicicio de la manera  mas simplificada que es tambien correcta
edad = int(input("Introduce tu edad: "))

if (20 <= edad < 30) or (30 <= edad < 40):
    print("Dentro del rango (20's) o (30's)")
else:
    print("Fuera del rango (20's) o (30's)")

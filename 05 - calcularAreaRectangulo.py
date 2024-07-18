#Instrucciones del ejercicio:
#En el siguiente ejercicio vamos  a calcular el area y el perimetro  de un rectangulo.
#Para ello crearemos las siguientes variables:
#alto  ( int )
#ancho ( int )

#El usuario debe de ingresar los valores de alto y ancho.
#despues debe de inprimir el resultado  en el siguiente formato:
#no usar acentos y respetar los espacios, mayusculas, minusculas y saltos de linea.

#proporcione el alto:
#proporcione el ancho:
#area : <area>
#perimetro: <perimetro>

#Formulas: para calcular el area y el perimetro de un rectangulo.
#area = alto * ancho
#perimetro = (alto + ancho) * 2

#Solucion del ejercicio.
#Solicitamos los datos de entrada al usuario.
alto = int(input("proporcione el alto del rectangulo: "))
ancho = int(input("proporcione el ancho del rectangulo: "))

#Realizamos los calculos de area y perimetro.
area = alto * ancho
perimetro = (alto + ancho) * 2

#Imprimimos los resultados.
print(" el area calculada del triangulo es: ", area)
print(" el perimetro calculado del triangulo es: ", perimetro)






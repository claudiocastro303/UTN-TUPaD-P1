#Ejercicio1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
#print("Hola Mundo!")

#Ejercicio2: 
"""Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""
#Solucón:
"""nombre=input("ingrese su nombre: ")
print(f"Hola {nombre}!")"""

# Ejercicio3: 
"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla."""
#Solucón:
"""nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")"""


#Ejercicio4: 
"""Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro."""
#Solucón:
"""import math
radio = float(input("ingrese el radio: "))
pi = math.pi 
area = pi * radio**2
print(f"El área del cilculo es {area}")  """

#Ejercicio5:
"""Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale """
#Solucón:
"""segundos = int(input("ingrese una cantidad de segundos: "))
horas= segundos/(60 * 60)
print(f"Los {segundos}seg. equivalen a {horas}hs")"""

#Ejercicio6:
"""Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""
#Solucón:
"""numero= int(input("ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}") """

#Ejercicio7:
"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """
#Solucón:
"""num1=int(input("ingrese un número entero distindo de cero: "))
num2=int(input("ingrese otro número entero distinto del cero: "))
print(f"la suma de los números ingresados es: {num1 + num2}")
print(f"la resta de los números ingresados es: {num1 - num2}")
print(f"la división de los números ingresados es: {num1 / num2}")
print(f"la multiplicacón de los números ingresados es: {num1 * num2}")"""

#Ejercicio8:
"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
IMC = peso en kg / (altura en 𝑚)^2   """
#Solucón:
"""altura=float(input("ingrese su altura en metros: "))
peso=float(input("ingrese su peso en kilogramos: "))
print(f"Su Indice de Masa Corporal es: {peso/(altura)**2}")  """

#Ejercicio9:
""" Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
Temperatura en Fahrenheit = (9/5) * Temperatura en Celsius + 32  """
#Solucón:
"""temp=float(input("ingrese la temperatura en °C:  "))
TempFahr=(9/5)* temp + 32
print(f"Los {temp} ° Centigrados equivalen a {TempFahr} ° Fahrenheit") """

#Ejercicio10:
"""Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números  """
#Solucón:
num1=float(input("ingrese el 1° número: "))
num2=float(input("ingrese el 2° número: "))
num3=float(input("ingrese el 3° número: "))
print(f"El promedio de los números ingresados es: {(num1+num2+num3)/3}")

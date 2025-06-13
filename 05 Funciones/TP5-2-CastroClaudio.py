import math
#Ejercicio1
"""
Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
"""
# Definición de Funciones
def imprimir_hola_mundo(mensaje):
  print(mensaje)

# Programa Principal
imprimir_hola_mundo("Hola Mundo!")
"""
#Ejercicio2
"""
Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
"""
"""
# Definición de Funciones
def saludar_usuario(nombre):
  print(f"Hola {nombre}!")
# Programa Principal
saludar_usuario("Marcos")
"""
#Ejercicio3
"""
Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
"""
# Definición de Funciones
def informacion_personal(nombre,apellido,edad,residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# Programa Principal
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=input("ingrese su edad: ")
residencia=input("ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)
"""
#Ejercicio4
"""
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el 
radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
"""
# Definición de Funciones
def calcular_area_circulo(radio):
  return math.pi * (radio**2)

def calcular_perimetro_circulo(radio):
  return 2 * math.pi * radio
# Programa Principal
radio = float(input("ingrese el radio: "))
print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")
"""
#Ejercicio5
"""
Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
"""
# Definición de Funciones
def segundos_a_horas(segundos):
  return segundos/3600
# Programa Principal
seg=float(input("ingrese los segundos: "))
print(f"Los {seg} segundos equivalen a {segundos_a_horas(seg)} horas")
"""
#Ejercicio6
"""
Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
"""
# Definición de Funciones
def tabla_multiplicar(mensaje):
  num=int(input(mensaje))
  for i in range(1,11):
    print(f"{i} x {num} = {i*num}")
    
# Programa Principal
tabla_multiplicar("ingrese un numero: ")
"""
#Ejercicio7
"""
Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""
"""
# Definición de Funciones
def operaciones_basicas(a,b):
  while b == 0:
    b=float(input("ingrese un numero distinto de cero: "))
  return (a+b, a-b, a*b, a/b)
# Programa Principal
num1=float(input("ingrese un número: "))
num2=float(input("ingrese otro número: "))
print(operaciones_basicas(num1,num2))
"""
#Ejercicio8
"""
Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
"""
# Definición de Funciones
def calcular_imc(peso,altura):
  return peso/(altura**2)
# Programa Principal
peso=float(input("ingrese su peso en kg: "))
altura=float(input("ingrese su altura en m: "))
print(f"Su IMC es: {calcular_imc(peso,altura)}")
"""
#Ejercicio9
"""
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
"""
"""
# Definición de Funciones
def celsius_a_fahrenheit(celsius):
  return celsius * 1.8 + 32
# Programa Principal
temp=float(input("ingrese la temperatura en grados Celsius: "))
print(f"La temparatura en Fahrenheit es: {celsius_a_fahrenheit(temp)} °F")
"""
#Ejercicio10
"""
Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función.
"""
"""
# Definición de Funciones
def calcular_promedio(a, b, c):
  return (a+b+c)/3
# Programa Principal
num1=float(input("ingrese un númro: "))
num2=float(input("ingrese un númro: "))
num3=float(input("ingrese un númro: "))
print(f"El promedio de los números ingresados es: {calcular_promedio(num1,num2,num3)}")
"""
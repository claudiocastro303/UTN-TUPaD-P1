#Ejercicio 1
"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """
#Solución
"""
for i in range(100+1):
  print(i)   """

#Ejercicio 2
"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene.  """
#Solución
"""
num = input("ingrese un numero entero: ")
print("la cantidad de dígitos del número ingresado es: ",len(num)) """

#Ejercicio 3
"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores  """
#Solución
"""
num1 = int(input("ingrese un valor entero: "))
num2 = int(input("ingrese otro valor entero: "))
sum = 0
if num1<num2:
  for i in range(num1+1,num2):
    sum += i
    print(sum)
else:
  for i in range(num2+1,num1):
    sum += i
    print(sum)
print("La suma numros comprendidos entre los valores ingresads(menos los valores ingresados) es: ",sum)  """

#Ejercicio 4
"""Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.   """
#Solución
"""
num = int(input("ingrese un número entero(0 para terminar): "))
sum = 0
while num != 0:
  sum += num
  #print("sum",sum,"num",num)
  num = int(input("ingrese otro número entero(0 para terminar): "))
print("La suma de números ingresados es: ",sum)   """

#Ejercicio 5
"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.   """
#Solución
"""
import random 
num = random.randint(0,3)
contador = 1
print(num)
num_ingresado = int(input("ingrese un numero entero entre 0 y 9: "))
if num_ingresado == num:
  print(f"Ha ganado!, en el {contador}° intento")
while num_ingresado != num and num_ingresado != 15:
  num_ingresado = int(input("ingrese otrto numero entre 0 y 9(15 para salir): "))
  contador += 1
  if num_ingresado == num:
    print(f"Ha ganado!, en el {contador}° intento!")   """
    
#Ejercicio 6
"""Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente  """
#Solución
"""
for i in range(100,0,-2):
  print(i)  """ 
  
#Ejercicio 7
"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario   """
#Solución
"""
num = int(input("ingrese un número entero positivo: "))
sum = 0
if num>0:
  for i in range(num+1):
    sum += i
    #print(f"sum {sum},i {i}")
else:
  print("El número ingresado es incorrecto")
print(f"La suma de los números ingresados es: {sum}")   """

#Ejercicio 8
"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio).  """
#Solución
"""
cont_pares = 0
cont_positivos = 0
cantidad_numeros = 5
for i in range(cantidad_numeros):
  num = int(input("ingrese un número entero: "))
  if num%2==0:
    cont_pares += 1
  if num>0:
    cont_positivos += 1
print(f"pares = {cont_pares} , impares = {cantidad_numeros-cont_pares} \npositivos = {cont_positivos} , negativos = 
{cantidad_numeros-cont_positivos}")   """
#Ejercicio 9
"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor).   """
#Solución
"""
sum = 0
iteraciones = 4
for i in range(iteraciones):
  num = int(input("ingrese un número entero: "))
  sum += num
  #print(sum) 
print("El promedo de los números ingresados es: ",sum)   """

#Ejercicio 10
"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745   """
#Solución

num = input("ingrese un número: ")
num_invertido = num[::-1]
print("Número invertido:", num_invertido) 


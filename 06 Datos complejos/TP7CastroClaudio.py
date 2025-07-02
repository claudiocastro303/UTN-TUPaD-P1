#Ejercicio1
"""
Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""


"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300
print(precios_frutas)
"""

#Ejercicio2
"""
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""


"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300
print(precios_frutas)
#Actualización de Precios
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]= 1700
precios_frutas["Melón"]= 2800
print("Precios Actualizados: ")
print(precios_frutas)
"""
#Ejercicio3
"""
Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios.
"""


"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300
#Actualización de Precios
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]= 1700
precios_frutas["Melón"]= 2800
print("Lista de Keys: ")
print(precios_frutas.keys())
"""
#Ejercicio4
"""
Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe
Ejemplo:
contactos = {"Juan":"123456", "Ana":"987654"}
consultar: "Juan" --> muestra "123456"
"""


"""
contactos={}
def cargar_usuario(i):
  for i in range(i):
    usuario = input(f"ingrese el nombre del {i+1}° contacto: ")
    num = input(f"ingrese el número de telefono del {i+1}° contacto: ")
    contactos[usuario] = num
    #print(contactos)
  
num=int(input("ingrese la cantidad de contactos que desea agregar al diccionario: "))
cargar_usuario(num)
print(contactos)
nom=input("ingrese el nombre para mostrar su telefono: ")
if nom in contactos:
  print(f"El teléfno asociado al nombre {nom} es: {contactos[nom]}")
else:
  print("El contacto no existe")
"""
#Ejercicio5
"""
Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
Entrada --> "hola mundo hola"
Salida --> Palabras_unicas: {"hola", "mundo"}
           Recuento: {"hola": 2,"mundo": 1} 
"""


"""
frase = input("Ingrese una frase: ")   # Pedimos la frase
palabras = frase.split()   # Separamos en palabras
palabras_unicas = set(palabras)    # Obtenemos palabras únicas con un set
# Contamos las apariciones de cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostramos resultados
print(f'Palabras únicas: {palabras_unicas}')
print(f'Recuento: {recuento}')
"""
#Ejercicio6   
"""
Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:
alumnos = { 
           "Sofia": (10,9,8),
           "Lui": (6,7,7)
}
"""


"""
alumnos={}
def ingresar_datos_alumnos():
  for i in range(3):
    nombre=input(f"ingrese el nombre del {i+1}° alumno: ")
    nota1=int(input(f"ingrese la 1° nota de {nombre}: "))
    nota2=int(input(f"ingrese la 2° nota de {nombre}: "))
    nota3=int(input(f"ingrese la 3° nota de {nombre}: "))
    alumnos[nombre] = (nota1,nota2,nota3)
        
ingresar_datos_alumnos()
print(alumnos)
# Obtenemos un iterador sobre los ítems
for nombre, nota in alumnos.items():
    print(f'Alumno: {nombre}, Notas: {nota}, promedio: {sum(nota) / len(nota)}')

"""
#Ejercicio7
# Definimos los sets (pueden ser números o nombres de alumnos)
"""Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""


"""
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
ambos = parcial1 & parcial2 # Alumnos que aprobaron ambos parciales (intersección)
solo_uno = parcial1 ^ parcial2  # Alumnos que aprobaron solo uno de los dos (diferencia simétrica)
al_menos_uno = parcial1 | parcial2 # Alumnos que aprobaron al menos uno (unión)
# Mostramos los resultados
print(f'Aprobaron ambos parciales: {ambos}')
print(f'Aprobaron solo uno de los dos: {solo_uno}')
print(f'Aprobaron al menos un parcial: {al_menos_uno}')
"""
#Ejercicio8
"""
 Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""


"""
almacen={
         "arroz": 10,
         "azucar": 10,
         "manteca": 10,
}
nombre=input("ingrese el nombre del producto: ")
print(f"el stock del producto {nombre} es: {almacen[nombre]}")
nombre=input("ingrese el producto que desea actualizar: ")
num=int(input("ingrese la cantidad a agregar: "))
almacen[nombre]=num
print(f"paroducto {nombre} actualizado: {almacen[nombre]}")
nombre=input("ingrese el nombre del producto a ingresar: ")
num=int(input(f"ingrese el stock del producto {nombre}: "))
almacen[nombre]=num
print(almacen)
"""
#Ejercicio9
"""Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo:
agenda = {
          ("lunes", "10:00"): "Reunion",
          ("martes", "15:00"): "clase de ingles"
}
  Permití consultar qué actividad hay en cierto día y hora."""
"""
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio"
}


# Solicitamos al usuario el día y hora a consultar
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")
evento = agenda.get((dia, hora))   # Buscamos el evento
# Mostramos el resultado
if evento:
    print(f'Actividad en el {dia} a las {hora}: {evento}')
else:
    print(f'No hay actividad programada el {dia} a las {hora}.')
"""
#Ejercicio10
"""Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde:

• Las capitales sean las claves.
• Los países sean los valores.
Ejemplo:
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}"""


original = {}
print("Ingresá los pares País - Capital (escribí 'fin' como país para terminar):")
while True:
    pais = input("País: ")
    if pais.lower() == 'fin':
        break
    capital = input("Capital: ")
    original[pais] = capital

invertido = {capital: pais for pais, capital in original.items()}  # Creamos el diccionario invertido
# Mostramos los resultados
print(f"\nDiccionario original: {original}")
print(f"Diccionario invertido: {invertido}")
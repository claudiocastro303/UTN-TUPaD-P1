import time
# Version Recursiva
def factorial_rec(num):
  if num==0:
    return 1
  else:
    return num * factorial_rec(num-1)
# Medición del tiempo de ejecucion con alta precisión
print("\t ---*** Versión Recursiva ***---")
print("n\t factorial de n Tiempo ejecucion(ms)")
for i in range(0,51,5):
  inicio = time.perf_counter()
  resultado = factorial_rec(i)
  fin = time.perf_counter()
  tiempo_ejecucion_rec = (fin - inicio) * 1000  # Tiempo en milisegundos
  print(f"{i}\t {resultado:.4e}\t {tiempo_ejecucion_rec:.4e} ")
print("-----------------------------------------")
# Version Iterativa
def factorial_iter(n):
  fact = 1
  for i in range(1,n+1):
    fact *= i
  return fact
print("\t ---*** Metodo Iterativo ***---")
print("n\t factorial de n  Tiempo ejecucion(ms)")
for i in range(0,51,5):
  inicio = time.perf_counter()
  resultado = factorial_iter(i)
  fin = time.perf_counter()
  tiempo_ejecucion_iter = (fin - inicio) * 1000  # Tiempo en milisegundos
  print(f"{i}\t {resultado:.4e}\t {tiempo_ejecucion_iter:.4e} ")
  
  

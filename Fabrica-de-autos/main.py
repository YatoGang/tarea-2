"""
import time

piezas_probadas=0
cantidad = float ( input ( "Digite la cantidad de piezas a realizar:"))
multiplicacion_cantidad=cantidad*9
piezas_ensambladas = 0
piezas_producidas = 0 
segundos=0.05
correctas= cantidad * 0.9
print("Comenzando la produccion de piezas...")
while piezas_producidas < cantidad:
  piezas_producidas += 10
  time.sleep(segundos)
  print(f"{piezas_producidas} piezas listas")

print ("Se completo la produccion de piezas")

print("Comenzando el proceso de ensamble...")
while piezas_ensambladas < cantidad:
  piezas_ensambladas += 5
  time.sleep(segundos)
  print(f"{piezas_ensambladas} piezas ensambladas")
  

print("Se completo el ensamble de piezas")

print("Comenzando las pruebas de calidad...")
while piezas_probadas < cantidad:
  piezas_probadas += 10
  time.sleep(segundos)
  print(f"{piezas_probadas} piezas puestas a prueba")

print("Se completo las pruebas de calidad")
print(f"Solo {correctas} piezas pasaron la prueba de calidad")
"""

#compuertas logicas
while True:
  tipo_compuerta = input("Ingrese el tipo de compuerta logica (AND, OR, NAND, NOR, XOR, XNOR)")
  a=input("Ingrese el primer valor True o False: ")
  b=input("Ingrese el segundo valor True o False: ")
  
  if tipo_compuerta == "AND":
    resultado = a and b
  elif tipo_compuerta == "OR":
    resultado = a or b
  elif tipo_compuerta == "NAND":
    resultado = not (a and b)
  elif tipo_compuerta == "NOR":
    resultado = not (a or b)
  elif tipo_compuerta == "XOR":
    resultado = (a and not b) or (not a and b)
  elif tipo_compuerta == "XNOR":
    resultado = not (a and not b) or (not a and b)
  else:
   print("Tipo de compuerta no valido")
  print("El resultado de la compuerta logica es:", resultado)
  pass
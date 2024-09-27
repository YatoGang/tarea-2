"""

empleados=[]
while True:

  print("Menu de opciones:")
  print("1. Agregar un empleado:")
  print("2. Ver lista de empleados")
  print("3. Salir")
  
  dato1 = input("Ingrese un dato: ")
  if dato1 == "1":
    dato2 = str (input("Ingrese el nombre del empleado: "))
    dato3 = float ( input ("ingrese el salario del empledo:"))
    print( "Se agrego correctamente a el empleado")
    lista = [dato2,dato3]
    empleados.append(lista)
  
  elif dato1 == "2":
    for i in empleados:
      print(i[0],"con salario de", i[1], "pesos")
   
   
  
  
  elif dato1 == "3":
    print("Gracias por usar el programa")
    break


  else: 
   print("Ingrese una opcion valida por favor")

  pass

"""
"""
#Fabrica de juguetes
cantidad_a_producir = int(input("Ingrese la cantidad de juguetes a producir: "))
velocidad_de_produccion = int(input("Ingrese la velocidad de produccion por hora: "))
horario_de_trabajo= int(input("Ingrese el horario de trabajo en horas: "))

def tiempo_de_produccion(cantidad, velocidad):
  if cantidad >= 1:
      tiempo = cantidad / velocidad
      return tiempo
  else:
      print("Ingrese una cantidad válida")
      return None
  
for i in range(cantidad_a_producir):




 tiempo = tiempo_de_produccion(cantidad_a_producir, velocidad_de_produccion)      
print("El tiempo de producción es de", tiempo, "horas")"""




"""while True:
  a = float(input("Digite el primer numero:"))
  b = float(input("Digite el segundo numero:"))  
  c = float(input("Digite el tercer numero:"))
  def suma(a, b, c):
    resultado = a + b + c
    return resultado
  def resta(a, b):
    resultado = a - b
    return resultado
  if a < b:
      print("xd")
  mi_sumaxd = suma (a,b,c)
  mi_resta = resta (a,b)
  print (mi_sumaxd)
  print (mi_resta)
pass"""


"""# Fabrica de juguetes
while True:
    try:
        cantidad_a_producir = int(input("Ingrese la cantidad de juguetes a producir: "))
        velocidad_de_produccion = int(input("Ingrese la velocidad de produccion por hora: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        exit()
    
    def tiempo_de_produccion(cantidad, velocidad):
        if cantidad >= 1:
            tiempo = cantidad / velocidad
            return tiempo
        else:
            print("Ingrese una cantidad válida")
            return None
    
    tiempo = tiempo_de_produccion(cantidad_a_producir, velocidad_de_produccion)
    if tiempo is not None:
        print(f"𝗘𝗹 𝘁𝗶𝗲𝗺𝗽𝗼 𝗱𝗲 𝗽𝗿𝗼𝗱𝘂𝗰𝗰𝗶ó𝗻 𝘀𝗲𝗿á 𝗱𝗲 {tiempo} 𝗵𝗼𝗿𝗮𝘀 😎")
    pass"""

"""
# Calculadora con interfaz
import tkinter as tk
ventana=tk.Tk()
ventana.geometry("600x400")
ventana.title("CALCULADORA")
num1=tk.StringVar()
num2=tk.StringVar()
resultado=tk.StringVar()
def suma():
  num1_a=int(num1.get())
  num2_b=int(num2.get())
  resultado_suma=num1_a+num2_b
  return resultado.set(resultado_suma)
def resta():
  num1_a=int(num1.get())
  num2_b=int(num2.get())
  resultado_resta=num1_a-num2_b
  return resultado.set(resultado_resta)
def multiplicacion():
  num1_a=int(num1.get())
  num2_b=int(num2.get())
  resultado_mul=num1_a*num2_b
  return resultado.set(resultado_mul)
def division():
    num1_a=int(num1.get())
    num2_b=int(num2.get())
    resultado_division=num1_a/num2_b
    return resultado.set(resultado_division)

    
entrada1=tk.Entry(ventana,textvariable=num1)
entrada1.pack()
entrada2=tk.Entry(ventana,textvariable=num2)
entrada2.pack()

boton=tk.Button(ventana,text="+",command=suma)
boton.pack()
boton=tk.Button(ventana,text="-",command=resta)
boton.pack()
boton=tk.Button(ventana,text="*",command=multiplicacion)
boton.pack()
boton=tk.Button(ventana,text="/",command=division)
boton.pack()

resultado_label=tk.Label(ventana,textvariable=resultado)
resultado_label.pack()
ventana.mainloop()"""

#Frames de pagina
import tkinter as tk
ventana=tk.Tk()
ventana.geometry("300x300")
ventana.title("Paginas")
Calculadora=tk.Frame(ventana,width=600,height=600)
Gestor=tk.Frame(ventana,width=600,height=600)
pagina3=tk.Frame(ventana,width=600,height=600)
pagina4=tk.Frame(ventana,width=600,height=600)
pagina5=tk.Frame(ventana,width=600,height=600)
Calculadora2=tk.Frame(ventana,width=600,height=600)
label_pagina1=tk.Label(Calculadora,text="Calculadora de compuertas", font= ('Helvertica',15))
label_pagina1.pack(padx=0,pady=0)
label_pagina1=tk.Label(Calculadora,text="USAR LOS DIGITOS 1 Y 0", font= ('Helvertica',10))
label_pagina1.pack(padx=100,pady=100)
label_pagina2=tk.Label(Gestor,text="Gestor de Empleados", font= ('Helvertica',10)) 
label_pagina2.pack(padx=100,pady=5)
label_pagina2=tk.Label(Gestor,text="Nombre", font= ('Helvertica',10)) 
label_pagina2.pack(padx=100,pady=10)
label_pagina2=tk.Label(Gestor,text="Edad", font= ('Helvertica',10)) 
label_pagina2.pack(padx=110,pady=15)
label_pagina2=tk.Label(Gestor,text="Salario", font= ('Helvertica',10)) 
label_pagina2.pack(padx=120,pady=20)
label_pagina3=tk.Label(pagina3,text="Pagina 3", font= ('Helvertica' ,10))
label_pagina3.pack(padx=0,pady=0)
label_pagina4=tk.Label(pagina4,text="Pagina 4", font= ('Helvertica' ,10))
label_pagina4.pack(padx=0,pady=0)
label_pagina5=tk.Label(pagina5,text="Pagina 5", font= ('Helvertica' ,10))
label_pagina5.pack(padx=0,pady=0)
label_pagina6=tk.Label(Calculadora2,text="Calculadora2", font= ('Helvertica' ,10))
label_pagina6.pack(padx=0,pady=0)
contenedor_botones=tk.Frame(ventana)
botones=[]
botones.append(tk.Button(contenedor_botones,text="Calculadora",command=lambda:cambiar_pagina(0)))
botones.append(tk.Button(contenedor_botones,text="Gestor",command=lambda:cambiar_pagina(1)))
botones.append(tk.Button(contenedor_botones,text="pagina 3",command=lambda:cambiar_pagina(2)))
botones.append(tk.Button(contenedor_botones,text="pagina 4",command=lambda:cambiar_pagina(3)))
botones.append(tk.Button(contenedor_botones,text="pagina 5",command=lambda:cambiar_pagina(4)))
botones.append(tk.Button(contenedor_botones,text="Calculadora2",command=lambda:cambiar_pagina(5)))

contenedor_botones.pack(side=tk.BOTTOM)
for boton in botones:
  boton.pack(side=tk.LEFT)

paginas=[Calculadora,Gestor,pagina3,pagina4,pagina5,Calculadora2]

def cambiar_pagina(pagina):
    for p in paginas:
        p.pack_forget()
        paginas[pagina].pack()
        resaltar_boton(pagina)
        ventana.update()


def resaltar_boton(pagina_actual):
    for i, boton in enumerate(botones):
        if i == pagina_actual:
            boton.config(bg='gold')
        else:
            boton.config(bg='white')

#Calculadora Normal

num1=tk.StringVar()
num2=tk.StringVar()
resultado=tk.StringVar()
def sumaa():
  num1_a=int(num1.get())
  num2_b=int(num2.get())
  resultado_suma=num1_a+num2_b
  return resultado.set(resultado_suma)
def resta():
  num1_a=int(num1.get())
  num2_b=int(num2.get())
  resultado_resta=num1_a-num2_b
  return resultado.set(resultado_resta)
def multiplicacionn():
  num1_a=int(num1.get())
  num2_b=int(num2.get())
  resultado_mul=num1_a*num2_b
  return resultado.set(resultado_mul)
def division():
    num1_a=int(num1.get())
    num2_b=int(num2.get())
    resultado_division=num1_a/num2_b
    return resultado.set(resultado_division)


entrada1 = tk.Entry(Calculadora2, textvariable=num1)
entrada1.pack()
entrada2 = tk.Entry(Calculadora2, textvariable=num2)
entrada2.pack()

boton_suma = tk.Button(Calculadora2, text="   +   ", command=sumaa)
boton_suma.pack()
boton_resta = tk.Button(Calculadora2, text="   -   ", command=resta)
boton_resta.pack()
boton_mul = tk.Button(Calculadora2, text="   *   ", command=multiplicacionn)
boton_mul.pack()
boton_div = tk.Button(Calculadora2, text="   /   ", command=division)
boton_div.pack()

resultado_label = tk.Label(Calculadora2, textvariable=resultado)
resultado_label.pack() 

 
#Calculadora compuertas

num3 = tk.StringVar()
num4 = tk.StringVar()
resultado_c = tk.StringVar()

def validar_entrada(valor):
    if valor not in ['0', '1']:
       
        return False
    return True

def or_c():
    if validar_entrada(num3.get()) and validar_entrada(num4.get()):
        num3_a = int(num3.get())
        num4_b = int(num4.get())
        resultado_or = 1 if (num3_a or num4_b) else 0
        resultado_c.set(resultado_or)

def and_c():
    if validar_entrada(num3.get()) and validar_entrada(num4.get()):
        num3_a = int(num3.get())
        num4_b = int(num4.get())
        resultado_and = 1 if (num3_a and num4_b) else 0
        resultado_c.set(resultado_and)

def not_c():
    if validar_entrada(num3.get()):
        num3_a = int(num3.get())
        resultado_not = 1 if not num3_a else 0
        resultado_c.set(resultado_not)

entrada3 = tk.Entry(Calculadora, textvariable=num3)
entrada3.pack()
entrada4 = tk.Entry(Calculadora, textvariable=num4)
entrada4.pack()

boton_or = tk.Button(Calculadora, text="OR", command=or_c)
boton_or.pack()
boton_and = tk.Button(Calculadora, text="AND", command=and_c)
boton_and.pack()
boton_not = tk.Button(Calculadora, text="NOT", command=not_c)
boton_not.pack()

resultado_label_c = tk.Label(Calculadora, textvariable=resultado_c, font=('Helvetica', 20), fg= 'red')
resultado_label_c.pack()


# Lista para almacenar los empleados
empleados = []

# Variables para los datos de los empleados
dato1 = tk.StringVar()
dato2 = tk.StringVar()
dato3 = tk.StringVar()

# Función para agregar un empleado
def agregar_empleado():
    dato1a = dato1.get()
    dato2a = dato2.get()
    dato3a = dato3.get()

    # Agregar el empleado a la lista
    empleados.append([dato1a, dato2a, dato3a])

    # Limpiar los campos de entrada
    dato1.set("")
    dato2.set("")
    dato3.set("")

# Función para mostrar la lista de empleados
def mostrar_empleados():
    lista_empleados.delete(0, tk.END)
    for empleado in empleados:
        lista_empleados.insert(tk.END, f"Nombre: {empleado[0]}, Edad: {empleado[1]}, Sueldo: {empleado[2]}")



# Campos de entrada para los datos de los empleados
entrada5 = tk.Entry(Gestor, textvariable=dato1)
entrada5.pack()
entrada6 = tk.Entry(Gestor, textvariable=dato2)
entrada6.pack()
entrada7 = tk.Entry(Gestor, textvariable=dato3)
entrada7.pack()

# Función para mostrar/ocultar la lista de empleados
def mostrar_lista():
    if lista_empleados.winfo_ismapped():
        lista_empleados.pack_forget()
    else:
        lista_empleados.pack()
        mostrar_empleados()

# Botones para agregar y mostrar empleados
boton_agregar = tk.Button(Gestor, text="Agregar un empleado", command=agregar_empleado)
boton_agregar.pack()
boton_lista = tk.Button(Gestor, text="Ver lista de empleados", command=mostrar_lista)
boton_lista.pack()

# Lista para mostrar los empleados (inicialmente oculta)
lista_empleados = tk.Listbox(Gestor, width=40)
lista_empleados.pack_forget()







ventana.mainloop()




















ventana.mainloop()
ventana.update()

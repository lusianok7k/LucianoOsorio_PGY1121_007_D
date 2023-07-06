import numpy
escenario = numpy.zeros((10,10),int)
fila = 0
entradas = 0


cantidad_silver = 0
cantidad_gold = 0
cantidad_platinium = 0

acumulador_gold = 0
acumulador_platinium = 0
acumulador_silver = 0

lista_ruts = []
lista_fila = []
lista_columna = []

def mostrar_menu ():
    print("""MENU:
    1. Comprar entradas
    2. Mostrar ubicaciones
    3. Ver listado de asistente
    4. Mostrar ganancias totales
    5. Salir""")


def validar_opcion ():
    opc = int(input("Ingrese la opcion: "))   
    if opc in (1,2,3,4,5):
        return opc
    else:
        print("Error!, opcion invalida") 

def validar_rut ():
    rut = int(input("Ingrese su rut: "))
    if rut > 100000000 and rut < 999999999:
        return rut
    else:
        print("Rut invalido")


def validar_entradas ():
    entradas = int(input("Ingrese la cantidad de entradas: "))  
    if entradas > 0 and entradas < 3:
        return entradas
    else:
        print("Numero invalido")      



def mostrar_ubicacion ():
    for x in range (10):
        print(f" Fila {x+1}")
        for y in range (10):
            print(f"{x}{y}",end="  ")
print()

def comprar_entrada ():
    fila = input("Ingrese la fila: ")
    columna = input("Ingrese la columna: ")
    if fila and columna != 0:
           print("Compra realizada con exito")
           posicion_fila = fila.index 
           posicion_columna = columna.index
           posicion = columna.index,fila.index
           if fila.index and columna.index:
               posicion = 0

    

def despedida():
    print("Adios, se despide Luciano Osorio")
    print("Fecha = 06-07-2023")
    return   


def buscar ():
    rut = int(input("Ingrese el rut: "))    
    if rut in lista_ruts:
            posicion = lista_ruts 
            for x in range(posicion):
                print(lista_ruts)
                print(lista_columna)
                print(lista_fila)
    else:
            print("Este rut no esta registrado")   



def ganancias ():
    if fila == 10 or 20:
        acumulador_platinium = entradas * 120000
        cantidad_platinium = cantidad_platinium + entradas
    elif fila == 21 or 50:
        acumulador_gold = entradas * 80000
        cantidad_gold = cantidad_gold + entradas
    else:
        acumulador_silver = entradas * 50000
        cantidad_silver = cantidad_silver + entradas
        print("-------------------------------------------------------------------------------|")    
        print(f"|La ganancia total es de {acumulador_gold+acumulador_platinium+acumulador_silver}|")  
        print(" |-------------------------------------------------------------------------------|")  
        print(f"|La cantidad de platinium fueron de {cantidad_platinium}|")
        print(f"|La cantidad de silver fueron de {cantidad_gold}|")
        print(f"|La cantidad de gold fueron de {cantidad_silver}|")



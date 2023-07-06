import numpy
import funciones as fn

fila = 0

cantidad_silver = 0
cantidad_gold = 0
cantidad_platinium = 0

acumulador_gold = 0
acumulador_platinium = 0
acumulador_silver = 0

lista_ruts = []
lista_fila = []
lista_columna = []

escenario = numpy.zeros((10,10),int)
while True:
    fn.mostrar_menu()
    opc = fn.validar_opcion()
    if opc == 1:
        ubicacion = fn.mostrar_ubicacion()
        print("Fila 10")

        entradas = fn.validar_entradas()
        rut = fn.validar_rut()
        fila = fn.comprar_entrada()

        lista_ruts.append(rut)
        lista_fila.append(fila)   
        
    elif opc == 2:
        fn.mostrar_ubicacion()
    elif opc == 3:
        fn.buscar()     
    elif opc == 4:
        fn.ganancias()        
    else:
        fn.despedida()
        break
       

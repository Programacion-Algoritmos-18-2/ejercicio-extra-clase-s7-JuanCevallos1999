from ordenamiento.OrdenamientoInsercion import * #Importacion de clases
arreglo = [10,0,3,2,1,8,2] #Arreglo desordenado
ordenamiento = OrdenamientoInsercion()  #Creamos el objeto de tipo OrdenamientoInsercion
print("Arreglo desordenado")
print(arreglo) #presentamos arreglo sin ordenar
ordenamiento.ordenamientoPorInsercion(arreglo) #Llamamos al metodo que lo ordena y lo presentamos
print(arreglo)
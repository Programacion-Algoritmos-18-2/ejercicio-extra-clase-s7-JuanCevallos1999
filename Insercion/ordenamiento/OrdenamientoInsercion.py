class OrdenamientoInsercion():

	def ordenamientoPorInsercion(self, arreglo): #Recibimos el arreglo 
		for indice in range(1,len(arreglo)): #Recoorremos el arreglo con un iterador
			valorActual = arreglo[indice] #Guardamos el valor actual de la iteracion en el arreglo
			posicion = indice #Almacenamos la posicion de este valor
			while posicion>0 and arreglo[posicion-1]>valorActual: #Siempre que se cumplan ambas condiciones poscion>0 y actual sea mayor al anterior
				arreglo[posicion]=arreglo[posicion-1] #arreglo en la posicio almacenada va a ser igual al valor anterior
				posicion = posicion-1
				arreglo[posicion]=valorActual

def __str__(self):
	temporal = " "
	for x in xrange(1,len(arreglo)):
		temporal = "%s- %s"%(temporal, x)
	temporal = "%s-%s"%(temporal)
	return temporal
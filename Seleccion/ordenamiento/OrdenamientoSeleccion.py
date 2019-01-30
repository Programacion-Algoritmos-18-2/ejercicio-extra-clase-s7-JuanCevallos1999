class OrdenamientoSeleccion(): 
	def __init__(self, arr): #Recibimos en el constructor el arreglo y lo inicializamos
		self.arreglo = arr

	def ordenamientoPorSeleccion(self): 
		for x in range(len(self.arreglo)-1): #Hacemos un for que recorra todo el arreglo 
			masPeque = x #Consideraremos el mas pequeño asignandole el contador del primer for
			for i in range(x+1,len(self.arreglo)): #Hacemos otro for que itere con el nuevo iterador
				if (self.arreglo[i] < self.arreglo[masPeque]): #Si los numeros que se encuentran delante de masPeque son menores masPeque tomara ese valor mas pequeño
					masPeque = i
			self.intercambiar(x, masPeque) #Llamamos el metodo intercambiar y le enviamos dos parametros
			print(self.__str__())


	def intercambiar(self,primero, segundo): #Recibe dos paramatros la posicion del primer iterador y la posicion del menor
		temporal= self.arreglo[primero] #Almacenamos el valor del primer iterador
		self.arreglo[primero] = self.arreglo[segundo] #Asignamos en la primera posicion el valor de masPeque
		self.arreglo[segundo] = temporal #En la posicion que quedaria "vacia" asignamos el tempral
			
			
#Metodo str similiar a ToString
	def __str__(self):
		temporal = " "
		for d in self.arreglo:
			temporal = "%s- %s"%(temporal, d)
		temporal = "%s %s"%(temporal,"\n")
		return temporal
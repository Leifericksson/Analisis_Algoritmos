# importamos la libreria random para realizar nodos aleatorios

import random as rd

# Creamos la clase Nodo
class Nodo:

	def __init__(self, id):
		self.id = id
		#print("aa:",id)

# Creamos la calse Arista
class Arista:

	def __init__(self,n0,n1,id):
		self.nodo0 = n0
		self.nodo1 = n1
		self.id = id

# Creamos la clase Grafo
class Grafo:

	def __init__(self):

		self.nodos = {}
		self.aristas = {}

	def agregarnodo(self, v):
		nodo = self.nodos.get(v)
		#print("nodo:", self.nodos.get)

		if not nodo in self.nodos:
			nodo = Nodo(v)
			print("nodo:", nodo.id)

	def agregararista(self,v,a,b):
		arista = self.aristas.get(v)
		#print("aristas:", arista)

		if arista is None:
			n0 = self.agregarnodo(a)
			n1 = self.agregarnodo(b)
			arista = Arista(n0, n1, v)
			print("ari:", arista.id)


'''     if a in self.nodos and b in self.nodos:
			self.nodos[a].agregar(b)
			self.nodos[b].agregar(a)'''

# definimos la funcion principal
def main():
	g = Grafo()

	n = int(input("introduzaca el numero de nodos:"))
	a = float(input("introduzca la probabilida(0-1):"))

	for i in range(n):
		g.agregarnodo(i)

	for i in range(n):
		for j in range(n):
			if rd.random() < a:
				if i != j:
					g.agregararista(str(i) + ' -- ' + str(j), i, j)


		#g.agregararista(n0,n1)

	#for p in g.nodos:
	#	print("b:", p, g.nodos[p].aristas)


main()
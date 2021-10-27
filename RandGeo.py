# importamos la libreria random para realizar nodos aleatorios

import random as rd
import numpy as np


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
		#print("nodo1:", self.nodos.get)

		if not nodo in self.nodos:
			nodo = Nodo(v)
			#print("nodo:", nodo.id)

	def agregararista(self,v,a,b):
		arista = self.aristas.get(v)
		#print("aristas:", arista)

		if arista is None:
			n0 = self.agregarnodo(a)
			n1 = self.agregarnodo(b)
			arista = Arista(n0, n1, v)
			print("arista:", arista.id)


'''     if a in self.nodos and b in self.nodos:
			self.nodos[a].agregar(b)
			self.nodos[b].agregar(a)'''

# definimos la funcion principal
def main():
	g = Grafo()
	var_x = []
	var_y = []

	n = int(input("introduzca el numero de nodos:"))
	r = float(input("introduzca el rango de cobertura (0-1):"))

	for i in range(n):
		g.agregarnodo(i)
		var_x.append(rd.random())
		var_y.append(rd.random())
	print("x:", var_x)
	print("y:", var_y)

	for i in range(n):
		for j in range(n):
			if i != j:
				dist = round(np.sqrt(np.sum(np.square(var_x[i]-var_x[j]))), 2)
				print("dist:", dist)
				if dist <= r:
					g.agregararista(str(i) + ' -- ' + str(j), i, j)
		#g.agregararista(n0,n1)
	#for p in g.nodos:
	#	print("b:", p, g.nodos[p].aristas)
main()
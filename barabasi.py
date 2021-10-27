# importamos la libreria random para realizar nodos aleatorios

import random as rd
import numpy as np


# Creamos la clase Nodo
class Nodo:

	def __init__(self, id):
		self.id = id
# print("aa:",id)


# Creamos la calse Arista
class Arista:

	def __init__(self, n0, n1, id):
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
		# print("nodo1:", self.nodos.get)

		if not nodo in self.nodos:
			nodo = Nodo(v)

	# print("nodo:", nodo.id)

	def agregararista(self, v, a, b):
		arista = self.aristas.get(v)
		# print("aristas:", arista)

		if arista is None:
			n0 = self.agregarnodo(a)
			n1 = self.agregarnodo(b)
			arista = Arista(n0, n1, v)

		return arista.id

def graph(self):
	g = Grafo()
	val = 'digraph example{\n'
	val += g.agregararista()
	val += "}\n"
	print("asd", val)
	return val


'''     if a in self.nodos and b in self.nodos:
			self.nodos[a].agregar(b)                                                           
			self.nodos[b].agregar(a)'''


# definimos la funcion principal
def main():
	g = Grafo()
	var = []

	n = int(input("introduzca el numero de nodos:"))
	a = int(input("introduzca el numero de arista por nodo:"))

	for i in range(n):
		g.agregarnodo(i)

	val = 'digraph example{\n'

	for j in range(1, n+1):
		# print("j", j)
		var.append(j)
		rd.shuffle(var)
		for k in range(j):
			# print("k", k)
			grad = var[k]
			p = 1 - (grad/a)
			# print("p", p)
			if rd.random() < p:
				if var[k] != j:
					r = g.agregararista(str(j) + ' -- ' + str(k), j, k)
					print(r)
					val += str(r)+";\n"
	val += "}\n"

	return val

			# g.agregararista(n0,n1)
# for p in g.nodos:
# print("b:", p, g.nodos[p].aristas)'''


r = main()
file = open("barabasi_500.dot", "w+")
file.write(r)
file.close()

main()



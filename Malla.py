import numpy as np
import random as rd

class Nodo:
	def __init__(self, id):
		self.nodoid = id


class Arista:
	def __init__(self, n0, n1, id):
		self.nodo0 = n0
		self.nodo1 = n1
		self.arisid = id


class Grafo:
	def __init__(self):
		self.aristas = {}
		self.nodos = {}

	def agregarnodo(self, nom):
		nodo = self.nodos.get(nom)
		return nodo


	def agregararista(self, nom, n0, n1):
		arista = self.aristas.get(nom)

		if arista in None:
			node0 = self.agregarnodo(n0)
			node1 = self.agregarnodo(n1)
			arista = Arista(node0, node1, nom)
		return arista

	def nodonom(self, i):
		return str(i)

	def ariname(self, i, j):
		return str(i) + "--" + str(j)


def main():

	g = Grafo()

	m = int(input("introducir filas: "))
	n = int(input("introducir columnas: "))

	val = 'digraph example{\n'

	for i in range(m):
		for j in range(n):
			if j < n - 1:
				p = g.ariname(i * n + j, i * n + j + 1)
				print(p)
				val += str(p) + ";\n"
			if i < m - 1:
				p = g.ariname(i * n + j, (i + 1) * n + j)
				val += str(p) + ";\n"
				print(p)
	val += "}\n"
	return val


r = main()
file = open("Malla_30.dot", "w+")
file.write(r)
file.close()

main()


# importamos la libreria random para realizar nodos aleatorios
import random as rd
from random import choice

# Creamos la clase Nodo


class Nodo:

	def __init__(self, i):
		self.i = i
		self.visitado = False
		self.nivel = 0
		self.vecinos = []
		# print("aa:",id)

	def agregavecinos(self, v):
		if not v in self.vecinos:
			self.vecinos.append(v)
		# print("vecinos:", self.vecinos)

# Creamos la calse Arista


class Arista:

	def __init__(self, n0, n1, i):
		self.nodo0 = n0
		self.nodo1 = n1
		self.i = i
		# print("ddd",self.i, self.nodo0, self.nodo1)

# Creamos la clase Grafo


class Grafo:

	def __init__(self):

		self.nodos = {}
		self.aristas = {}

	def agregarnodo(self, v):
		if not v in self.nodos:
			self.nodos[v] = Nodo(v)  # <--
			r = self.nodos[v]
		return r

	def agregararista(self, v, a, b):
		if a in self.nodos and b in self.nodos:
			self.nodos[a].agregavecinos(b)
			# print("nodos[a]", self.nodos[a].id)
			self.nodos[b].agregavecinos(a)
		# print("nodos[b]", self.nodos[b].id)

	def bfs(self, s):
		if s in self.nodos:
			cola = [s]

			self.nodos[s].visitado = True
			self.nodos[s].nivel = 0

			print("(" + str(s) + "," + str(self.nodos[s].nivel) + ")")

			while len(cola) > 0:
				act = cola[0]
				cola = cola[1:]
			# print("act", act)
			# print("cola", cola)
			for v in self.nodos[act].vecinos:

				if self.nodos[v].visitado == False:
					cola.append(v)
					# print("cola.append", cola)
					# print("v",v)
					self.nodos[v].visitado = True
					self.nodos[v].nivel = self.nodos[act].nivel + 1
					print("(" + str(v) + "," + str(self.nodos[v].nivel) + ")")
			'''if a in self.nodos and b in self.nodos:
			self.nodos[a].agregar(b)
			self.nodos[b].agregar(a)'''

# definimos la funcion principal


def main():

	g = Grafo()
	n = int(input("introduzca el numero de nodos:"))
	a = int(input("introduzca el numero de aristas:"))

	for i in range(n):
		r = g.agregarnodo(i)
		# print("agregarnodo", r.i)
	val = 'digraph example{\n'
	for i in range(a):
		n0 = rd.randint(0, n-1)
		n1 = choice([i for i in range(0, a) if i not in [n0]])
		# print("n0", n0)
		# print("n1", n1)
		#if n0 != n1:
		g.agregararista(i, n0, n1)
			# print(str(v.nodo0) + " -- " + str(v.nodo1))
	for p in g.nodos:
		f = g.nodos[p].vecinos
		val += str(p) + " -- " + str(f)[1:-1] + ";\n"
	val += "}\n"
	g.bfs(2)
	return val

		#g.agregararista(n0,n1)

	#for p in g.nodos:
	#	print("b:", p, g.nodos[p].aristas)


r = main()
file = open("BFS30.dot", "w+")
file.write(r)
file.close()

main()


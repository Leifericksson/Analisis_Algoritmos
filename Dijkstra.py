import random as rd
import numpy as np


class Nodo:
	def __init__(self, i):
		self.i = i
		self.visitado = False
		self.nivel = 0
		self.vecinos = []
		self.padre = None
		self.distancia = float('inf')

	# print("aa:",id)

	def agregavecinos(self, v, p):
		if not v in self.vecinos:
			self.vecinos.append([v, p])
		print("vecinos:", self.vecinos)


# Creamos la clase Arista
class Arista:

	def __init__(self, n0, n1, id):
		self.nodo0 = n0
		self.nodo1 = n1
		self.id = id


class Grafo:
	def __init__(self):
		self.nodos = {}
		self.aristas = []

	def agregarnodo(self, v):
		if not v in self.nodos:
			self.nodos[v] = Nodo(v)
			print("nodos:", self.nodos[v].i)

	def agregararista(self, a, b, p):
		if a in self.nodos and b in self.nodos:
			self.nodos[a].agregavecinos(b, p)
			print("nodos[a]", self.nodos[a].i)
			self.nodos[b].agregavecinos(a, p)
			print("nodos[b]", self.nodos[b].i)

	def ariname(self, i, a, b):
		self.a = a
		self.b = b
		self.i = i

		return self.a, self.b

	def distancia(self, lista):
		if len(lista) > 0:
			m = self.nodos[lista[0]].distancia
			print("m1", m)
			v = lista[0]
			for e in lista:
				print("e", e)
				if m > self.nodos[e].distancia:
					m = self.nodos[e].distancia
					v = e
					print("m", m)
					print("v", v)
			return v

	def dijkstra(self, a):
		if a in self.nodos:
			self.nodos[a].distancia = 0  # Actualiza la dist del nodo padre = 0
			actual = a
			nodvisitado = []  # Conjunto de nodos

			for v in self.nodos:
				if v != a:
					self.nodos[v].distancia = float('inf')  # los nodos previamente identifi se asigna valor inf peso
				nodvisitado.append(v)
		

			while len(nodvisitado) > 0:  # Mientras la cola no este vacia
				for vecino in self.nodos[actual].vecinos:
					# print("vecino0", vecino[0], "vecino1", vecino[1])
					if self.nodos[vecino[0]].visitado == False:
						if self.nodos[vecino[0]].distancia > self.nodos[actual].distancia + vecino[1]:
							self.nodos[vecino[0]].distancia = self.nodos[actual].distancia + vecino[1]
							self.nodos[vecino[0]].padre = actual
							print("test1", self.nodos[vecino[0]].distancia)
							print("test2", self.nodos[vecino[0]].padre)
				self.nodos[actual].visitado = True
				nodvisitado.remove(actual)
				actual = self.distancia(nodvisitado)
				# print("actual", actual)
		else:
			return False


class Listas:
	def __init__(self):

		self.g = Grafo()
		self.peso = []
		self.listaDj = []

	def Ghephi(self, listaAristas):
		self.listaAristas = listaAristas

		listaAristasL = []

		self.listaAristasS = self.listaAristas
		for i in self.listaAristasS:
			for j in i:
				listaAristasL.append(j)
		l = listaAristasL

		li = l
		val = 'digraph example{\n'
		for i in range(0, len(li) - 1, 2):
			val += str(li[i]) + " -- " + str(li[i + 1]) + ";\n"
		val += "}\n"

		file = open("Generados.dot", "w+")
		file.write(val)
		file.close()

		return l


class algoritmos:
	def __int__(self):
		self.Listas = []

	def malla(self, m, n):

		g = Grafo()
		hor = []
		ver = []

		graf = []

		for i in range(m):
			for j in range(n):
				if j < n - 1:
					hor = g.ariname(i, i * n + j, i * n + j + 1)
					print("hor", hor)
				if i < m - 1:
					ver = g.ariname(i, i * n + j, (i + 1) * n + j)
					print("ver", ver)
				graf.append(hor + ver)
				hor = ()
				ver = ()
		return graf

	def erdos(self, n, a):

		g = Grafo()
		graf = []

		for i in range(a):
			n0 = rd.randint(0, n - 1)
			n1 = rd.randint(0, n - 1)

			if n0 != n1:
				graf.append(g.ariname(i, n0, n1))
				print("arime", graf)
		return graf

	def gilbert(self, n, a):

		g = Grafo()
		graf = []

		for i in range(n):
			for j in range(n):
				if rd.random() < a:
					if i != j:
						graf.append(g.ariname(n, i, j))
						print("arime", graf)
		return graf

	def geo(self, n, r):

		g = Grafo()
		graf = []
		var_x = []
		var_y = []

		for i in range(n):
			var_x.append(rd.random())
			var_y.append(rd.random())
		# print("x:", var_x)
		# print("y:", var_y)
		for i in range(n):
			for j in range(n):
				if i != j:
					dist = round(np.sqrt(np.sum(np.square(var_x[i] - var_x[j]))), 2)
					# print("dist:", dist)
					if dist <= r:
						graf.append(g.ariname(n, i, j))
						print(graf)
		return graf

	def bara(self, n, a):

		g = Grafo()
		graf = []
		var = []

		for j in range(1, n + 1):
			# print("j", j)
			var.append(j)
			rd.shuffle(var)
			for k in range(j):
				# print("k", k)
				grad = var[k]
				p = 1 - (grad / a)
				# print("p", p)
				if rd.random() < p:
					if var[k] != j:
						graf.append(g.ariname(n, j, k))
						print(graf)

		return graf


class Main:
	h = algoritmos()
	g = Grafo()
	c = Listas()
	peso = []
	listDij = []

	# n = int(input("introduzca el numero de nodos:"))
	# a = int(input("introduzca el numero de arista por nodo:"))
	n = int(input("valor de malla nxn: "))
	m = n * n
	for l in range(m):
		g.agregarnodo(l)

	result = h.malla(n, n)
	print("result", result)

	bfss = c.Ghephi(result)
	print(bfss)

	for i in range(0, len(bfss) - 1, 2):
		p = rd.randint(100, 500)
		peso.append((bfss[i], bfss[i + 1], p))
		print("peso", peso)

	for i in range(0, len(peso)):
		for j in range(0, 3):
			listDij.append(peso[i][j])
			print("listDij", listDij)

	for i in range(0, len(listDij) - 1, 3):
		g.agregararista(listDij[i], listDij[i + 1], listDij[i + 2])

	for v in g.nodos:
		print("vecino", (v, g.nodos[v].vecinos))

	n = int(input("seleccionar nodo: "))

	g.dijkstra(n)
	val = 'digraph example{\n'
	for v in g.nodos:
		val += str(g.nodos[v].padre) + " -> " + str(v) + " [Label = 'nodo_" + str(n) + " (" + str(g.nodos[v].distancia) \
		       + ")'];\n"
	val += "}\n"
	file = open("Calculados.dot", "w+")
	file.write(val)
	file.close()

Main()

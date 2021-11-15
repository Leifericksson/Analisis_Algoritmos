import random as rd
import numpy as np


class Nodo:
	def __init__(self, i):
		self.i = i
		self.visitado = False
		self.nivel = 0
		self.vecinos = []
		self.padre = None
		# print("aa:",id)

	def agregavecinos(self, v):
		if not v in self.vecinos:
			self.vecinos.append(v)
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
			self.nodos[v] = Nodo(v)  # <--revisar_bien
			print("nodos:", self.nodos[v].i)

	def agregararista(self, a, b):
		if a in self.nodos and b in self.nodos:
			self.nodos[a].agregavecinos(b)
			print("nodos[a]", self.nodos[a].i)
			self.nodos[b].agregavecinos(a)
			print("nodos[b]", self.nodos[b].i)

	def ariname(self, v, a, b):
		self.a = a
		self.b = b

		return self.a, self.b

	def bfs(self, r):
		guardabfs = []
		if r in self.nodos:
			cola = [r]

			self.nodos[r].visitado = True
			self.nodos[r].nivel = 0
			print("(" + str(r) + ", " + str(self.nodos[r].nivel) + ")")
			while (len(cola) > 0):
				act = cola[0]
				cola = cola[1:]

				for v in self.nodos[act].vecinos:
					if self.nodos[v].visitado == False:
						cola.append(v)
						self.nodos[v].visitado = True
						self.nodos[v].nivel = self.nodos[act].nivel + 1
						guardabfs.append((v, self.nodos[v].nivel))
						print("(" + str(v) + ", " + str(self.nodos[v].nivel) + ")")
		self.storeR = guardabfs
		print("bfs:", self.storeR)

	def dfs_I(self, r):
		self.guardadfs = []
		if r in self.nodos:
			self.nodos[r].visitado = True
			d = self.nodos[r].vecinos
			#print("d", d)
			l = len(self.nodos[r].vecinos) - 1

			newlista = []
			while (l >= 0):
				newlista.append(d[l])
				l = l - 1
				#print("new",newlista)
			for nodo in newlista:

				if self.nodos[nodo].visitado == False:
					self.nodos[nodo].padre = r
					self.guardadfs.append((r, nodo))
					print("(" + str(r) + ", " + str(nodo) + ")")
					self.dfs_I(nodo)
		self.storeR = self.guardadfs
		#print("dfs:", self.storeR)


class Cadena:
	def __init__(self):

		self.g = Grafo()

	def ID(self, listaAristas):
		# Se prorciona la lista de nodo a la clase nodo
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

		file = open("Malla.dot", "w+")
		file.write(val)
		file.close()

		return l


class algoritmos:
	def __int__(self):
		self.Listas = []

	def malla(self, m, n):

		g = Grafo()
		graf = []

		for i in range(m):
			for j in range(n):
				if j < n - 1:
					hor = g.ariname(i * n + j, i * n + j + 1)
					print("hor",hor)
				if i < m - 1:
					ver =g.ariname(i * n + j, (i + 1) * n + j)
					print("ver",ver)
				graf.append(hor + ver)
		return graf

	def erdos(self, n, a):

		g = Grafo()
		graf = []

		for i in range(a):
			n0 = rd.randint(0, n-1)
			n1 = rd.randint(0, n-1)
			#print("n0", n0)
			#print("n1", n1)
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


class Main:

	h = algoritmos()
	g = Grafo()
	c = Cadena()

	n = int(input("introduzca el numero de nodos:"))
	r = float(input("introduzca el rango de cobertura (0-1):"))

	for l in range(n):
		g.agregarnodo(l)

	result = h.geo(n, r)
	print("result", result)

	bfss = c.ID(result)
	print(bfss)

	for i in range(0, len(bfss) - 1, 2):
		g.agregararista(bfss[i], bfss[i + 1])

	for v in g.nodos:
		print("vecino", (v, g.nodos[v].vecinos))

	n = int(input("seleccionar nodo: "))

	g.bfs(n)
	#g.dfs_I(n)


Main()

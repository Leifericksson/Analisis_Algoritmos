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
		print("vecinos:", self.vecinos)


class Grafo:
	def __init__(self):
		self.nodos = {}

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

	def ariname(self, i, j):
		self.i = i
		self.j = j
		return i, j

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


class Cadena:
	def __init__(self):
		#self.b = Biblioteca()
		self.g = Grafo()
		#self.csvR = CsvRecorrido()

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

		file = open("mallita.dot", "w+")
		file.write(val)
		file.close()

		return l


class Main:

	h = algoritmos()
	g = Grafo()
	c = Cadena()

	n = int(input("valor de malla nxn "))
	m = n*n
	for a in range(m):
		g.agregarnodo(a)

	print("n", n)
	print('Graficar la malla')
	result = h.malla(n, n)
	print(result)
	bfss = c.ID(result)
	print(bfss)

	for i in range(0, len(bfss) - 1, 2):
		g.agregararista(bfss[i], bfss[i + 1])

	for v in g.nodos:
		print((v, g.nodos[v].vecinos))

	n = int(input("seleccionar nodo: "))
	g.bfs(n)

Main()

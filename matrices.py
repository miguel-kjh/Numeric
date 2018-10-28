import math

class Matrices(object):
	def __init__(self, m,n):
		self.n = n
		self.m = m
		self.l0 = list(range(m))
		for i in range(m):
			self.l0[i] = list(range(n))

	def tamaño(self):
		print("El tamaño de la matriz es: ", str(self.m), "x", str(self.n))

	def filas(self):
		return self.n

	def columnas(self):
		return self.m

	def definir(self, ele):
		for i in range(self.m):
			piv = self.l0[i]
			for j in range(self.n):
				piv[j] = ele

	def mostrar(self):
		for i in range(self.m):
			print(self.l0[i])

	def insertar(self, m, n, ele):
		try:
			piv = self.l0[m]
			piv[n] = ele
		except IndexError:
			print("Index Error")
			return "Operative Error"

	def mostrarElemento(self, m, n):
		try:
			piv = self.l0[m]
			return piv[n]
		except IndexError:
			print("Index Error")
			return "Operative Error"

	def copiar(self):
		m0 = Matrices(self.m, self.n)
		for i in range(self.m):
			piv = self.l0[i]
			for j in range(self.n):
				m0.insertar(i,j,piv[j])
		return m0

	def factorizacion(self):
		#Metodo de factorización de LU para no simetricas
		l = Matrices(self.m, self.n)
		u = Matrices(self.m, self.n)
		u.definir(0)
		l.definir(0)
		for i in range(self.m):
			l.insertar(i,i, 1)
			suma = 0
			for k in range(i): suma = suma + (l.mostrarElemento(i,k) * u.mostrarElemento(k,i))
			u.insertar(i,i, self.mostrarElemento(i,i) - suma)
			if(u.mostrarElemento(i,i) == 0):return None
			p = i+1
			for p in range(self.m):
				suma = 0
				for k in range(i): suma = suma + (l.mostrarElemento(i,k) * u.mostrarElemento(k,p))
				u.insertar(i,p, self.mostrarElemento(i,p) - suma)
				suma = 0
				for k in range(i): suma = suma + (l.mostrarElemento(p,k) * u.mostrarElemento(k,i))
				l.insertar(p, i, (self.mostrarElemento(p,i) - suma)/u.mostrarElemento(i,i))
		res = 1
		for i in range(self.m):
			res = res * u.mostrarElemento(i,i)
		return res

	def simetria(self):
		for i in range(self.m):
			for j in range(self.n):
					if(self.mostrarElemento(i,j) != self.mostrarElemento(j,i)):return False
		return True

	def cholesky(self):
		#Metodo de cholesky para simétricas
		b = Matrices(self.m, self.n)
		b.definir(0)
		for q in range(self.m):
			suma = 0
			for k in range(q):
				suma = suma + b.mostrarElemento(q,k)**2
			res = self.mostrarElemento(q,q) - suma
			if(res == 0): return None
			b.insertar(q,q, math.sqrt(abs(res)))
			p = q+1
			for p in range(self.m):
				suma = 0
				for k in range(q):
					suma = suma + b.mostrarElemento(p,k)*b.mostrarElemento(q,k)
				b.insertar(p,q, (self.mostrarElemento(p,q) - suma)/b.mostrarElemento(q,q))
		res = 1
		for i in range(self.m):
			res = res * b.mostrarElemento(i,i)
		if res < 0: return -res*res
		else: return res*res

	def determinante(self):
		if(self.m != self.n): return None
		if self.simetria(): return self.cholesky()
		else: return self.factorizacion()

	def suma(self, m1):
		if(self.m != m1.m or self.n != m1.n): return None
		res = Matrices(self.m, self.n)
		for i in range(self.m):
			piv0 = self.l0[i]
			piv1 = m1.l0[i]
			piv2 = res.l0[i]
			for j in range(self.n): piv2[j] = piv0[j] + piv1[j]
		return res

	def mult(self, n):
		res = Matrices(self.m, self.n)
		for i in range(self.m): 
			piv = res.l0[i] 
			piv1 = self.l0[i]
			for j in range(self.n): piv[j] = piv1[j]*n
		return res

	def multiplicar(self, m1):
		if(self.n != m1.m): return None
		res = Matrices(self.m, self.n)
		for i in range(self.m): 
			piv = res.l0[i]
			piv1 = self.l0[i] 
			piv2 = list(range(m1.n))
			for p in range(m1.n):
				for k in range(m1.n):
					pivote = m1.l0[k]
					piv2[k] = pivote[p]
				suma = 0
				for j in range(self.n):suma = (piv1[j] * piv2[j]) + suma
				piv[p] = suma
		return res

		
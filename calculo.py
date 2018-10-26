import math
"""
Function that calculates the roots of P (x) = ax2 + bx + c
Returns 0 if it ends well and -1 otherwise 
"""
def quadratic(a,b,c, raiz):
	if a == 0:
		if b == 0: return -1
		raiz[0] = raiz[1] = -c/b
		return 0
	else:
		det = b*b-4*a*c
		if det < 0: return -1
		det = math.sqrt(det)
		if b > 0: raiz[0] = (-b-det)/(2*a)
		else: raiz[0] = (-b+det)/(2*a)
		if raiz[0] != 0: raiz[1] = c/(a*raiz[0])
		else:raiz[1] = 0
		return 0

"""derivadas más precisas"""
def derivative(func, x, h):
	return (func(x+h)-func(x-h))/2*h

def second_derivative(func, x, h):
	return (func(x+h)-2*func(x)+func(x-h))/h*h

def double_derivative_x(func, x, y, h):
	pass

def root_calculations(func, x0, tol, Nmax):
	#algoritmo Newton_Raphson
	fx = 0
	fx_1 = 0
	x1 = 0
	for i in range(Nmax):
		fx = func(x0)
		if(fx == 0): return x0
		fx_1 = derivative(func, x0, 1.)
		if(fx_1 == 0):return None
		x1 = x0 -(fx/fx_1)
		if(abs(x1-x0) <= abs(x1 + 1.)*tol):return x1
		x0 = x1


def integral(f, a, b, Nmax):
	#algortimo de Simpson 1D
	rest = (b-a)/Nmax
	intg = 0
	for k in range(Nmax):
		xk = a+(k*rest)
		xk1 = a+((k+1)*rest)
		intg = intg + (f(xk) + 4*f((xk+xk1)/2.) + f(xk1))*1/6*rest
	return intg

def double_integral(f, a, b, c, d, M, N):
	#algortimo de Simpson 2D
	res = 0
	hx = (b-a)/M
	hy = (d-c)/N
	for k in range(M):
		for n in range(N):
			#PARA LAS X
			xk = a+(k*hx)
			xk1 = a+((k+1)*hx)
			xm = (xk+xk1)/2.
            #PARA LAS Y
			yn = c+(n*hy)
			yn1 = c + ((n+1)*hy)
			ym = (yn+yn1)/2.
            #CALCULO DE LA INTREGRAL
			fxk = ((f(xk,ym) + 4*f(xk, ym) + f(xk, yn1))/6.)*hy
			fxm = ((f(xm,yn) + 4*f(xm, ym) + f(xm, yn1))/6.)*hy
			fxk1 = ((f(xk1,yn) + 4*f(xk1, ym) + f(xk1, yn1))/6.)*hy
			res = res + ((fxk+4*fxm+fxk1)/6.)*hx
	return res

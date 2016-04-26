from numpy import log10, ones_like, asarray, exp, cos, linspace
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import csv

A_Metilico = []
E_Etilico = []
E_Petroleo = []
alpha = []
beta = []
lamnda = []


with open("Untitled.csv", "r") as archivo:
    datos = csv.reader(archivo, delimiter="\t")
    #next(datos, None)
    next(datos, None)
    for fila in datos:
        lamnda.append(float(fila[0]))
        A_Metilico.append(float(fila[1])    )
        E_Petroleo.append(float(fila[2]))
        beta.append(float(fila[3]))
        alpha.append(float(fila[4]))


def absorbance(T):
    A = 2.0*ones_like(T) - log10(T)
    return A

def gaussian(x, a, b, c):
    val = a* exp(-(x - b)**2 / c**2)
    return val
    #return a*x+b

def maximos(X, v):
    x_max = []
    y_max = []
    for i in range(len(v)-1):
        if (v[i+1] > v[i]) and (v[i+2] <= v[i+1]):
            x_max.append(i+1)
            y_max.append(v[i+1])

            print(i+1, v[i+1])
    mitad = int(len(y_max)/2)
    print(mitad)

    y = [max(y_max[:mitad]), max(y_max[mitad:])]
    x = [x_max[y_max.index(y[0], 0, mitad)],  x_max[y_max.index(y[1], mitad, len(y_max))]]

    #print(x,y)

    r = [x[0] - 4, x[0] + 4]
    s = [x[1] - 3, x[1] + 2]

    X1 = X[r[0]:r[1]]
    X2 = X[s[0]:s[1]]

    Y1 = v[r[0]:r[1]]
    Y2 = v[s[0]:s[1]]

    m1 = asarray([X1, Y1])
    m2 = asarray([X2, Y2])

    return m1, m2



T_Met = absorbance(asarray(A_Metilico))
T_Ee = absorbance(asarray(E_Etilico))
T_Ep = absorbance(asarray(E_Petroleo))
T_a = absorbance(asarray(alpha))
T_b = absorbance(asarray(beta))
L = asarray(lamnda)

m1a, m2a = maximos(L, T_a)

spl1 = UnivariateSpline(m1a[0], m1a[1])
spl2 = UnivariateSpline(m2a[0], m2a[1])
xint1 = linspace(m1a[0][0], m1a[0][-1], 1000)
wint1 = linspace(m2a[0][0], m2a[0][-1], 1000)

aa1= spl1(xint1).argmax()
aa2 = spl2(wint1).argmax()

la1 = xint1[aa1]
la2 = wint1[aa2]

n1a, n2a = maximos(L, T_b)

rpl1 = UnivariateSpline(n1a[0], n1a[1])
rpl2 = UnivariateSpline(n2a[0], n2a[1])
xint2 = linspace(n1a[0][0], n1a[0][-1], 1000)
wint2 = linspace(n2a[0][0], n2a[0][-1], 1000)

ab1= rpl1(xint2).argmax()
ab2 = rpl2(wint2).argmax()

lb1 = xint1[ab1]
lb2 = wint1[ab2]
print(ab1, ab2)



fig = plt.figure(1)
plt.plot(L, T_a, 'x', color="red", label="Experimental")
plt.plot(xint1, spl1(xint1), color="purple", label=r"Splines 1er máximo $\lambda$ = %i nm"%la1)
plt.plot(wint1, spl2(wint1), color="deeppink", label= r"Splines 2do máximo  $\lambda$ =%i nm"%la2)
plt.xlim(380,710)
plt.xlabel(r"$ \lambda  (nm)$")
plt.ylabel(r"Absorbancia")
plt.title(r"Espectro de Absorción para la $\alpha$ - clorofila")
plt.legend()
fig.show()


fig2 = plt.figure(2)
plt.plot(L, T_b, 'x', color="crimson", label="Experimental")
plt.plot(xint2, rpl1(xint2), color="purple", label=r"Splines 1er máximo $\lambda$ = %i nm"%lb1)
plt.plot(wint2, rpl2(wint2), color="deeppink", label= r"Splines 2do máximo  $\lambda$ =638 nm"%lb2)
plt.xlim(380,710)
plt.xlabel(r"$ \lambda  (nm)$")
plt.ylabel(r"Absorbancia")
plt.title(r"Espectro de Absorción para la $\beta$ - clorofila")
plt.legend()
fig2.show()

plt.show()

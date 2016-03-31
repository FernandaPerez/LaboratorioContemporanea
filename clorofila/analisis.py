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

    r = [x[0] - 3, x[0] + 10]
    s = [x[1] - 10, x[1] + 3]

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

M1_Int = []
M2_Int = []

for fun in [T_b, T_a]:
    m1, m2 = maximos(L, fun)
    spl1 = UnivariateSpline(m1[0], m1[1])
    spl2 = UnivariateSpline(m2[0], m2[1])

    M1_Int.append(spl1)
    M2_Int.append(spl2)


plt.figure(1)
plt.plot(L, T_a, '.', color="deeppink")
plt.plot(L, M1_Int[0](L))

#plt.plot(L, gaussian(L, coef[0], coef[1], coef[2]))
plt.xlim(380,710)
plt.xlabel(r"$ \lambda  (nm)$")
plt.ylabel(r"Absorbancia")
plt.title(r"Espectro de Absorción para la $\alpha$ - clorofila")
plt.show()

plt.figure(2)
plt.plot(L, T_b, '.', color="crimson")
plt.xlim(380,710)
plt.xlabel(r"$ \lambda  (nm)$")
plt.ylabel(r"Absorbancia")
plt.title(r"Espectro de Absorción para la $\beta$ - clorofila")
plt.show()

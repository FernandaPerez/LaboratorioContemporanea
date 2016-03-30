from numpy import log10, ones_like, asarray, exp, cos
from scipy.optimize import curve_fit
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

def maximos(v):
    x_max = []
    y_max = []
    for i in range(len(v)-1):
        if (v[i+1] > v[i]) and (v[i+2] <= v[i+1]):
            x_max.append(i+1)
            y_max.append(v[i+1])

            print(i+1, v[i+1])
    mitad = int(len(y_max)/2)
    #print(mitad)

    y = [max(y_max[:mitad]), max(y_max[mitad:])]
    x = [x_max[y_max.index(y[0], 1, mitad)],  x_max[y_max.index(y[1], mitad, len(y_max))]]

    print(x,y)
    return asarray(x), asarray(y)



T_Met = absorbance(asarray(A_Metilico))
T_Ee = absorbance(asarray(E_Etilico))
T_Ep = absorbance(asarray(E_Petroleo))
T_a = absorbance(asarray(alpha))
T_b = absorbance(asarray(beta))
L = asarray(lamnda)

x,y = maximos(T_a)

r1 = x[1] - 3
r2 = x[1] + 3

XL = L[r1:r2]
YT = T_a[r1:r2]

mean = sum(YT)/len(YT)
sigma = sum((YT - mean)**2)/len(YT)

p = [1., mean, sigma]

coef, matriz = curve_fit(gaussian, XL, YT, p0 = p)
print(coef)

print(mean,sigma)


plt.figure(1)
plt.plot(L, T_a, '.', color="deeppink")
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
#plt.show()

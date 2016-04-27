#Técnicas de Vacío

## Contenido:
- programa `programa.f90` : calcula los intervalos temporales de la serie de datos obtenidos secuencialmente de uno de los videos de adquisición y los anexa en un nuevo archivo de salida. Es necesario hacer
 ```
 $ gfortran programa.f90
 ```
- Macro `fit.C`: fitea la curva de presión característica de un sistema de vacío para obtener el valor de la velocidad efecticva de bombeo. Es necesario tener la paquetería de análisis CERN-ROOT.
```
$ sudo apt-get install root
$ root -l fit.C
```


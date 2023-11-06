# Reto-Once
En esta oportunidad tenemos como reto solucionar los siguientes puntos:
### Punto 1:
Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#Desarrollar un programa para suma y resta de matrices.

def matriz(fil,colum):  #se definene las variables de la funcion
  m1 = [] # se crea una lista vacía para elmacenar los elementos de la matriz
  for i in range(fil):
    filas =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
    for j in range(colum):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
        filas.append(n) #se agregan los elementos de las filas
    m1.append(filas) #va almacenando todo dentro de la matriz
  return m1

def sumaMatrices(A, B):
  suma = [] #lista vacía para almacenar los elementos de la suma de matrices
  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    m = []
    for j in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
      m.append(A[i][j] + B[i][j]) #realiza la suma de los elementos en ambas matrices
        
    suma.append(m) #los resultados de la suma se agregan a la matriz resultante
  return suma

def restaMatrices(A, B):
  resta = [] #lista vacía para almacenar los elementos de la resta de matrices
  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    m = []
    for j in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
      m.append(A[i][j] - B[i][j]) #realiza la resta de los elementos en ambas matrices

    resta.append(m) #los resultados de la resta se agregan a la matriz resultante
  return resta
      
  

if __name__ == "__main__":  
  fil = int(input("Ingrese num de filas: ")) #se ingresa la cantidad de filas de la matriz
  colum = int(input("Ingrese num de columnas: ")) #se ingresa la cantidad de columnas de la matriz
  matrizA = matriz(fil,colum) #se evalúa la función para formar las matriz 1
  print("Matriz A: ")
  for i in range(len(matrizA)):
    print(matrizA[i])
  matrizB = matriz(fil,colum) #se evalúa la función para formar las matriz 2
  print("Matriz B: ")
  for i in range(len(matrizB)):
    print(matrizB[i]) 
  if len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0]): # se verifica que ambas matrices tengan el mismo número de filas y columnas
    suma = sumaMatrices(matrizA, matrizB) #se evalúa la función para restar las matrices
    resta = restaMatrices(matrizA, matrizB) #se evalúa la función para restar las matrices
    print("Sí se pueden realizar la suma y la resta de matrices")
    print("La suma de las matrices es: ")
    for i in range(len(suma)):
      print(suma[i])
    print("la resta de las matrices es: ")
    for i in range(len(resta)):
      print(resta[i])
  else:
    print("No se puede realizar la suma ni la resta de matrices")
```

### Punto 2:
Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
#2. Programa para calcular el producto de matrices

def matriz(fil,colum):  #se definenen las variables de la funcion
  m = [] # se crea una lista vacía para elmacenar los elementos de la matriz
  for i in range(fil):
    filas =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
    for j in range(colum):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
        filas.append(n) #se agregan los elementos de las filas
    m.append(filas) #va almacenando todo dentro de la matriz
  return m


def productoMatrices(A, B): #se definen los productos de la funcion
  producto = [] #lista vacía para almacenar los elementos de la matriz del producto
  for i in range(len(A)):
      producto.append([])
      for j in range(len(B[0])):
        producto[i].append(0)

  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    for j in range(len(B[0])):#toma cada uno de los elementos de las columnas de las matrices
      for k in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
       producto[i][j] += A[i][k] * B[k][j] #realiza la multiplicación de los elementos de las columnas de una matriz por las filas de la otra.
  return producto

if __name__ == "__main__":  
  fil = int(input("Ingrese num de filas: ")) #se ingresa la cantidad de filas de la matriz
  colum = int(input("Ingrese num de columnas: ")) #se ingresa la cantidad de columnas de la matriz
  matrizA = matriz(fil,colum) #se evalúa la función para formar las matriz 1
  print("Matriz A: ")
  for i in range(len(matrizA)):
    print(matrizA[i])
  matrizB = matriz(fil,colum) #se evalúa la función para formar las matriz 2
  print("Matriz B: ")
  for i in range(len(matrizB)):
    print(matrizB[i]) 
  if len(matrizA[0]) == len(matrizB): # se verifica que las colu,mnas de la matriz A sean iguales al  número de filas dede la matriz B
    product = productoMatrices(matrizA, matrizB) #se evalúa la función para multiplicar las matrices
    print("Sí se pueden realizar la suma y la resta de matrices")
    print("El producto de las matrices es: ")
    for i in range(len(product)):
      print(product[i])
  else:
    print("No se puede realizar la multiplicación de las matrices")
```

### Punto 3:
Desarrolle un programa que permita obtener la [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
#3. programa para obtener la matriz transpuesta

def matriz(fila,columna):  #se definenen las variables de la funcion
  m = [] # se crea una lista vacía para elmacenar los elementos de la matriz
  for i in range(fila):
    filas =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
    for j in range(columna):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
        filas.append(n) #se agregan los elementos de las filas
    m.append(filas) #va almacenando todo en la matriz
  
  return m

def matrizTranspuesta(A):
  transp = [] #lista vacía para almacenar los elementos de la suma de matriz transpuesta
  for i in range(len(A[0])): #toma cada uno de los elementos de las filas de la matriz
    transp.append([])
    for j in range(len(A)): #toma cada uno de los elementos de las columnas de la matricez
      transp[i].append(A[j][i]) #realiza el cambio de pocisión entre los elementos de las filas y columnas de la matriz

  return transp



if __name__ == "__main__":  
  fila = int(input("Ingrese numero de filas: ")) #se ingresa la cantidad de filas de la matriz
  columna = int(input("Ingrese numero de columnas: ")) #se ingresa la cantidad de columnas de la matriz
  matrizOriginal = matriz(fila,columna) #se evalúa la función
  print("M: ")
  for i in range(len(matrizOriginal)):
    print(matrizOriginal[i])
  maTranspuesta = matrizTranspuesta(matrizOriginal) #se evalúa la función para hacer la trnaspocisión de la matriz
  print("la matriz transpuesta es: ")
  for i in range(len(maTranspuesta)):
    print(maTranspuesta[i])
```

### Punto 4:
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
#4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

def matriz(filas, columnas):
    m = [] # se crea una lista vacía para elmacenar los elementos de la matriz
    for i in range(filas):
       fila =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
       for j in range(columnas):
           n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
           fila.append(n) #se agregan los elementos de las filas
       m.append(fila) #va almacenando todo en la matriz
  
    return m
    
    
def suma(matrizA:list, columna:int) -> float: # las entradas de la función son una lista y un entero, retorna un flotante
    sumaCol= sum(list(zip(*matrizA))[columna-1]) #En esta variable se realiza la suma de los elementos de la columna dada, para ello la matriz primero se transpone en orden.
    return sumaCol


if __name__ == "__main__":
    filas = int(input("ingrese el número de filas para la matriz: "))
    columnas = int(input("ingrese el número de columnas para la matriz: "))
    columna = int(input("ingrese la columna a sumar: "))
    matrizA= matriz(filas, columnas)
    print ("Matriz:")
    for i in range(len(matrizA)):
        print(matrizA[i])
        
    sumaColumna = suma(matrizA, columna)
    print("La suma de los elementos de la columna " + str(columna) + " es: ")
    print(sumaColumna)
```

### Punto 5:
Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
#5.Desarrollar un programa que sume los elementos de una fila dada de una matriz.

def matriz(filas, columnas):
    m = [] # se crea una lista vacía para elmacenar los elementos de la matriz
    for i in range(filas):
       fila =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
       for j in range(columnas):
           n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
           fila.append(n) #se agregan los elementos de las filas
       m.append(fila) #va almacenando todo en la matriz
  
    return m
    
    
def suma(matrizA:list, fila:int) -> float: # las entradas de la función son una lista y un entero, retorna un flotante
    sumaFil= sum(matrizA[fila-1]) #En esta variable se realiza la suma de los elementos de la columna dada.
    return sumaFil


if __name__ == "__main__":
    filas = int(input("ingrese el número de filas para la matriz: "))
    columnas = int(input("ingrese el número de columnas para la matriz: "))
    fila = int(input("ingrese la fila a sumar: "))
    matrizA= matriz(filas, columnas)
    print ("Matriz:")
    for i in range(len(matrizA)):
        print(matrizA[i])
        
    sumaFila = suma(matrizA, fila)
    print("La suma de los elementos de la fila " + str(fila) + " es: ")
    print(sumaFila)
```

### Listooooo :smile:

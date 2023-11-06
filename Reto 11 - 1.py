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
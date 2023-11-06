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
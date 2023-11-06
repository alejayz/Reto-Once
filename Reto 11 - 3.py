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
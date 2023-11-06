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
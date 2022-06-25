import pandas as pd

s1 = pd.Series([10,20,10]) #Creación de la Serie 1
s2 = pd.Series(["rojo","verde","azul"]) # Creación de la Serie 2

#Creación del dataframe df
df = pd.DataFrame(
  {
    "A":s1, #Asignamos la serie 1 a la columna 1 llamada "A"
    "B":s2, #Asignamos la serie 2 a la columna 2 llamada "B"
  }
)

#Leer el archivo avengers.csv y lo asignamos al dataframe avengers
avengers = pd.read_csv("./src/pandas/avengers.csv")

#Mostramos las 5 primeras filas
print(avengers.head())

#Mostramos las 10 primeras filas
print(avengers.head(10))

#Mostramos las 5 últimas filas
print(avengers.tail(5))

#Mostrar el tamaño del dataframe
print("\nEl tamaño del dataframe es: " + str(avengers.size)+"\n")

#Mostrar los datatypes
print(avengers.dtypes)

#Editar el índice
avengers = avengers.sort_values(by="fecha_inicio")
print(avengers)

#Ordenar el índice de forma descendiente
avengers = avengers.sort_index(ascending=False)
print(avengers)

#Resetear el índice
avengers = avengers.reset_index()
print(avengers)
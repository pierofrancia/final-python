import pandas as pd
import matplotlib.pyplot as plt

df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")

#CASO 1
#Filtramos por el número de cuartos, el número de opiniones y la puntuación del cuarto
df_caso1 = df_airbnb.query(
    '(bedrooms == 4) & (reviews > 10) & (overall_satisfaction > 4)')

#Ordenamos por la puntuación y el número de opiniones
df_caso1 = df_caso1.sort_values(
    by=["overall_satisfaction", "reviews"], ascending=False)

#Mostramos el top 3
print(df_caso1.head(3))

#CASO 2
#Filtramos las habitaciones de Roberto y Clara
df_caso2 = df_airbnb.query('(room_id == 97503) | (room_id == 90387)')

#Mostramos el resultado
print(df_caso2)

#Guardamos el dataframe en un excel
df_caso2.to_excel('roberto.xlsx')

#CASO 3
#Filtramos por el precio y el tipo de habitación
df_caso3 = df_airbnb.query('(price <= 50) & (room_type == "Shared room")')

#Ordenamos por las habitaciones más baratas y mejor calificadas
df_caso3 = df_caso3.sort_values(by=["price", "overall_satisfaction"],ascending=[True,False])

#Mostramos las 10 habitaciones más baratas
print(df_caso3.head(10))

#Gráfico circular por tipo de habitación
plot = df_airbnb.groupby('room_type')['room_type'].count().plot(kind='pie')

#Mostramos el gráfico
plt.show()

import mysql.connector
import json
from prettytable import PrettyTable

with open('/app/config.json') as f:
    config = json.load(f)

mydb = mysql.connector.connect(**config)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM coches")
resultados = cursor.fetchall()

tabla = PrettyTable()
# Definimos los títulos de las columnas
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "Kilometraje", "Precio"]

for c in resultados:
    # Añadimos una fila por cada coche
    tabla.add_row([c[0], c[1], c[2], c[3], c[4], c[5]])

print("\n")
print(tabla)
print("\n")

mydb.close()
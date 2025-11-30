import mysql.connector
import json

with open('/app/config.json') as f:
    config = json.load(f)

mydb = mysql.connector.connect(**config)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM coches")
resultados = cursor.fetchall()

print("\n--- LISTADO DE COCHES (Desde JSON) ---")
print(f"{'ID':<5} {'MARCA':<15} {'MODELO':<15} {'COLOR':<10} {'KM':<10} {'PRECIO':<10}")
print("-" * 75)

for c in resultados:
    print(f"{c[0]:<5} {c[1]:<15} {c[2]:<15} {c[3]:<10} {c[4]:<10} {c[5]:<10}")

print("\n")
mydb.close()
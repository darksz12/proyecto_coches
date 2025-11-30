import mysql.connector

# Conexión a la base de datos
mydb = mysql.connector.connect(
  host="mi_mysql",       # Nombre del contenedor MySQL
  user="root",           # Usuario
  password="secret",     # Contraseña que pusimos antes
  database="concesionario"
)

cursor = mydb.cursor()

# Ejecutamos la consulta
cursor.execute("SELECT * FROM coches")
resultados = cursor.fetchall()

# Imprimimos la cabecera bonita
print("\n")
print(f"{'ID':<5} {'MARCA':<15} {'MODELO':<15} {'COLOR':<10} {'KM':<10} {'PRECIO':<10}")
print("-" * 75)

# Imprimimos cada coche
for coche in resultados:
    # coche[0] es ID, coche[1] es Marca, etc.
    print(f"{coche[0]:<5} {coche[1]:<15} {coche[2]:<15} {coche[3]:<10} {coche[4]:<10} {coche[5]:<10}")

print("\n")

# Cerramos conexión
mydb.close()
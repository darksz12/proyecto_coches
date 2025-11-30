import pymongo
from prettytable import PrettyTable

client = pymongo.MongoClient("mongodb://mongo_nube:27017/")

db = client["concesionario"]
coleccion = db["coches"]

tabla = PrettyTable()
tabla.field_names = ["Marca", "Modelo", "Color", "KM", "Precio"]

print("\n--- COCHES DESDE MONGODB ---")
for coche in coleccion.find():
    tabla.add_row([
        coche['marca'], 
        coche['modelo'], 
        coche['color'], 
        coche['km'], 
        coche['precio']
    ])

print(tabla)
print("\n")
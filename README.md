# Proyecto Docker: Gestión de Concesionario

**Alumno:** Marcos Valero Báscones

## Descripción
Este proyecto despliega un entorno contenerizado para gestionar una base de datos de coches utilizando **MySQL** y **MongoDB**, interactuando con ellos mediante scripts de **Python**.

## Tecnologías usadas
* Docker & Docker Hub
* Python (mysql-connector, pymongo, prettytable)
* MySQL 8.0
* MongoDB
* Git & GitHub

## Retos Completados

### Reto 1-3: Entorno y Git
* Creada imagen personalizada de Ubuntu con Python.
* Configurado volumen (Bind Mount) en `/app`.
* Repositorio conectado a GitHub.

### Reto 4-7: MySQL y Python
* Base de datos `concesionario` creada.
* Script de conexión seguro (lectura desde `config.json`).
* Visualización de datos con `PrettyTable`.

### Reto 8-9: MongoDB y Docker Hub
* Implementación de base de datos NoSQL.
* Imagen personalizada subida a Docker Hub: `darksens05/mongo-concesionario:v1`
* Despliegue simulado descargando la imagen desde la nube.

## Cómo ejecutar el proyecto

1. **Configuración:**
   Crear un archivo `config.json` con los datos de conexión a MySQL.

2. **Ejecución MySQL:**
   ```bash
   docker exec -w /app -it mi_python python3 reto7.py
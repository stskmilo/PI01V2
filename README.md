# Proyecto Individual 1- Data 03- Soy Henry   
## Creación de una API
### Camilo Cook


# Version 2

A partir de datasets en formatos JSON y CSV se creó un API para responder a las siguientes preguntas:

- Año con más carreras
- Piloto con mayor cantidad de primeros puestos
- Nombre del circuito más corrido
- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
Adicionalmente, se retorna un dataset con los datos de los distintos pilotos /tabla/pilotos

# Update 15-09-2022
- Añadido retorno de tablas:
    - /tabla/circuitos
    - /tabla/constructores
    - /tabla/carreras
    - /tabla/campeones
    - /tabla/pilotos
    - /PILOTO/wins : mostrará búsqueda de victoria de piloto indicado. Ver /tabla/pilotos para obtener posibles valores. Podrán indicar nombre incompleto. Ej: /mi/wins traerá a las victorias de "MI"chael Schumacher y ha"MI"lton

El deployment fue realizado de forma local con una base de datos MySQL y un servidor ASGI mediante el uso de FastAPI y Uvicorn


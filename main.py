from fastapi import FastAPI
import respuestas
import uvicorn

app = FastAPI(title='PI01',
            description='Primer proyecto individual',
            version='2.0.0')

@app.get('/')
async def index():
    prueba = {'Pregunta 1': 'Año con más carreras',
            'Pregunta 2': 'Piloto con mayor cantidad de primeros puestos',
            'Pregunta 3': 'Nombre del circuito más corrido',
            'Pregunta 4': 'Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British'}
    return prueba

@app.get('/pregunta/{id}')
async def respuesta(id):
    return respuestas.respuesta(id)

@app.get('/tabla/pilotos')
async def pilotos():
    return respuestas.pilotos()

@app.get('/tabla/circuitos')
async def circuitos():
    return respuestas.circuitos()

@app.get('/tabla/constructores')
async def constructores():
    return respuestas.constructores()

@app.get('/tabla/carreras')
async def carreras():
    return respuestas.carreras()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

#Iniciar el server: uvicorn main:app --reload

@app.get("/")
async def read_root():
    return {"Hello": "World", "url_curso":"https://renatocuellar.com"}

@app.get("/url")
async def read_root():
    return {"url_curso":"https://renatocuellar.com"}

#Documentación con Swagger: http://127.0.0.1:8000/docs
#Documentación con Redocly: http://127.0.0.1:8000/redoc

"""
Para APIs puedo usar operaciones o metodos HTTP

- POST @app.post()
- GET  @app.get()
- PUT  @app.put()
- DELETE  @app.delete()

- OPTIONS  @app.options()
- HEAD  @app.head()
- PATCH  @app.patch()
- TRACE  @app.trace()
"""


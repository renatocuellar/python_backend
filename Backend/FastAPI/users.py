from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Iniciar el server: uvicorn users:app --reload

"""
@app.get("/usersjson")
async def usersjson():
    return [{"Name": "Renato", "Surname":"Cuéllar", "url":"https://renatocuellar.com"},
            {"Name": "Teffy", "Surname":"Valencia", "url":"https://sthephanievalencia.com"},
            {"Name": "Matías", "Surname":"Hernández", "url":"https://matihernan.com"},
            {"Name": "Angie", "Surname":"Rojas", "url":"https://angierojas.com"},
            {"Name": "Carlos", "Surname":"Hernández", "url":"https://carloshernandez.com"}]
"""
# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Renato", surname="Cuéllar", url="https://renatocuellar.com", age= 35),
                        User(name="Teffy", surname="Valencia", url="https://sthephanievalencia.com", age= 36),
                        User(name="Matías", surname="Hernández", url="https://matihernan.com", age= 10),
                        User(name="Angie", surname="Rojas", url="https://angierojas.com", age= 31),
                        User(name="Carlos", surname="Hernández", url="https://carloshernandez.com", age= 34),]

@app.get("/users")
async def users():
    return users_list

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World", "url_curso":"https://renatocuellar.com"}

@app.get("/url")
async def read_root():
    return {"url_curso":"https://renatocuellar.com"}
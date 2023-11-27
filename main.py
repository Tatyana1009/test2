from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Кузнецова Татьяна Алексеевна"}

@app.get('/tools')
async def f_indexT():
    return "Начальные навыки разработчика"

@app.get('/users')
async def f_indexU():
    return "+79130001234"
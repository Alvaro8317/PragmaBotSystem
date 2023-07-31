from fastapi import FastAPI
# from . import tasks
from persistence import test
app = FastAPI()

# Agregar las rutas definidas en el módulo tasks.py al enrutador principal
# app.include_router(tasks.router)
print(test())
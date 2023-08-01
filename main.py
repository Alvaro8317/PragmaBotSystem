from fastapi import FastAPI
from persistence import DatabaseConnection
app = FastAPI()

database = DatabaseConnection()
database.connect()
database.show_databases()
database.disconnect()
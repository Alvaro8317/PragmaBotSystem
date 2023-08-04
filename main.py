from fastapi import FastAPI
from persistence import DatabaseConnection
from helpers import ensure_logs_directory

ensure_logs_directory()
if __name__ == "__main__":
    app = FastAPI()
    database = DatabaseConnection()
    database.show_databases()
    database.disconnect()

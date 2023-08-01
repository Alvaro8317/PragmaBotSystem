from pymongo import MongoClient
from configuration import *

class DatabaseConnection:
    MONGODB_URI = f"mongodb+srv://{db_user}:{db_password}@{db_cluster}/?retryWrites=true&w=majority"
    client = None
    def __init__(self) -> None:
        pass

    def connect(self):
        self.client = MongoClient(self.MONGODB_URI)
        print("Connected")

    def show_databases(self):
        for db_name in self.client.list_database_names():
            print(db_name)

    def disconnect(self):
        self.client.close()
        print("Disconnected")
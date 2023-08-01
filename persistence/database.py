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

    def get_context(self):
        return "Take the context"

    def post_a_context(self):
        return "Posted"

    def update_a_context(self, id):
        return f"Updated the context with the id: {id}"
    
    def delete_a_context(self, id):
        return f"Deleted the context with the id: {id}"

    def show_databases(self):
        for db_name in self.client.list_database_names():
            print(db_name)

    def disconnect(self):
        self.client.close()
        print("Disconnected")

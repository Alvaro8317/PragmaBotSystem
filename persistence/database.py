from pymongo import MongoClient, errors
from pymongo.errors import OperationFailure
from configuration import *
from helpers import *


class DatabaseConnection:
    MONGODB_URI = f"mongodb+srv://{db_user}:{db_password}@{db_cluster}/?retryWrites=true&w=majority"
    client = None

    def __init__(self) -> None:
        try:
            self.client = MongoClient(self.MONGODB_URI)
            log_info("Conected to the database")
            print("Conected to the database successfully")
        except OperationFailure as e:
            print("Captured")
            log_exception(e)

    def reconnect(self):
        try:
            self.client = MongoClient(self.MONGODB_URI)
            print("Connected")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_context(self, id):
        return f"Take the context with the id: {id}"

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

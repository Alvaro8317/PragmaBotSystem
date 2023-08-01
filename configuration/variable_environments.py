import os
from dotenv import load_dotenv
load_dotenv()

db_cluster = os.getenv('MONGO_CLUSTER')
db_user = os.getenv('MONGO_USER')
db_password = os.getenv('MONGO_PASS')
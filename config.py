import os

class Config:
    SECRET_KEY = 'chiave_segreta_di_esempio'  # In produzione, usare una chiave segreta più sicura
    SQLITE_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
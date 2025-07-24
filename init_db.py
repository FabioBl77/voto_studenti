import sqlite3
import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db():
    db = sqlite3.connect(app.config['SQLITE_DB_PATH'])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())
    db.commit()
    print('Database inizializzato con successo!')

if __name__ == '__main__':
    # Verifica se il database esiste già
    if os.path.exists(app.config['SQLITE_DB_PATH']):
        # Se esiste, lo elimina per ricrearlo da zero
        os.remove(app.config['SQLITE_DB_PATH'])
        print(f"Database esistente rimosso: {app.config['SQLITE_DB_PATH']}")
    
    # Inizializza il database
    init_db()
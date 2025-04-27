import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'db')
    DB_NAME = os.getenv('POSTGRES_DB', 'todo_db')
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
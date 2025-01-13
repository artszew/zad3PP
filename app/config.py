#Zawiera konfigurację aplikacji (np. URI do bazy danych, klucz tajny).
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost/db_name")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

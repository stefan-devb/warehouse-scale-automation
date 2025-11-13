import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///warehouse.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5001


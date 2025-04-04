import os
import psycopg2
from psycopg2 import OperationalError
import logging
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
load_dotenv()

class PostgresDB:
    _instance = None

    # Database Configuration
    _db_config = {
        "user": "postgres",
        "password": "123456789",
        "host": "localhost",
        "port": "5432",
        "database": "data_integration"
    }

    def __new__(cls):
        if cls._instance is None:
            try:
                cls._instance = super().__new__(cls)
                '''cls._instance.connection = psycopg2.connect(
                    user=cls._db_config["user"],
                    password=cls._db_config["password"],
                    host=cls._db_config["host"],
                    port=cls._db_config["port"],
                    database=cls._db_config["database"]
                )'''
                cls._instance.connection = psycopg2.connect(
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    database=os.getenv("DB_NAME")
                )
                cls._instance.connection.autocommit = False
                logging.info("Database connection established successfully")
            except OperationalError as e:
                logging.error("Error connecting to PostgreSQL: %s", e)
                raise
        return cls._instance

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed")

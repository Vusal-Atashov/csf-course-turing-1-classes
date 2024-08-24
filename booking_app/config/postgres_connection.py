import os
from psycopg2 import connect, OperationalError
from dotenv import load_dotenv

load_dotenv('/Users/macbook/Desktop/Development/csf-course-turing-1-classes/booking_app/resources/.env')

def connect_to_database():
    try:
        conn = connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Connected to the database")
        return conn
    except OperationalError as e:
        print(f"Database connection error: {e}")
        return None



'''import psycopg2

def insert_data(data_list):
    insert_query = """
    INSERT INTO public.unified_data(name, "timestamp", category, source_type) VALUES (%s, %s,%s, %s);
    """
    cursor.executemany(insert_query, data_list)
    conn.commit()'''


import logging
from psycopg2 import sql, Error
from psycopg2.extras import execute_batch
from app.extraction.db_operations.psy_conn_db import PostgresDB

logging.basicConfig(level=logging.INFO)


class DataInserter:
  def __init__(self):
    self.connection = PostgresDB()

  def insert_record(self, records):
    insert_query = sql.SQL("""
                INSERT INTO employee_data (
                    name,
                    organization,
                    email,
                    department,
                    role,
                    hire_date,
                    salary,
                    source_type,
                    timestamp,
                    extra_data
                )
                VALUES (
                    %(name)s,
                    %(organization)s,
                    %(email)s,
                    %(department)s,
                    %(role)s,
                    %(hire_date)s,
                    %(salary)s,
                    %(source_type)s,
                    %(timestamp)s,
                    %(extra_data)s
                );
            """)

    try:
      conn = self.connection.get_connection()
      cursor = conn.cursor()
      #cursor.executemany(insert_query, records)
      execute_batch(cursor,insert_query,records, page_size=1000)
      conn.commit()
      logging.info("Record inserted successfully")
    except Error as e:
      conn.rollback()
      logging.error("Insertion failed: %s", e)
    except Exception as e:
      conn.rollback()
      logging.error(e)  
    finally:
      if cursor:
        cursor.close()
      if conn:
        self.connection.close_connection()
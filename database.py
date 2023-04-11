from sqlalchemy import create_engine, text
import os


db_connection_string= os.environ['DB_CONNECTION_STRING']




engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })


def load_products_from_db():
    with engine.connect() as conn:
      
      result = conn.execute(text("SELECT * FROM products"))
      rows = result.fetchall()
      column_names = result.keys()
      products = [dict(zip(column_names, row)) for row in rows]
      return products



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

def load_product_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM products WHERE id= :val"), {"val": id})
    rows = result.fetchall()
    column_names = result.keys()
    products = [dict(zip(column_names, row)) for row in rows]
    if len(rows) == 0:
      return None
    else:
      return products[0]
    
def adding_users_to_the_db(Form):
    with engine.connect() as conn:
        query = text("INSERT INTO users (username,email,password,password_confirmation) VALUES (:username, :email, :password, :password_confirmation)")

        conn.execute(query, {
            'username': Form.username.data,
            'email': Form.email.data,
            'password': Form.password.data,
            'password_confirmation': Form.password_confirmation.data
        })
'''''def get_user_by_email(email):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users WHERE email= :email"), {"email": email})
    row = result.fetchone()
    if row:
      column_names = result.keys()
      user = dict(zip(column_names, row))
      return user
    else:
      return None
'''''

def get_user_by_email(email):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT password FROM users WHERE email = :email"), {"email": email})
        password = result.scalar()
        return password if password else None

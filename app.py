from flask import Flask, render_template, jsonify
from database import load_products_from_db,load_product_from_db


app = Flask(__name__)

@app.route("/")
def hello_world():
  products = load_products_from_db()
  return render_template('home.html',products=products)

@app.route("/api/products")
def list_products():
  products = load_products_from_db()
  return jsonify(products)

@app.route("/product/<id>")
def show_product(id):
  product = load_product_from_db(id)
  if not product:
    return "Not Found",404
  return render_template('productpage.html',product=product)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
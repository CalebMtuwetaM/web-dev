from flask import Flask, render_template, jsonify
app = Flask(__name__)
Products = [
  {
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },
  {
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },
  {
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },
  {
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },
  {
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },
  {
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },{
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },{
    'name': 'Wrist watch',
    'Description': 'New',
    'Price': 'ksh 1500'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html',products=Products)

@app.route("/api/products")
def list_products():
  return jsonify(Products)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
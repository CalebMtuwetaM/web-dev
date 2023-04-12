from flask import Flask, render_template, jsonify,url_for,flash,redirect
from database import load_products_from_db,load_product_from_db,adding_users_to_the_db
from forms import RegistrationForm,LoginForm

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
from flask_wtf.csrf import CSRFProtect


app.config['SECRET_KEY'] = 'your_secret_key_here' # Set your secret key here
csrf = CSRFProtect(app)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("hello_world"))
    return render_template('register.html', title='Register', form=form)
    adding_users_to_the_db(form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('hello_world'))
        else:
            flash('Login unsuccessful. Please check username and password','danger')
    return render_template("login.html",title="Login",form=form)



if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
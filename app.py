from flask import Flask, render_template, jsonify,url_for,flash,redirect,session
from database import load_products_from_db,load_product_from_db,adding_users_to_the_db,get_user_by_email
from forms import RegistrationForm,LoginForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import check_password_hash


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



app.config['SECRET_KEY'] = 'Gratia_Premium' # Set your secret key here
csrf = CSRFProtect(app)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    Form = form
    adding_users_to_the_db(Form)
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("hello_world"))
      
    return render_template('register.html', title='Register', form=form)
    

@app.route("/login", methods=['GET','POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        entered_password = form.password.data

        # Retrieve the stored password from the database
        stored_password = get_user_by_email(email)

        if stored_password == entered_password:
            # Passwords match
            #session['user_id'] = user.id
            flash('You have been logged in!', 'success')
            return redirect(url_for('products'))
        else:
            # Passwords don't match
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)



@app.route("/products")
def products():
  products = load_products_from_db()
  return render_template("products.html",products=products)

@app.route("/admin")
def admin():
  return render_template("admin.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
  
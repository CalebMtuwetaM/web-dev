Website Project with Flask, MySQL, and Bootstrap
This is a website project built with Flask framework for the backend, Python for the server-side logic, HTML, CSS, and Bootstrap for the frontend, and a MySQL database to store user accounts and product records.

Features
User Authentication:

Login Page: Users can log in to their accounts.
Registration Page: New users can create an account.
User Dashboard:

Upon logging in, users can access their personalized dashboard.
Users can view and edit their profile information.
Product Management:

Users can add, edit, and delete products.
Products are stored in the MySQL database.
Search and Filter:

Users can search for products by name or category.
Filters are available to narrow down product listings.
Prerequisites
Before running the application, make sure you have the following installed:

Python
Flask
MySQL Server
Bootstrap
HTML/CSS knowledge
Getting Started
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-project.git
cd your-project
Install the Python dependencies:

bash
Copy code
pip install -r requirements.txt
Create a MySQL database and update the config.py file with your database credentials:

python
Copy code
# config.py

DATABASE_URI = "mysql://username:password@localhost/database_name"
Create the necessary database tables by running:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Start the Flask application:

bash
Copy code
flask run
Access the website in your browser at http://localhost:5000.

Folder Structure
app: Contains the Flask application and routes.
templates: HTML templates for rendering web pages.
static: CSS files, images, and other static assets.
models: Defines the database models.
migrations: Database migration files.
config.py: Configuration settings for the application.
requirements.txt: List of Python dependencies.
Usage
Visit http://localhost:5000 to access the website.
Register an account or log in to an existing account.
Use the dashboard to manage products and update your profile information.
Contributing
Feel free to contribute to this project by opening issues or pull requests. Your contributions are highly appreciated!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Flask, Python, Bootstrap, and MySQL for making this project possible.
Special thanks to the open-source community for their contributions and support.
Happy coding! 🚀# Gratia Shopping
This is a professional Website I have made for Gratia shopping 

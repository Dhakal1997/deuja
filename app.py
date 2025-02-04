from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




@app.route("/")
def index():
    with open('data.json') as data_file:
        data = json.load(data_file)
    return render_template("index.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
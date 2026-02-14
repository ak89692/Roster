from flask import Blueprint, render_template, url_for, request
from database.db import collection
home_bp = Blueprint('home',__name__)

@home_bp.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        email = request.form['email']
        name = request.form['name']
        collection.insert_one({'name':name,'email':email})
        print(email,name)
        return render_template('home.html')
    else:
        name = "Amit"
        print(url_for('static',filename='css/style.css'))
        
        return render_template('home.html')
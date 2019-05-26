import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = 'some_secret' 
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] ='mongodb://dude:h310db@ds149706.mlab.com:49706/cook_book'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_tasks():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
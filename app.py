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
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addRecipe.html",
    seasons=mongo.db.seasons.find(),
    difficulties=mongo.db.difficulties.find(),
    types=mongo.db.types.find())
    
    
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipe=mongo.db.recipes
    ingredients_needed=request.form.getlist('ingredients')
    recipe_form_fields = {
        'recipe_name':request.form['name_of_recipe'],
        'author':request.form['author'],
        'season':request.form['season'],
        'serves': request.form['serves'],
        'type': request.form['type'],
        'difficulty':request.form['difficulty'],
        'prep_time': request.form['prep_time'],
        'rating':request.form['rating'],
        'image_url': request.form['image_url'],
        'ingredients': ingredients_needed,
        'method': request.form['method']
    }
    recipe.insert_one(recipe_form_fields)
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import json 
from bson import json_util
from bson.json_util import dumps

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
    flash("Recipe ADDED! Thank you")
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
        'rating':int(request.form['rating']),
        'image_url': request.form['image_url'],
        'ingredients': ingredients_needed,
        'method': request.form['method']
    }
    recipe.insert_one(recipe_form_fields)
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    seasons_collection=mongo.db.seasons.find()
    difficulties_collection=mongo.db.difficulties.find()
    types_collection=mongo.db.types.find()
    
    return render_template('editRecipe.html', 
                            recipe=the_recipe, 
                            seasons=seasons_collection,
                            difficulties=difficulties_collection,
                            types=types_collection)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    flash("Recipe UPDATED! Thank you")
    recipe=mongo.db.recipes
    ingredients_needed=request.form.getlist('ingredients')
    recipe.update_one( {'_id': ObjectId(recipe_id)}, 
    {'$set':
        {
        'recipe_name':request.form['name_of_recipe'],
        'author':request.form['author'],
        'season':request.form['season'],
        'serves': request.form['serves'],
        'type': request.form['type'],
        'difficulty':request.form['difficulty'],
        'prep_time': request.form['prep_time'],
        'rating': int(request.form['rating']),
        'image_url': request.form['image_url'],
        'ingredients': ingredients_needed,
        'method': request.form['method']
        }
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    flash("DELETED! Maybe now you should add one")
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

# search by season

@app.route('/get_spring')
def get_spring():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"season" : "Spring"}))
    
@app.route('/get_summer')
def get_summer():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"season" : "Summer"}))
    
@app.route('/get_autumn')
def get_autumn():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"season" : "Autumn"}))  
    
@app.route('/get_winter')
def get_winter():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"season" : "Winter"}))

# search by difficulty
@app.route('/get_easy')
def get_easy():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"difficulty": "Easy"}))  
    
@app.route('/get_medium')
def get_medium():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"difficulty": "Medium"}))

@app.route('/get_hard')
def get_hard():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"difficulty": "Hard"}))

# search by type
@app.route('/get_vegetarian')
def get_vegetarian():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"type" : "Vegetarian"}))  
    
@app.route('/get_with_meat')
def get_with_meat():
    return render_template('filteredRecipes.html',
    recipes=mongo.db.recipes.find({"type" : "With meat"}))

# search by popularity    
    
@app.route('/less_popular')
def less_popular():
    return render_template('filteredRecipes.html',
   recipes=mongo.db.recipes.find( { '$query': {"rating": {'$lt': 4 }}, '$orderby': { 'rating' : -1 } } ))
   
@app.route('/most_popular')
def most_popular():
    return render_template('filteredRecipes.html',
   recipes=mongo.db.recipes.find( { '$query': {"rating": {'$gt': 3 }}, '$orderby': { 'rating' : -1 } } ))
   
   
   
@app.route('/data_chart')
def data_chart():

    data_labels=[]
    data = []
    spring_recipes_number = mongo.db.recipes.count({"season": "Spring"})
    summer_recipes_number = mongo.db.recipes.count({"season": "Summer"})
    autumn_recipes_number = mongo.db.recipes.count({"season": "Autumn"})
    winter_recipes_number = mongo.db.recipes.count({"season": "Winter"})
    data.extend([spring_recipes_number,spring_recipes_number,autumn_recipes_number,winter_recipes_number])
    
    seasons_collection=mongo.db.seasons.find()
    
    
    for season in seasons_collection:
        label = season["season"]
        data_labels.append(label) 
        
    print(data)
    print(data_labels)

    return render_template('dataChart.html', data_labels=data_labels, data=data)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    
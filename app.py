import os
import math
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:0t0rin0laring0l0gija@myfirstcluster-ol1er.mongodb.net/cook_book?retryWrites=true&w=majority')
app.config['SECRET_KEY'] = os.urandom(24)
mongo = PyMongo(app)

""" Variables """
users = mongo.db.users
recipe = mongo.db.recipes
recipes = mongo.db.recipes
cuisine = mongo.db.cuisine
dishes = mongo.db.dishes
allergens = mongo.db.allergens

@app.route('/')

def index():
    # Pagination function
    page_limit = 6
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.Recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.DESCENDING).skip(
                            (current_page - 1)*page_limit).limit(page_limit)

    return render_template("index.html", recipe=recipes, pages=pages,
                           current_page=current_page)

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
                           recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipes
    recipe.insert_one({'recipe_title': request.form['recipe_title'],
                       'recipe_description': request.form['recipe_description'],
                       'serves': request.form['serves'],
                       'food_type': request.form['food_type'],
                       'cuisine': request.form['cuisine'],
                       'calories': request.form['calories'],
                       'food_type': request.form['food_type'],
                       'cook_time': request.form['cook_time'],
                       'ingredients': request.form.getlist('ingredients'),
                       'steps': request.form.getlist('steps'),
                       'allergens': request.form.getlist('allergens'),
                       # Lists for Ingredients and Method to store in an array.
                       'upload_image': request.form['upload_image']})
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template("edit_recipe.html", cuisine=cuisine.find(),
            recipe=recipes.find_one({"_id": ObjectId(recipe_id)}))


@app.route('/the_recipe/<recipe_id>/<recipe_title>')
def the_recipe(recipe_id, recipe_title):
    return render_template("the_recipe.html",
            recipe=recipes.find_one({'_id': ObjectId(recipe_id),
            'recipe_title': recipe_title}))


""" Removes a recipe from MongoDB """
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes')) 


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
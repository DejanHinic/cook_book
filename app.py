import os
import math
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:0t0rin0laring0l0gija@myfirstcluster-ol1er.mongodb.net/cook_book?retryWrites=true&w=majority')
app.config['SECRET_KEY'] = os.urandom(24)
mongo = PyMongo(app)

# """ Variables """
users = mongo.db.users
recipes = mongo.db.recipes
allergens = ['Gluten', 'Milk', 'Eggs', 'Mullosc', 'Fish', 'Soyabeans', 'Peanuts', 'Nuts', 'Celery', 'Mustard', 'Sesame seeds', 'Sulphur dioxide and sulphites', 'Lupin','Crustaceans']


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template("index.html")
    
# logging to account (still have issues)
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'
# send reg info to database
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/')
def pages():
    # Pagination function
    page_limit = 6
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.DESCENDING).skip(
                            (current_page - 1)*page_limit).limit(page_limit)

    return render_template("recipes.html", recipe=recipes, pages=pages,
                           current_page=current_page)

# CRUD operations

# get data
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
                           recipes=mongo.db.recipes.find())
# add data
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')
# add recipe
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
                       'prep_time': request.form['prep_time'],
                       'ingredients': request.form.getlist('ingredients'),
                       'steps': request.form.getlist('steps'),
                       'allergens': request.form.getlist('allergens'),
                       # Lists for Ingredients and Method to store in an array.
                       'upload_image': request.form['upload_image']})
    return redirect(url_for('get_recipes'))

# get and edit data to sent back to database

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template("edit_recipe.html",allergens = allergens,
            recipe=recipes.find_one({"_id": ObjectId(recipe_id)}))

# Send form data to update recipe in MongoDB

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes.update( {'_id': ObjectId(recipe_id)},
        { 
            '$set' :{
                'recipe_title' :request.form.get('recipe_title'),
                'recipe_description' :request.form.get('recipe_description'),
                'serves' : request.form.get('serves'),
                'food_type' : request.form.get('food_type'),
                'cuisine' :request.form.get('cuisine'),
                'calories' :request.form.get('calories'),
                'food_type' :request.form.get('food_type'),
                'cook_time' :request.form.get('cook_time'),
                'ingredients' :request.form.getlist('ingredients'),
                'steps' :request.form.getlist('steps'),
                'allergens' :request.form.getlist('allergens'),
                'upload_image' :request.form.get('upload_image')
            }
        })
    return redirect(url_for('get_recipes'))

# recipe info
@app.route('/the_recipe/<recipe_id>/<recipe_title>')
def the_recipe(recipe_id, recipe_title):
    return render_template("the_recipe.html",
            recipe=recipes.find_one({'_id': ObjectId(recipe_id),
            'recipe_title': recipe_title}))


# Removes a recipe from MongoDB
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)

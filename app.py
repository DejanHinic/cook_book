import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:0t0rin0laring0l0gija@myfirstcluster-ol1er.mongodb.net/cook_book?retryWrites=true&w=majority')
mongo = PyMongo(app)


@app.route('/')
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
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
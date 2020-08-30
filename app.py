import os
from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get('MyTestDB')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index_recipe')
def index_recipe():

    return render_template('index.html')


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html"), 404


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    Checks first in the database if username exist.
    Then matches username and password and returns
    to index Page. If not then show a flash message.
    A variable login_page=True is passed to set if statement
    to hide nav buttons on login page.
    """
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username':
                                    request.form['username'].lower()})
        if login_user:
            if bcrypt.hashpw(request.form['pasword'].encode('utf-8'),
                             login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index_recipe'))
        flash("Invalid username / password. Please try again.")
    return render_template('login.html', login_page=True)


@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    Check first in the database if username exist.
    If yes, show flash message. If not, let
    user to register. A variable login_page=True is passed
    to set if statement to hide nav buttons on register page.
    """
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username':
                                        request.form.get('username').lower()})
        if existing_user is None:
            hash_password = bcrypt.hashpw(
                request.form['pasword'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': request.form['username'],
                             'password': hash_password})
            session['username'] = request.form['username']
            return redirect(url_for('index_recipe'))
        flash('Username already exists')
    return render_template('register.html', login_page=True)


@app.route('/logout')
def logout():
    """Logs out the user and pops session"""
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index_recipe'))


# Search function
@app.route('/search_recipe', methods=['POST'])
def search_recipe():
    search_recipes = request.form.get("search_recipes")
    #  i could put this in main to not create every time. i leave it to future.
    mongo.db.recipe.create_index([("$**", 'text')])
    # search with the names
    recipe = mongo.db.recipe.find({"$text": {"$search": search_recipes}})
    return render_template('recipes.html', recipe=recipe, search=True)


@app.route('/get_recipes')
def get_recipes():
    """
    ......... Get the recipes from database and render them
    ......... on recipes.html page.
    """
    return render_template('recipes.html', recipe=mongo.db.recipe.find())


# recipe page loged in as user
@app.route('/my_recipes')
def my_recipes():
    recipe = mongo.db.recipe.find({"recipe_author": session["username"]})
    return render_template('recipes.html', recipe=recipe, my_recipes=True)


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           cuisines=mongo.db.cuisines.find()
                           .sort("recipe_cuisine"),
                           maketime=mongo.db.maketime.find(),
                           recipetype=mongo.db.recipetype.find()
                           .sort("recipe_type"),
                           serving=mongo.db.serving.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """
    Add the user's inserted data in the database and redirect
    the user to recipes.html (get_recipe route) showing a flash message.
    """
    recipe = mongo.db.recipe
    recipe.insert_one(
        {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('recipe_description'),
            'recipe_ingredients': request.form.get('recipe_ingredients'),
            'recipe_preparation': request.form.get('recipe_preparation'),
            'recipe_cuisine': request.form.get('recipe_cuisine'),
            'making_time': request.form.get('making_time'),
            'recipe_type': request.form.get('recipe_type'),
            'recipe_serving': request.form.get('recipe_serving'),
            'recipe_author': session["username"]
        })
    flash('Recipe Successfully Added', 'success')
    return redirect(url_for('get_recipes'))


"""
view viewrecipe page
"""


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):

    """
    Takes the recipe _id and show the details of the recipe.
    """
    try:
        the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
        return render_template('viewrecipe.html', recipe=the_recipe)
    except Exception:
        return render_template("404.html")


"""
eidit recipe page
"""


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """
    It will check whether user in session is the owner of the recipe.
    It also takes the recipe _id and show it in the edit form.
    """
    try:
        the_user = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
        if session["username"] == the_user['recipe_author']:
            the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
            all_cuisines = mongo.db.cuisines.find()
            all_maketime = mongo.db.makingtime.find()
            all_recipetype = mongo.db.recipetype.find()
            all_serving = mongo.db.serving.find()
            return render_template('editrecipe.html', recipe=the_recipe,
                                   cuisines=all_cuisines,
                                   maketime=all_maketime,
                                   recipetype=all_recipetype,
                                   serving=all_serving)
        else:
            return redirect(url_for('get_recipes'))
    except Exception as e:
        print(e)
        return render_template("404.html")


"""
update recipe page using post mehtod
"""


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipe_id)},
                  {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('recipe_description'),
            'recipe_ingredients': request.form.get('recipe_ingredients'),
            'recipe_preparation': request.form.get('recipe_preparation'),
            'recipe_cuisine': request.form.get('recipe_cuisine'),
            'making_time': request.form.get('making_time'),
            'recipe_type': request.form.get('recipe_type'),
            'recipe_serving': request.form.get('recipe_serving'),
            'recipe_date': request.form.get('recipe_date'),
            'recipe_author': session["username"]
        })
    flash('Recipe Successfully Updated', 'success')
    return redirect(url_for('get_recipes'))


"""
delete recipe page
"""


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """
    It takes the recipe _id and delete it from database.
    It will also show a flash message on the screen.
    """
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe Successfully Deleted', 'success')
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

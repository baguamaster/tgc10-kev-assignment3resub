import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from Recipe import Recipe

load_dotenv()

# (Test) Admin account
# username: root_admin
# password: admin_root
# email: root@root.com

# Sample Recipe to test without MongoDB
# sample = Recipe(
#     _id = "601003511615884e24186cf8",
#     cuisine_type = "Nigerian",
#     recipe_name = "Fried Plantain",
#     meal_time = ["Breakfast", "Lunch", "Dinner"],
#     description = "A very delicious global dish cooked wherever plantains grow.",
#     servings = "4",
#     is_vegetarian = "Yes",
#     prep_time = "2",
#     cooking_time = "15",
#     ingredients = {
#         "Plantain": "100g",
#         "Oil": "50g"
#     },
#     method = {
#         "1": "Heat oil",
#         "2": "Cook plantain",
#         "3": "Plate"
#     },
#     allergens = ["Plantain"],
#     image = "https://static01.nyt.com/images/2019/10/13/dining/kwr-maduros/kwr-maduros-articleLarge.jpg",
#     video = "https://www.youtube.com/watch?v=sQJ9ioyNhEA",
#     recipe_by = "jesse"
# )

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

'''
`All Recipes` Template Rendering
'''

@app.route("/")
@app.route("/recipes")
def recipes():
    # recipes=[sample,sample]
    recipes = list(mongo.db.recipes.find())
    recipes.sort(key=lambda k: k['recipe_name'])
    return render_template("recipes.html", recipes=recipes)

'''
`Full Recipe` Template Rendering
'''

@app.route("/recipes/<recipe_id>", methods=["GET", "POST"])
def full_recipe(recipe_id):
    # recipe=sample
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)

'''
Register User Functionality & Template Rendering
'''

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Test for existing_user
        # if request.form.get("username") == "Jonny":
        #     flash("Username already exists")
        #     return redirect(url_for("register"))

        # Test for exisiting_email
        # if request.form.get("email") == "john@gmail.com":
        #     flash("Email already exists")
        #     return redirect(url_for("register"))

        # Checking if username already exists in the DB as lowercase:
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Checking if email already exists in the DB:
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))

        # If username does not exist, then store in db:
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        # After clicking register, user will now be in session:
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")

'''
User Login Functionality & Template Rendering
'''

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Test if username does not exist
        # if request.form.get("username").lower() == "jonny":
        #     flash("Incorrect Username and/or Password")
        #     return redirect(url_for("login"))

        # Test if incorrect password
        # if request.form.get("password") == "11111":
        #     flash("Incorrect Username and/or Password")
        #     return redirect(url_for("login"))

        # Test if username exists
        # session["user"] = request.form.get("username").lower()
        # return redirect(url_for("profile", username=session["user"]))

        # Checking if username already exists in the DB as lowercase:
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Checking if the hashed password matches the user's input:
            if check_password_hash(
                existing_user["password"],
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # If the invalid password is incorrect then alert user.
                # For security reasons message displays either username
                # or password is incorrect. This minimises brute-forcing.
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If the username does not exist then display the same message
            # as if the password was incorrect.
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
        return render_template("login.html")

    return render_template("login.html")

'''
User Logout Functionality
'''

@app.route("/logout")
def logout():
    # Remove user from the browser session cookies:
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

'''
User Profile Template Rendering
'''

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # recipes=[sample, sample]
    # The session user's username is retrieved from MongoDB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find(
        {"recipe_by": session["user"]}))
    return render_template(
        "profile.html", username=username,
        recipes=recipes)

'''
Search Functionality
'''

@app.route("/search")
def search():
    # recipes=[sample]
    query = request.args.get("query", "-minutes -mins")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)

'''
`Add New Recipe` Functionality & Template Rendering
'''

@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        is_vegetarian = "Yes" if request.form.get(
            "is_vegetarian") == "Yes" else "No"

        # Creating a dictionary for ingredients with 'key:value' pairs
        # being 'ingredient_name:ingredient_amount' respectively.
        ingredient_name = request.form.getlist("ingredient_name")
        ingredient_amount = request.form.getlist("ingredient_amount")
        ingredients = {}
        for index in range(len(ingredient_name)):
            ingredients[ingredient_name[index]] = ingredient_amount[index]

        # Creating a dictionary for the method with 'key:value' pairs
        # being 'step number:step description' respectively.
        method = request.form.getlist("method")
        method_obj = {}
        for element in method:
            # Starting the steps from 1; as by default, the starting
            # index of a list is 0. For the step to be a key of the
            # dictionary, it must be converted to a string.
            method_step = method.index(element) + 1
            method_obj[str(method_step)] = str(element)

        allergens = request.form.get("allergens")
        allergens_list = [x.strip() for x in allergens.split(",")]

        recipe = {
            "cuisine_type": request.form.get("cuisine_type"),
            "recipe_name": request.form.get("recipe_name"),
            "meal_time": request.form.getlist("meal_time"),
            "description": request.form.get("description"),
            "servings": request.form.get("servings"),
            "is_vegetarian": is_vegetarian,
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": ingredients,
            "method": method_obj,
            "allergens": allergens_list,
            "image": request.form.get("image"),
            "video": request.form.get("video"),
            "recipe_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you! Your recipe has been successfully added.")
        return redirect(url_for("recipes"))

    return render_template("new_recipe.html")

'''
`Edit Recipe` Functionality & Template Rendering
'''

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_vegetarian = "Yes" if request.form.get(
            "is_vegetarian") == "Yes" else "No"

        # Creating a dictionary for ingredients with 'key:value' pairs
        # being 'ingredient_name:ingredient_amount' respectively.
        ingredient_name = request.form.getlist("ingredient_name")
        ingredient_amount = request.form.getlist("ingredient_amount")
        ingredients = {}
        for index in range(len(ingredient_name)):
            ingredients[ingredient_name[index]] = ingredient_amount[index]

        # Creating a dictionary for the method with 'key:value' pairs
        # being 'step number:step description' respectively.
        method = request.form.getlist("method")
        method_obj = {}
        for element in method:
            # Starting the steps from 1; as by default, the starting
            # index of a list is 0. For the step to be a key of the
            # dictionary, it must be converted to a string.
            method_step = method.index(element) + 1
            method_obj[str(method_step)] = str(element)

        allergens = request.form.get("allergens")
        allergens_list = [x.strip() for x in allergens.split(",")]

        submit = {
            "cuisine_type": request.form.get("cuisine_type"),
            "recipe_name": request.form.get("recipe_name"),
            "meal_time": request.form.getlist("meal_time"),
            "description": request.form.get("description"),
            "servings": request.form.get("servings"),
            "is_vegetarian": is_vegetarian,
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": ingredients,
            "method": method_obj,
            "allergens": allergens_list,
            "image": request.form.get("image"),
            "video": request.form.get("video"),
            "recipe_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    # recipe=None
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)

'''
`Delete Recipe` Functionality
'''

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))

'''
`Cooking Tools` Template Rendering
'''

@app.route("/cooking_tools")
def cooking_tools():
    return render_template("cooking_tools.html")

if __name__ == "__main__":
    # app.run(host=os.environ.get("IP"),
    #         port=int(os.environ.get("PORT")),
    #         debug=False)
    app.run()
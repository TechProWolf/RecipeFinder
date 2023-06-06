# app.py
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Load the Spoonacular API key from the environment variable
API_KEY = os.environ.get("API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    ingredients = request.form.get("ingredients")
    dietary_preference = request.form.get("dietary_preference")

    # Make a request to the Spoonacular API to search for recipes
    url = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY}&ingredients={ingredients}&diet={dietary_preference}"
    response = requests.get(url)
    recipes = response.json()

    return render_template("results.html", recipes=recipes)

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # Make a request to the Spoonacular API to retrieve the details of a recipe
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}"
    response = requests.get(url)
    recipe = response.json()

    return render_template("recipe.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)

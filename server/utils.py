from config import db
from models import Recipe, Alchemist

def get_all_recipes():
    return db.session.query(Recipe).all()

def get_all_alchemist():
    return db.session.query(Alchemist).all()

def find_alchemist_by_id(id):
    return db.session.get(Alchemist, id)

def find_recipe_by_id(id):
    return db.session.get(Recipe, id)

def add_recipe():
    print("Adding Recipe")
    new_name = input("Enter new name: ")
    new_ingredients = input("Enter new ingredients: ")
    new_description = input("Enter new description: ")
    assigned_alchemist_id = input("Enter the ID of the alchemist this recipe belong to: ")

    new_recipe = Recipe(name = new_name, ingredients = new_ingredients, description = new_description, alchemistID = assigned_alchemist_id)
    
    db.session.add(new_recipe)
    db.session.commit()

def erase_recipe(recipe):
    db.session.delete(recipe)
    db.session.commit()

def modify_recipe(recipe):
    print(f"Modifying Recipe: {recipe.name}")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_ingredients = input("Enter new ingredients (leave blank to keep current): ")
    new_description = input("Enter new description (leave blank to keep current): ")

    if new_name:
        recipe.name = new_name
    if new_ingredients:
        recipe.ingredients = new_ingredients
    if new_description:
        recipe.description = new_description

    db.session.commit()
    print("Recipe Modified Successfully")


#Combining two recipes using the id of each recipe
    
def combine_recipes():
    print("Input ID of recipes to combine")
    print("----------")
    recipe1_id = input("Recipe 1: ")
    recipe2_id = input("Recipe 2: ")
    print(f"{get_all_alchemist()}")
    assigned_alchemist_id = input("Enter the ID of the alchemist this recipe belong to: ")
    recipe1 = find_recipe_by_id(recipe1_id)
    recipe2 = find_recipe_by_id(recipe2_id)
    recipe3 = Recipe()
    recipe3.name = f"{recipe1.name} {recipe2.name}"
    recipe3.ingredients = f"{recipe1.ingredients}, {recipe2.ingredients}"
    recipe3.description = f"{recipe1.description}, {recipe2.description}"
    recipe3.alchemistID = assigned_alchemist_id
    db.session.add(recipe3)
    db.session.delete(recipe1)
    db.session.delete(recipe2)
    db.session.commit()

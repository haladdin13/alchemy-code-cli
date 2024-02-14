from config import app, migrate
# from rich import print


from models import db
from utils import get_all_recipes, find_recipe_by_id, modify_recipe, erase_recipe, get_all_alchemist, find_alchemist_by_id, add_recipe

def display_intro():
  print("Welcome back to the circle...")

def display_main_menu():
  print("Main Menu")
  print("----------")
  print("1. Open the recipe tome")
  print("2. View recipies by Alchemist")
  print("3. Create a new recipe")
  print("4. Modify a recipe")
  print("5. Erase a recipe")
  print("6. Leave the circle")
  print("----------")

def get_main_choice():
  return input("What is your command? ")

def display_all_recipes():
    recipes = get_all_recipes()
    for recipe in recipes:
        print(f"{recipe.id} | {recipe.name}")
    print("----------")
    print("What is your desire?")
    print("1. Delve into a recipe's secrets")
    print("2. Return to the main menu")
    print("----------")
    choice = input()
    if choice == "1":
        choose_recipe_by_id()
    else:
        return
    

def choose_recipe_by_id():
   search_id = input("Enter the ID of the recipe you want to see: ")
   recipe = find_recipe_by_id(search_id)
   print(
      f"ID: {recipe.id} | Name: {recipe.name} | Ingredients: {recipe.ingredients} | Description: {recipe.description} | Creation Date: {recipe.creation_date} | Modification Date: {recipe.modification_date}"
   )
   display_recipe_submenu(recipe)

def display_recipe_submenu(recipe):
   print("1. Modify recipe")
   print("2. Erase recipe")
   print("3. Return to main menu")
   choice = input()
   handle_recipe_choice(choice, recipe)

def handle_recipe_choice(choice, recipe):
    if choice == "1":
        modify_recipe(recipe)
    elif choice == "2":
        erase_recipe(recipe)
    else:
        return
    

def display_all_alchemists():
    alchemists = get_all_alchemist()
    for alchemist in alchemists:
        print(f"{alchemist.id} | {alchemist.name}")
    print("----------")
    print("Who's tome do you wish to view?")
    print("1. Procure your desired tome")
    print("2. Return to the main menu")
    print("----------")
    choice = input()
    if choice == "1":
        choose_alchemist_by_id()
    else:
        return
    
def choose_alchemist_by_id():
   search_id = input("Enter the ID of the alchemist's recipe tome you wish to see: ")
   alchemist = find_alchemist_by_id(search_id)
   print(
      f"ID: {alchemist.id} | Name: {alchemist.name} | Experience Level: {alchemist.experienceLevel} | Recipe Number: {alchemist.recipe_number}"
   )
   display_alchemist_submenu(alchemist)


def display_alchemist_submenu(alchemist):
   print("1. View alchemist's recipes")
   print("2. Return to previous menu")
   print("3. Return to main menu")
   choice = input()
   handle_alchemist_choice(choice, alchemist)


def handle_alchemist_choice(choice, alchemist):
    if choice == "1":
      display_alchemist_recipes(alchemist)
    elif choice == "2":
      return
    else:
      return
    

def display_alchemist_recipes(alchemist):
    recipes = get_all_recipes()
    for recipe in recipes:
        if recipe.alchemistID == alchemist.id:
            print(f"{recipe.id} | {recipe.name}")


def create_recipe_menu():
    print("----------")
    print("Do you want to create a new recipe?")
    print("1. Create a new recipe")
    print("2. Return to the main menu")
    print("----------")
    choice = input()
    if choice == "1":
        add_recipe()
    else:
        return

  

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
     
     #CLI Start
    display_intro()
    while True:
      display_main_menu()
      choice = get_main_choice()
      if choice == "1":
        display_all_recipes()
      elif choice == "2":
        display_all_alchemists()
      elif choice == "3":
          create_recipe_menu()
      elif choice == "4":
        print("Leave the circle")
      else:
        break
      

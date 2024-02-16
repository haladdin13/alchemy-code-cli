from config import db
from rich import print
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
    print("[bold yellow]Concocting a New Recipe[/bold yellow]")
    new_name = input("[green]Name your creation:[/green] ")
    new_ingredients = input("[green]What elements shall bind together?[/green] ")
    new_description = input("[green]Describe its essence and effects:[/green] ")
    assigned_alchemist_id = input("[green]Whose wisdom guides this brew? Enter the Sage ID:[/green] ")

    new_recipe = Recipe(name = new_name, ingredients = new_ingredients, description = new_description, alchemistID = assigned_alchemist_id)
    
    db.session.add(new_recipe)
    db.session.commit()

def erase_recipe(recipe):
    print(f"[bold yellow]Dissolving Concoction of:[/bold yellow] {recipe.name}")
    db.session.delete(recipe)
    db.session.commit()

def modify_recipe(recipe):
    print(f"[bold magenta]Transmuting Essence of:[/bold magenta] {recipe.name}")
    new_name = input("Inscribe new name (leave blank to keep current): ")
    new_ingredients = input("Inscribe new ingredients (leave blank to keep current): ")
    new_description = input("Inscribe new description (leave blank to keep current): ")

    if new_name:
        recipe.name = new_name
    if new_ingredients:
        recipe.ingredients = new_ingredients
    if new_description:
        recipe.description = new_description

    db.session.commit()
    print("[bold yellow]The recipe's essence has been transmuted.[/bold yellow]")


#Combining two recipes using the id of each recipe
    
def combine_recipes():
    print("[bold yellow]At the ancient altar, two essences await their union...[/bold yellow]")
    print("----------")
    print("Inscribe the numerals of the recipies to be merged:")
    recipe1_id = input("Recipe 1: ")
    recipe2_id = input("Recipe 2: ")
    print("[bold red]Behold, the guardians of arcane knowledge:[/bold red]")
    alchemists = get_all_alchemist()
    for alchemist in alchemists:
        print(f"{alchemist.id} | {alchemist.name}")
    assigned_alchemist_id = input("Choose the guardian for this new creation: ")
    recipe1 = find_recipe_by_id(recipe1_id)
    recipe2 = find_recipe_by_id(recipe2_id)
    recipe3 = Recipe()
    recipe3.name = f"{recipe1.name} {recipe2.name}"
    recipe3.ingredients = f"{recipe1.ingredients}, {recipe2.ingredients}"
    recipe3.description = f"{recipe1.description}, {recipe2.description}"
    recipe3.alchemistID = assigned_alchemist_id
    print("[bold yellow]A new synthesis has been created[/bold yellow]")
    db.session.add(recipe3)
    db.session.delete(recipe1)
    db.session.delete(recipe2)
    db.session.commit()

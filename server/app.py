from config import app, migrate
from rich import print


from models import db
from utils import get_all_recipes, find_recipe_by_id, modify_recipe, erase_recipe, get_all_alchemist, find_alchemist_by_id, add_recipe, combine_recipes

def display_intro():
  print(
     ''' 

      __      ___       ______    __    __    _______  ___      ___  ___  ___       ______    ______    ________    _______  
     /""\    |"  |     /" _  "\  /" |  | "\  /"     "||"  \    /"  ||"  \/"  |     /" _  "\  /    " \  |"      "\  /"     "| 
    /    \   ||  |    (: ( \___)(:  (__)  :)(: ______) \   \  //   | \   \  /     (: ( \___)// ____  \ (.  ___  :)(: ______) 
   /' /\  \  |:  |     \/ \      \/      \/  \/    |   /\\  \/.    |  \\  \/       \/ \    /  /    ) :)|: \   ) || \/    |   
  //  __'  \  \  |___  //  \ _   //  __  \\  // ___)_ |: \.        |  /   /        //  \ _(: (____/ // (| (___\ || // ___)_  
 /   /  \\  \( \_|:  \(:   _) \ (:  (  )  :)(:      "||.  \    /:  | /   /        (:   _) \\        /  |:       :)(:      "| 
(___/    \___)\_______)\_______) \__|  |__/  \_______)|___|\__/|___||___/          \_______)\"_____/   (________/  \_______) 
                                                                                                                             


 '''
     )
  print("[bold purple]Step forth, seeker of the arcane...[/bold purple]")

def display_main_menu():
  print("----------")
  print("[bold magenta]Sanctum Main Chamber[/bold magenta]")
  print("----------")
  print("1. [bold green]Unveil[/bold green] the tome of recipes")
  print("2. [bold green]Peer into[/bold green] the archive of Alchemists")
  print("3. [bold green]Concoct[/bold green] a new recipe")
  print("4. [bold green]Depart[/bold green] the sanctum")
  print("----------")

def get_main_choice():
  return input("What is your command? ")

def display_all_recipes():
    recipes = get_all_recipes()
    for recipe in recipes:
        print(f"{recipe.id} | {recipe.name}")
    print("----------")
    print("Decipher the scripts or combine essences for new alchemy?")
    print("1. [bold green]Decipher[/bold green] a recipe's secrets")
    print("2. [bold green]Alchemize[/bold green] two essences")
    print("3. [bold green]Return[/bold green] to the main chamber")
    print("----------")
    choice = input()
    if choice == "1":
        choose_recipe_by_id()
    elif choice == "2":
        combine_recipes()
    else:
        return
    

def choose_recipe_by_id():
   search_id = input("Enter the numeral of identity to unveil its mysteries: ")
   recipe = find_recipe_by_id(search_id)
   print(
      f"[bold green]ID:[/bold green] {recipe.id} | [bold green]Name:[/bold green] {recipe.name} | [bold green]Ingredients:[/bold green] {recipe.ingredients} | [bold green]Description:[/bold green] {recipe.description} | [bold green]Creation Date:[/bold green] {recipe.creation_date} | [bold green]Modification Date:[/bold green] {recipe.modification_date}"
   )
   display_recipe_submenu(recipe)

def display_recipe_submenu(recipe):
   print("----------")
   print("What do you wish to do?")
   print("1. [bold green]Transmute[/bold green] the essence of the recipe")
   print("2. [bold red]Dissolve[/bold red] the concoction into the aether")
   print("3. [bold cyan]Decipher[/bold cyan] another recipe")
   print("4. [bold yellow]Return[/bold yellow] to the sanctum's heart")
   choice = input()
   handle_recipe_choice(choice, recipe)

def handle_recipe_choice(choice, recipe):
    if choice == "1":
        modify_recipe(recipe)
    elif choice == "2":
        erase_recipe(recipe)

    elif choice == "3":
        return display_all_recipes()
    else:
        return
    

def display_all_alchemists():
    alchemists = get_all_alchemist()
    for alchemist in alchemists:
        print(f"{alchemist.id} | {alchemist.name}")
    print("----------")
    print("Which sage's secrets do you seek to unlock?")
    print("1. [bold green]Summon[/bold green] the tome of a wise one")
    print("2. [bold green]Return[/bold green] to the main sanctum")
    print("----------")
    choice = input()
    if choice == "1":
        choose_alchemist_by_id()
    else:
        return
    
def choose_alchemist_by_id():
   search_id = input("Whose ancient wisdom do you seek to commune with? Apply the numeral of the sage: ")
   alchemist = find_alchemist_by_id(search_id)
   print(
      f"[bold green]ID:[/bold green] {alchemist.id} | [bold green]Name:[/bold green] {alchemist.name} | [bold green]Experience Level:[/bold green] {alchemist.experienceLevel}"
   )
   display_alchemist_submenu(alchemist)


def display_alchemist_submenu(alchemist):
   print(f"The Codex of {alchemist.name}")
   print("1. [bold green]Reveal[/bold green] the alchemist's concoctions")
   print("2. [bold green]Return[/bold green] to previous menu")
   print("3. [bold yellow]Return[/bold yellow] to the sanctum's heart")
   choice = input()
   handle_alchemist_choice(choice, alchemist)


def handle_alchemist_choice(choice, alchemist):
    if choice == "1":
      display_alchemist_recipes(alchemist)
    elif choice == "2":
      return choose_alchemist_by_id()
    else:
      return
    

def display_alchemist_recipes(alchemist):
    recipes = get_all_recipes()
    for recipe in recipes:
        if recipe.alchemistID == alchemist.id:
            print(f"{recipe.id} | {recipe.name}")
    alchemist_recipe_submenu(alchemist)

#select an alchemist's recipe to modify

def alchemist_recipe_submenu(alchemist):
    print("----------")
    print("What do you wish to do?")
    print("1. [bold green]Delve[/bold green] into an alchemist's recipe")
    print("1. [bold green]Tread back[/bold green] through the hall of sages")
    print("2. [bold yellow]Return[/bold yellow] to the sanctum's heart")
    print("----------")
    choice = input()
    if choice == "1":
        recipe_id = input("Inscribe the numeral of the recipe of your interest: ")
        recipe = find_recipe_by_id(recipe_id)
        if recipe and recipe.alchemistID == alchemist.id:
           print(f"[bold green]ID:[/bold green] {recipe.id} | [bold green]Name:[/bold green] {recipe.name} | [bold green]Ingredients:[/bold green] {recipe.ingredients} | [bold green]Description:[/bold green] {recipe.description} | [bold green]Creation Date:[/bold green] {recipe.creation_date} | [bold green]Modification Date:[/bold green]")
           print("----------")
           print("What is your intention?")
           print("1. Transmute this recipe")
           print("2. Dissolve this recipe")
           print("3. The id is a fickle thing")
           print("----------")
           choice = input()
           if choice == "1":
              modify_recipe(recipe)
           elif choice == "2":
              erase_recipe(recipe)
           else:
              return
    elif choice == "2":
        display_all_alchemists()
    else:
        return


def create_recipe_menu():
    print("----------")
    print("Do you wish to bind the ether and craft anew, or shall you return to the sanctum's heart?")
    print("1. [bold green]Inscribe[/bold green] a new recipe of power")
    print("2. [bold green]Return[/bold green] to the sanctum's embrace")
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
        print("[italic cyan]You dissolve into the mists, leaving the sanctum... for now.[/italic cyan]")
        break
      else:
        break
      

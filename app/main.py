import os
import json

def get_recipe(name):
    try:
        # Ustala sciezke do recipes.json wzgledem main.py
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, '../data/recipes.json')

        with open(file_path, 'r') as file:
            recipes = json.load(file)

        recipe = recipes.get(name.lower())

        if recipe:
            return recipe
        else:
            return "Recipe not found"
    except FileNotFoundError:
        return "Recipe file not found!"


if __name__ == '__main__':
    print("Welcome to Prepify - Your Recipe Assistant!")
    while True:
        recipe_name = input("\nEnter a recipe name (or type 'exit' to quit): ").strip()

        if recipe_name.lower() == 'exit':
            print("Thank you for using Prepify!")
            break

        result = get_recipe(recipe_name)
        if isinstance(result, dict):
            print("\nRecipe found:")
            print("Ingredients:")
            for ingredient in result['ingredients']:
                print(f"- {ingredient}")
            print("Instructions:")
            for step in result['steps']:
                print(f"{step}")
        else:
            print(f"\n{result}")

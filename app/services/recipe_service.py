import os, json

def get_recipe(name: str):
    try:
        base = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(base, 'data', 'recipes.json')
        with open(path, 'r', encoding='utf-8') as f:
            recipes = json.load(f)
        return recipes.get(name.lower(), None)
    except FileNotFoundError:
        return None

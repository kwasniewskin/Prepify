from fastapi import APIRouter, HTTPException
from app.services.recipe_service import get_recipe

router = APIRouter()

@router.get("/recipe/{name}")
def read_recipe(name: str):
    recipe = get_recipe(name)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

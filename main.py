from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, crud, database
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: str
    ingredients: str
    instructions: str

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/recipes/", response_model=RecipeResponse)
def create_recipe(recipe: RecipeResponse, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe.dict())

@app.get("/recipes/{recipe_id}", response_model=RecipeResponse)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.get("/recipes/", response_model=list[RecipeResponse])
def read_recipes(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip, limit)
    return recipes

@app.put("/recipes/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, updated_recipe: RecipeResponse, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return crud.update_recipe(db, recipe, updated_recipe.dict())

@app.delete("/recipes/{recipe_id}", response_model=RecipeResponse)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return crud.delete_recipe(db, recipe)

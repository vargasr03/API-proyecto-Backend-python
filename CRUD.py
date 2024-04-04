from sqlalchemy.orm import Session
from .models import Recipe

def create_recipe(db: Session, recipe_data: dict):
    db_recipe = Recipe(**recipe_data)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 5):
    return db.query(Recipe).offset(skip).limit(limit).all()

def update_recipe(db: Session, recipe: Recipe, updated_recipe_data: dict):
    for key, value in updated_recipe_data.items():
        setattr(recipe, key, value)
    db.commit()
    db.refresh(recipe)
    return recipe

def delete_recipe(db: Session, recipe: Recipe):
    db.delete(recipe)
    db.commit()
    return recipe

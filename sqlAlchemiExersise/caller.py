from typing import List

from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker

from helper import session_decorator
from models import Recipe
from seed import recipes

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/sqlAlchemyExercise")
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)

    session.add(new_recipe)


@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str) -> int:
    records_changed: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .update({
            Recipe.name: new_name,
            Recipe.ingredients: new_ingredients,
            Recipe.instructions: new_instructions
        })
    )

    return records_changed


@session_decorator(session)
def delete_recipe_by_name(name: str) -> int:
    records_changed: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .delete()
    )

    return records_changed


@session_decorator(session, auto_close=False)
def get_recipes_by_ingredient(ingredient_name: str) -> List:
    recipes_with_ingredient = (
        session.query(Recipe)
        .filter(Recipe.ingredients.ilike(f"%{ingredient_name}%"))
        .all()
    )

    return recipes_with_ingredient


@session_decorator(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    first_recipe = (
        session.query(Recipe)
        .filter_by(name=first_recipe_name)
        .with_for_update()
        .one()
    )

    second_recipe = (
        session.query(Recipe)
        .filter_by(name=second_recipe_name)
        .with_for_update()
        .one()
    )

    first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients


swap_recipe_ingredients_by_name("Spaghetti Carbonara", "Chicken Stir-Fry")
#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
#set batches to 0
    batches = 0

    for name, qty in recipe.items():
#look for milk in your inventory and if you don't have milk then can't do recipe       
# check if I have enough milk in inventory if I don't then can't do recipe 
# if I have both milk and enough milk I can compare the qty needed against the quantity I have.
#     
            
            
        return batches

     


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 150, 'flour': 51 }
  
def recipe_batches(recipe, ingredients):
      
  
  
  # Grab the name of the ingredients
  recipe_ingredients = recipe.keys()
  
  print(recipe_ingredients)
  
  # Set batch to 0
  batch_count = 0
  
  # Loop through ingredients
  for recipe_key in recipe_ingredients:
        
        try: 
          
          # Test to see if required amount of ingredients is available
          if ingredients[recipe_key] >= recipe[recipe_key]:
                print(F'available {recipe_key}:{ingredients[recipe_key]}, need {recipe_key}:{recipe[recipe_key]}')
                
                #Subtract required ingredient quantity from ingredients dictionary value
                ingredients[recipe_key] -= recipe[recipe_key]
                print(F'new available {recipe_key}:{ingredients[recipe_key]}')
          
          # Returns the amount of batches if there is not enough for another batch     
          else:
                print(F'Not enough {recipe_key}')
                print(F'batch_count: {batch_count}')
                return batch_count
              
          # Print message if an ingredient does not exist in ingredients dictionary
        except KeyError:
          print(F'No {recipe_key} in available')
          print(F'batch_count: {batch_count}')
          return 0
        
  batch_count += 1
    
recipe_batches(recipe, ingredients)


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
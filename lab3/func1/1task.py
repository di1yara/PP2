"""
## Python Function

1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately,
 your store only sells items in ounces. Create a function to convert grams to ounces. 
`ounces = 28.3495231 * grams`
"""
def ounces(ingredient):
    oun=28.3495231*ingredient
    return oun
ingredient=int(input("Enter a gramm for recipe: "))

print(ounces(ingredient))



   
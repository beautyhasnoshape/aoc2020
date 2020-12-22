import regex as re

with open('21.txt') as f:
    lines = [a.strip() for a in f.readlines()]

all_allergens, all_ingredients, all_recipes = {}, set(), []

for line in lines:
    a, b = re.match('(.*) \(contains (.*)\)', line).groups()
    ingredients, allergens = set(a.split()), b.split(', ')

    all_ingredients |= ingredients
    all_recipes.append(ingredients)

    for allergen in allergens:
        if allergen not in all_allergens:
            all_allergens[allergen] = ingredients.copy()
        else:
            all_allergens[allergen] &= ingredients  # update ingredients by intersecting it with another set

ok_ingredients = set()
for ingredient in all_ingredients:
    if not any(ingredient in x for x in all_allergens.values()):
        ok_ingredients.add(ingredient)

result = sum([1 for recipe in all_recipes for ingredient in ok_ingredients if ingredient in recipe])
print(result)  # 2423
assert 2423 == result


for _ in all_allergens:
    stop = True
    for allergen in all_allergens:
        if len(all_allergens[allergen]) == 1:
            ingredient = next(iter(all_allergens[allergen]))
            for a in all_allergens:
                if a == allergen:
                    continue
                ingredients = all_allergens[a]
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
                    stop = False
    if stop:
        break
    stop = True

result = ','.join([next(iter(all_allergens[key])) for key in sorted(all_allergens.keys())])
print(result)  # jzzjz,bxkrd,pllzxb,gjddl,xfqnss,dzkb,vspv,dxvsp
assert 'jzzjz,bxkrd,pllzxb,gjddl,xfqnss,dzkb,vspv,dxvsp' == result

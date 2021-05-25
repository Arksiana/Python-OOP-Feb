class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = dict(ingredients)

    def add_extra(self, ingredient, quantity, ingredient_price):
        if not PizzaDelivery.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += quantity * ingredient_price
            else:
                self.ingredients[ingredient] = quantity
                self.price += quantity * ingredient_price
        else:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if not PizzaDelivery.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            if quantity > self.ingredients[ingredient] and ingredient in self.ingredients:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * ingredient_price
                return self.price
        else:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

    def make_order(self):
        PizzaDelivery.ordered = True
        res_dict = []
        for k, v in self.ingredients.items():
            res_dict.append(f"{k}: {v}")
        return f"You've ordered pizza {self.name} prepared with {', '.join(res_dict)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

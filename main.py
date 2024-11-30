class MenuItem():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    def displayDetails(self):
        print(f"{self.name} - {self.description} - {self.price}")

class Beverage(MenuItem):
    def __init__(self, name, description, price, volume, isCold, isMilkFree, isAlcoholic):
        super().__init__(name, description, price)
        self.volume = volume
        self.isCold = isCold
        self.isMilkFree = isMilkFree
        self.isAlcoholic = isAlcoholic

    def displayDetails(self):
        print(f"{self.name} - {self.description} - {self.price} - {self.volume}ml - {self.isCold} - {self.isMilkFree} - {self.isAlcoholic}")


class Appetizer(MenuItem):
    def __init__(self, name, description, price, isVegetarian, isGlutenFree, recommendedDip):
        super().__init__(name, description, price)
        self.isVegetarian = isVegetarian
        self.isGlutenFree = isGlutenFree
        self.recommendedDip = recommendedDip

    def displayDetails(self):
        print(f"{self.name} - {self.description} - {self.price} - {self.isVegetarian} - {self.isGlutenFree} - {self.recommendedDip}")

    
class MainCourse(MenuItem):
    def __init__(self, name, description, price, isVegetarian, isVegan, calories):
        super().__init__(name, description, price)
        self.isVegetarian = isVegetarian
        self.isVegan = isVegan
        self.calories = calories

    def displayDetails(self):
        print(f"{self.name} - {self.description} - {self.price} - {self.isVegetarian} - {self.isVegan} - {self.calories}")

class Order():
    def __init__(self, menuItems):
        self.MenuItems = menuItems

    def displayOrder(self):
        for item in self.MenuItems:
            item.displayDetails()
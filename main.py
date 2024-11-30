from tabulate import tabulate

class MenuItem():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    def displayDetails(self):
        table = tabulate([["name","description", "price"],[self.name, self.description, str(self.price) + "$"]], headers="firstrow")
        print(table)

class Beverage(MenuItem):
    def __init__(self, name, description, price, volume, isCold, isMilkFree, isAlcoholic):
        super().__init__(name, description, price)
        self.volume = volume
        self.isCold = isCold
        self.isMilkFree = isMilkFree
        self.isAlcoholic = isAlcoholic

    def displayDetails(self):
        table = tabulate([["name","description", "price", "volume", "isCold", "isMilkFree", "isAlcoholic"],[self.name, self.description, str(self.price) + "$", str(self.volume) + "ml", self.isCold, self.isMilkFree, self.isAlcoholic]], headers="firstrow")
        print(table)


class Appetizer(MenuItem):
    def __init__(self, name, description, price, isVegetarian, isGlutenFree, recommendedDip):
        super().__init__(name, description, price)
        self.isVegetarian = isVegetarian
        self.isGlutenFree = isGlutenFree
        self.recommendedDip = recommendedDip

    def displayDetails(self):
        table = tabulate([["name","description", "price", "isVegetarian", "isGlutenFree", "recommendedDip"],[self.name, self.description, str(self.price)+ "$", self.isVegetarian, self.isGlutenFree, self.recommendedDip]], headers="firstrow")        
        print(table)
    

class MainCourse(MenuItem):
    def __init__(self, name, description, price, isVegetarian, isVegan, calories):
        super().__init__(name, description, price)
        self.isVegetarian = isVegetarian
        self.isVegan = isVegan
        self.calories = calories

    def displayDetails(self):
        table = tabulate([["name","description", "price", "isVegetarian", "isVegan", "calories"],[self.name, self.description, str(self.price) + "$", self.isVegetarian, self.isVegan, self.calories]], headers="firstrow")
        print(table)


class Order():
    def __init__(self, menuItems, tableNumber):
        self.MenuItems = menuItems
        self.tableNumber = tableNumber
    
    def addItems(self, menuItems):
        self.MenuItems.extend(menuItems)
    
    def removeItems(self, menuItems):
        for item in menuItems:
            self.MenuItems.remove(item)

    def calculateBill(self):
        total = 0
        for item in self.MenuItems:
            total += item.price
        return total
    
    def displayOrderDetails(self):

        print("Table Number: " + str(self.tableNumber))
        table = []
        for item in self.MenuItems:
            table.append([item.name, str(item.price) + "$"])
        print(tabulate(table, headers=["Item", "Price"]))

        print("Total: " + str(self.calculateBill()) + "$")



# Create objects of MenuItem, Beverage, Appetizer, MainCourse

cocaCola = Beverage("Coca Cola", "Refreshing drink", 2.5, 500, True, True, False)
beer = Beverage("Beer", "Alcoholic drink", 5, 500, True, True, True)
orangeJuice = Beverage("Orange Juice", "Fresh orange juice", 3, 300, True, True, False)
chicha = Beverage("Chicha", "Traditional Colombian drink", 2, 300, True, True, False)

nachos = Appetizer("Nachos", "Crispy chips with cheese", 6, True, False, "Cheddar")
onionRings = Appetizer("Onion Rings", "Fried onion rings", 5, True, True, "Ketchup")
frenchFries = Appetizer("French Fries", "Crispy fries", 4, True, True, "Mayonnaise")
patacones = Appetizer("Patacones", "Fried plantain", 4, True, True, "Guacamole")

beefSteak = MainCourse("Beef Steak", "Grilled beef steak", 15, False, False, 500)
pasta = MainCourse("Pasta", "Spaghetti with tomato sauce", 10, True, True, 300)
bandejaPaisa = MainCourse("Bandeja Paisa", "Traditional Colombian dish", 12, False, False, 700)
cuchuco = MainCourse("Cuchuco", "Traditional Colombian soup", 10, True, True, 500)

# Create an Order object and add the created objects to it
order = Order([cocaCola, patacones, bandejaPaisa], 1)
order.displayOrderDetails()

# Create another order
order2 = Order([beer, nachos, beefSteak], 2)
order2.displayOrderDetails()
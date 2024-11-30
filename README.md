# poo-reto-3
1. Create a repo with the class exercise
2. **Restaurant scenario:** You want to design a program to calculate the bill for a customer's order in a restaurant.
- Define a base class *MenuItem*: This class should have attributes like name, price, and a method to calculate the total price.
- Create subclasses for different types of menu items: Inherit from *MenuItem* and define properties specific to each type (e.g., Beverage, Appetizer, MainCourse).

```mermaid
classDiagram
    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse

    class MenuItem {
        +String name
        +String description
        +float price

        +void displayDetails()

    }

    class Beverage {
        +float volume
        +bool isCold
        +bool isMilkFree
        +bool alcoholic
    }

    class Appetizer {
        +bool isVegetarian
        +bool isGlutenFree
        +String recommendedDip
    }

    class MainCourse {
        +bool isVegetarian
        +bool isVegan
        +int calories
    }
``` 

- Define an Order class: This class should have a list of *MenuItem* objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.

Create a class diagram with all classes and their relationships.
```mermaid
classDiagram
    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse

    class MenuItem {
        +String name
        +String description
        +float price

        +void displayDetails()

    }

    class Beverage {
        +float volume
        +bool isCold
        +bool isMilkFree
        +bool alcoholic
    }

    class Appetizer {
        +bool isVegetarian
        +bool isGlutenFree
        +String recommendedDip
    }

    class MainCourse {
        +bool isVegetarian
        +bool isVegan
        +int calories
    }


    class Order {
        -List~MenuItem~ items
        
        -String tableNumber
        +void addItem(MenuItem item)
        +void removeItem(MenuItem item)
        +float calculateBill()
        +void displayOrderDetails()
    }
```

The menu should have at least 10 items.
The code should follow PEP8 rules.

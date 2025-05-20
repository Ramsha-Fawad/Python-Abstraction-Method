from abc import ABC, abstractmethod

# Abstract class
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass

# Concrete class 1
class Pizza(Food):
    def prepare(self):
        print("Preparing dough, adding sauce and toppings.")

    def serve(self):
        print("Serving hot pizza in a box.")

# Concrete class 2
class Burger(Food):
    def prepare(self):
        print("Grilling patty, placing it in buns with veggies.")

    def serve(self):
        print("Serving burger wrapped in paper.")

# Using the classes
def serve_food(food: Food):
    food.prepare()
    food.serve()

# Create objects
pizza = Pizza()
burger = Burger()

# Serve them
serve_food(pizza)
print("-----")
serve_food(burger)

#Output
#Preparing dough, adding sauce and toppings.
#Serving hot pizza in a box.
#-----
#Grilling patty, placing it in buns with veggies.
#Serving burger wrapped in paper.

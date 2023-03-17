# First task
class Rectangle:

    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
        return "მართკუთხედის პერიმეტრი: ", 2 * (self.width + self.length)

    def area(self):
        return "მართკუთხედის ფართობი: ", self.width * self.length

obj1 = Rectangle(1, 5, "blue")
obj2 = Rectangle(3, 3, "green")
obj3 = Rectangle(3, 7, "purple")
print(obj1.area())

# Second task
class car:

    def __init__(self, color, brand, model, ):
        self.color = color
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"car brand: {self.brand}, car model: {self.model}, car color: {self.color} "


car1 = car("Red", "Ford", "Mustang")
car2 = car("Blue", "Toyota", "Prius")
car3 = car("Green", "Volkswagen", "Golf")
print("\n", car1, "\n", car2, "\n", car3)

# third task
class dog:

    def __init__(self, breed="napolitan mastiff", size="large", age="5 years", color="black"):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def __str__(self):
        return f"breed:{self.breed}, size:{self.size}, age:{self.age}, color:{self.color}"

    def eat(self):
        return "ძაღლებს უყვართ ჭამა"

    def sleep(self):
        return "ძაღლებს უყვართ ძილი"

    def sit(self):
        return "ძაღლები ხანდახან ბრძანებაზე ჯდებიან"

    def run(self):
        return "ძაღლებს შეუძლიათ სწრაფად სირბილი"


dog1 = dog()
dog2 = dog("maltese", "small", "2 years", "white")
dog3 = dog("chow chow", "midium", "3 years", "brown")
print("\n", dog1, "\n", dog2, "\n", dog3)
print("\n", dog().eat(), ",", dog().sleep(), ",", dog().run(), ",", dog().sit())



class CoffeeMachine:
    def __init__(self, name, color, weight, price):
        print("Creating the coffee machine")
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price
        print(f"Created the coffee machine ({self.name})")

    def switch_on(self):
        print(f"{self.name}: Switching on the coffee machine..")

    def making_coffee(self):
        print(f"{self.name}: Making Coffee..")

    def cleaning(self):
        print(f"{self.name}: Started Cleaning...")
        print(f"{self.name}: The coffee machine is ready for the next use")

    def switch_off(self):
        print(f"{self.name}: Switching off the coffee machine")

    def get_details(self):
        print('===================')
        print(self.name)
        print(self.color)
        print(self.weight)
        print(self.price)
        print('===================')


x = CoffeeMachine("Coffee Machine", "Red", "10KG", "$100")
x.switch_on()
x.making_coffee()
x.cleaning()
x.switch_off()
x.get_details()

y = CoffeeMachine("Coffee Machine V2", "Green", "3KG", "$50")
y.get_details()

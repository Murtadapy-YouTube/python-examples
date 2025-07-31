
class WoodenShield:
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

    def get_name(self):
        return self.name

    def get_durability(self):
        return self.durability


x = WoodenShield("Shield", 90)
y = WoodenShield("Shield", 100)

print(f"x: {x} id: {id(x)}")
print(f"y: {y} id: {id(y)}")

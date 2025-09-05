

class Sword:
    def __init__(self, name, damage, rarity):
        self.name = name
        self.damage = damage
        self.rarity = rarity

    @classmethod
    def from_rarity(cls, name, rarity):
        rarity_damage = {"common": 10,
                         "rare": 20,
                         "legendary": 30}

        if rarity not in rarity_damage:
            raise ValueError(
                f"{rarity} is not exist in the list: {list(rarity_damage.keys())}")

        return cls(name, rarity_damage[rarity], rarity)


s1 = Sword("Sword 1", 10, "rare")
print(s1.name, s1.damage, s1.rarity)


s2 = Sword.from_rarity("Sword 2", "rare")
print(s2.name, s2.damage, s2.rarity)

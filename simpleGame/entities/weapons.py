class Weapons:

    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

# Default weapons

fists = Weapons("Fists", 2)
short_bow = Weapons("Short Bow", 7)
mace = Weapons("Mace", 8)
iron_sword = Weapons("Iron Sword", 10)
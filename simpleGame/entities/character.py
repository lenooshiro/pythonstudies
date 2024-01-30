from entities.weapons import fists

class Character:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped with {weapon.name}")
        input()
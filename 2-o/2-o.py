from enum import Enum

""" OCP - Open-Closed Principle
Each entity (classes, structures, methods) should be open for extension, but closed for modification. 
In other words, directly changing already existing code should be avoided as much as possible.
Instead, we should try to extend existing code (class inhetirance/ getting existing methods' output and extending it without directly changing the method)
"""


"""We have a character who has a certain weapon and can attack monsters. Everything seems to be working fine. 
However, what if we wanted to and another weapon of a completely different type and display a different message depending on what type of weapon is used?
In this case, we'd have to modify our Weapon class and add a property 'type' to it. 
We'd then have to check for weapon type, which would mean further modifying the existing 'attack' method
"""

# class Weapon:
#     def __init__(self, name: str, damage: int):
#         self.name = name
#         self.damage = damage

#     def __str__(self):
#         return self.name

#     def attack(self):
#             print(f'{self.name} inflicts {self.damage} points of physical damage')


# class Monster:
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def __str__(self):
#         return self.name


# class Character:
#     def __init__(self, name: str, weapon: Weapon):
#         self.name = name
#         self.weapon = weapon

#     def attack(self, weapon: Weapon, target: Monster):
#         print(
#             f'{self.name} is preparing to attack {target}'
#         )
#         weapon.attack()

# needle = Weapon(name="Needle", damage=10)
# arya = Character(name="Arya", weapon=needle)
# white_walker = Monster("White Walker")
# arya.attack(weapon=needle, target=white_walker)


"""Following the Open-Closed principle allows us to write extendable code without the need to directly modify existing entities. 
This way, if we create other types of weapons we'll be able to extend the logic in our newly-created subclasses without the need to change the codebase"""


# Basic interface which requires that every weapon type implements the 'attack' method
class Attacker:
    def attack():
        raise NotImplementedError


# Weapon class that describes common properties for each weapon. It can be subclassed by multiple weapons of different types and different logic can be applied to them
class Weapon(Attacker):
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name


# Subclass that implements the weapon-specific logic
class Sword(Weapon):
    def attack(self):
        print(f"{self.name} inflicts {self.damage} points of damage")


class Monster:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return self.name


class Character:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def __str__(self) -> str:
        return self.name

    def attack(self, target: Monster):
        print(f"{self.name} attacks {target.name}")
        self.weapon.attack()


needle = Sword(name="Needle", damage=10)
arya = Character(name="Arya", weapon=needle)
white_walker = Monster("White Walker")
arya.attack(target=white_walker)

# Import necessary modules
import random

# Example: A simple RPG combat system
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack // 2, self.attack)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

# Create characters
player = Character("Knight", 100, 20)
enemy = Character("Goblin", 50, 15)

# Simulate combat
player.attack_enemy(enemy)
enemy.attack_enemy(player)
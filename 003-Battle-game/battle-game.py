import random

# ----- Base Class -----
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def show_status(self):
        print(f"{self.name} | Health: {self.health}")

# ----- Player Class -----
class Player(Character):
    def heal(self):
        heal_amount = random.randint(5, 10)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")

# ----- Enemy Class -----
class Enemy(Character):
    pass  # No special abilities for now

# ----- Game Logic -----
def battle_game():
    print("🎮 Welcome to Battle Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name, health=50, attack_power=10)
    enemy = Enemy("Goblin", health=40, attack_power=8)

    while player.is_alive() and enemy.is_alive():
        print("\n--- Your Turn ---")
        player.show_status()
        enemy.show_status()

        choice = input("Do you want to (A)ttack or (H)eal? ").lower()
        if choice == 'a':
            player.attack(enemy)
        elif choice == 'h':
            player.heal()
        else:
            print("Invalid choice!")

        # Enemy's turn (only if still alive)
        if enemy.is_alive():
            print("\n--- Enemy's Turn ---")
            enemy.attack(player)

    # Game Over
    if player.is_alive():
        print("\n🏆 You win!")
    else:
        print("\n💀 You lost!")

# Run the game
if __name__ == "__main__":
    battle_game()

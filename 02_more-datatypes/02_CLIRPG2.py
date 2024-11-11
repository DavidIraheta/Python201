# Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending
# on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game.
# This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.
import random

# Set of valid choices and initial inventory
set_of_choices = {"left", "right", "far left", "far right", "look around", "fight", "leave", "inventory", "use"}
inventory = []
items = {"sword": 5, "golden axe": 10, "shield": 3, "potion": 15, "rusty dagger": 2}

# Player and opponent stats
user_attack = random.randint(4, 8)
user_defense = 8
user_health = 10
goblin_attack = random.randint(1, 3)
ogre_attack = random.randint(3, 8)
dragon_attack = random.randint(10, 12)

user_name = input("To get started, please enter your name: ")
print(f"Hello {user_name}! Welcome to Echoes of the Keep!")

while user_health > 0:
    door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower().strip()
    
    if door_choice not in set_of_choices:
        print("Invalid choice. Try again.")
        continue

    if door_choice == "left":
        print("You have entered an empty-looking room.")
        if input("Would you like to look around? yes / no: ").lower() == "yes":
            print("You found a sword!")
            if input("Take the sword? yes / no: ").lower() == "yes":
                inventory.append("sword")
                print("You now have a sword! (Attack Power: 5)")
        print("You have returned to the castle lobby.")

    elif door_choice == "far left":
        print("You enter a room with a chest and are ambushed by an ogre!")
        
        # Battle logic for ogre
        ogre_health = 6
        while user_health > 0 and ogre_health > 0:
            # Prompt to use an item or attack
            action = input("Do you want to 'attack' or 'use' an item? ").lower()
            
            if action == "use":
                # Let user choose item to use
                print("Inventory:", inventory)
                item_choice = input("Choose an item to use: ").lower().strip()
                
                if item_choice == "potion" and "potion" in inventory:
                    user_health += items["potion"]
                    inventory.remove("potion")
                    print(f"You used a potion and restored health. Current health: {user_health}")
                elif item_choice in items and item_choice in inventory:
                    # Temporarily increase attack power with chosen weapon
                    print(f"You used the {item_choice} to increase your attack power.")
                    effective_attack = user_attack + items[item_choice]
                else:
                    print("Item not found or cannot be used.")
                    effective_attack = user_attack
            else:
                # Regular attack without using an item
                effective_attack = user_attack

            # Attack the ogre
            attack_multiplier = random.uniform(0.8, 1.2)
            effective_attack = int(effective_attack * attack_multiplier)
            ogre_health -= effective_attack
            print(f"You attack the ogre! It now has {max(0, ogre_health)} health.")

            if ogre_health <= 0:
                print("You defeated the ogre and found a potion!")
                inventory.append("potion")
                break

            user_health -= ogre_attack
            print(f"The ogre attacks you! You now have {max(0, user_health)} health.")

        if user_health <= 0:
            print("You were defeated by the ogre. Game over.")
            inventory.clear()
            break

        print("You have returned to the castle lobby.")

    elif door_choice == "far right":
        print("You enter a room with two armoires.")
        if input("Open the large armoire? yes / no: ").lower() == "yes":
            print("You found a rusty dagger!")
            if input("Take the rusty dagger? yes / no: ").lower().strip() == "yes":
                inventory.append("rusty dagger")
                print("You now have a rusty dagger! (Attack Power: 2)")
        
        if input("Open the small armoire? yes / no: ").lower() == "yes":
            print("A goblin attacks!")
            
            # Battle logic for goblin
            goblin_health = 2
            while user_health > 0 and goblin_health > 0:
                action = input("Do you want to 'attack' or 'use' an item? ").lower().strip()
                
                if action == "use":
                    print("Inventory:", inventory)
                    item_choice = input("Choose an item to use: ").lower().strip()
                    
                    if item_choice == "potion" and "potion" in inventory:
                        user_health += items["potion"]
                        inventory.remove("potion")
                        print(f"You used a potion and restored health. Current health: {user_health}")
                    elif item_choice in items and item_choice in inventory:
                        print(f"You used the {item_choice} to increase your attack power.")
                        effective_attack = user_attack + items[item_choice]
                    else:
                        print("Item not found or cannot be used.")
                        effective_attack = user_attack
                else:
                    effective_attack = user_attack

                attack_multiplier = random.uniform(0.8, 1.2)
                effective_attack = int(effective_attack * attack_multiplier)
                goblin_health -= effective_attack
                print(f"You attack the goblin! It now has {max(0, goblin_health)} health.")

                if goblin_health <= 0:
                    print("You defeated the goblin! It dropped a golden axe.")
                    if input("Take the golden axe? yes / no: ").lower().strip() == "yes":
                        inventory.append("golden axe")
                    break

                user_health -= goblin_attack
                print(f"The goblin attacks you! You now have {max(0, user_health)} health.")

            if user_health <= 0:
                print("You were defeated by the goblin. Game over.")
                inventory.clear()
                break

        print("You have returned to the castle lobby.")

    elif door_choice == "right":
        print("You have entered a room with a dragon!")
        if input("Would you like to fight the dragon? yes / no: ").lower().strip() == "yes":
            # Check if the player has the golden axe for the dragon fight tt
            if "golden axe" in inventory:
                print("You bravely fight the dragon with your golden axe!")
                
                dragon_health = 10
                while user_health > 0 and dragon_health > 0:
                    action = input("Do you want to 'attack' or 'use' an item? ").lower()
                    
                    if action == "use":
                        print("Inventory:", inventory)
                        item_choice = input("Choose an item to use: ").lower()
                        
                        if item_choice == "potion" and "potion" in inventory:
                            user_health += items["potion"]
                            inventory.remove("potion")
                            print(f"You used a potion and restored health. Current health: {user_health}")
                        elif item_choice in items and item_choice in inventory:
                            print(f"You used the {item_choice} to increase your attack power.")
                            effective_attack = user_attack + items[item_choice]
                        else:
                            print("Item not found or cannot be used.")
                            effective_attack = user_attack
                    else:
                        effective_attack = user_attack

                    attack_multiplier = random.uniform(0.8, 1.2)
                    effective_attack = int(effective_attack * attack_multiplier)
                    dragon_health -= effective_attack
                    print(f"You attack the dragon! It now has {max(0, dragon_health)} health.")

                    if dragon_health <= 0:
                        print("You defeated the dragon and emerged victorious!")
                        break

                    user_health -= dragon_attack
                    print(f"The dragon attacks you! You now have {max(0, user_health)} health.")

                if user_health <= 0:
                    print("You were defeated by the dragon. Game over.")
                    inventory.clear()
                    break
            else:
                print("Without the golden axe, you have no chance. Game over.")
                break
        else:
            print("You chose not to fight the dragon and return to the lobby.")

    if inventory:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"- {item} (Effect: {items.get(item, 'Unknown')})")
    else:
        print("Your inventory is empty.")

print("Thank you for playing!")
from classes.game import bcolors, Person
from classes.magic import Spell
from classes.inventory import Item
import random


# BLACK MAGIC spells
fire = Spell(name = "Fire", cost = 25, dmg = 600, type = "Black")
thunder = Spell(name = "Thunder", cost = 25, dmg = 620, type = "Black")
blizzard = Spell(name ="Blizzard", cost = 25, dmg = 640, type = "Black")
meteor = Spell(name = "Meteor", cost = 30, dmg = 760, type = "Black")
quake = Spell(name = "Quake", cost = 38, dmg = 780, type = "Black")

# WHITE MAGIC spells
heal = Spell(name = "Heal", cost = 25, dmg  = 1200, type = "White")
cure = Spell(name = "Cure", cost = 40, dmg = 2000, type = "White")

# CREATE SOME ITEMS
potion = Item(name = "Potion", type = "potion", description = "Heals 50 HP", prop = 50)
hipotion = Item(name = "Hi-Potion", type = "potion", description = "Heals 100 HP", prop = 100)
superpotin = Item(name = "Super-Potion", type = "potion", description = "Heals 500 HP", prop = 1000)
elixir = Item(name = "Elixir", type = "elixir", description = "Fully restores HP/MP of one party member", prop = 9999)
hielixir = Item(name = "Mega-Elixir", type = "elixir", description = "Fully restores party's HP/MP", prop = 9999)

grenade = Item(name = "Grenade", type = "attack", description = "Deals 800 damage", prop = 800)


# DECLARATION OF THE PLAYERS
player_spells = [meteor, quake, blizzard, cure, heal]

enemy_spells = [fire, meteor, thunder, heal]

player_items = [{"item": potion, "qty": 15},
                {"item": hipotion, "qty": 5},
                {"item": superpotin, "qty": 5},
                {"item": elixir, "qty": 5},
                {"item": hielixir, "qty": 2},
                {"item": grenade, "qty": 5}]

# MULTI-PLAYER DECLARATION
player1 = Person(name = "Khyati", hp = 5234, mp = 150, atk = 400, df = 34, magic = player_spells, items = player_items)  # name, hp, mp, atk, df, magic, items
player2 = Person(name = "Himani", hp = 3440, mp = 350, atk = 333, df = 34, magic = player_spells, items = player_items)
player3 = Person(name = "Saumya", hp = 6460, mp = 100, atk = 558, df = 34, magic = player_spells, items = player_items)

players = [player1, player2, player3]

enemy1 = Person(name = "Witcher", hp = 18200, mp = 300, atk = 530, df = 525, magic = enemy_spells, items = [])
enemy2 = Person(name = "Magus  ", hp = 1250, mp = 250, atk = 650, df = 25, magic = enemy_spells, items = [])
enemy3 = Person(name = "Serpent", hp = 1550, mp = 351, atk = 430, df = 425, magic = enemy_spells, items = [])

enemies = [enemy2, enemy1, enemy3]

running = True
i = 0

print()

print(bcolors.BOLD + bcolors.WARNING + "                                  LET'S BEGIN !!!" + bcolors.ENDC)

while running:
    print("=====================================================================================")
    print()
    print(bcolors.BOLD + bcolors.OKBLUE + "Names:                    HP                                               MP" + bcolors.ENDC)

    for player in players:
        player.get_status()


    print("\n")
    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:
        print("\n")
        player.choose_action()
        choice = input("\t" + bcolors.CYAN + "Choose action: " + bcolors.ENDC)
        index = int(choice) - 1

        # PLAYER IN ATTACK MODE

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print()
            print("You attacked " + enemies[enemy].name.replace("  ", "") + " for " + bcolors.BOLD + bcolors.FAIL + str(dmg) + bcolors.ENDC + " points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " is dead now.")
                del enemies[enemy]

                # CHECK IF BATTLE IS OVER

            if len(enemies) == 0:
                print("=====================================================================================")
                print(bcolors.OKGREEN + bcolors.BOLD + "                                    YOU WON !" + bcolors.ENDC)
                print("=====================================================================================")
                exit()

            if len(players) == 0:
                print("=====================================================================================")
                print(bcolors.FAIL + bcolors.BOLD + "                             ENEMIES HAVE DEFEATED YOU !" + bcolors.ENDC)
                print("=====================================================================================")
                exit()

            print()

        # PLAYER IN MAGIC MODE

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("\t" + bcolors.CYAN + "Choose magic spell: " + bcolors.ENDC)) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if current_mp < spell.cost:
                print(bcolors.FAIL + "\nYou do not have enough magic points" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "White":
                player.heal(magic_dmg)
                print(bcolors.OKGREEN + "\n" + spell.name + " heals for " + str(magic_dmg) + " health pints." + bcolors.ENDC)
            elif spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace("  ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " is dead now.")
                    del enemies[enemy]

                    # CHECK IF BATTLE IS OVER

                if len(enemies) == 0:
                    print("=====================================================================================")
                    print(bcolors.OKGREEN + bcolors.BOLD + "                                    YOU WON !" + bcolors.ENDC)
                    print("=====================================================================================")
                    exit()

                if len(players) == 0:
                    print("=====================================================================================")
                    print(bcolors.FAIL + bcolors.BOLD + "                             ENEMIES HAVE DEFEATED YOU !" + bcolors.ENDC)
                    print("=====================================================================================")
                    exit()

        # PLAYER IN ITEM MODE
        
        elif index == 2:
            player.choose_item()
            item_choice = int(input("\t" + bcolors.CYAN + "Choose item: " + bcolors.ENDC)) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["qty"] == 0:
                print(bcolors.FAIL + "\nNone left......" + bcolors.ENDC)
                continue

            player.items[item_choice]["qty"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + bcolors.OKGREEN + item.name + " heals for " + str(item.prop) + " HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Mega-Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print("\n" + bcolors.OKGREEN + item.name + "Fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print("\n" + bcolors.FAIL + item.name + " deals " + str(item.prop) + " points of damage to " + enemies[enemy].name.replace("  ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace("  ", "") + " is dead now.")
                    del enemies[enemy]

                # CHECK IF BATTLE IS OVER

            if len(enemies) == 0:
                print("=====================================================================================")
                print(bcolors.OKGREEN + bcolors.BOLD + "                                    YOU WON !" + bcolors.ENDC)
                print("=====================================================================================")
                exit()

            if len(players) == 0:
                print("=====================================================================================")
                print(bcolors.FAIL + bcolors.BOLD + "                             ENEMIES HAVE DEFEATED YOU !" + bcolors.ENDC)
                print("=====================================================================================")
                exit()

    # ENEMY IN ACTION

    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        target = random.randrange(0, len(players))

        # ENEMY IN ATTACK MODE

        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " has attacked " + players[target].name + " for " + bcolors.BOLD + bcolors.FAIL + str(enemy_dmg) + bcolors.ENDC + " points of damage.")
            print()

        if players[target].get_hp() == 0:
            print(players[target].name + " is dead now.")
            del players[target]

            # CHECK IF BATTLE IS OVER

        if len(enemies) == 0:
            print("=====================================================================================")
            print(bcolors.OKGREEN + bcolors.BOLD + "                                    YOU WON !" + bcolors.ENDC)
            print("=====================================================================================")
            exit()

        if len(players) == 0:
            print("=====================================================================================")
            print(bcolors.FAIL+ bcolors.BOLD + "                             ENEMIES HAVE DEFEATED YOU !" + bcolors.ENDC)
            print("=====================================================================================")
            exit()


        # ENEMY IN MAGIC MODE

        elif enemy_choice == 1:
            magic_choice = random.randrange(0, len(enemy.magic))
            spell = enemy.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = enemy.get_mp()

            if current_mp < spell.cost:
                print(bcolors.FAIL + "\nYou do not have enough magic points" + bcolors.ENDC)
                continue

            enemy.reduce_mp(spell.cost)

            if spell.type == "White":
                enemy.heal(magic_dmg)
                print(bcolors.OKGREEN + "\n" + spell.name + " heals for " + str(magic_dmg) + " health points." + bcolors.ENDC)
            elif spell.type == "Black":
                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + players[target].name.replace("  ", "") + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " is dead now.")
                    del players[target]

  # CHECK IF BATTLE IS OVER

            if len(enemies) == 0:
                print("=====================================================================================")
                print(bcolors.OKGREEN + bcolors.BOLD + "                                    YOU WON !" + bcolors.ENDC)
                print("=====================================================================================")
                exit()

            if len(players) == 0:
                print("=====================================================================================")
                print(bcolors.FAIL + bcolors.BOLD + "                             ENEMIES HAVE DEFEATED YOU !" + bcolors.ENDC)
                print("=====================================================================================")
                exit()



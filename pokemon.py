import random

# Bulbasaur's Stats
pokemonHP = 100

# Bulbasaur's Skills
vineWhipDMG = 20
razorLeafDMG = 25
tackleDMG = 10

# Enemy Stats
enemyName = "Rat"
enemyHP = 80



print("=== Pokemon Battle  ===")
print("My Pokemon: Bulbasaur\n")
print(f"A wild {enemyName} appeared!")
print("Go, Bulbasaur!")

turn = 1

while enemyHP > 0 and pokemonHP > 0:
    print(f"\n--- Turn {turn} ---")
    print(f"Bulbasaur HP: {pokemonHP}")
    print(f"{enemyName} HP: {enemyHP}")

    print("\nChoose a skill:")
    print("1. Vine Whip")
    print("2. Razor Leaf")
    print("3. Tackle")
    print("4. Run")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print("\nBulbasaur used Vine Whip!")
        enemyHP = enemyHP - vineWhipDMG
        
    elif choice == "2":
        print("\nBulbasaur used Razor Leaf!")
        enemyHP = enemyHP - razorLeafDMG
        
    elif choice == "3":
        print("\nBulbasaur used Tackle!")
        enemyHP = enemyHP - tackleDMG
        
    elif choice == "4":
        print("\nBulbasaur ran away from the battle!")
        break
        
    else:
        print("Invalid choice. Bulbasaur wasted a turn!")
        

    if enemyHP <= 0:
        print(f"\n{enemyName} fainted! Bulbasaur wins!")
        break

    # Enemy attack with a random damage amount
    enemyAtk = random.randint(15, 30)
    pokemonHP = pokemonHP - enemyAtk
    print(f"{enemyName} attacked back for {enemyAtk} damage!")

    if pokemonHP <= 0:
        print(f"\nBulbasaur fainted! {enemyName} wins!")
        break
        
    turn += 1

print("\n=== Battle Over ===")

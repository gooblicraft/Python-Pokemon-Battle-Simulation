class Pokemon: 
    def __init__ (self, name, health, damage, skills):
        self.name=name
        self.health=health
        self.damage=damage
        self.skills=skills

    
    def run(self):
        print(f"{self.name} ran away!")

pikachu = Pokemon(
    "Pikachu",
    100,
    1,
    {
        "thunder fart": 99,
        "lightning strike": 1,
        "lightning whatever": 23,
        "i dont play pokemon attack": 100
    }
)

print(pikachu.name)
print(pikachu.health)
print(pikachu.damage)
print(pikachu.skills)
pikachu.run()
class Skill:
    def __init__(self, name, dmg, stun):
        self.name=name
        self.dmg=dmg
        self.stun=stun

class Pokemon: 
    def __init__ (self, name, health, skills):

        self.name=name
        self.health=health
        self.skills=skills

##skill list
#PIKACHU
pika1=Skill("thunder fart", 99, 100)
pika2=Skill("lightning whatever", 99, 100)
pika3=Skill("i dont play pokemon attack", 99, 100)

pokedex={
    "pikachu": Pokemon(
        "Pikachu",
        100,
        [pika1, pika2, pika3]
    ),
}

p1 = pokedex["pikachu"]

print(p1.name)
print(p1.health)
print("--------------------------")
print(p1.skills[0].name)
print(p1.skills[0].dmg)
print(p1.skills[0].stun)

print(p1.skills[1].name)
print(p1.skills[1].dmg)
print(p1.skills[1].stun)

print(p1.skills[2].name)
print(p1.skills[2].dmg)
print(p1.skills[2].stun)
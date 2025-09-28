# Base class - Blueprint for all superheroes
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Different superhero types that inherit from Superhero
class Flyer(Superhero):
    def move(self):
        return "🦸♂️ Flying through the sky!"
    
    def use_power(self):  
        return f"{self.name} soars high with {self.power}!"

class Swimmer(Superhero):
    def move(self):
        return "🏊♂️ Swimming through water!"
    
    def use_power(self):  
        return f"{self.name} dives deep with {self.power}!"

# Demonstration
def main():
    # Create superhero objects
    superman = Flyer("Superman", "super strength")
    aquaman = Swimmer("Aquaman", "water control")
    
    print("=== SUPERHERO SHOWCASE ===")
    
    # Polymorphism in action - same method, different behaviors
    heroes = [superman, aquaman]
    
    for hero in heroes:
        print(f"\n{hero.name}:")
        print(f"Power: {hero.use_power()}")  # Polymorphism!
        print(f"Movement: {hero.move()}")    # Each has unique movement


if __name__ == "__main__":
    main()
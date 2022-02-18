class Pet: 
    def __init__(self, name, type, tricks):
        self.name = name 
        self.type = type 
        self.tricks = tricks 
        self.health = 100
        self.energy = 50 
    
    def sleep(self):
        self.energy += 25 
        return self 
    
    def eat(self):
        self.energy += 5 
        self.health += 10 
        print(f"Total Health: {self.health} Total Energy: {self.energy}")
        return self 
    
    def play(self):
        self.health += 5 
        print(f"Total Health: {self.health} Total Energy: {self.energy}")
        print("Thanks for the walk owner :))")
        return self 

    def noise(self):
        print("Hehe")
        return self 

class Ninja:
    def __init__(self, firstName, lastName, treats, petFood):
        self.firstName = firstName 
        self.lastName = lastName
        self.treats = treats 
        self.petfood = petFood 
        self.pet = Pet("Bunny", "doggie", "he could fly") 
    
    def walk(self):
        self.pet.play()
        return self 
    
    def feed(self):
        self.pet.eat() 
        print(f'{self.pet.name} is eating {self.petfood}.')
        return self 
    
    def bathe(self):
        self.pet.noise()
        return self 

bunny = Pet("Bunny", "doggie", "he could fly")
zee = Ninja("Zainab", "Mirza", ['bacon', 'bone'], 'steak')

zee.feed()
zee.walk()
zee.bathe()


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


class Lion(Pet): 
    def __init__(self, name, tricks, location):
        super().__init__(self, name, tricks)
        self.location = location 
    
    def sleep(self):
        super().sleep()
        return self 
    
    def eat(self):
        super().eat()
        return self 
    
    def play(self):
        super().play()
        return self 


class Ninja:
    def __init__(self, firstName, lastName, treats, pet, petFood):
        self.firstName = firstName 
        self.lastName = lastName
        self.treats = treats 
        self.petfood = petFood 
        self.pet = pet 
    
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

bunny = Pet("Bunny", "doggie", "fly")
zee = Ninja("Zainab", "Mirza", ['bacon', 'bone'], bunny, 'steak')
zee.feed()
zee.walk()
zee.bathe()


lolo = Lion("lolo", "super speed", "safari desert")
lolo.play()
lolo.sleep()
lolo.eat()

# Soldier
import random 

class Soldier:
    def __init__(self,health=0, strength=0):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage
        return
    

# Viking


class Viking(Soldier):
    def __init__(self,name='',health=0,strength=0):

        Soldier.__init__(self,name,strength)
        self.name = name
        self.strength = strength
        self.health = health
        
        

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0: return (f"{self.name} has received {damage} points of damage")
        else: return (f"{self.name} has died in act of combat")
            

    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health=0, strength=0):
        super().__init__(self)
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0: 
            return (f"A Saxon has received {damage} points of damage")
        else: 
            return "A Saxon has died in combat"
    

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
       
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        return

    def vikingAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        a = s.receiveDamage(v.attack())
        #s.health = s.health - v.attack(v)
        if s.health <= 0 :
            self.saxonArmy.remove(s)
        return a
      

    
    def saxonAttack(self):
        s=random.choice(self.saxonArmy)
        v=random.choice(self.vikingArmy)
        a = v.receiveDamage(s.attack())
        #v.health =  v.health - s.attack(s)
        if v.health <= 0 :
            self.vikingArmy.remove(v)
        return a
        

    def showStatus(self):
        lista_vacia=[]
        if self.saxonArmy == lista_vacia:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == lista_vacia:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        





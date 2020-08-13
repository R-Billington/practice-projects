class Pokemon:
    def __init__(self, name, level, type, health, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = 4 * level
        if health == 'max':
            self.health = 4 * level
        else:
            self.health = health
        self.is_knocked_out = is_knocked_out
        
    def lose_health(self, damage):
        self.health -= damage
        print('{} took {} points of damage!\nThey have {} health points left.\n'.format(self.name, damage, self.health))
        if self.health <= 0:
            self.knock_out()
            
    def gain_health(self, healed_amount):
        if self.health + healed_amount > self.max_health:
            healed_amount = self.max_health - self.health
            
        self.health += healed_amount
        print('{} healed for {} points and now has {} health! \n'.format(self.name, healed_amount, self.health))
        
    def knock_out(self):
        self.health = 0
        self.is_knocked_out = True
        print('{} fainted!\n'.format(self.name))
        
    def revive(self):
        self.is_knocked_out = False
        self.health = self.max_health / 2
        print('{} was revived with {} health! \n'.format(self.name, self.health))
        
    def attack(self, other):
        has_advantage = None
        has_disadvantage = None
        if self.type == 'Fire':
            if other.type =='Water':
                has_advantage = False
                has_disadvantage = True
            elif other.type == 'Grass':
                has_advantage = True
                has_disadvantage = False
            elif other.type == 'Fire':
                has_advantage = False
                has_disadvantage = False
        if self.type == 'Water':
            if other.type =='Water':
                has_advantage = False
                has_disadvantage = False
            elif other.type == 'Grass':
                has_advantage = False
                has_disadvantage = True
            elif other.type == 'Fire':
                has_advantage = True
                has_disadvantage = False
        if self.type == 'Grass':
            if other.type =='Water':
                has_advantage = True
                has_disadvantage = False
            elif other.type == 'Grass':
                has_advantage = False
                has_disadvantage = False
            elif other.type == 'Fire':
                has_advantage = False
                has_disadvantage = True
        
        attack_power = None
        if has_advantage:
            attack_power = self.level * 2
        elif has_disadvantage:
            attack_power = self.level / 2
        else:
            attack_power = self.level
        
        other.lose_health(attack_power)
        
        
class Trainer:
    def __init__(self, name, pokemon, potions, active_pokemon):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions
        self.active_pokemon = active_pokemon
        
    def use_potion(self):
        print('{} is using a potion!'.format(self.name))
        self.pokemon[self.active_pokemon].gain_health(100)
        self.potions -= 1
        print('{} has {} potions left. \n'.format(self.name, self.potions))
        
    def attack_other_trainer(self, other):
        print('{}\'s {} is attacking {}\'s {}!\n'.format(self.name, self.pokemon[self.active_pokemon].name, other.name, other.pokemon[other.active_pokemon].name))
        self.pokemon[self.active_pokemon].attack(other.pokemon[other.active_pokemon])
        
    def switch_pokemon(self, new_pokemon):
        print('{} switched pokemon. Go {}! \n'.format(self.name, self.pokemon[new_pokemon].name))
        self.active_pokemon = new_pokemon
        
        
        
charizard = Pokemon('Charizard', 50, 'Fire', 'max', False)
venusaur = Pokemon('Venusaur', 50, 'Grass', 'max', False)
blastoise = Pokemon('Blastoise', 50, 'Water', 'max', False)

ash = Trainer('Ash', [charizard, venusaur, blastoise], 3, 0)
brock = Trainer('Brock', [charizard, venusaur, blastoise], 3, 1)

ash.attack_other_trainer(brock)
brock.use_potion()
ash.switch_pokemon(2)
brock.attack_other_trainer(ash)
ash.attack_other_trainer(brock)
brock.attack_other_trainer(ash)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
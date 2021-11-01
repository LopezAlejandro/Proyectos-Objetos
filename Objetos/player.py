class Player:

    vocation = "No vocation"
    spell = "Puff"
    movement_speed = 50

    def __init__(self,**kwargs) :
        self.hit_point = kwargs.get('hit_point',50)
        self.mana = kwargs.get('mana',50)
        self.name = input("Elige tu nombre : ")

    def __str__(self):
        return "{} es un  {} tiene {} de vida y {} de mana , puede lanzar {} y corre a {} movement speed\n".format(
                    self.name,
                    self.vocation,
                    self.hit_point,
                    self.mana,
                    self.cast_spell(),
                    self.movement_speed)

    def cast_spell(self):
        return self.spell

class Sorcerer(Player):

    vocation = "Sorcerer"
    spell = "Utevo Lux"
    movement_speed = 20

class Knight(Player):

    vocation = "Knigth"
    spell = "Exordi"
    movement_speed = 80

class Paladin(Player):

    vocation = "Paladin"
    spell = "Spiderman"
    movement_speed = 50

class Druid(Player):

    vocation = "Druid"
    spell = "Super Tree"
    movement_speed = 20
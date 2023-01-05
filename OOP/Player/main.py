#import the file name.
from player import Player

#creating the class of the Player class.
tim = Player("Tim")

from enemy import Enemy
random_monster = Enemy("Basic Enemy", 12, 1)
random_monster.take_damage(4)

print(random_monster)
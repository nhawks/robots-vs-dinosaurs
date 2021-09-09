from weapon import Weapon


class Robot:
  
  def __init__ (self, robot_name):
    self.robot_name = robot_name
    self.robot_health = 10
    self.robot_weapon = Weapon("sword")

  #attack selected dinosaur  
  def attack(self, dinosaur):
    dinosaur.dinosaur_health -= self.robot_weapon.weapon_damage
    print (
f"{self.robot_name} attacked {dinosaur.dinosaur_name} with {self.robot_weapon.weapon_name}\n\
{self.robot_weapon.weapon_name} dealt {self.robot_weapon.weapon_damage} damage!\n\
{dinosaur.dinosaur_name}'s Health is now: {dinosaur.dinosaur_health}/10!"
)
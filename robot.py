from weapon import Weapon


class Robot:
  
  def __init__ (self, robot_name):
    self.robot_name = robot_name
    self.robot_health = 10
    self.robot_weapon = Weapon("sword")

  #attack selected dinosaur  
  def attack(self, dinosaur):
    pass
  ##* end of class Robot 
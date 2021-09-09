import random
from weapon import Weapon
from herd import Herd

class Robot:
  
  #will be used to copy list to Fleet.robot_fleet
  created_robots = []

  def __init__ (self, robot_name):
    self.robot_name = robot_name
    self.robot_health = 10
    self.robot_weapon = Weapon("sword")

    #add each robot object to created_robots
    Robot.created_robots.append(self)

  #select a random dinosaur for opponent then attack    
  def attack(self, dinosaur):
    dinosaur = random.choice(Herd.dinosaur_herd)
    print(f"Opponent: {dinosaur.dionsaur.firstname}")
    dinosaur.dinosaur_health -= self.robot_weapon.weapon_damage
  #end of class Robot 
  

#Instance Robot Objects
robot_one = (Robot("Vanquish-X4"))
robot_two = (Robot("Neon-VX4"))
robot_three = (Robot("Leo-BE3"))
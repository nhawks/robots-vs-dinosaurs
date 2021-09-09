from weapon import Weapon

class Robot:
  
  #will be used to copy list to Fleet.robot_fleet
  created_robots = []

  def __init__ (self, robot_name):
    self.robot_name = robot_name
    self.robot_health = 10
    self.robot_weapon = Weapon("sword")

    #add each robot object to created_robots
    Robot.created_robots.append(self)

#Instance Robot Objects
robot_one = (Robot("Vanquish-X4"))
robot_two = (Robot("Neon-VX4"))
robot_three = (Robot("Leo-BE3"))
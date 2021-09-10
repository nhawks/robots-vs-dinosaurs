from weapon import Weapon
from robot import Robot


class Fleet:

  fleet_weapons = ["sword", "laser", "handcannon"]

  def __init__ (self):
    self.robots = []
    self.create_fleet()
 
  #create a fleet of robots and append to self.robots
  def create_fleet (self): #void
    robot_one = (Robot("Vanquish-X4"))
    robot_two = (Robot("Neon-VX4"))
    robot_three = (Robot("Leo-BE3"))
    self.robots.append(robot_one)
    self.robots.append(robot_two)
    self.robots.append(robot_three)
  #end of class Fleet
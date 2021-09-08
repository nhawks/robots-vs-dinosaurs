from weapon import Weapon

class Robot:
  def __init__ (self, robot_name):
    self.robot_name = robot_name
    self.robot_health = 10
    self.robot_weapon = Weapon("sword")


# robot_one = Robot("Test-X")
# print(robot_one.robot_name)
# print(robot_one.robot_health)
# print(robot_one.robot_weapon.weapon_name)
# print(robot_one.robot_weapon.attack_power)

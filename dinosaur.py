class Dinosaur:

  def __init__ (self, dinosaur_name, attack_power):
    self.dinosaur_name = dinosaur_name
    self.attack_name = ""
    self.attack_power = attack_power
    self.dinosaur_health = 10
    self.dinosaur_energy_level = 100

  #attack selected robot
  def attack (self, robot): #void
    self.dinosaur_energy_level -= 10
    robot.robot_health -= self.attack_power
    print (
f"{self.dinosaur_name} attacked {robot.robot_name} with {self.attack_name.upper()}!\n\
{self.attack_name.upper()} dealt {self.attack_power} damage!\n\
{robot.robot_name}'s Health is now: {robot.robot_health}/10!"
)
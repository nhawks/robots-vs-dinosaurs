from fleet import Fleet
from herd import Herd


class Battlefield:

  def __init__ (self):
    self.fleet = Fleet()
    self.herd = Herd()

  def run_game(self): #void
    pass 

  def display_welcome (self): #void
    pass

  def battle (self): #void
    self.selected_dinosaur
    pass

  def selected_dinosaur (self):
    self.show_dinosaur_opponent_options()
    fighter = int(input("Please select one number to select the fighter you'd like to choose: "))
    self.dinosaur_turn(fighter)

  def selected_robot (self):
    self.show_robot_opponent_options()
    fighter = int(input("Please select one number to select the fighter you'd like to choose: "))
    return fighter

  def dinosaur_turn (self, dinosaur): #void
    dinosaur = self.herd.dinosaurs[dinosaur]
    self.show_robot_opponent_options()
    opponent_index = int(input("Please select one number to select your opponent: "))
    opponent = self.fleet.robots[opponent_index]
    self.dinosaur.attack(opponent)
    #TODO: add optiont to select the fighter's weapon
    #old cold below
    # self.herd.dinosaur.attack(opponent)
    # fighter = int(input("Please select one number to select the fighter you'd like to choose: "))
    # dinosaur = self.herd.dinosaurs[fighter]

  def robot_turn (self, robot): #void
    robot = self.fleet.robots[robot]
    self.show_robot_opponent_options()
    opponent_index = int(input("Please select one number to select your opponent: "))
    opponent = self.herd.dinosaurs[opponent_index]
    self.robot.attack(opponent)
    #TODO: add optiont to select the fighter's weapon

  def show_dinosaur_opponent_options (self): #void
    for dinosaur in self.herd.dinosaurs:
      print(f"{self.herd.dinosaurs[dinosaur]} - {dinosaur.name}\n")

  def show_robot_opponent_options (self): #void
    for robot in self.fleet.robots:
      print(f"{self.fleet.robots[robot]} - {robot.name}")

  def display_winners (self): #void
    pass
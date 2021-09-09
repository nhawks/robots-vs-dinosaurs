from fleet import Fleet
from herd import Herd


class Battlefield:

  def __init__ (self):
    self.fleet = Fleet()
    self.herd = Herd()
    self.run_game()

  def run_game(self): #void
    self.display_welcome()
    self.battle()
    self.display_winners()

  def display_welcome (self): #void
    print("\nWelcome to ROBOTS vs DINOSAURS\nMay the best team win!")

  def battle (self): #void
    while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
      self.selected_dinosaur(), self.selected_robot()
      # self.choose_attacking_team()
      # print("\nTHE HERD\n")
      # self.selected_dinosaur()
      # if len(self.fleet.robots) > 0:
      #   print("\nTHE FLEET\n")
      #   self.selected_robot()

  def selected_dinosaur (self):
    print("\nTHE HERD\n")
    self.show_dinosaur_opponent_options()
    fighter = int(input("\nPlease enter one number to select the fighter you'd like to choose: "))
    self.dinosaur_turn(fighter)

  def selected_robot (self):
    print("\nTHE FLEET\n")
    self.show_robot_opponent_options()
    fighter = int(input("\nPlease enter one number to select the fighter you'd like to choose: "))
    self.robot_turn(fighter)

  def dinosaur_turn (self, dinosaur): #void
    dinosaur = self.herd.dinosaurs[dinosaur]
    print(f"You chose: {dinosaur.dinosaur_name}\n")
    self.show_robot_opponent_options()
    opponent_index = int(input("\nPlease select one number to select your opponent: "))
    opponent = self.fleet.robots[opponent_index]
    print(f"\n{dinosaur.dinosaur_name} vs. {opponent.robot_name}")
    dinosaur.attack(opponent)

    #TODO: add optiont to select the fighter's weapon
    #old cold below
    # self.herd.dinosaur.attack(opponent)
    # fighter = int(input("Please select one number to select the fighter you'd like to choose: "))
    # dinosaur = self.herd.dinosaurs[fighter]

  def robot_turn (self, robot): #void
    robot = self.fleet.robots[robot]
    print(f"You chose: {robot.robot_name}\n")
    self.show_dinosaur_opponent_options()
    opponent_index = int(input("Please select one number to select your opponent: "))
    opponent = self.herd.dinosaurs[opponent_index]
    print(f"\n{robot.robot_name} vs. {opponent.dinosaur_name}")
    robot.attack(opponent)
    #TODO: add optiont to select the fighter's weapon
    self.next_team = "herd"


  def show_dinosaur_opponent_options (self): #void
    for dinosaur in self.herd.dinosaurs:
      print(f"{self.herd.dinosaurs.index(dinosaur)} - {dinosaur.dinosaur_name} | Health: {dinosaur.dinosaur_health}/10")

  def show_robot_opponent_options (self): #void
    for robot in self.fleet.robots:
      print(f"{self.fleet.robots.index(robot)} - {robot.robot_name} | Health: {robot.robot_health}")

        
     

  def display_winners (self): #void
    pass
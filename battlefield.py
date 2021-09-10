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
    while len(self.herd.dinosaurs) != 0 and len(self.fleet.robots) != 0:
      if self.herd.dinosaurs:
        self.selected_dinosaur(), 
      if self.fleet.robots:
        self.selected_robot()
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
    self.check_robot_health(opponent, dinosaur, opponent_index)
    #TODO: add optiont to select the fighter's weapon

  def robot_turn (self, robot): #void
    robot = self.fleet.robots[robot]
    print(f"You chose: {robot.robot_name}\n")
    self.show_dinosaur_opponent_options()
    opponent_index = int(input("Please select one number to select your opponent: "))
    opponent = self.herd.dinosaurs[opponent_index]
    print(f"\n{robot.robot_name} vs. {opponent.dinosaur_name}")
    robot.attack(opponent)
    self.check_dino_health(opponent, robot, opponent_index)
    #TODO: add optiont to select the fighter's weapon

  def show_dinosaur_opponent_options (self): #void
    for dinosaur in self.herd.dinosaurs:
      print(f"{self.herd.dinosaurs.index(dinosaur)} - {dinosaur.dinosaur_name} | Health: {dinosaur.dinosaur_health}/10")

  def show_robot_opponent_options (self): #void
    for robot in self.fleet.robots:
      print(f"{self.fleet.robots.index(robot)} - {robot.robot_name} | Health: {robot.robot_health}")

  #methods to determine if robot/dinosaur health > 0, if not remove from game (list)
  def check_dino_health(self, dinosaur, robot, dino_index):
    self.dino_index = dino_index
    if dinosaur.dinosaur_health <= 0:
      del self.herd.dinosaurs[dino_index]
      print(f"{robot.robot_name} defeated {dinosaur.dinosaur_name}")
  
  def check_robot_health(self, robot, dinosaur, robot_index):
    self.robot_index = robot_index
    if robot.robot_health <= 0:
      del self.fleet.robots[robot_index]
      print(f"{dinosaur.dinosaur_name} defeated {robot.robot_name}")

  #runs if the herd or fleet len(list) == 0
  def display_winners (self): #void
    if len(self.fleet.robots) == 0:
      print("THE HERD WINS: The fleet was defeated!")
    elif len(self.herd.dinosaurs) == 0:
      print("THE FLEET WINS: The herd was defeated!")
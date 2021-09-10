from fleet import Fleet
from herd import Herd


class Battlefield:

  def __init__ (self):
    self.fleet = Fleet()
    self.herd = Herd()
    self.run_game() #starts game everytime Battlefield() is called 

  def run_game(self): #void
    
    #Start the game with a welcome msg
    self.display_welcome()

    #run battle while loop until a team loses
    self.battle()

    #once team loses end the game and display the winners
    self.display_winners()

  def display_welcome (self): #void
    print("\nWelcome to ROBOTS vs DINOSAURS\nMay the best team win!")

  def battle (self): #void
    while len(self.herd.dinosaurs) != 0 and len(self.fleet.robots) != 0:
      if self.herd.dinosaurs:
        self.selected_dinosaur(), 
      if self.fleet.robots:
        self.selected_robot()
 
  #methods that displays the current team members that a user can pick
  def selected_dinosaur (self):
    print("\nTHE HERD: Attacking - Choose your Dinosaur!\n")
    self.show_dinosaur_opponent_options()
    fighter = int(input("\nPlease enter a number to select the dinosaur you'd like to choose: "))
    self.dinosaur_turn(fighter)

  def selected_robot (self):
    print("\nTHE FLEET: Attacking - Choose your Robot!\n")
    self.show_robot_opponent_options()
    fighter = int(input("\nPlease enter a number to select the robot you'd like to choose: "))
    self.robot_turn(fighter)

  #methods that attack the opposite team member by selection 
  #then calls a method to determine if opponenet's health > 0
  def dinosaur_turn (self, dinosaur): #void
    dinosaur = self.herd.dinosaurs[dinosaur]
    print(f"You chose: {dinosaur.dinosaur_name.upper()}\n")
    print("THE FLEET: Defending - Choose your opponent! \n")
    self.show_robot_opponent_options()
    opponent_index = int(input("\nPlease enter a number to select your opponent: "))
    opponent = self.fleet.robots[opponent_index]
    print(f"\n{dinosaur.dinosaur_name.upper()} vs. {opponent.robot_name.upper()}")
    dinosaur.attack(opponent)
    self.check_robot_health(opponent, dinosaur, opponent_index)
    #TODO: add optiont to select the fighter's weapon

  def robot_turn (self, robot): #void
    robot = self.fleet.robots[robot]
    print(f"You chose: {robot.robot_name.upper()}\n")
    print("THE HERD: Defending - Choose your opponent!\n")
    self.show_dinosaur_opponent_options()
    opponent_index = int(input("Please enter a number to select your opponent: "))
    opponent = self.herd.dinosaurs[opponent_index]
    print(f"\n{robot.robot_name.upper()} vs. {opponent.dinosaur_name.upper()}")
    robot.attack(opponent)
    self.check_dino_health(opponent, robot, opponent_index)
    #TODO: add optiont to select the fighter's weapon

  #methods that display the current robots/dinosaurs and their health
  def show_dinosaur_opponent_options (self): #void
    for dinosaur in self.herd.dinosaurs:
      print(f"{self.herd.dinosaurs.index(dinosaur)} - {dinosaur.dinosaur_name} | Health: {dinosaur.dinosaur_health}/10")

  def show_robot_opponent_options (self): #void
    for robot in self.fleet.robots:
      print(f"{self.fleet.robots.index(robot)} - {robot.robot_name} | Health: {robot.robot_health}/10")

  #methods to determine if robot/dinosaur health > 0, if not remove from game (del list[i])
  def check_dino_health(self, dinosaur, robot, dino_index):
    self.dino_index = dino_index
    if dinosaur.dinosaur_health <= 0:
      del self.herd.dinosaurs[dino_index]
      print(f"\n{robot.robot_name.upper()} DEFEATED {dinosaur.dinosaur_name.upper()}!")
  
  def check_robot_health(self, robot, dinosaur, robot_index):
    self.robot_index = robot_index
    if robot.robot_health <= 0:
      del self.fleet.robots[robot_index]
      print(f"\n{dinosaur.dinosaur_name.upper()} DEFEATED {robot.robot_name.upper()}!")

  #runs if the herd or fleet len(list) == 0
  def display_winners (self): #void
    if len(self.fleet.robots) == 0:
      print("\nTHE HERD WINS: The Fleet was defeated!\nGAME OVER!")
    elif len(self.herd.dinosaurs) == 0:
      print("\nTHE FLEET WINS: The Herd was defeated!\nGAME OVER!")
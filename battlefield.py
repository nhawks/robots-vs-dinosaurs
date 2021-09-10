from fleet import Fleet
from herd import Herd
from weapon import Weapon
from dino_attacks import DinoAttacks


class Battlefield:

  def __init__ (self):
    self.fleet = Fleet()
    self.herd = Herd()
    self.run_game() ##?starts game everytime Battlefield() is called 

  def run_game(self): #void
    
    ##*Start the game with a welcome msg
    self.display_welcome()

    ##*run battle while loop until a team loses
    self.battle()

    ##*once team loses end the game and display the winners
    self.display_winners()

  def display_welcome (self): #void
    print("\nWelcome to ROBOTS vs DINOSAURS\nMay the best team win!")

  def battle (self): #void
    while len(self.herd.dinosaurs) != 0 and len(self.fleet.robots) != 0:
      if self.herd.dinosaurs:
        self.selected_dinosaur(), 
      if self.fleet.robots:
        self.selected_robot()
 
  ##*methods that displays the current team members that a user can pick
  def selected_dinosaur (self):
    print("\nTHE HERD: Attacking - Choose your Dinosaur!")
    self.show_dinosaur_opponent_options()
    fighter = int(input("\nPlease enter a number to select the dinosaur you'd like to choose: "))
    self.dinosaur_turn(fighter)

  def selected_robot (self):
    print("\nTHE FLEET: Attacking - Choose your Robot!")
    self.show_robot_opponent_options()
    fighter = int(input("\nPlease enter a number to select the robot you'd like to choose: "))
    self.robot_turn(fighter)

  #* robot and dinosaur attack selection methods

  #*prompts the robot to select a weapon
  def pick_robot_weapon (self, robot):
    self.robot = robot

    #?run if robot doesn't have a weapon, else skip
    if self.robot.robot_weapon.weapon_name == "":

      #?store new weapon values in loadout which calls Weapon class
      loadout = Weapon( input(
      f"Fleet Weapons {self.fleet.fleet_weapons}\n"\
      "Please enter the name of the weapon you'd like to choose: ").lower() )

      #?assign new weapon values based on selection
      self.robot.robot_weapon.weapon_name = loadout.weapon_name
      self.robot.robot_weapon.weapon_damage = loadout.weapon_damage
      
      #?once weapon is selected del from list so other robots can't choose the weapon
      weapon_index = self.fleet.fleet_weapons.index(loadout.weapon_name)
      del self.fleet.fleet_weapons[weapon_index]
      return self.robot #return weapon values in robot

  #*prompts the dinosaur each time before attacking to select an attack
  def pick_dino_attack (self, dinosaur):
    self.dinosaur = dinosaur

    #?store values in attack_info which calls DinoAttack Class
    attack_info = DinoAttacks( input(
      f"Dinosaur Attacks {self.herd.herd_attacks}\n"\
      "Please enter the name of the attack you'd like to choose: ").lower() )

    #?assign new attack values based on selection 
    self.dinosaur.attack_power = attack_info.attack_damage
    self.dinosaur.attack_name = attack_info.attack_name
    return self.dinosaur #return attack info in dinosaur

  #*methods that attack the opposite team member by selection 
  #*then calls a method to determine if opponenet's health > 0
  def dinosaur_turn (self, dinosaur): #void
    dinosaur = self.herd.dinosaurs[dinosaur]
    self.pick_dino_attack(dinosaur)
    print(f"You chose: {dinosaur.dinosaur_name.upper()}\n"\
          "\nTHE FLEET: Defending - Choose your opponent!")
    self.show_robot_opponent_options()
    opponent_index = int(input("\nPlease enter a number to select your opponent: "))
    opponent = self.fleet.robots[opponent_index]
    print(f"\n{dinosaur.dinosaur_name.upper()} vs. {opponent.robot_name.upper()}")
    dinosaur.attack(opponent)
    self.check_robot_health(opponent, dinosaur, opponent_index)

  def robot_turn (self, robot): #void
    robot = self.fleet.robots[robot]
    self.pick_robot_weapon(robot)
    print(f"You chose: {robot.robot_name.upper()}\n"\
          "\nTHE HERD: Defending - Choose your opponent!")
    self.show_dinosaur_opponent_options()
    opponent_index = int(input("\nPlease enter a number to select your opponent: "))
    opponent = self.herd.dinosaurs[opponent_index]
    print(f"\n{robot.robot_name.upper()} vs. {opponent.dinosaur_name.upper()}")
    robot.attack(opponent)
    self.check_dino_health(opponent, robot, opponent_index)

  ##*methods that display the current robots/dinosaurs and their health
  def show_dinosaur_opponent_options (self): #void
    for dinosaur in self.herd.dinosaurs:
      self.show_dinosaur_info(dinosaur)

  def show_robot_opponent_options (self): #void
    for robot in self.fleet.robots:
      self.show_robot_info(robot)

  #*methods for displaying info for a robot/dinosaur
  def show_dinosaur_info (self, dinosaur):
    self.dinosaur = dinosaur
    print(f"{self.herd.dinosaurs.index(dinosaur)} - {dinosaur.dinosaur_name} | "\
          f"Health: {dinosaur.dinosaur_health}/10 | "\
          f"Energy Level: {dinosaur.dinosaur_energy_level}/100")

  def show_robot_info (self, robot):
    self.robot = robot
    print(f"{self.fleet.robots.index(robot)} - {robot.robot_name} | "\
          f"Health: {robot.robot_health}/10 | "\
          f"Power Level: {robot.robot_power_level}/100")

  #*methods to determine if robot/dinosaur health > 0, else remove from game (del list[i])
  #! NOTE for instructor: I had to use del because remove would re-populate the list when I called display_winners
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

  #*runs if the herd or fleet len(list) == 0
  def display_winners (self): #void
    if len(self.fleet.robots) == 0:
      print("\nTHE HERD WINS: The Fleet was defeated!\nGAME OVER!")
    elif len(self.herd.dinosaurs) == 0:
      print("\nTHE FLEET WINS: The Herd was defeated!\nGAME OVER!")
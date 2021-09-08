class Weapon:
  def __init__ (self, weapon_name):
      self.weapon_name = weapon_name
      self.attack_power = self.weapon_power(weapon_name)


  def weapon_power (self, weapon_name):
    if weapon_name == "sword":
      attack_power = 2
      return attack_power


# Weapon("sword")

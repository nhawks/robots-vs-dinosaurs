class Weapon:
  def __init__ (self, weapon_name):
      self.weapon_name = weapon_name
      self.weapon_damage = self.get_weapon_damage(weapon_name)


  def get_weapon_damage (self, weapon_name):
    if weapon_name == "sword":
      weapon_damage = 2
      return weapon_damage
      ##*end of class Weapon
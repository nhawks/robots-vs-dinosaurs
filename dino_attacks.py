class DinoAttacks:
  
  def __init__ (self, attack_name):
      self.attack_name = attack_name
      self.attack_damage = self.get_attack_damage(attack_name)
  
  def get_attack_damage (self, attack_name):
    if attack_name == "headbutt":
      attack_damage = 2
    elif attack_name == "tailwhip":
      attack_damage = 3
    elif attack_name == "bite":
      attack_damage = 4
    else:
      attack_damage = 0
    return attack_damage
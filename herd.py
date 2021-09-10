from dinosaur import Dinosaur


class Herd:

  herd_attacks = ("headbutt", "tailwhip", "bite")

  def __init__ (self):
    self.dinosaurs = []
    self.create_herd()
  
  #create a herd of dinosaurs and append to self.dinosaurs
  def create_herd (self): #void
    #Dinosaur(name, attack_power)
    dinosaur_one = Dinosaur("Pteranodon", 0)
    dinosaur_two = Dinosaur("Cearadactylus", 0)
    dinosaur_three = Dinosaur("Tropeognathus", 0)

    self.dinosaurs.append(dinosaur_one)
    self.dinosaurs.append(dinosaur_two)
    self.dinosaurs.append(dinosaur_three)
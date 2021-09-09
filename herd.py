from dinosaur import Dinosaur


class Herd:

  def __init__ (self):
    self.dinosaurs = []
    self.create_herd()
  
  #create a herd of dinosaurs and append to self.dinosaurs
  def create_herd (self): #void
    #Dinosaur(name, attack_power)
    dinosaur_one = Dinosaur("Pteranodon", 2)
    dinosaur_two = Dinosaur("Cearadactylus", 4)
    dinosaur_three = Dinosaur("Tropeognathus", 3)

    self.dinosaurs.append(dinosaur_one)
    self.dinosaurs.append(dinosaur_two)
    self.dinosaurs.append(dinosaur_three)
class Dinosaur:

  #will be used to copy list to Herd.dinosaur_herd
  created_dinosaurs = []

  def __init__ (self, dinosaur_name):
    self.dinosaur_name = dinosaur_name
    self.dinosaur_health = 10
    self.dinosaur_attack_power = 4

    #add each robot object to created_robots
    Dinosaur.created_dinosaurs.append(self)

#Instance Robot Objects
dinosaur_one = Dinosaur("Pteranodon")
dinosaur_two = Dinosaur("Cearadactylus")
dinosaur_three = Dinosaur("Tropeognathus")
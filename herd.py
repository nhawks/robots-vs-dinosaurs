from dinosaur import Dinosaur


class Herd:

  #list of created dinosaurs
  dinosaur_herd = Dinosaur.created_dinosaurs.copy()

  def __init__ (self):
    self.create_fleet(self)
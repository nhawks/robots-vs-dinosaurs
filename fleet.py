from robot import Robot


class Fleet:

  #copy created_robots list
  robot_fleet = Robot.created_robots.copy()

  def __init__ (self):
    self.create_fleet(self)
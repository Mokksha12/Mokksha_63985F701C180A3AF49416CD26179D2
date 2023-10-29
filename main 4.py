class Batsman:
  def __init__(self, name):
      self.name = name

  def play(self):
      print(f"{self.name} is a batsman. They are ready to bat!")

class Bowler:
  def __init__(self, name):
      self.name = name

  def play(self):
      print(f"{self.name} is a bowler. They are ready to bowl!")

batsman1 = Batsman("Virat Kohli")
bowler1 = Bowler("Jasprit Bumrah")

batsman1.play()
bowler1.play()



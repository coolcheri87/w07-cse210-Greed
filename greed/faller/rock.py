
from greed.faller import Faller

class Rock(Faller):
    
    def __init__(self):
        super().__init__()
        self.impact = -1
        self.symbol = 'o'
        self.speed = Speed()

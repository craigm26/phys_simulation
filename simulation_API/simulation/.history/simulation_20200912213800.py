from datetime import datetime
import numpy as np


class Simulation():
    def __init__(self, ini_cndtn, user_name=None):
        self.ini_cndtn = ini_cndtn
        self.date = datetime.now()
        self.user_name = user_name


class HarmonicOsc(Simulation):
    pass

print(HarmonicOsc([0,0], "Juan").ini_cndtn)
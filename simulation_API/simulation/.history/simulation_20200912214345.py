from datetime import datetime
import numpy as np


class Simulation():
    """Class: Simulation

    Atributes
    ---------
    ini_cndtn : list
        initial condition of simulation, its specification depends on
        simulation
    date : datetime
        date of simulation
    user_name : str
        name of person that called the simulation

    """
    def __init__(self, ini_cndtn, user_name=None):
        self.ini_cndtn = ini_cndtn
        self.date = datetime.now()
        self.user_name = user_name
        self.integration_method = None
        self.sim_type = None


class HarmonicOsc(Simulation):
    """
    """
    pass

HarmonicOsc([0,0], "Juan")
from datetime import datetime
import numpy as np


class Simulation(object):
    """Class: Simulation

    Attributes
    ---------
    ini_cndtn : list
        Initial condition of simulation, its specification depends on
        the system being simulated.
    date : datetime
        Date of instantiation of object.
    method : str, optional
        Method of integration, varies depending on simulation. See
        avaliable methods on `scipy.integrate.solve_ivp` documentation.
        Default is 'RK45'.
    user_name : str, optional
        Username that called the simulation.
    """
    def __init__(self, ini_cndtn, method=None, user_name=None):
        """
        Parameters
        ----------
        ini_cndtn : list
            Initial condition of simulation, its specification depends on
            the system being simulated.
        date : datetime
            Date of instantiation of object.
        method : str, optional
            Method of integration, varies depending on simulation. See
            avaliable methods on `scipy.integrate.solve_ivp` documentation.
            Default is 'RK45'.
        user_name : str, optional
            Username that called the simulation.
        """
        self.ini_cndtn = ini_cndtn
        self.method = method
        self.date = datetime.now()
        self.user_name = user_name
        


class HarmonicOsc(Simulation):
    """Harmonic Oscillator simulation

    Attributes
    ---------
    In addition to Simulation's attributes:

    k : float
        Force constant of harmonic oscilltor.

    Methods
    -------

    Notes
    -----
    The hamiltonian describing the harmonic oscillator is written as

    .. math::
        
        H = \sqrt{1}{2}p^2 + \sqrt{1}{2}k q^2

    
    """
    def __init__(self, ini_cndtn, k=1, method=None, user_name=None):
        """Extends __init__ from Simulation
        
        Adds attribute `k` to bunch of Simulation's attributes.
        
        Parameters
        ----------
        k : float, optional
            Force constant of harmonic oscilltor. Default is 1. 
        """
        super().__init__(ini_cndtn, method, user_name)
        self.k = k

    def simulate(self):
        
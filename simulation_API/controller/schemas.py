

from typing import Optional, List, Tuple
from enum import Enum
from datetime import datetime

from pydantic import BaseModel
from scipy.integrate._ivp.ivp import OdeResult


class SimSystem(str, Enum):
    """List of the available systems to simulate"""
    ho = "Harmonic-Oscillator"
    qho = "Quantum-Harmonic-Oscillator" #Just an example. Not simulating it.


class IntegrationMethods(str, Enum):
    RK45 = "RK45"
    RK34 = "RK23"


class HOParams(BaseModel):
    m: float
    k: float    


class SimRequest(BaseModel):
    """Schema needed to request harmonic oscillator simulations
    
    See `HarmonicOsc1D` documentation in simulation.py to understand atributes
    """
    t_span: List[float]
    t_eval: Optional[List[float]]
    ini_cndtn: List[float]
    params: HOParams
    method: Optional[IntegrationMethods] = 'RK45'
    user_name: Optional[str]
    system: SimSystem


class SimResults(BaseModel):
    """Results of simulation as returned by  scipy.integrate.solve_ivp
    """
    sim_results: OdeResult


class SimResultsPaths(BaseModel):
    """Schema of the results of simulations

    This pydantic model is intended to store paths of results of the simulations
    algong with some metadata. This is what the API returns when someone
    requests a simulation via /api/simulate/{system}/ with method=post.
    
    Atributes
    ---------
    sim_id : int
        ID number of simulation.
    date : datetime
        Late of request of simulation
    routes_plots : list
        Routes of plots generated by the simulation backend.
    route_pickle : str
        Route of pickle file generated by the simulation backend.
    route_results : str
        Route of frontend showing results.
    """
    sim_id: int
    date: datetime
    routes_plots: List[str]
    route_pickle: str
    route_results: str


from datetime import datetime
from scipy.integrate import solve_ivp


class Simulation(object):
    """Simulation of mechanical system

    Attributes
    ---------
    t_span : 2-tuple of floats
        Interval of integration (t0, tf).
    t_eval : array_like or None, optional
        Times at which to store the computed solution, must be sorted and
        lie within t_span.
    ini_cndtn : list or None, optional
        Initial condition of simulation, its specification depends on
        the system being simulated.
    results : OdeResult
        Results of simulation.
    system : string or None, optional
        Description of simulated system.
    method : str, optional
        Method of integration.
    user_name : str, optional
        Username that called the simulation. D
    date : datetime.
        Date of instantiation of object.
    """
    def __init__(self, t_span, t_eval=None, ini_cndtn=None,
                 method='RK45', user_name=None):
        """
        Parameters
        ----------
        t_span : 2-tuple of floats
            Interval of integration (t0, tf). The solver starts with t=t0 and
            integrates until it reaches t=tf.
        t_eval : array_like or None, optional
            Times at which to store the computed solution, must be sorted and
            lie within t_span. If None (default), use points selected by the
            solver.
        ini_cndtn : list or None, optional
            Initial condition of simulation, its specification depends on
            the system being simulated. Default is optional.
        results : OdeResult
            Results of simulation. Default is None.
        system : string
            Description of simulated system.
        method : str, optional
            Method of integration, varies depending on simulation. See
            avaliable methods on `scipy.integrate.solve_ivp` documentation.
            Default is 'RK45'.
        user_name : str, optional
            Username that called the simulation.
        date : datetime
            Date of instantiation of object.
        """
        self.ini_cndtn = ini_cndtn
        self.t_span = t_span
        self.t_eval = t_eval
        self.method = method
        self.results = None
        self.system = None
        self.date = datetime.now()
        self.user_name = user_name
        


class HarmonicOsc1D(Simulation):
    """One-dimensional Harmonic Oscillator simulation

    Attributes
    ---------
    In addition to Simulation's attributes:

    m : float
        Mass of object.
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
    def __init__(self, t_span, t_eval, m=1., k=1., ini_cndtn=[0., 1.],
                 method='RK45', user_name=None):
        """Extends __init__ from Simulation
        
        Adds attributes `k` and `m` Simulation's attributes.
        
        Parameters
        ----------
        m : float
            Mass of object. Default is 1. 
        k : float, optional
            Force constant of harmonic oscilltor. Default is 1.
        ini_cndtn : array_like, shape (2,)
            Initial condition of 1D Harmonic Oscillator. Convention: [q0, p0].
            Default is [0., 1.]. A list of initial conditions can be used, in 
            this case a list of solutions will be returned by `simulate` method.
        """
        super().__init__(t_span, t_eval, ini_cndtn, method, user_name)
        self.m = m
        self.k = k
        self.system = " 1D Harmonic Oscillator"


    def h_eqns(self, t, y):
        """Hamilton's equations for 1D-Harmonic Oscillator

        Parameters
        ----------
        t : float
            Time of evaluation of Hamilton's equations.
        y : array_like, shape (2,)
            Canonical coordinates. Convention: [q, p].
        m : float
            Mass of object. Default is `self.m`. 
        k : float, optional
            Force constant of harmonic oscilltor. Default is `self.k`. 

        Returns
        -------
        dydt : list
            Hamilton's equations for 1d Harmonic Oscillator.
            dydt = [dqdt, dpdt] = [dHdp, - dHdq]
        """
        q, p = y
        dydt = [p / self.m, - q * self.k]
        return dydt

    def simulate(self):
        """Simulates 1d harmonic oscillator using `scipy.integrate.solve_ivp`
        
        Returns
        -------
        self.results : OdeResult
            Bunch object with the following fields defined:
                t : ndarray, shape (n_points,)
                    Time points.
                y : ndarray, shape (n, n_points)
                    Values of the solution at t.
                sol : OdeSolution or None
                    Found solution as OdeSolution instance; None if 
                    dense_output was set to False.
                t_events : list of ndarray or None
                    Contains for each event type a list of arrays at which an
                    event of that type event was detected. None if events was
                    None.
                y_events : list of ndarray or None
                    For each value of t_events, the corresponding value of the
                    solution. None if events was None.
                nfev : int
                    Number of evaluations of the right-hand side.
                njev : int
                    Number of evaluations of the Jacobian.
                nlu : int
                    Number of LU decompositions.
                status : int
                    Reason for algorithm termination:
                        -1: Integration step failed.
                        0: The solver successfully reached the end of tspan.
                        1: A termination event occurred.
                message : string
                    Human-readable description of the termination reason.
                success : bool
                    True if the solver reached the interval end or a
                    termination event occurred (status >= 0).
        """
        self.results = solve_ivp(self.h_eqns, self.t_span, self.ini_cndtn,
                             self.method, self.t_eval)
        return self.results
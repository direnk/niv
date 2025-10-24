import numpy as np
from dataclasses import dataclass

@dataclass
class NIVParams:
    X0: float = 1.0
    F0: float = 1.0
    P0: float = 1.0
    u0: float = 0.5
    delta: float = 0.02
    Phi: float = 0.03
    K0: float = 0.5
    beta: float = 0.8
    kp: float = 0.2
    dt: float = 0.01
    sigma: float = 0.01

class NIVAgent:
    """Represents an economic node with throughput, friction, and regeneration dynamics."""

    def __init__(self, params: NIVParams):
        self.params = params
        self.X = params.X0
        self.F = params.F0
        self.P = params.P0
        self.u = params.u0
        self.rng = np.random.default_rng(seed=42)

    def step(self, coupling: float = 0.0):
        """Advance the agent one time step with stochastic noise and optional coupling."""
        p = self.params
        dX = (p.delta - self.u * self.X) * p.dt + self.rng.normal(0, p.sigma)
        dF = (p.Phi - p.K0 * self.u + coupling) * p.dt + self.rng.normal(0, p.sigma)
        dP = (p.beta * self.P - p.kp * self.P) * p.dt + self.rng.normal(0, p.sigma)
        self.X += dX
        self.F = max(self.F + dF, 1e-6)
        self.P = max(self.P + dP, 1e-6)
        return self.X, self.F, self.P

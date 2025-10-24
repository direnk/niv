import numpy as np

class NIVMetrics:
    """Compute and track National Impact Velocity and auxiliary metrics."""

    def compute_niv(self, agents, eta: float = 1.0) -> float:
        """Aggregate NIV across agents."""
        P_mean = np.mean([a.P for a in agents])
        F_mean = np.mean([a.F for a in agents])
        return P_mean / (F_mean ** eta)

    def friction_index(self, agents) -> float:
        return np.var([a.F for a in agents])

    def regeneration_index(self, agents) -> float:
        return np.mean([a.P for a in agents])

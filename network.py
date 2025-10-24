import numpy as np
import networkx as nx
from .core import NIVAgent, NIVParams
from .metrics import NIVMetrics
from .logger import get_logger

class NetworkSimulator:
    """Simulate a network of NIV agents with Laplacian coupling."""

    def __init__(self, n_agents: int = 10, alpha: float = 0.1, steps: int = 1000):
        self.n_agents = n_agents
        self.alpha = alpha
        self.steps = steps
        self.graph = nx.erdos_renyi_graph(n_agents, 0.2, seed=42)
        self.A = nx.laplacian_matrix(self.graph).toarray()
        self.logger = get_logger("NetworkSimulator")

    def run(self, params: NIVParams):
        self.logger.info(f"Starting NIV simulation with {self.n_agents} agents.")
        agents = [NIVAgent(params) for _ in range(self.n_agents)]
        metrics = NIVMetrics()
        niv_series = []

        for t in range(self.steps):
            F_array = np.array([a.F for a in agents])
            for i, agent in enumerate(agents):
                coupling = self.alpha * np.sum(self.A[i] * (F_array - agent.F))
                agent.step(coupling)
            niv_value = metrics.compute_niv(agents)
            niv_series.append(niv_value)

            if t % 100 == 0:
                self.logger.info(f"Step {t}: NIV = {niv_value:.4f}")

        self.logger.info("Simulation complete.")
        return np.array(niv_series)

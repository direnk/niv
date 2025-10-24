class AdaptiveController:
    """Simple adaptive controller to stabilize friction F_t."""

    def __init__(self, lr: float = 0.05, target_F: float = 1.0):
        self.lr = lr
        self.target_F = target_F

    def update(self, agent):
        """Adjust control intensity u_t based on friction deviation."""
        error = agent.F - self.target_F
        agent.u = max(0.0, min(1.0, agent.u - self.lr * error))
        return agent.u

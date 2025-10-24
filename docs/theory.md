# National Impact Velocity (NIV) – Theoretical Foundations

## 1 . Framework Overview
NIV formalizes the **throughput dynamics** of complex economic networks where
capital, friction, and regeneration interact over time.

Let each agent _i_ be characterized by three core states:
- **\(X_t\)** – Idle capacity or unutilized potential  
- **\(F_t\)** – Friction or delay/transaction cost  
- **\(P_t\)** – Regeneration rate of productive output  

A control input \(u_t\) represents the policy or activation intensity.

---

## 2 . Core Dynamics
\[
\begin{aligned}
dX_t &= (\delta - u_t X_t)\,dt + \sigma_x\,dW_t, \\
dF_t &= (\Phi - K_0 u_t + \sum_j a_{ij}(F_j - F_i))\,dt + \sigma_f\,dB_t, \\
dP_t &= (\beta EORS_t - k_p P_t)\,dt + \sigma_p\,dW_t^p.
\end{aligned}
\]

Where:
- \(EORS_t = U P_t (1 + \lambda L_t)\) – effective output regeneration share  
- \(\delta, \Phi, K_0, \beta, k_p\) are model coefficients  
- \(\sigma_x,\sigma_f,\sigma_p\) are stochastic diffusion terms  

---

## 3 . Objective Functional
We define **National Impact Velocity (NIV)** as a throughput ratio measuring
regeneration per unit friction raised to an efficiency exponent \(\eta\):

\[
NIV_t = \frac{EORS_t \, E_{y,t} \, SRI_t}{(F_t)^{\eta}},
\]
where \(E_{y,t} = \frac{X_t}{X_t + F_t}\) and \(SRI_t = P_t\).

The system objective is to maximize discounted throughput:
\[
\max_{u_t}\int_0^{\infty} e^{-(\rho t + \phi X_t + \psi F_t)} NIV_t \, dt.
\]

---

## 4 . Interpretation
- **\(X_t\)** ↓ → capacity fully activated  
- **\(F_t\)** ↑ → system friction rising, NIV falls  
- **\(P_t\)** ↑ → greater regenerative flow  
- **\(u_t\)** ↑ → stronger activation at potential cost of higher friction  

---

## 5 . Network Coupling
For a network of _n_ agents with Laplacian L:
\[
dF_i = (\Phi - K_0 u_i + \alpha\sum_j L_{ij}(F_j - F_i))dt.
\]
Coupling coefficient \(\alpha\) represents liquidity diffusion between agents.

---

## 6 . Debt-Efficiency Relation
Define cumulative regeneration \(R_t = \int_0^t P_\tau d\tau\)  
and cumulative friction \(C_t = \int_0^t F_\tau d\tau\).  
Then the **Debt-Efficiency Index (DEI)** is:
\[
DEI_t = \frac{R_t}{C_t + \epsilon},
\]
providing an empirical measure of sovereign fiscal efficiency.

---

## 7 . DARPA Challenge 2 Relevance
DARPA Mathematical Challenge 2 asks how to *“understand, predict, and control
the dynamics of networks.”*  
NIV contributes a **continuous-time control-theoretic model** that unifies
diffusion, stochasticity, and optimal control across nodes—  
a candidate architecture for **real-world scalable network regulation**.

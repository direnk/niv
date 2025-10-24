# NIV-DARPA v1.0 – Release Notes
**Date:** 2025-10-23  
**Author:** Diren Kumaratilleke (UNC-Chapel Hill)

## Summary
Initial public release of the *National Impact Velocity* framework.
Implements continuous-time control, Laplacian network coupling, adaptive controller, and real Treasury-data validation.

## Key Features
- Deterministic stochastic-differential engine (`niv/core.py`)
- Laplacian network simulation (`niv/network.py`)
- Adaptive control law for friction stabilization
- Full FRED-cache pipeline with offline fallback
- Empirical *Debt-Efficiency Index* validation (2010 – 2024)
- Complete mathematical derivations in `/docs/theory.md`

## Reproducibility
1. `pip install -r requirements.txt`
2. Run any notebook in `/experiments/`
3. Figures auto-save to `/visuals/`

## Next Milestones
- Extend control optimization via HJB solver  
- Multi-sovereign NIV benchmarking  
- Publish whitepaper v2.0 (Hoover / Treasury circulation)


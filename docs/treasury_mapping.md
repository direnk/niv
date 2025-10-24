# Mapping Treasury Data to NIV Variables

| NIV Variable | Treasury Proxy | Interpretation |
|---------------|----------------|----------------|
| \(X_t\) | \(1 - \frac{\text{spread}}{\max(\text{spread})}\) | idle fiscal capacity |
| \(F_t\) | \(\frac{\text{spread}}{\max(\text{spread})}\) | friction / funding cost |
| \(P_t\) | \(\frac{\text{1Y}}{\text{10Y}}\) | regeneration efficiency |
| \(u_t\) | Issuance intensity | policy control |

**Data Source:** FRED – U.S. Department of the Treasury (series DGS1MO, DGS1, DGS10)  
**Update Frequency:** Daily (market days)  
**Time Span:** 2010 – Present  
**Normalization:** Min–max across the full sample to yield dimensionless variables.


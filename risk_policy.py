# risk_policy.py
import numpy as np

def compute_cvar(returns, alpha=0.05):
    """Computes Conditional Value at Risk (CVaR) for risk-aware credit decisioning."""
    return np.mean(np.sort(returns)[:int(len(returns) * alpha)])

def risk_adjusted_approval(default_prob, loan_amount, interest_rate):
    """Approves loan if risk-adjusted return is above a threshold."""
    return int((1 - default_prob) * loan_amount * (1 + interest_rate) - default_prob * loan_amount > 5000)

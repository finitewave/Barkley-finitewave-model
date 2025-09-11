"""
ops.py — mathematical core of the model.

This module provides functions to compute the model equations,
as well as functions to retrieve default parameters and initial
values for the state variables.

References:
"""

__all__ = (
    "get_variables",
    "get_parameters",
    "calc_rhs",
    "calc_dv",
)


def get_variables() -> dict[str, float]:
    """
    Returns default initial values for state variables.
    """
    return {"u": 0.0, "v": 0.0}


def get_parameters() -> dict[str, float]:
    """
    Returns default parameter values for the model.
    """
    return {"a": 0.75, "b": 0.02, "eps": 0.02}


def calc_rhs(u, v, a, b, eps) -> float:
    """
    Computes the right-hand side of the model.

    Parameters
    ----------
    u : float
        Current value of the excitation variable.
    v : float
        Current value of the recovery variable.
    a : float
        Parameter controlling the excitation threshold.
    b : float
        Parameter influencing the recovery dynamics.
    eps : float
        Parameter scaling the time dynamics.
    
    Returns
    -------
    float
        Right-hand side of the model.
    """
    return (u*(1 - u)*(u - (v + b)/a))/eps


def calc_dv(v, u):
    """
    Calculates the recovery variable v for the Barkley model.

    The recovery variable follows a simple linear relaxation toward the
    excitation variable `u`, simulating return to the resting state after excitation.

    Parameters
    ----------
    v : float
        Current value of the recovery variable.
    u : float
        Current value of the excitation variable.

    Returns
    -------
    float
        Updated value of the recovery variable.
    """
    return (u-v)
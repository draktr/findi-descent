"""
Finite Difference Gradient Descent

Finite Difference Gradient Descent (FDGD) can optimize any function, including the ones without analytic form, by employing finite difference numerical differentiation within a gradient descent algorithm.
"""

from fdgd.fdgd import FDGD

__all__ = [s for s in dir() if not s.startswith("_")]

__version__ = "0.1.0"
__author__ = "draktr"
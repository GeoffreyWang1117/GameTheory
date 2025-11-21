"""
Game Theory Learning Platform
A hands-on learning platform for game theory concepts, similar to rustlings.
"""

__version__ = "1.0.0"
__author__ = "Game Theory Learning Platform"

from .runner import ExerciseRunner
from .validator import ExerciseValidator

__all__ = ['ExerciseRunner', 'ExerciseValidator']

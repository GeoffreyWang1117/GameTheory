"""
Test suite for game theory exercises.

Run with: pytest tests/test_exercises.py
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestIntroExercises:
    """Test introduction exercises."""
    
    def test_prisoners_dilemma_loads(self):
        """Test that Prisoner's Dilemma exercise loads."""
        from exercises.exercises_01_intro import prisoners_dilemma_01_prisoners_dilemma as pd
        assert hasattr(pd, 'create_payoff_matrix')
        assert hasattr(pd, 'test_solution')
    
    def test_prisoners_dilemma_runs(self):
        """Test that Prisoner's Dilemma tests pass."""
        import subprocess
        result = subprocess.run(
            ['python', 'exercises/01_intro/01_prisoners_dilemma.py'],
            capture_output=True,
            text=True,
            timeout=5
        )
        assert result.returncode == 0, f"Exercise failed: {result.stderr}"


class TestBargainingExercises:
    """Test bargaining exercises."""
    
    def test_nash_bargaining_exists(self):
        """Test Nash bargaining exercise exists."""
        assert os.path.exists('exercises/06_bargaining/01_nash_bargaining.py')
    
    def test_rubinstein_exists(self):
        """Test Rubinstein exercise exists."""
        assert os.path.exists('exercises/06_bargaining/02_rubinstein_bargaining.py')


class TestMatchingExercises:
    """Test matching theory exercises."""
    
    def test_stable_marriage_exists(self):
        """Test stable marriage exercise exists."""
        assert os.path.exists('exercises/07_matching/01_stable_marriage.py')
    
    def test_gale_shapley_runs(self):
        """Test Gale-Shapley algorithm runs."""
        import subprocess
        result = subprocess.run(
            ['python', 'exercises/07_matching/01_stable_marriage.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        assert result.returncode == 0, f"Exercise failed: {result.stderr}"


class TestFramework:
    """Test the learning platform framework."""
    
    def test_runner_imports(self):
        """Test that runner module imports."""
        from gametheory.runner import ExerciseRunner
        assert ExerciseRunner is not None
    
    def test_validator_imports(self):
        """Test that validator imports."""
        from gametheory.validator import ExerciseValidator
        assert ExerciseValidator is not None
    
    def test_utils_imports(self):
        """Test that utilities import."""
        from gametheory import utils
        assert hasattr(utils, 'print_success')
        assert hasattr(utils, 'print_error')


class TestExerciseStructure:
    """Test exercise file structure."""
    
    @pytest.mark.parametrize("section", [
        '01_intro',
        '02_basic_concepts',
        '03_cooperative_games',
        '04_repeated_games',
        '05_advanced',
        '06_bargaining',
        '07_matching',
        '08_voting',
        '09_networks',
        '10_learning'
    ])
    def test_section_exists(self, section):
        """Test that exercise section exists."""
        path = f'exercises/{section}'
        assert os.path.exists(path), f"Section {section} not found"
        assert os.path.isdir(path), f"{section} is not a directory"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

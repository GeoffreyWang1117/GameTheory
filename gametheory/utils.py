"""
Utility functions for the game theory learning platform.
"""

import json
import os
from typing import Dict, List, Any


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_success(message: str):
    """Print success message in green."""
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")


def print_error(message: str):
    """Print error message in red."""
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")


def print_info(message: str):
    """Print info message in cyan."""
    print(f"{Colors.OKCYAN}ℹ {message}{Colors.ENDC}")


def print_warning(message: str):
    """Print warning message in yellow."""
    print(f"{Colors.WARNING}⚠ {message}{Colors.ENDC}")


def print_header(message: str):
    """Print header message in bold."""
    print(f"\n{Colors.BOLD}{Colors.HEADER}{message}{Colors.ENDC}\n")


def load_exercise_info(exercises_dir: str) -> Dict[str, Any]:
    """Load exercise information from info.json."""
    info_path = os.path.join(exercises_dir, "info.json")
    if os.path.exists(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def get_all_exercises(exercises_dir: str) -> List[Dict[str, str]]:
    """Get all exercise files in order."""
    exercises = []
    info = load_exercise_info(exercises_dir)

    for section in info.get('sections', []):
        section_name = section['name']
        section_path = os.path.join(exercises_dir, section['path'])

        for exercise in section['exercises']:
            exercise_path = os.path.join(section_path, exercise['file'])
            if os.path.exists(exercise_path):
                exercises.append({
                    'section': section_name,
                    'name': exercise['name'],
                    'file': exercise['file'],
                    'path': exercise_path,
                    'description': exercise.get('description', '')
                })

    return exercises


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

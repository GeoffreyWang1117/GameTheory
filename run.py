#!/usr/bin/env python3
"""
Game Theory Learning Platform - Main Entry Point

Run this script to start learning game theory!
"""

import sys
import os
import argparse

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gametheory.runner import ExerciseRunner


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Game Theory Learning Platform - Learn game theory through hands-on exercises!'
    )
    parser.add_argument(
        'command',
        nargs='?',
        default='interactive',
        choices=['interactive', 'watch', 'verify', 'list'],
        help='Command to run (default: interactive)'
    )
    parser.add_argument(
        '--exercise',
        '-e',
        help='Specific exercise file to verify'
    )

    args = parser.parse_args()

    # Get exercises directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    exercises_dir = os.path.join(project_root, 'exercises')

    if not os.path.exists(exercises_dir):
        print("Error: exercises directory not found!")
        return 1

    # Create runner
    runner = ExerciseRunner(exercises_dir)

    # Execute command
    if args.command == 'interactive':
        runner.interactive_mode()
    elif args.command == 'watch':
        runner.watch_mode()
    elif args.command == 'list':
        runner.list_exercises()
    elif args.command == 'verify':
        if args.exercise:
            # Verify specific exercise
            from gametheory.validator import ExerciseValidator
            validator = ExerciseValidator(args.exercise)
            is_valid, message = validator.validate()
            if is_valid:
                print(f"✓ {message}")
                return 0
            else:
                print(f"✗ {message}")
                return 1
        else:
            runner.run_current_exercise()

    return 0


if __name__ == '__main__':
    sys.exit(main())

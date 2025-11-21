"""
Exercise runner for the game theory learning platform.
"""

import os
import sys
import time
from typing import Optional, List, Dict
from .validator import ExerciseValidator
from .utils import (
    print_success, print_error, print_info, print_warning,
    print_header, get_all_exercises, clear_screen
)


class ExerciseRunner:
    """Main exercise runner."""

    def __init__(self, exercises_dir: str):
        self.exercises_dir = exercises_dir
        self.exercises = get_all_exercises(exercises_dir)
        self.current_index = 0
        self.progress_file = os.path.join(exercises_dir, '.progress')
        self.load_progress()

    def load_progress(self):
        """Load user progress from file."""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    self.current_index = int(f.read().strip())
            except Exception:
                self.current_index = 0

    def save_progress(self):
        """Save user progress to file."""
        try:
            with open(self.progress_file, 'w') as f:
                f.write(str(self.current_index))
        except Exception as e:
            print_warning(f"Could not save progress: {e}")

    def print_welcome(self):
        """Print welcome message."""
        clear_screen()
        print_header("🎮 Welcome to Game Theory Learning Platform!")
        print("""
This platform will teach you game theory concepts through hands-on exercises.
Each exercise contains explanations and code challenges.

Commands:
  - run/r:    Run and check the current exercise
  - hint/h:   Show a hint for the current exercise
  - list/l:   List all exercises
  - next/n:   Move to the next exercise
  - prev/p:   Move to the previous exercise
  - reset:    Reset your progress
  - quit/q:   Exit the platform
        """)
        self.print_progress()

    def print_progress(self):
        """Print current progress."""
        if not self.exercises:
            print_error("No exercises found!")
            return

        completed = self.current_index
        total = len(self.exercises)
        percentage = (completed / total) * 100 if total > 0 else 0

        print_info(f"Progress: {completed}/{total} exercises completed ({percentage:.1f}%)")

        if completed < total:
            current = self.exercises[completed]
            print_info(f"Current exercise: {current['section']} - {current['name']}")
            print_info(f"File: {current['file']}")
            if current.get('description'):
                print(f"\n{current['description']}\n")

    def run_current_exercise(self):
        """Run and validate the current exercise."""
        if self.current_index >= len(self.exercises):
            print_success("🎉 Congratulations! You've completed all exercises!")
            return True

        current = self.exercises[self.current_index]
        print_header(f"Running: {current['section']} - {current['name']}")

        validator = ExerciseValidator(current['path'])
        is_valid, message = validator.validate()

        if is_valid:
            print_success(f"Exercise passed! {message}")
            print_success(f"Moving to next exercise...\n")
            self.current_index += 1
            self.save_progress()
            time.sleep(1)

            if self.current_index < len(self.exercises):
                self.print_progress()
            else:
                print_success("🎉 Congratulations! You've completed all exercises!")
                return True
        else:
            print_error(f"Exercise failed!")
            print(f"\n{message}\n")
            print_info(f"Fix the issues and run again.")

        return is_valid

    def list_exercises(self):
        """List all exercises with their status."""
        print_header("📚 All Exercises")

        current_section = None
        for i, exercise in enumerate(self.exercises):
            if exercise['section'] != current_section:
                current_section = exercise['section']
                print(f"\n{current_section}:")

            status = "✓" if i < self.current_index else "○"
            marker = "→" if i == self.current_index else " "
            print(f"  {marker} {status} {exercise['name']} ({exercise['file']})")
        print()

    def show_hint(self):
        """Show hint for the current exercise."""
        if self.current_index >= len(self.exercises):
            print_info("No more exercises!")
            return

        current = self.exercises[self.current_index]
        print_header(f"💡 Hint for: {current['name']}")

        # Read the exercise file and extract hint
        try:
            with open(current['path'], 'r', encoding='utf-8') as f:
                content = f.read()

            # Look for hint in comments
            lines = content.split('\n')
            in_hint = False
            hint_lines = []

            for line in lines:
                if 'HINT:' in line.upper():
                    in_hint = True
                    hint_lines.append(line.split('HINT:', 1)[1].strip())
                elif in_hint and (line.strip().startswith('#') or line.strip().startswith('"""')):
                    hint_lines.append(line.strip().lstrip('#').lstrip('"').strip())
                elif in_hint and line.strip() and not line.strip().startswith('#'):
                    break

            if hint_lines:
                for hint_line in hint_lines:
                    if hint_line:
                        print(f"  {hint_line}")
            else:
                print_info("No hint available for this exercise. Read the comments carefully!")
        except Exception as e:
            print_error(f"Could not read hint: {e}")

        print()

    def next_exercise(self):
        """Move to the next exercise."""
        if self.current_index < len(self.exercises) - 1:
            self.current_index += 1
            self.save_progress()
            self.print_progress()
        else:
            print_info("Already at the last exercise!")

    def prev_exercise(self):
        """Move to the previous exercise."""
        if self.current_index > 0:
            self.current_index -= 1
            self.save_progress()
            self.print_progress()
        else:
            print_info("Already at the first exercise!")

    def reset_progress(self):
        """Reset all progress."""
        response = input("Are you sure you want to reset all progress? (yes/no): ")
        if response.lower() in ['yes', 'y']:
            self.current_index = 0
            self.save_progress()
            print_success("Progress reset!")
            self.print_progress()
        else:
            print_info("Reset cancelled.")

    def interactive_mode(self):
        """Run in interactive mode."""
        self.print_welcome()

        while True:
            try:
                command = input(f"\n{'='*50}\nEnter command (run/hint/list/next/prev/reset/quit): ").strip().lower()
                print()

                if command in ['run', 'r']:
                    self.run_current_exercise()
                elif command in ['hint', 'h']:
                    self.show_hint()
                elif command in ['list', 'l']:
                    self.list_exercises()
                elif command in ['next', 'n']:
                    self.next_exercise()
                elif command in ['prev', 'p']:
                    self.prev_exercise()
                elif command == 'reset':
                    self.reset_progress()
                elif command in ['quit', 'q', 'exit']:
                    print_success("Thanks for learning game theory! Goodbye! 👋")
                    break
                else:
                    print_warning(f"Unknown command: {command}")
                    print_info("Available commands: run, hint, list, next, prev, reset, quit")

            except KeyboardInterrupt:
                print("\n")
                print_success("Thanks for learning game theory! Goodbye! 👋")
                break
            except EOFError:
                break

    def watch_mode(self):
        """Run in watch mode (auto-run on file change)."""
        print_header("👀 Watch Mode")
        print_info("Watching for file changes... Press Ctrl+C to stop.")
        print()

        if self.current_index >= len(self.exercises):
            print_success("All exercises completed!")
            return

        current = self.exercises[self.current_index]
        last_mtime = os.path.getmtime(current['path'])

        try:
            while self.current_index < len(self.exercises):
                current = self.exercises[self.current_index]
                current_mtime = os.path.getmtime(current['path'])

                if current_mtime != last_mtime:
                    last_mtime = current_mtime
                    print_info(f"Detected change in {current['file']}...")
                    self.run_current_exercise()

                time.sleep(1)

            print_success("🎉 All exercises completed!")

        except KeyboardInterrupt:
            print("\n")
            print_info("Watch mode stopped.")

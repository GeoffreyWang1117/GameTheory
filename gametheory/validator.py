"""
Exercise validator for checking if exercises are completed correctly.
"""

import ast
import sys
from typing import Tuple, Optional
from io import StringIO
import traceback


class ExerciseValidator:
    """Validates exercise solutions."""

    def __init__(self, exercise_path: str):
        self.exercise_path = exercise_path
        self.exercise_name = exercise_path.split('/')[-1]

    def check_syntax(self) -> Tuple[bool, Optional[str]]:
        """Check if the Python file has valid syntax."""
        try:
            with open(self.exercise_path, 'r', encoding='utf-8') as f:
                code = f.read()
            ast.parse(code)
            return True, None
        except SyntaxError as e:
            return False, f"Syntax error at line {e.lineno}: {e.msg}"
        except Exception as e:
            return False, str(e)

    def has_todo_markers(self) -> Tuple[bool, int]:
        """Check if the file still has TODO markers."""
        try:
            with open(self.exercise_path, 'r', encoding='utf-8') as f:
                content = f.read()

            todo_count = content.count('TODO') + content.count('todo')
            return todo_count > 0, todo_count
        except Exception:
            return False, 0

    def run_tests(self) -> Tuple[bool, str]:
        """Run the tests defined in the exercise."""
        try:
            # Read the file
            with open(self.exercise_path, 'r', encoding='utf-8') as f:
                code = f.read()

            # Create a namespace for execution
            namespace = {}

            # Redirect stdout to capture output
            old_stdout = sys.stdout
            sys.stdout = StringIO()

            try:
                # Execute the code
                exec(code, namespace)

                # Get output
                output = sys.stdout.getvalue()

                # Check if test_solution function exists and run it
                if 'test_solution' in namespace:
                    test_result = namespace['test_solution']()
                    if test_result is True:
                        return True, "All tests passed!"
                    else:
                        return False, f"Tests failed: {test_result}"
                else:
                    # If no test function, just check if it runs without error
                    return True, "Exercise runs successfully!"

            finally:
                sys.stdout = old_stdout

        except Exception as e:
            error_trace = traceback.format_exc()
            return False, f"Runtime error:\n{error_trace}"

    def validate(self) -> Tuple[bool, str]:
        """
        Validate the exercise completely.
        Returns (is_valid, message)
        """
        # Check syntax first
        syntax_valid, syntax_error = self.check_syntax()
        if not syntax_valid:
            return False, f"Syntax Error:\n{syntax_error}"

        # Check for TODO markers
        has_todos, todo_count = self.has_todo_markers()
        if has_todos:
            return False, f"Still has {todo_count} TODO marker(s). Complete them first!"

        # Run tests
        tests_passed, message = self.run_tests()
        if not tests_passed:
            return False, message

        return True, message

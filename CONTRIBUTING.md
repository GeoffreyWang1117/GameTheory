# Contributing to Game Theory Learning Platform

Thank you for your interest in contributing! This platform aims to make game theory accessible through hands-on learning.

## 🎯 Ways to Contribute

### 1. Add New Exercises

We're always looking for new exercises covering:
- Advanced topics (e.g., differential games, global games)
- Real-world applications
- Recent research developments
- Interactive visualizations

### 2. Improve Existing Exercises

- Add better explanations
- Include more test cases
- Provide additional hints
- Fix bugs or unclear instructions

### 3. Enhance the Platform

- Improve the CLI interface
- Add visualization tools
- Better progress tracking
- Performance optimizations

### 4. Documentation

- Tutorial videos
- Blog posts explaining concepts
- Translations to other languages
- Better error messages

## 📝 Exercise Guidelines

### Structure

Each exercise should follow this template:

```python
"""
Exercise N: Title

Brief introduction explaining the concept (2-3 paragraphs).
Include real-world context and motivation.

TODO: Clear description of what students need to implement.
"""

def main_function(args):
    """
    Docstring explaining the function.
    
    Args:
        Clearly documented arguments
    
    Returns:
        Clear return type
    
    TODO: Implementation task.
    """
    pass  # Student implements here


def test_solution():
    """Test function - Do not modify."""
    # Comprehensive tests
    assert main_function(test_input) == expected_output
    
    # Print insights
    print("Key insights:")
    print("1. First insight...")
    print("2. Second insight...")
    
    return True


if __name__ == '__main__':
    test_solution()
```

### Best Practices

1. **Clear Learning Objectives**
   - State what students will learn
   - Build on previous exercises
   - Include practical applications

2. **Progressive Difficulty**
   - Start with simple cases
   - Gradually increase complexity
   - Provide scaffolding

3. **Good Tests**
   - Test edge cases
   - Provide helpful error messages
   - Include examples that illustrate concepts

4. **Educational Content**
   - Explain the theory
   - Provide intuition
   - Include references

## 🔧 Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/GameTheory.git
cd GameTheory

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8

# Run tests
pytest tests/
```

## 🎨 Code Style

We follow PEP 8 with some modifications:

```bash
# Format code
black .

# Check style
flake8 gametheory/ exercises/

# Run linter
pylint gametheory/
```

## 📋 Pull Request Process

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write clear, commented code
   - Add tests for new features
   - Update documentation

3. **Test Thoroughly**
   ```bash
   # Run all tests
   pytest tests/
   
   # Test specific exercise
   python exercises/XX_section/YY_exercise.py
   
   # Test the platform
   python run.py list
   ```

4. **Commit with Clear Messages**
   ```bash
   git commit -m "Add exercise on Nash bargaining solution
   
   - Implements axiomatic approach
   - Includes fairness axiom verification
   - Adds examples with asymmetric bargaining power"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   
   Then open a pull request on GitHub with:
   - Clear description of changes
   - Why the changes are needed
   - Any relevant issue numbers

## ✅ Checklist for New Exercises

- [ ] Exercise file follows template structure
- [ ] Clear TODO markers for students
- [ ] Comprehensive test cases
- [ ] Educational content explains concepts
- [ ] Hints are helpful but not complete solutions
- [ ] Code is well-commented
- [ ] No syntax errors
- [ ] Tests pass
- [ ] Added to `exercises/info.json`
- [ ] Updated relevant documentation

## 🐛 Reporting Bugs

Please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots

## 💡 Suggesting Exercises

Open an issue with:
- Topic/concept to cover
- Why it's important
- Target difficulty level
- Relevant references

## 📚 Resources for Contributors

### Game Theory References
- Fudenberg & Tirole - "Game Theory"
- Osborne & Rubinstein - "A Course in Game Theory"
- Myerson - "Game Theory: Analysis of Conflict"

### Educational Design
- Make It Stick - Brown, Roediger, McDaniel
- How Learning Works - Ambrose et al.

### Similar Projects
- rustlings - Rust learning platform
- cryptopals - Cryptography challenges
- exercism - Code practice platform

## 🙏 Recognition

Contributors will be:
- Listed in README.md
- Credited in exercise files
- Mentioned in release notes

## 📞 Questions?

- Open an issue
- Join discussions on GitHub
- Email: [project maintainer email]

---

Thank you for helping make game theory more accessible to everyone! 🎮🧠

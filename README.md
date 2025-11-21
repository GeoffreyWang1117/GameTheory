# Game Theory Learning Platform

> 🎮 Learn game theory through hands-on Python exercises - from Prisoner's Dilemma to Mechanism Design

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📚 Overview

This is an interactive learning platform for game theory, inspired by [rustlings](https://github.com/rust-lang/rustlings). Learn economic game theory concepts by completing progressively challenging Python exercises, from basic concepts like the Prisoner's Dilemma to advanced topics like evolutionary game theory and mechanism design.

## ✨ Features

- **Progressive Learning**: 19 exercises organized from basic to advanced topics
- **Interactive CLI**: Real-time feedback and validation
- **Comprehensive Coverage**: From Nash Equilibrium to Auction Theory
- **Hands-on Practice**: Learn by implementing game theory concepts in code
- **Watch Mode**: Auto-run exercises as you edit them
- **Progress Tracking**: Save your progress automatically

## 🎯 Learning Path

### 📖 **Introduction to Game Theory** (3 exercises)
- Prisoner's Dilemma - The classic game theory problem
- Nash Equilibrium - Finding stable strategy profiles
- Dominant Strategies - When one strategy is always best

### 🎲 **Basic Concepts** (4 exercises)
- Zero-Sum Games - Pure competition and the minimax theorem
- Mixed Strategies - Randomization as optimal play
- Payoff Matrices - Working with game representations
- Coordination Games - Multiple equilibria and selection

### 🤝 **Cooperative Games** (3 exercises)
- Coalition Formation - How players form groups
- Shapley Value - Fair payoff distribution
- The Core - Stable allocations

### 🔄 **Repeated and Dynamic Games** (4 exercises)
- Iterated Prisoner's Dilemma - Repeated interactions
- Tit-for-Tat - Famous strategies and their properties
- Folk Theorem - Sustaining cooperation
- Sequential Games - Backward induction and subgame perfection

### 🚀 **Advanced Topics** (5 exercises)
- Evolutionary Game Theory - ESS and replicator dynamics
- Hawk-Dove Game - Conflict and mixed strategies
- Asymmetric Information - Bayesian games and signaling
- Auction Theory - Mechanism design for resource allocation
- Mechanism Design - Reverse game theory

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- NumPy (for advanced exercises)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/GameTheory.git
cd GameTheory
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start learning:
```bash
python run.py
```

## 💻 Usage

### Interactive Mode (Default)

```bash
python run.py
```

In interactive mode, you can use these commands:
- `run` or `r` - Run and check the current exercise
- `hint` or `h` - Show a hint for the current exercise
- `list` or `l` - List all exercises and your progress
- `next` or `n` - Move to the next exercise
- `prev` or `p` - Move to the previous exercise
- `reset` - Reset your progress
- `quit` or `q` - Exit the platform

### Watch Mode

Automatically run exercises when files change:
```bash
python run.py watch
```

### List All Exercises

```bash
python run.py list
```

### Verify Specific Exercise

```bash
python run.py verify --exercise path/to/exercise.py
```

## 📝 How It Works

1. **Read the Exercise**: Each exercise file contains:
   - Educational content explaining the concept
   - Code with `TODO` markers
   - A test function to verify your solution

2. **Complete the TODOs**: Fill in the missing code where you see `TODO` comments

3. **Run and Test**: Use `run` command to check your solution

4. **Learn from Feedback**: The system provides detailed feedback on what's wrong

5. **Move Forward**: Once an exercise passes, automatically advance to the next one

## 📊 Exercise Structure

Each exercise file follows this pattern:

```python
"""
Exercise N: Topic Name

Educational content explaining the concept...

TODO: What you need to implement
"""

def function_to_implement():
    """
    Description of what this function should do.

    TODO: Implement this function.
    """
    # Your code here
    pass

def test_solution():
    """Test function - Do not modify."""
    # Tests that verify your implementation
    assert function_to_implement() == expected_result
    return True

if __name__ == '__main__':
    test_solution()
```

## 🎓 Learning Tips

1. **Read Carefully**: Each exercise includes explanations of the game theory concepts
2. **Start Simple**: Begin with the introduction exercises even if you know some game theory
3. **Use Hints**: If stuck, use the `hint` command for guidance
4. **Experiment**: Try different approaches to understand the concepts better
5. **Reference Materials**: The exercises include references to key theorems and results

## 🧪 Testing

Run all exercise tests:
```bash
python -m pytest tests/
```

Test a specific exercise:
```bash
python exercises/01_intro/01_prisoners_dilemma.py
```

## 📚 Additional Resources

### Books
- "Game Theory" by Drew Fudenberg and Jean Tirole
- "A Course in Game Theory" by Martin J. Osborne and Ariel Rubinstein
- "The Art of Strategy" by Avinash Dixit and Barry Nalebuff

### Online Courses
- Game Theory (Coursera) by Stanford/Yale
- Strategy (edX) by MIT

### Papers
- John Nash - "Non-Cooperative Games" (1951)
- Robert Axelrod - "The Evolution of Cooperation" (1984)
- Shapley & Scarf - "On Cores and Indivisibility" (1974)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add New Exercises**: Create exercises for topics not yet covered
2. **Improve Explanations**: Make concepts clearer
3. **Fix Bugs**: Report or fix issues
4. **Enhance Features**: Improve the learning platform

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [rustlings](https://github.com/rust-lang/rustlings)
- Game theory concepts from classic textbooks and papers
- Thanks to all contributors and the game theory community

---

**Happy Learning! 🎮🧠**

*"In game theory, as in life, what's rational for the individual may not be optimal for the group."*

# Quick Start Guide - Game Theory Learning Platform

## 🚀 5-Minute Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/GeoffreyWang1117/GameTheory.git
cd GameTheory

# Install dependencies
pip install -r requirements.txt

# Start learning!
python run.py
```

### Your First Exercise

The platform will start with the Prisoner's Dilemma. Here's what you'll see:

```
🎮 Welcome to Game Theory Learning Platform!

Progress: 0/34 exercises completed (0.0%)
Current exercise: Introduction to Game Theory - Prisoner's Dilemma
File: 01_prisoners_dilemma.py

The Prisoner's Dilemma is the most famous game in game theory...

Commands: run/hint/list/next/prev/reset/quit
>
```

### How to Complete an Exercise

1. **Open the exercise file** in your editor:
   ```bash
   # Open in your favorite editor
   vim exercises/01_intro/01_prisoners_dilemma.py
   # or
   code exercises/01_intro/01_prisoners_dilemma.py
   ```

2. **Find the TODO markers** and complete the implementation:
   ```python
   def create_payoff_matrix():
       """Create the Prisoner's Dilemma payoff matrix."""
       payoff = {
           ('C', 'C'): (-1, -1),  # TODO: Fill in payoffs
           # ... complete the rest
       }
       return payoff
   ```

3. **Test your solution**:
   ```bash
   # In the interactive platform
   > run

   # Or run the file directly
   python exercises/01_intro/01_prisoners_dilemma.py
   ```

4. **Get help if stuck**:
   ```bash
   > hint
   ```

### Example: Completing the First Exercise

Here's the Prisoner's Dilemma payoff structure:
- Both cooperate: (-1, -1)
- Both defect: (-3, -3)
- One defects, one cooperates: (0, -5)

Complete the `create_payoff_matrix()` function:

```python
def create_payoff_matrix():
    payoff = {
        ('C', 'C'): (-1, -1),  # Both cooperate
        ('C', 'D'): (-5, 0),   # P1 cooperates, P2 defects
        ('D', 'C'): (0, -5),   # P1 defects, P2 cooperates
        ('D', 'D'): (-3, -3),  # Both defect
    }
    return payoff
```

Then run to verify:
```bash
> run
✓ Exercise passed! All tests passed!
✓ Moving to next exercise...
```

## 📚 Learning Paths

### Path 1: Economics/Business Student (10-15 hours)
Focus on strategic thinking and applications:
```
1-7 → 20-22 → 23-25 → 18-19
(Intro → Bargaining → Matching → Auctions)
```

### Path 2: Computer Science Student (12-18 hours)
Focus on algorithms and computational aspects:
```
1-4 → 14 → 23-25 → 29-31 → 32-34
(Basics → Sequential → Matching → Networks → Learning)
```

### Path 3: Mathematics Student (15-20 hours)
Focus on theoretical foundations:
```
1-10 → 11-14 → 15-17 → 32-34
(All fundamentals → Repeated → Advanced → Learning)
```

### Path 4: Complete Mastery (40-60 hours)
Do all 34 exercises in order for comprehensive understanding.

## 💡 Pro Tips

### Tip 1: Use Watch Mode
Auto-run tests as you edit:
```bash
python run.py watch
```

### Tip 2: Test Directly
Run exercise files directly for faster iteration:
```bash
python exercises/01_intro/01_prisoners_dilemma.py
```

### Tip 3: Read the Theory
Each exercise has detailed explanations - read them carefully before coding!

### Tip 4: Experiment
Try breaking your solution to understand what the tests check for.

### Tip 5: Use Hints Wisely
Hints are there to help, but try solving first!

## 🎯 What You'll Learn

### After 10 exercises (Beginner):
- ✅ Find Nash equilibria
- ✅ Identify dominant strategies
- ✅ Solve zero-sum games
- ✅ Work with payoff matrices

### After 20 exercises (Intermediate):
- ✅ Analyze repeated games
- ✅ Calculate Shapley values
- ✅ Understand evolutionary stability
- ✅ Design simple auctions

### After 34 exercises (Advanced):
- ✅ Implement Gale-Shapley algorithm
- ✅ Analyze voting systems
- ✅ Design mechanisms
- ✅ Simulate learning dynamics

## 🐛 Common Issues

### Issue: "Module not found: numpy"
**Solution:**
```bash
pip install numpy
```

### Issue: "No exercises found"
**Solution:** Make sure you're in the GameTheory directory:
```bash
cd GameTheory
python run.py
```

### Issue: "Tests fail even though code looks correct"
**Solution:**
- Check for typos in variable names
- Make sure return types match expected format
- Read error messages carefully
- Use `print()` statements to debug

## 📖 Next Steps

1. **Complete your first 3 exercises** to understand the platform
2. **Choose a learning path** based on your background
3. **Join discussions** on GitHub for questions
4. **Contribute** new exercises or improvements!

## 🆘 Getting Help

- **In-platform hints**: Use `hint` command
- **GitHub Issues**: Report bugs or ask questions
- **Documentation**: Read EXERCISES_SUMMARY.md for details
- **Discord Community**: [Link to community if available]

---

**Ready to start?** Run `python run.py` and begin your game theory journey! 🎮


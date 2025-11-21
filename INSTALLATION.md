# Installation Guide

## Quick Install

### Option 1: Basic Installation (Recommended for Learners)

```bash
# Clone the repository
git clone https://github.com/GeoffreyWang1117/GameTheory.git
cd GameTheory

# Install dependencies
pip install -r requirements.txt

# Start learning!
python run.py
```

### Option 2: Using Make (Linux/Mac)

```bash
# Clone the repository
git clone https://github.com/GeoffreyWang1117/GameTheory.git
cd GameTheory

# Install dependencies
make install

# Start learning
make run
```

### Option 3: Install as Package (Advanced)

```bash
# Clone and install
git clone https://github.com/GeoffreyWang1117/GameTheory.git
cd GameTheory

# Install in development mode
pip install -e .

# Run from anywhere
gametheory
```

## Detailed Installation

### Prerequisites

**Required:**
- Python 3.7 or higher
- pip (Python package manager)

**Optional:**
- Git (for cloning repository)
- Make (for convenience commands)
- Virtual environment tool (recommended)

### Step-by-Step Installation

#### 1. Install Python

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

#### 2. Verify Installation

```bash
python3 --version  # Should be 3.7 or higher
pip3 --version     # Should be installed
```

#### 3. Set Up Virtual Environment (Recommended)

**Linux/Mac:**
```bash
# Create virtual environment
python3 -m venv gametheory-env

# Activate it
source gametheory-env/bin/activate
```

**Windows:**
```bash
# Create virtual environment
python -m venv gametheory-env

# Activate it
gametheory-env\Scripts\activate
```

#### 4. Clone Repository

**With Git:**
```bash
git clone https://github.com/GeoffreyWang1117/GameTheory.git
cd GameTheory
```

**Without Git (Download ZIP):**
- Download from GitHub
- Extract the ZIP file
- Navigate to the folder

#### 5. Install Dependencies

```bash
# Make sure you're in the GameTheory directory
pip install -r requirements.txt
```

This installs:
- NumPy (for numerical computations)
- Matplotlib (optional, for visualizations)

#### 6. Verify Installation

```bash
# Test the platform
python run.py list

# Should show all 34 exercises
```

## Platform-Specific Notes

### Linux

Usually works out of the box. If you have issues:

```bash
# Install development tools
sudo apt install build-essential python3-dev

# Reinstall numpy
pip install --upgrade numpy
```

### macOS

```bash
# Install Xcode command line tools if needed
xcode-select --install

# Use Python 3 explicitly
python3 run.py
```

### Windows

**PowerShell Execution Policy:**
If you get execution policy errors:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Path Issues:**
Add Python to PATH manually if needed:
- Control Panel → System → Advanced → Environment Variables
- Add Python installation directory to PATH

## Docker Installation (Alternative)

If you prefer Docker:

```bash
# Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
EOF

# Build and run
docker build -t gametheory .
docker run -it gametheory
```

## Troubleshooting

### Issue: "Command not found: python"

**Solution:** Use `python3` instead:
```bash
python3 run.py
```

Or create an alias:
```bash
# Add to ~/.bashrc or ~/.zshrc
alias python=python3
```

### Issue: "Permission denied"

**Linux/Mac Solution:**
```bash
chmod +x run.py
./run.py
```

### Issue: "Module not found: numpy"

**Solution:**
```bash
# Reinstall requirements
pip install -r requirements.txt --force-reinstall

# Or install numpy specifically
pip install numpy
```

### Issue: "No exercises found"

**Solution:**
Make sure you're in the correct directory:
```bash
# Check current directory
pwd

# Should end with /GameTheory
# If not, navigate there
cd path/to/GameTheory
```

### Issue: Virtual environment not activating

**Windows Solution:**
```bash
# Try with full path
C:\path\to\GameTheory\gametheory-env\Scripts\activate.bat

# Or use PowerShell
.\gametheory-env\Scripts\Activate.ps1
```

### Issue: Tests fail

**Solution:**
```bash
# Update all packages
pip install --upgrade pip
pip install -r requirements.txt --upgrade

# Clear cache
make clean  # or manually delete __pycache__ folders

# Try again
python run.py
```

## Development Installation

For contributors:

```bash
# Clone repository
git clone https://github.com/GeoffreyWang1117/GameTheory.git
cd GameTheory

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install in editable mode with dev dependencies
pip install -e .
pip install pytest black flake8 pylint

# Verify installation
pytest tests/
make test
```

## Updating

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Clear cache
make clean
```

## Uninstallation

```bash
# Remove virtual environment
rm -rf gametheory-env/

# Remove repository
rm -rf GameTheory/

# Or if installed as package
pip uninstall gametheory-learning
```

## System Requirements

**Minimum:**
- Python 3.7
- 100 MB disk space
- 512 MB RAM

**Recommended:**
- Python 3.9+
- 200 MB disk space
- 1 GB RAM
- Terminal with color support

## Next Steps

After installation:
1. Read [QUICKSTART.md](QUICKSTART.md) for a 5-minute intro
2. Run `python run.py` to start learning
3. Try the first exercise: Prisoner's Dilemma

## Getting Help

- **Installation issues**: Open an issue on GitHub
- **Platform bugs**: See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Exercise questions**: Use the `hint` command in platform

---

Happy learning! 🎮🧠

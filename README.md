# DBus CCM Testing Project (Professional Setup)

## Setup

### 1. Create virtual environment
python -m venv venv

### 2. Activate
Windows:
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run tests
pytest -v

## Structure
- tests/: test cases
- helper.py: communication + shell abstraction
- ccm_simulator.py: mock ECU
- data_set.py: test data
- conftest.py: fixtures

## AI Prompt Context
This project demonstrates:
- Low-level embedded testing mindset
- DBus-like communication testing
- State verification via shell abstraction
- Pytest best practices (fixtures, structure)

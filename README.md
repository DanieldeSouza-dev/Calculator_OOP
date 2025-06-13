
# 🧮 Object-Oriented Calculator in Python

![Status](https://img.shields.io/badge/status-complete-blue)
![Built with](https://img.shields.io/badge/built%20with-Python%203.13-yellow)

This is an **object-oriented calculator** project written in Python, focused on applying fundamental OOP principles such as encapsulation, modularity, and clean separation of responsibilities.



## 📦 Project Structure

```
📂 Calculator/
│ ├── __init__.py # Initializes the package and simplifies internal imports.
│ ├── app.py # Conect users input to calculation logic.
│ ├── core.py # Contains all calculation functions with validation.
│ └── interface.py # Handles user input/output and validation via command line.
└── main.py # Entry point that starts the calculator application.
```

## Implemented Features

### Init
- Works as the **package initializer** for Python.
- Makes the Calculator/ folder an importable module in other parts of the project.
- Helps organize and simplify imports of internal classes or functions.
- Can be used to centralize imports for easier access, e.g., from .core import Calculadora.

### App
- Controls the main workflow of the application.
- Implements the Calculadora class to manage the user interaction loop.
- Clears the screen, shows the menu, gets user input, and handles calculations.
- Delegates math to core.py and input/output to interface.py.
- Includes division-by-zero validation and clean exit with Ctrl+C.

### Core
- Contains the core logic for all calculator operations.
- Implements the calculate() function, using match to handle each operator.
- Supports addition, subtraction, multiplication, division, exponentiation, percentage, and square root.
- Uses math.sqrt() for root calculations.
- Includes a check for division by zero and returns user-friendly error messages.

### Interface
- Manages user interaction via the command line.
- Displays a simple operation menu with symbols and labels.
- Provides claim_number() to safely read numbers, with validation against invalid input.
- Provides claim_operator() to validate chosen operators, accepting common math symbols.
- Handles input/output separately from logic, following good modular design.

### Main
- Serves as the program’s main entry point.
- Imports the Calculadora class from app.py.
- Creates an instance of Calculadora and starts the calculator with execute().
- Allows running the app simply by executing python main.py.

## ✅ Current Features

- Addition (`+`)  
- Subtraction (`-`)  
- Multiplication (`*`)  
- Division (`/`)  
- Power (`**`)  
- Percentage (`%`)  
- Square Root (`R`)  
- Terminal-based user interaction



## 🚧 Upcoming Features

- New operations:
  - Quadratic equation (discriminant)
  - Hypotenuse calculation  
- GUI integration (Tkinter or similar)  
- Save operation history for future sessions


## 🧠 Key Concepts

- Object-Oriented Programming (OOP)  
- Modular architecture in Python  
- CLI-based user interaction  
- Separation of logic, interface, and control layers



## ▶️ How to Run

1. Make sure you have **Python 3.13** installed.  
2. Run the main file using:

```bash
python main.py
```

3. Use the terminal prompts to interact with the calculator like the example:

```python
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Hello! Welcome to the Calculator OOP 2.0
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] Adiction
[-] Subtraction
[*] Multiplication
[/] Division
[**] Exponentiation
[%] Percentage
[R] Square Root
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Choose operator: +
Choose the first number: 5
Choose the second number: 5
The result is 10.0
Would you like to proceed? [y/n]
```

## ✍️ Author
- Developed by Daniel de Souza

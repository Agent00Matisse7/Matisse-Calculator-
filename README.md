💜 Matisse Calculator 🧡

A simple, graphical desktop calculator built using Python's Tkinter library, featuring a vibrant, artistic color scheme inspired by Henri Matisse.

✨ Features

Basic Arithmetic: Supports addition (+), subtraction (-), multiplication (*), and division (/).

Decimal Support: Handles floating-point numbers and calculations (.).

Clear Functionality: The C button clears the current input/result.

Distinct Aesthetic: Uses a visually striking color palette of dark orange and purple for the display and buttons.

🛠️ Requirements

This project requires only a standard Python installation.

Python 3: (3.6 or higher recommended)

Tkinter: Included by default in most Python distributions.

🚀 How to Run

Save the Code: Save the provided Python code into a file named calculator.py.

Execute: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

python calculator.py


Use the GUI: A small, non-resizable window titled "Matisse Calculator" will appear. Click the buttons to build your expression (e.g., 5 * 8 =).

⚙️ Code Implementation Details

The calculator uses the Python built-in eval() function within a try...except block to safely calculate the string expression built by the button clicks.

Display: Implemented using a tk.Entry widget.

Layout: Uses the grid layout manager for a standard calculator arrangement.

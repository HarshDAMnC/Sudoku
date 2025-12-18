# Sudoku
got stuck in your daily sudoku problem? Don't worry!!

🧩 Sudoku Solver (Backtracking + Flask)

A simple 9×9 Sudoku Solver built using pure backtracking in Python, with a minimal HTML + CSS + JavaScript frontend and a Flask backend.

The user enters a valid Sudoku puzzle, submits it, and the backend solves it using recursion and backtracking.

✨ Features

✅ Solves any valid 9×9 Sudoku

✅ Pure backtracking algorithm (no libraries for solving)

✅ Minimal frontend (no React or frameworks)

✅ Arrow-key navigation between cells

✅ Clean board on page refresh

✅ REST API-based communication (JSON)

🧠 Algorithm Used

The solver uses depth-first search with backtracking:

Traverse the grid cell-by-cell

Try placing numbers 1–9

Check safety:

Row constraint

Column constraint

3×3 subgrid constraint

If placement leads to a dead end, backtrack

Continue until the board is solved

This demonstrates a complete understanding of recursion, backtracking, and constraint checking.

🛠 Tech Stack
Backend

Python

Flask

NumPy

Frontend

HTML

CSS

Vanilla JavaScript (no frameworks)

from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

def safe_place(board,row,col,num):
    if board[row][col] != 0:
        return False
    for i in range(9):
        if board[i][col] == num or board[row][i] == num:
            return False
    sr, sc = row - row%3, col - col%3
    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == num:
                return False
    return True

def solve(board, row=0, col=0):
    if row == 9:
        return True
    if col == 9:
        return solve(board, row+1, 0)
    if board[row][col] != 0:
        return solve(board, row, col+1)

    for num in range(1,10):
        if safe_place(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col+1):
                return True
            board[row][col] = 0
    return False


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve_sudoku():
    data = request.json
    board = np.array(data)
    if solve(board):
        return jsonify(board.tolist())
    return jsonify({"error": "No solution"}), 400

app.run(debug=True)

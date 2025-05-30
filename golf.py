import random

# Character Counting Function
"""
**Objective:** Count the number of occurrences of each character in a string.

**Key Concept:** Text analysis using dictionaries.

**Output:** A dictionary with character counts.
"""
def character_count(text):
    from collections import Counter
    return dict(Counter(text))



# Hole 5: Text Tokenizer
"""
**Objective:** Count the frequency of each word in a string and find the most common word.

**Key Concept:** Text processing and word counting using `collections.Counter`.

**Clue Output:** The most frequent word.
"""
def hole5_word_frequency(text):
    from collections import Counter
    words = text.lower().split()
    return Counter(words)

# Input and output
hole5_input = "data science is fun science is data data science boy oh boy do i love data science it is the best science data is king data is love data is love is data science data science data"
hole5_freq = hole5_word_frequency(hole5_input)
hole5_output = hole5_freq.most_common(1)[0][0]  # Clue: "data"
print("Hole 5 Output:", hole5_output)

# Hole 9: Encode the Message
"""
**Objective:** Encode a string using a Caesar cipher with a fixed shift.

**Key Concept:** String manipulation and encoding.

**Clue Output:** The encoded string.
"""
def hole9_caesar_cipher(text, shift):
    def shift_char(c):
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - start + shift) % 26 + start)
        return c
    return ''.join(shift_char(c) for c in text)

# Input and output
hole9_input = "datascience"
hole9_shift = 5
hole9_output = hole9_caesar_cipher(hole9_input, hole9_shift)  # Clue: "ifxyxhnjshj"
print("Hole 9 Output:", hole9_output)

## Hole 3: Pattern Recognition
#**Task:** Output the first 9 Fibonacci numbers, separated by commas.
# Code here for Hole 3
def hole_3():
    fib = [1, 1]
    while len(fib) < 9:
        fib.append(fib[-1] + fib[-2])
    return ",".join(map(str, fib))

# Run Hole 3
output_3 = hole_3()
print("Hole 3 Output:", output_3)


def hole():
# Print numbers from 1 to 15, replacing multiples of 3 with "Fizz",
# multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    for i in range(1, 16):
        # HOLE: Participants fill this part
        return


# Initialize the board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for a win
def check_winner(board, symbol):
    for row in board:  # Check rows
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):  # Check columns
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)):  # Check diagonal
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):  # Check anti-diagonal
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

# Get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Player makes a move
def player_move(board, symbol):
    while True:
        try:
            move = input("Enter your move (row and column separated by a space, e.g., '1 2'): ")
            row, col = map(int, move.split())
            if board[row][col] == " ":
                board[row][col] = symbol
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

# Bot makes a move
def bot_move(board, symbol):
    moves = get_available_moves(board)
    move = random.choice(moves)
    board[move[0]][move[1]] = symbol

# Main Tic Tac Toe function
def tic_tac_toe():
    print("Welcome to Data Scientist's Tic Tac Toe!")
    print("You are 'X' and the bot is 'O'.")
    
    board = initialize_board()
    player_symbol = "X"
    bot_symbol = "O"
    
    print_board(board)
    while True:
        # Player's turn
        print("Your Turn!")
        player_move(board, player_symbol)
        print_board(board)
        if check_winner(board, player_symbol):
            print("Congratulations! You win! Data is indeed the new gold!")
            break
        if is_full(board):
            print("It's a draw! Data science is about exploring possibilities!")
            break
        
        # Bot's turn
        print("Bot's Turn!")
        bot_move(board, bot_symbol)
        print_board(board)
        if check_winner(board, bot_symbol):
            print("Oh no! The bot wins! Try again; data science rewards perseverance!")
            break
        if is_full(board):
            print("It's a draw! Data science is about exploring possibilities!")
            break

# Run the Tic Tac Toe game
tic_tac_toe()

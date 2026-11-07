# 🔤 Word Scrambler

A simple command-line Word Scrambler game built with Python. The program randomly selects a word, shuffles its letters, and challenges the player to guess the original word.

## 🎮 How It Works

1. The program randomly selects a word from a predefined list of 20 words.
2. It converts the selected word into a list of characters.
3. The characters are shuffled randomly.
4. The player enters their guess.
5. The program checks the answer and displays whether it is correct.
6. The player can choose to play again or exit the game.

## 🛠️ Concepts Used

- Python strings
- Lists
- `random` module
- `random.choice()`
- `random.shuffle()`
- `list()` and `"".join()`
- `while` loops
- Conditional statements (`if/else`)
- User input
- `break` and `continue`

## ▶️ How to Run

1. Make sure Python is installed.
2. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

3. Navigate to the project folder.
4. Run the program:

   ```bash
   python main.py
   ```

## 📸 Example Output

```text
===== WORD SCRAMBLER =====

Scrambled word: nohtyp
Guess the original word: python

Right! The word was: python

Play again? (y/n): n
Bye!
```

## 🎯 Project Purpose

Built as part of my Python practice journey to revise and strengthen my understanding of strings, lists, randomization, loops, and conditional statements.

---

**Language:** Python 3
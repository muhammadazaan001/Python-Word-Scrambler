import random

print("===== WORD SCRAMBLER =====")

words = [
    "python",
    "computer",
    "keyboard",
    "developer",
    "programming",
    "function",
    "variable",
    "internet",
    "database",
    "algorithm",
    "software",
    "hardware",
    "artificial",
    "intelligence",
    "machine",
    "learning",
    "security",
    "browser",
    "network",
    "technology"
]
while True:
    word = random.choice(words)

    letters = list(word)
    random.shuffle(letters)

    print("".join(letters))

    user = input("Guess the original word: ")

    if user.lower() == word:
        print(f"Right! The word was: {word}")
    else:
        print(f"Wrong! The word was: {word}")

    choice = input("Play again?(y/n): ").strip().lower()
    if choice == "y":
        continue
    else:
        print("Bye!")
        break
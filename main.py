import random
import time
import sys 
from collections import Counter

options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0
history = []

def slow_print(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def slow_input(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    return input()

playing = True

while playing:
    player = None

    # 🔥 AI logic (Level 5)
    if history:
        player_moves = [p for p, _ in history]
        most_common = Counter(player_moves).most_common(1)[0][0]

        if most_common == "rock":
            computer = "paper"
        elif most_common == "paper":
            computer = "scissors"
        else:
            computer = "rock"
    else:
        computer = random.choice(options)

    while player not in options:
        player = slow_input("Enter a choice (rock, paper, scissors): ").lower()
        if player not in options:
            slow_print("Invalid choice, try again!")

    # 🎮 Animation (Level 2)
    slow_print("\nRock...")
    time.sleep(0.5)
    slow_print("Paper...")
    time.sleep(0.5)
    slow_print("Scissors!")
    time.sleep(0.3)

    slow_print("\n--- RESULT ---")
    slow_print(f"You chose: {player}")
    slow_print(f"Computer chose: {computer}")

    # 🧠 Clean logic (Level 3)
    if player == computer:
        slow_print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        slow_print("You win!")
        player_score += 1
    else:
        slow_print("You lose!")
        computer_score += 1

    history.append((player, computer))

    slow_print(f"Score → You: {player_score} | Computer: {computer_score}")

    # 🏆 Best of 3 (Level 1)
    if player_score == 3:
        slow_print("🎉 You won the game!")
        break
    elif computer_score == 3:
        slow_print("💀 Computer won the game!")
        break

    answer = input("Play again? (y/n): ").lower()
    if answer != "y":
        playing = False

# 📜 History (Level 4)
slow_print("\nGame History:")
for i, (p, c) in enumerate(history, 1):
    slow_print(f"Round {i}: You - {p} | Computer - {c}")

slow_print("\nThanks for playing!")

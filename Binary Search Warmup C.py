# Binary Search Graph Warmup C
# Elizabeth Matos
# 2023-11-16

import csv

lowest = 1
highest = 100
count = 0
total_guesses = 0
max_guesses = 0
target = int(input("What's your secret number? "))

guess_data = []

while True:
    guess = (lowest + highest) // 2
    count += 1
    total_guesses += 1
    max_guesses = max(max_guesses, count)
    print(f"Guess #{count}: {guess}")
    if guess < target:
        lowest = guess + 1
    elif guess > target:
        highest = guess - 1
    else: # guess == target
        break
    
    average_guesses = total_guesses / 2
    
    guess_data.append([target, average_guesses, max_guesses])
    
with open('BinarySearchGraph.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Target", "Average Guesses", "Max Guesses"])
    writer.writerows(guess_data)
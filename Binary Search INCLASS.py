# Binary Search Algorithm Analysis
# Prof. O & CPTR-215
# 2023-11-13

lowest = 1
highest = 100
count = 0
target = int(input("What's your secret number? "))

while True:
    guess = (lowest + highest) // 2
    count += 1
    print(f"Guess #{count}: {guess}")
    if guess < target:
        lowest = guess + 1
    elif guess > target:
        highest = guess - 1
    else: # guess == target
        break
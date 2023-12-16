import random
import time

# Set the timer (in seconds)
timer = 60

# Create a list of 20 random words
word_list = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
             "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]
random.shuffle(word_list)

print("Memorize the following list of words:")
print(word_list)

# Wait for the timer to expire
time.sleep(timer)

# Cover up the list and try to write down as many words as you can remember
print("\nNow try to write down as many of the words as you can remember:")
remembered_words = input()

# Check how many words were correctly remembered
correct_count = 0
for word in word_list:
    if word in remembered_words:
        correct_count += 1

# Calculate the percentage of correctly remembered words
percentage = correct_count / len(word_list) * 100
print(f"You correctly remembered {correct_count} out of {len(word_list)} words ({percentage:.2f}%)")

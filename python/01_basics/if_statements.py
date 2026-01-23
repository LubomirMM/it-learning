# if_statements.py
# Goal: practice if/elif/else with real input.

# TASK 1:
# Ask the user for a number.
# If it's positive print "positive"
# If it's negative print "negative"
# Otherwise print "zero"

# TASK 2:
# Ask the user for a score (0-100).
# Print:
# 90-100 -> "A"
# 80-89  -> "B"
# 70-79  -> "C"
# 60-69  -> "D"
# 0-59   -> "F"
# If the input is outside 0-100, print "invalid score"

# Start here:
# Write your solutions below this line.
n = int(input("Number: "))

if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

score = int(input("Score (0-100): "))

if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")  
elif score >= 60:
    print("D")
else:
    print("F")
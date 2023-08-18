# This is my code
import math

def paint_calc(height, width, cover):
    cans_needed = float(height * width / cover)
    cans = math.ceil(cans_needed)
    print(f"You'll need {cans} number of cans.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


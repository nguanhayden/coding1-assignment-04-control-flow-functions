def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:
Haydens-MacBook-Pro:coding1-assignment-04-control-flow-functions nguanhayden$ uv run python assignment.py
3
4

the for loop: Iterates through the list [1, 2, 3] one element at a time, assigning each element to the variable number.

the if condition: Evaluates number > 1 for each item:
when number = 1: 1 > 1 is False, so the code inside the block is skipped (nothing is printed or passed to add_one).
when number = 2: 2 > 1 is True, so add_one(2) runs, returning 3, which is then printed.
when number = 3: 3 > 1 is True, so add_one(3) runs, returning 4, which is then printed.


# 2. What does add_one(2) return? Explain the difference between return

# inside the function and print in the loop.
# Your answer:
It returns 3.

return sends a resulting value back from inside the function to whatever code called it (in this case, handing 3 back to the print statement). It also immediately exits the function.
print() simply displays output on the console/screen so a human can see it. It does not give a usable value back to the program's logic.
# Task: Fix Sliding Window Average

You are given a function that calculates the average of the last K numbers.

The current implementation is BUGGY.

Your task is to FIX the function so that it works correctly.

Function:
    add_number(num)

Requirements:

1. Maintain a window of last 3 numbers
2. Return the average of current window
3. If less than 3 numbers, return average of available numbers
4. The window should always contain ONLY last 3 elements

Example:

add_number(1) → 1.0
add_number(2) → 1.5
add_number(3) → 2.0
add_number(4) → 3.0   (window becomes [2,3,4])
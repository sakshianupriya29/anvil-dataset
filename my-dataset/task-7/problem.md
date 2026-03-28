# Task: Unique Visitor Counter

You are building a system to track unique visitors per day.

Function:
    visit(user_id, day)

Rules:

1. Count unique users per day
2. If same user visits multiple times in same day → count once
3. New day → reset count
4. Return current unique count for that day

Example:

visit("u1", 1) → 1
visit("u2", 1) → 2
visit("u1", 1) → 2
visit("u3", 2) → 1
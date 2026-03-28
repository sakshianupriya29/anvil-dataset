# Task: API Cooldown System

You are building an API rate control system.

Function:
    can_request(user_id, timestamp)

Rules:

1. A user can only make 1 request every 5 seconds
2. If user makes request before 5 seconds → return False
3. Otherwise → return True

4. First request is always allowed

5. Exactly 5 seconds gap is allowed

6. Each user is independent

Example:

can_request("u1", 1) → True
can_request("u1", 3) → False
can_request("u1", 6) → True
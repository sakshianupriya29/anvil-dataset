Task: Login Attempt System

Implement a login attempt tracker.

Function:
    login(user_id, password_correct, timestamp)

Rules:

1. If password_correct is True → return "SUCCESS"
2. If False → count as failed attempt

3. After 3 failed attempts → user is LOCKED for 10 seconds

4. During lock:
   → return "LOCKED"

5. After 10 seconds:
   → user can try again

6. Successful login resets failed attempts

7. Users are independent

Example:

login("u1", False, 1) → "FAIL"
login("u1", False, 2) → "FAIL"
login("u1", False, 3) → "LOCKED"
login("u1", True, 5) → "LOCKED"
login("u1", True, 15) → "SUCCESS"
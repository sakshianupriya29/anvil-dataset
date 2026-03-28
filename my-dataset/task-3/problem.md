Task: Message Deduplication System

You are building a system to prevent duplicate messages.

Function:
    send_message(user_id, message, timestamp)

Rules:

1. If the same user sends the SAME message within 10 seconds:
   → return False (duplicate)

2. Otherwise:
   → return True

3. After 10 seconds:
   → same message is allowed again

4. Different users can send same message anytime

5. Messages are case-sensitive

Example:

send_message("u1", "Hi", 1) → True
send_message("u1", "Hi", 5) → False
send_message("u1", "Hi", 12) → True
send_message("u2", "Hi", 5) → True
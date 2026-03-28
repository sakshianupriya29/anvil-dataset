Task: Session-Based Rate Limiter

You are given a system that tracks user requests.

Implement a function:

    allow_request(user_id, timestamp)

Rules:

1. Each user can make at most 3 requests within 5 seconds.
2. If the user exceeds the limit → return False
3. Otherwise → return True

4. The system must automatically reset the count after 5 seconds.

5. Each user must be tracked independently.

6. IMPORTANT EDGE CASE:
   If requests are exactly 5 seconds apart, they should be allowed.

Example:

allow_request("u1", 1) → True
allow_request("u1", 2) → True
allow_request("u1", 3) → True
allow_request("u1", 4) → False
allow_request("u1", 6) → True  (reset happens)
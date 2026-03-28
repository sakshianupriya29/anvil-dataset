# Task: Notification Queue System

You are building a simple notification system.

Functions:

1. send_notification(user_id, message)
2. get_next_notification(user_id)

Rules:

1. Notifications must be delivered in FIFO order
2. Each user has their own queue
3. If no notifications → return None
4. After fetching, notification is removed
5. Users are independent

Example:

send_notification("u1", "Hello")
send_notification("u1", "World")

get_next_notification("u1") → "Hello"
get_next_notification("u1") → "World"
get_next_notification("u1") → None
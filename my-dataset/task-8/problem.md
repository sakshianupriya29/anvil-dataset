# Task: Expiring Task Scheduler

You are building a system that schedules tasks with expiry.

Functions:

1. add_task(task_id, timestamp)
2. get_next_task(timestamp)

Rules:

1. Tasks expire after 10 seconds
2. Expired tasks must NOT be returned
3. Tasks should be returned in FIFO order
4. If no valid task → return None

Example:

add_task("t1", 1)
add_task("t2", 2)

get_next_task(5) → "t1"
get_next_task(12) → "t2"
get_next_task(25) → None
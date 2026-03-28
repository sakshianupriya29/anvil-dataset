from collections import deque

tasks = deque()

def add_task(task_id, timestamp):
    tasks.append((task_id, timestamp))

def get_next_task(timestamp):
    while tasks:
        task_id, t = tasks[0]

        if timestamp - t >= 10:
            tasks.popleft()
        else:
            return tasks.popleft()[0]

    return None
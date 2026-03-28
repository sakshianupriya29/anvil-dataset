from collections import defaultdict, deque

queues = defaultdict(deque)

def send_notification(user_id, message):
    queues[user_id].append(message)

def get_next_notification(user_id):
    if queues[user_id]:
        return queues[user_id].popleft()
    return None
from collections import defaultdict, deque

history = defaultdict(deque)

def search(user_id, query):
    user_history = history[user_id]

    if query in user_history:
        user_history.remove(query)

    user_history.appendleft(query)

    if len(user_history) > 5:
        user_history.pop()

    return list(user_history)
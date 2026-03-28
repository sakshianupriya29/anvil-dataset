from collections import defaultdict

fail_count = defaultdict(int)
lock_time = {}

def login(user_id, password_correct, timestamp):
    # Check lock
    if user_id in lock_time:
        if timestamp - lock_time[user_id] < 10:
            return "LOCKED"
        else:
            del lock_time[user_id]
            fail_count[user_id] = 0

    if password_correct:
        fail_count[user_id] = 0
        return "SUCCESS"
    
    fail_count[user_id] += 1

    if fail_count[user_id] >= 3:
        lock_time[user_id] = timestamp
        return "LOCKED"

    return "FAIL"
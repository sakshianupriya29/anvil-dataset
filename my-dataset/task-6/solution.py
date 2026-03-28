last_request_time = {}

def can_request(user_id, timestamp):
    if user_id not in last_request_time:
        last_request_time[user_id] = timestamp
        return True
    
    if timestamp - last_request_time[user_id] >= 5:
        last_request_time[user_id] = timestamp
        return True
    
    return False
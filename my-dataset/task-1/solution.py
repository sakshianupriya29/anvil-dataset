from collections import defaultdict

user_requests = defaultdict(list)

def allow_request(user_id, timestamp):
    requests = user_requests[user_id]

    # Remove old timestamps
    while requests and timestamp - requests[0] >= 5:
        requests.pop(0)

    if len(requests) < 3:
        requests.append(timestamp)
        return True
    return False
    # temp change
    
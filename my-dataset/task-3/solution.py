from collections import defaultdict

message_log = defaultdict(dict)

def send_message(user_id, message, timestamp):
    user_data = message_log[user_id]

    if message in user_data:
        if timestamp - user_data[message] < 10:
            return False

    user_data[message] = timestamp
    return True
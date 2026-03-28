from collections import defaultdict

daily_users = defaultdict(set)
current_day = None

def visit(user_id, day):
    global current_day

    if current_day != day:
        daily_users.clear()
        current_day = day

    daily_users[day].add(user_id)
    return len(daily_users[day])
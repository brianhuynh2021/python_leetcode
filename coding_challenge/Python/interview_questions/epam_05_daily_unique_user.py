# 5. Daily unique users

# Problem

# Given logs with user and ISO timestamp, return (date, unique_user_count) sorted by date.

# Input

logs = [
    {"user": "u1", "timestamp": "2025-08-09T10:00:00"},
    {"user": "u1", "timestamp": "2025-08-09T11:00:00"},
    {"user": "u2", "timestamp": "2025-08-10T09:00:00"},
]

# Output

# [('2025-08-09', 1), ('2025-08-10', 1)]

def daily_unique_user(logs):
    days = sorted({l["timestamp"][:10] for l in logs})
    res = []
    for d in days:
        users = set(l["user"] for l in logs if l["timestamp"][:10] == d)
        res.append((d, len(users)))
    return res

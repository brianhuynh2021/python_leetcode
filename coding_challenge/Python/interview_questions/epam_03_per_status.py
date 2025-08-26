# Count how many rows per status and return sorted by count descending.

# Input

rows = [
    {"id": 1, "status": "pending"},
    {"id": 2, "status": "done"},
    {"id": 3, "status": "pending"},
]

# Output

# [('pending', 2), ('done', 1)]

def rows_per_status(rows):
    result = {}
    for r in rows:
        status = r["status"]
        result[status] = result.get(status, 0) + 1
    print(result)
    return sorted(result.items(),key=lambda x: x[1], reverse=True)
print(rows_per_status(rows))
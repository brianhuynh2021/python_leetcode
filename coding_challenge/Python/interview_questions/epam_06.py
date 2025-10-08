# 6. Revenue per day (fill gaps)

# Problem

# Sum revenue by date and fill missing days with 0 between min and max date.

# Input

# rows = [
#     {"date": "2025-08-08", "amount": 100},
#     {"date": "2025-08-10", "amount": 50},
# ]

# Output

# [('2025-08-08', 100), ('2025-08-09', 0), ('2025-08-10', 50)]

# Brute‑force solution

from datetime import datetime, timedelta


def revenue_per_day_bruteforce(rows):
    dates = sorted({r["date"] for r in rows})
    d0, d1 = dates[0], dates[-1]
    cur = datetime.fromisoformat(d0).date()
    end = datetime.fromisoformat(d1).date()
    res = []
    while cur <= end:
        day = cur.isoformat()
        s = sum(r["amount"] for r in rows if r["date"] == day)
        res.append((day, s))
        cur += timedelta(days=1)
    return res

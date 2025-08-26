# EPAM Live Coding Practice - 42 Problems
# Each problem includes Input and Expected Output examples

# Problem 1: Total price per customer (sorted by total desc)
orders_1 = [
    {"customer": "Alice", "amount": 120},
    {"customer": "Bob", "amount": 90},
    {"customer": "Alice", "amount": 50},
]
expected_1 = [("Alice", 170), ("Bob", 90)]

# Problem 2: Average rating per product (sorted by average desc then product asc)
ratings_2 = [
    {"product": "A", "rating": 5},
    {"product": "A", "rating": 3},
    {"product": "B", "rating": 4},
]
expected_2 = [("A", 4.0), ("B", 4.0)]

# TODO: Fill in problems 3 to 42 with their input/output examples



# 1. Total amount per customer (group & sum)

# Problem

# Given a list of orders (dicts), compute the total amount per customer and return a list of tuples sorted by total descending.

# Input

orders = [
    {"customer": "Alice", "amount": 120},
    {"customer": "Bob", "amount": 90},
    {"customer": "Alice", "amount": 50},
]

# Output

# [('Alice', 170), ('Bob', 90)]

# Brute‑force solution

def total_per_customer_bruteforce(orders):
    res = []
    customers = {o["customer"] for o in orders}
    for c in customers:
        s = 0
        for o in orders:
            if o["customer"] == c:
                s += o["amount"]
        res.append((c, s))
    return sorted(res, key=lambda x: x[1], reverse=True)

Optimized solution

from collections import defaultdict
def total_per_customer(orders):
    totals = defaultdict(int)
    for o in orders:
        totals[o["customer"]] += o["amount"]
    return sorted(totals.items(), key=lambda x: x[1], reverse=True)


⸻

2. Average rating per product

Problem

Given ratings with product and rating, compute average rating per product. Sort by average desc then product asc.

Input

ratings = [
    {"product": "A", "rating": 5},
    {"product": "A", "rating": 3},
    {"product": "B", "rating": 4},
]

Output

[('A', 4.0), ('B', 4.0)]

Brute‑force solution

def avg_per_product_bruteforce(ratings):
    res = []
    prods = {r["product"] for r in ratings}
    for p in prods:
        vals = [r["rating"] for r in ratings if r["product"] == p]
        res.append((p, sum(vals)/len(vals)))
    return sorted(res, key=lambda x: (-x[1], x[0]))

Optimized solution

from collections import defaultdict
def avg_per_product(ratings):
    sums, cnt = defaultdict(int), defaultdict(int)
    for r in ratings:
        sums[r["product"]] += r["rating"]
        cnt[r["product"]] += 1
    out = [(p, sums[p]/cnt[p]) for p in sums]
    return sorted(out, key=lambda x: (-x[1], x[0]))


⸻

3. Count per status

Problem

Count how many rows per status and return sorted by count descending.

Input

rows = [
    {"id": 1, "status": "pending"},
    {"id": 2, "status": "done"},
    {"id": 3, "status": "pending"},
]

Output

[('pending', 2), ('done', 1)]

Brute‑force solution

def count_per_status_bruteforce(rows):
    res = []
    statuses = {x["status"] for x in rows}
    for s in statuses:
        res.append((s, sum(1 for x in rows if x["status"] == s)))
    return sorted(res, key=lambda x: x[1], reverse=True)

Optimized solution

from collections import Counter
def count_per_status(rows):
    c = Counter(x["status"] for x in rows)
    return sorted(c.items(), key=lambda x: x[1], reverse=True)


⸻

4. Top-K items per category

Problem

For each category, find the top K items by price.

Input

items = [
    {"category": "A", "name": "i1", "price": 10},
    {"category": "A", "name": "i2", "price": 50},
    {"category": "B", "name": "i3", "price": 20},
    {"category": "A", "name": "i4", "price": 30},
]
K = 2



{'A': [{'category': 'A', 'name': 'i2', 'price': 50}, {'category': 'A', 'name': 'i4', 'price': 30}], 'B': [{'category': 'B', 'name': 'i3', 'price': 20}]}

# Brute‑force solution

def topk_per_category_bruteforce(items, k=2):
    res = {}
    cats = {x["category"] for x in items}
    for cat in cats:
        arr = [x for x in items if x["category"] == cat]
        arr.sort(key=lambda x: x["price"], reverse=True)
        res[cat] = arr[:k]
    return res

Optimized solution

from collections import defaultdict
from heapq import nlargest
def topk_per_category(items, k=2):
    groups = defaultdict(list)
    for x in items:
        groups[x["category"]].append(x)
    return {cat: nlargest(k, lst, key=lambda x: x["price"]) for cat,lst in groups.items()}


⸻

5. Daily unique users

Problem

Given logs with user and ISO timestamp, return (date, unique_user_count) sorted by date.

Input

logs = [
    {"user": "u1", "timestamp": "2025-08-09T10:00:00"},
    {"user": "u1", "timestamp": "2025-08-09T11:00:00"},
    {"user": "u2", "timestamp": "2025-08-10T09:00:00"},
]

Output

[('2025-08-09', 1), ('2025-08-10', 1)]

Brute‑force solution

def daily_unique_users_bruteforce(logs):
    days = sorted({l["timestamp"][:10] for l in logs})
    res = []
    for d in days:
        users = set(l["user"] for l in logs if l["timestamp"][:10] == d)
        res.append((d, len(users)))
    return res

Optimized solution

from collections import defaultdict
def daily_unique_users(logs):
    by_day = defaultdict(set)
    for l in logs:
        day = l["timestamp"][:10]
        by_day[day].add(l["user"])
    return sorted(((d, len(s)) for d,s in by_day.items()), key=lambda x: x[0])


⸻

6. Revenue per day (fill gaps)

Problem

Sum revenue by date and fill missing days with 0 between min and max date.

Input

rows = [
    {"date": "2025-08-08", "amount": 100},
    {"date": "2025-08-10", "amount": 50},
]

Output

[('2025-08-08', 100), ('2025-08-09', 0), ('2025-08-10', 50)]

Brute‑force solution

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

Optimized solution

from collections import defaultdict
from datetime import datetime, timedelta
def revenue_per_day(rows):
    sums = defaultdict(int)
    min_d = max_d = None
    for r in rows:
        sums[r["date"]] += r["amount"]
        d = datetime.fromisoformat(r["date"]).date()
        if not min_d or d < min_d: min_d = d
        if not max_d or d > max_d: max_d = d
    res = []
    cur = min_d
    while cur <= max_d:
        day = cur.isoformat()
        res.append((day, sums.get(day, 0)))
        cur += timedelta(days=1)
    return res


⸻

7. Weighted average per student

Problem

Each row has student, score, weight. Return (student, weighted_avg).

Input

rows = [
    {"student": "A", "score": 80, "weight": 2},
    {"student": "A", "score": 100, "weight": 1},
    {"student": "B", "score": 70, "weight": 3},
]

Output

[('A', 86.66666666666667), ('B', 70.0)]

Brute‑force solution

def weighted_avg_bruteforce(rows):
    students = {r["student"] for r in rows}
    out = []
    for s in students:
        sc = sum(r["score"]*r["weight"] for r in rows if r["student"] == s)
        w  = sum(r["weight"] for r in rows if r["student"] == s)
        out.append((s, sc/w if w else 0))
    return out

Optimized solution

from collections import defaultdict
def weighted_avg(rows):
    num, den = defaultdict(float), defaultdict(float)
    for r in rows:
        num[r["student"]] += r["score"]*r["weight"]
        den[r["student"]] += r["weight"]
    return [(s, num[s]/den[s] if den[s] else 0) for s in num]


⸻

8. Action pivot per user

Problem

Given (user, action) pairs, return list of dicts: {‘user’: u, action1: count1, …}.

Input

events = [('u1','login'), ('u1','buy'), ('u1','login'), ('u2','login')]

Output

[{'user': 'u1', 'buy': 1, 'login': 2}, {'user': 'u2', 'buy': 0, 'login': 1}]

Brute‑force solution

def action_pivot_bruteforce(events):
    users = sorted({u for u,_ in events})
    actions = sorted({a for _,a in events})
    out = []
    for u in users:
        row = {"user": u}
        for a in actions:
            row[a] = sum(1 for uu,aa in events if uu==u and aa==a)
        out.append(row)
    return out

Optimized solution

from collections import defaultdict, Counter
def action_pivot(events):
    per_user = defaultdict(Counter)
    for u,a in events:
        per_user[u][a] += 1
    actions = sorted({a for _,a in events})
    out = []
    for u,c in per_user.items():
        row = {"user": u}
        for a in actions:
            row[a] = c.get(a,0)
        out.append(row)
    return out


⸻

9. Bucket aggregation (prices)

Problem

Count how many prices fall into bins: 0-99, 100-199, >=200.

Input

prices = [5, 120, 150, 205, 99, 100, 200]

Output

{'0-99': 2, '100-199': 3, '>=200': 2}

Brute‑force solution

def bucket_prices_bruteforce(prices):
    bins = {"0-99":0, "100-199":0, ">=200":0}
    for p in prices:
        if p < 100: bins["0-99"] += 1
        elif p < 200: bins["100-199"] += 1
        else: bins[">=200"] += 1
    return bins

Optimized solution

# Same as brute; already O(n) one pass.
def bucket_prices(prices):
    bins = {"0-99":0, "100-199":0, ">=200":0}
    for p in prices:
        if p < 100: bins["0-99"] += 1
        elif p < 200: bins["100-199"] += 1
        else: bins[">=200"] += 1
    return bins


⸻

10. Rolling sum with window W

Problem

Return list of sums for each contiguous window of size W.

Input

arr = [1,2,3,4,5]; W = 3

Output

[6, 9, 12]

Brute‑force solution

def rolling_sum_bruteforce(arr, w):
    return [sum(arr[i:i+w]) for i in range(0, max(0, len(arr)-w+1))]

Optimized solution

def rolling_sum(arr, w):
    n = len(arr)
    if w <= 0 or w > n: return []
    s = sum(arr[:w])
    out = [s]
    for i in range(w, n):
        s += arr[i] - arr[i-w]
        out.append(s)
    return out


⸻

11. Join authors and books (author -> titles)

Problem

Join two lists by author id; output dict author_name -> list of titles.

Input

authors = [{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]
books = [{"author_id":1,"title":"B1"},{"author_id":2,"title":"B2"},{"author_id":1,"title":"B3"}]

Output

{'Alice': ['B1', 'B3'], 'Bob': ['B2']}

Brute‑force solution

from collections import defaultdict
def authors_books_bruteforce(authors, books):
    res = defaultdict(list)
    for a in authors:
        for b in books:
            if b["author_id"] == a["id"]:
                res[a["name"]].append(b["title"])
    return dict(res)

Optimized solution

from collections import defaultdict
def authors_books(authors, books):
    id2name = {a["id"]: a["name"] for a in authors}
    res = defaultdict(list)
    for b in books:
        res[id2name.get(b["author_id"], "Unknown")].append(b["title"])
    return dict(res)


⸻

12. Users total spent (join + sum)

Problem

Join users and transactions by id, sum amounts per user and sort desc.

Input

users = [{"id":1,"name":"Ann"},{"id":2,"name":"Ben"}]
txs = [{"user_id":1,"amount":30.5},{"user_id":1,"amount":10},{"user_id":2,"amount":50}]

Output

[('Ben', 50.0), ('Ann', 40.5)]

Brute‑force solution

def user_spent_bruteforce(users, txs):
    out = []
    for u in users:
        s = sum(t["amount"] for t in txs if t["user_id"] == u["id"])
        out.append((u["name"], s))
    return sorted(out, key=lambda x: x[1], reverse=True)

Optimized solution

from collections import defaultdict
def user_spent(users, txs):
    id2name = {u["id"]: u["name"] for u in users}
    totals = defaultdict(float)
    for t in txs:
        totals[id2name.get(t["user_id"], "Unknown")] += t["amount"]
    return sorted(totals.items(), key=lambda x: x[1], reverse=True)


⸻

13. Inner join products and prices by SKU

Problem

Return list of (sku, name, price) only where SKU exists in both lists.

Input

products = [{"sku":"S1","name":"A"},{"sku":"S2","name":"B"}]
prices = [{"sku":"S1","price":10},{"sku":"S3","price":99}]

Output

[('S1', 'A', 10)]

Brute‑force solution

def join_products_prices_bruteforce(products, prices):
    res = []
    for p in products:
        for q in prices:
            if q["sku"] == p["sku"]:
                res.append((p["sku"], p["name"], q["price"])) 
    return res

Optimized solution

def join_products_prices(products, prices):
    sku2price = {x["sku"]: x["price"] for x in prices}
    return [(p["sku"], p["name"], sku2price[p["sku"]])
            for p in products if p["sku"] in sku2price]


⸻

14. Left-join users with profiles

Problem

Attach optional profile dict to each user; profile may be missing.

Input

users = [{"id":1,"name":"A"},{"id":2,"name":"B"}]
profiles = [{"user_id":1,"title":"Dev"}]

Output

[{'id': 1, 'name': 'A', 'profile': {'user_id': 1, 'title': 'Dev'}}, {'id': 2, 'name': 'B', 'profile': None}]

Brute‑force solution

def left_join_profiles_bruteforce(users, profiles):
    out = []
    for u in users:
        prof = None
        for p in profiles:
            if p["user_id"] == u["id"]:
                prof = p
                break
        out.append({**u, "profile": prof})
    return out

Optimized solution

def left_join_profiles(users, profiles):
    id2prof = {p["user_id"]: p for p in profiles}
    return [{**u, "profile": id2prof.get(u["id"])} for u in users]


⸻

15. Many-to-many: courses per student

Problem

Using enrollments, list course names per student (sorted).

Input

students = [{"id":1,"name":"S1"},{"id":2,"name":"S2"}]
courses = [{"id":10,"name":"C1"},{"id":20,"name":"C2"}]
enrollments = [{"student_id":1,"course_id":10},{"student_id":1,"course_id":20},{"student_id":2,"course_id":20}]

Output

{'S1': ['C1', 'C2'], 'S2': ['C2']}

Brute‑force solution

def courses_per_student_bruteforce(students, courses, enrollments):
    id2name = {c["id"]: c["name"] for c in courses}
    res = {}
    for s in students:
        res[s["name"]] = sorted([id2name[e["course_id"]] for e in enrollments if e["student_id"]==s["id"]])
    return res

Optimized solution

from collections import defaultdict
def courses_per_student(students, courses, enrollments):
    id2name = {c["id"]: c["name"] for c in courses}
    res = defaultdict(list)
    for e in enrollments:
        res[e["student_id"]].append(id2name[e["course_id"]])
    id2student = {s["id"]: s["name"] for s in students}
    return {id2student[i]: sorted(names) for i,names in res.items()}


⸻

16. Orders not refunded (anti-join)

Problem

Return orders whose id is not present in refunds.order_id.

Input

orders = [{"id":1},{"id":2},{"id":3}]
refunds = [{"order_id":2}]

Output

[{'id': 1}, {'id': 3}]

Brute‑force solution

def orders_not_refunded_bruteforce(orders, refunds):
    out = []
    for o in orders:
        if not any(r["order_id"] == o["id"] for r in refunds):
            out.append(o)
    return out

Optimized solution

def orders_not_refunded(orders, refunds):
    refunded = {r["order_id"] for r in refunds}
    return [o for o in orders if o["id"] not in refunded]


⸻

17. Sum quantity per order

Problem

Join orders and items; return list of (order_id, total_qty).

Input

orders = [{"id":1},{"id":2}]
items = [{"order_id":1,"qty":2},{"order_id":1,"qty":3},{"order_id":2,"qty":1}]

Output

[(1, 5), (2, 1)]

Brute‑force solution

def qty_per_order_bruteforce(orders, items):
    res = []
    for o in orders:
        q = sum(it["qty"] for it in items if it["order_id"] == o["id"])
        res.append((o["id"], q))
    return res

Optimized solution

from collections import defaultdict
def qty_per_order(orders, items):
    totals = defaultdict(int)
    for it in items:
        totals[it["order_id"]] += it["qty"]
    return [(o["id"], totals.get(o["id"],0)) for o in orders]


⸻

18. Products missing in inventory (anti-join by sku)

Problem

Return products whose sku is not present in inventory list.

Input

products = [{"sku":"A"},{"sku":"B"},{"sku":"C"}]
inventory = [{"sku":"B"}]

Output

[{'sku': 'A'}, {'sku': 'C'}]

Brute‑force solution

def missing_products_bruteforce(products, inventory):
    inv = [i["sku"] for i in inventory]
    return [p for p in products if p["sku"] not in inv]

Optimized solution

def missing_products(products, inventory):
    inv = {i["sku"] for i in inventory}
    return [p for p in products if p["sku"] not in inv]


⸻

19. Remove vowels and reverse string

Problem

Remove vowels (a,e,i,o,u) from the string, then reverse the result.

Input

s = 'Epam Python'

Output

nthP mp

Brute‑force solution

def remove_vowels_reverse_bruteforce(s):
    vowels = set("aeiouAEIOU")
    out = []
    for ch in s[::-1]:
        if ch not in vowels:
            out.append(ch)
    return "".join(out)

Optimized solution

def remove_vowels_reverse(s):
    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in reversed(s) if ch not in vowels)


⸻

20. Normalize spaces

Problem

Trim and collapse multiple spaces into a single space.

Input

s = '  Hello   EPAM   Team  '

Output

Hello EPAM Team

Brute‑force solution

def normalize_spaces_bruteforce(s):
    out, prev_space = [], False
    for ch in s.strip():
        if ch.isspace():
            if not prev_space:
                out.append(" ")
            prev_space = True
        else:
            out.append(ch); prev_space = False
    return "".join(out)

Optimized solution

def normalize_spaces(s):
    return " ".join(s.split())


⸻

21. Convert kebab-case <-> snake_case

Problem

Implement converters between ‘my-var-name’ and ‘my_var_name’.

Input

s1='my-var-name'; s2='my_var_name'

Output

kebab_to_snake(s1) -> 'my_var_name'; snake_to_kebab(s2) -> 'my-var-name'

Brute‑force solution

def kebab_to_snake_bruteforce(s):
    out = []
    for ch in s:
        out.append('_' if ch == '-' else ch)
    return "".join(out)

def snake_to_kebab_bruteforce(s):
    out = []
    for ch in s:
        out.append('-' if ch == '_' else ch)
    return "".join(out)

Optimized solution

def kebab_to_snake(s): return s.replace('-', '_')
def snake_to_kebab(s): return s.replace('_', '-')


⸻

22. Validate emails (simple regex)

Problem

Return only valid emails using a simple regex.

Input

emails = ['a@b.com','bad@','x@y.z']

Output

['a@b.com', 'x@y.z']

Brute‑force solution

import re
def valid_emails_bruteforce(lst):
    good = []
    for e in lst:
        if '@' in e and '.' in e.split('@')[-1] and e[0].isalnum():
            good.append(e)
    return good

Optimized solution

import re
_email_re = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
def valid_emails(lst):
    return [e for e in lst if _email_re.match(e)]


⸻

23. Mask card number

Problem

Replace all digits with ‘*’ except the last 4 (preserve spaces).

Input

s = '4111 1111 1111 1234'

Output

**** **** **** 1234

Brute‑force solution

def mask_card_bruteforce(s):
    digits = [ch for ch in s if ch.isdigit()]
    keep = digits[-4:]
    res, di = [], 0
    total_digits = len(digits)
    keep_from = total_digits - 4
    seen = 0
    for ch in s:
        if ch.isdigit():
            if seen < keep_from: res.append('*')
            else: res.append(ch)
            seen += 1
        else:
            res.append(ch)
    return "".join(res)

Optimized solution

def mask_card(s):
    total_digits = sum(ch.isdigit() for ch in s)
    keep_from = total_digits - 4
    res = []
    seen = 0
    for ch in s:
        if ch.isdigit():
            res.append(ch if seen >= keep_from else '*')
            seen += 1
        else:
            res.append(ch)
    return "".join(res)


⸻

24. Extract root domain

Problem

From a URL, extract the registrable domain (simple heuristic for some multi-part TLDs).

Input

url = 'https://sub.shop.example.co.uk/path'

Output

example.co.uk

Brute‑force solution

from urllib.parse import urlparse
def extract_domain_bruteforce(url):
    host = urlparse(url).netloc.lower()
    host = host.split('@')[-1].split(':')[0]
    parts = [p for p in host.split('.') if p]
    if len(parts) <= 2:
        return '.'.join(parts)
    # simple fallback: last two
    return '.'.join(parts[-2:])

Optimized solution

MULTIPART_TLDS = {"co.uk","org.uk","ac.uk","com.au","net.au","co.jp"}
def extract_domain(url):
    host = urlparse(url).netloc.lower().split('@')[-1].split(':')[0]
    parts = [p for p in host.split('.') if p]
    if len(parts) <= 2: return '.'.join(parts)
    last2 = '.'.join(parts[-2:])
    last3 = '.'.join(parts[-3:])
    if last2 in MULTIPART_TLDS or last3 in MULTIPART_TLDS:
        return '.'.join(parts[-3:])
    return last2


⸻

25. Group anagrams

Problem

Group words that are anagrams, case-insensitive.

Input

words = ['eat','Tea','tan','ate','Nat','bat']

Output

[['eat', 'Tea', 'ate'], ['tan', 'Nat'], ['bat']]

Brute‑force solution

def group_anagrams_bruteforce(words):
    used = [False]*len(words)
    groups = []
    for i,w in enumerate(words):
        if used[i]: continue
        key = ''.join(sorted(w.lower()))
        cur = [w]; used[i]=True
        for j in range(i+1,len(words)):
            if not used[j] and ''.join(sorted(words[j].lower()))==key:
                cur.append(words[j]); used[j]=True
        groups.append(cur)
    return groups

Optimized solution

from collections import defaultdict
def group_anagrams(words):
    d = defaultdict(list)
    for w in words:
        d[''.join(sorted(w.lower()))].append(w)
    return list(d.values())


⸻

26. Longest words

Problem

Return all longest words (ties allowed).

Input

words = ['aa','bbb','cc','dddd','eee']

Output

['dddd']

Brute‑force solution

def longest_words_bruteforce(words):
    m = 0
    for w in words:
        if len(w) > m: m = len(w)
    return [w for w in words if len(w) == m]

Optimized solution

def longest_words(words):
    if not words: return []
    m = max(len(w) for w in words)
    return [w for w in words if len(w) == m]


⸻

27. Run-length encoding/decoding

Problem

Encode ‘aaabbc’ -> ‘a3b2c1’ and decode back.

Input

s = 'aaabbc'

Output

encode: 'a3b2c1'; decode('a3b2c1') -> 'aaabbc'

Brute‑force solution

def rle_encode(s):
    if not s: return ''
    out, cnt, prev = [], 1, s[0]
    for ch in s[1:]:
        if ch == prev: cnt += 1
        else: out.append(f"{prev}{cnt}"); prev, cnt = ch, 1
    out.append(f"{prev}{cnt}")
    return ''.join(out)
def rle_decode(s):
    out, i = [], 0
    while i < len(s):
        ch = s[i]; i += 1
        j = i
        while j < len(s) and s[j].isdigit(): j += 1
        cnt = int(s[i:j]); i = j
        out.append(ch * cnt)
    return ''.join(out)

Optimized solution

None (same approach is optimal/clear).

⸻

28. Flatten products from nested categories

Problem

Return list of (name, price) tuples from nested structure.

Input

data = {"categories":[
    {"products":[{"name":"A","price":10},{"name":"B","price":20}]},
    {"products":[{"name":"C","price":30}]}
]}

Output

[('A', 10), ('B', 20), ('C', 30)]

Brute‑force solution

def flatten_products_bruteforce(payload):
    out = []
    cats = payload.get('categories', [])
    for c in cats:
        prods = c.get('products', [])
        for p in prods:
            out.append((p['name'], p['price']))
    return out

Optimized solution

def flatten_products(payload):
    out = []
    for cat in payload.get('categories', []):
        for p in cat.get('products', []):
            out.append((p['name'], p['price']))
    return out


⸻

29. Pick fields from nested objects

Problem

From items with nested category, pick id, name, price, category_name.

Input

items = [
    {"id":1,"name":"A","price":10,"category":{"name":"Cat1"}},
    {"id":2,"name":"B","price":20,"category":{}},
]

Output

[{'id': 1, 'name': 'A', 'price': 10, 'category_name': 'Cat1'}, {'id': 2, 'name': 'B', 'price': 20, 'category_name': None}]

Brute‑force solution

def pick_fields_bruteforce(items):
    out = []
    for x in items:
        cat = x.get('category', {})
        out.append({'id': x['id'], 'name': x['name'], 'price': x['price'], 'category_name': cat.get('name')})
    return out

Optimized solution

def pick_fields(items):
    return [{"id":x["id"],"name":x["name"],"price":x["price"],"category_name": x.get("category",{}).get("name")}
            for x in items]


⸻

30. Tree to root-to-leaf paths

Problem

Given a tree with ‘name’ and ‘children’, list all root-to-leaf paths as ‘a/b/c’.

Input

tree = {"name":"root","children":[
    {"name":"A","children":[{"name":"A1"}]},
    {"name":"B"}
]}

Output

['root/A/A1', 'root/B']

Brute‑force solution

def tree_paths_bruteforce(tree):
    paths = []
    def dfs(node, path):
        path.append(node['name'])
        if not node.get('children'):
            paths.append('/'.join(path))
        else:
            for ch in node['children']:
                dfs(ch, path)
        path.pop()
    dfs(tree, [])
    return paths

Optimized solution

# Same as brute; DFS is optimal here.
def tree_paths(tree):
    paths = []
    def dfs(node, path):
        path.append(node['name'])
        if not node.get('children'):
            paths.append('/'.join(path))
        else:
            for ch in node['children']:
                dfs(ch, path)
        path.pop()
    dfs(tree, [])
    return paths


⸻

31. Sum by nested key (shipping.country)

Problem

Sum order amounts grouped by shipping.country; sort by sum desc then country asc.

Input

orders = [
    {"amount": 100, "shipping": {"country": "US"}},
    {"amount": 50,  "shipping": {"country": "VN"}},
    {"amount": 70,  "shipping": {"country": "US"}},
]

Output

[('US', 170), ('VN', 50)]

Brute‑force solution

def sum_by_country_bruteforce(orders):
    countries = {o.get('shipping',{}).get('country') for o in orders}
    out = []
    for c in countries:
        s = sum(o['amount'] for o in orders if o.get('shipping',{}).get('country') == c)
        out.append((c, s))
    return sorted(out, key=lambda x: (-x[1], x[0] or ''))

Optimized solution

from collections import defaultdict
def sum_by_country(orders):
    sums = defaultdict(float)
    for o in orders:
        c = o.get('shipping',{}).get('country')
        sums[c] += o['amount']
    return sorted(sums.items(), key=lambda x: (-x[1], x[0] or ''))


⸻

32. Merge duplicate IDs (prefer later rows)

Problem

If multiple dicts share the same id, merge them; later rows override earlier.

Input

rows = [
    {"id": 1, "name": "A"},
    {"id": 1, "price": 10},
    {"id": 2, "name": "B"},
]

Output

[{'id': 1, 'name': 'A', 'price': 10}, {'id': 2, 'name': 'B'}]

Brute‑force solution

def merge_duplicates_by_id_bruteforce(rows):
    ids = []
    res = []
    for r in rows:
        if r['id'] not in ids:
            ids.append(r['id'])
            res.append(r.copy())
        else:
            i = ids.index(r['id'])
            res[i] = {**res[i], **r}
    return res

Optimized solution

def merge_duplicates_by_id(rows):
    merged = {}
    for r in rows:
        rid = r['id']
        merged[rid] = {**merged.get(rid, {}), **r}
    return list(merged.values())


⸻

33. Sort by multiple keys

Problem

Sort list of (name, score) by score desc, then name asc.

Input

items = [('banana',2),('apple',2),('cherry',1)]

Output

[('apple', 2), ('banana', 2), ('cherry', 1)]

Brute‑force solution

def sort_custom_bruteforce(items):
    return sorted(items, key=lambda x: (-x[1], x[0]))

Optimized solution

def sort_custom(items):
    return sorted(items, key=lambda x: (-x[1], x[0]))


⸻

34. Natural sort

Problem

Sort strings with embedded numbers in human order: a1 < a2 < a10.

Input

lst = ['a2','a10','a1']

Output

['a1','a2','a10']

Brute‑force solution

import re
def natural_sort_bruteforce(lst):
    def parse(s):
        parts = re.findall(r"\d+|\D+", s)
        out = []
        for p in parts:
            out.append(int(p) if p.isdigit() else p.lower())
        return out
    return sorted(lst, key=parse)

Optimized solution

import re
def natural_key(s):
    parts = re.findall(r"\d+|\D+", s)
    return [int(p) if p.isdigit() else p.lower() for p in parts]
def natural_sort(lst):
    return sorted(lst, key=natural_key)


⸻

35. Sort dicts (created_at then id)

Problem

Sort orders by created_at asc, then id asc (stable).

Input

orders = [
    {"id": 2, "created_at": "2025-08-09 10:00:00"},
    {"id": 1, "created_at": "2025-08-09 10:00:00"},
    {"id": 3, "created_at": "2025-08-08 09:00:00"},
]

Output

[{'id': 3, ...}, {'id': 1, ...}, {'id': 2, ...}]

Brute‑force solution

def sort_orders_bruteforce(orders):
    return sorted(orders, key=lambda o: (o['created_at'], o['id']))

Optimized solution

def sort_orders(orders):
    return sorted(orders, key=lambda o: (o['created_at'], o['id']))


⸻

36. Top-K frequent elements

Problem

Return the K most frequent elements in an array.

Input

arr = [1,1,1,2,2,3]; K=2

Output

[1, 2]

Brute‑force solution

def top_k_frequent_bruteforce(arr, k):
    freq = []
    for x in set(arr):
        freq.append((x, arr.count(x)))
    freq.sort(key=lambda x: x[1], reverse=True)
    return [x for x,_ in freq[:k]]

Optimized solution

from collections import Counter
def top_k_frequent(arr, k):
    return [x for x,_ in Counter(arr).most_common(k)]


⸻

37. Sum above threshold

Problem

Sum amounts for transactions strictly greater than threshold.

Input

txs = [{'amount':10},{'amount':200},{'amount':50}]; thr=40

Output

250

Brute‑force solution

def sum_above_threshold_bruteforce(txs, thr):
    s = 0
    for t in txs:
        if t['amount'] > thr:
            s += t['amount']
    return s

Optimized solution

def sum_above_threshold(txs, thr):
    return sum(t['amount'] for t in txs if t['amount'] > thr)


⸻

38. Sliding window maximum

Problem

Given array and window size K, return the maximum of each window.

Input

arr=[1,3,-1,-3,5,3,6,7]; K=3

Output

[3,3,5,5,6,7]

Brute‑force solution

def sliding_max_bruteforce(arr, k):
    if k <= 0 or k > len(arr): return []
    return [max(arr[i:i+k]) for i in range(len(arr)-k+1)]

Optimized solution

from collections import deque
def sliding_max(arr, k):
    if k <= 0 or k > len(arr): return []
    dq, out = deque(), []
    for i, x in enumerate(arr):
        while dq and dq[0] <= i-k: dq.popleft()
        while dq and arr[dq[-1]] <= x: dq.pop()
        dq.append(i)
        if i >= k-1:
            out.append(arr[dq[0]])
    return out


⸻

39. Rate limiter (N per 60s)

Problem

Given timestamps history for a user, decide if a new request at ‘now’ is allowed (<=N per 60s).

Input

history=[0,10,20,30,40]; now=50; N=5

Output

False  # already 5 in last 60s

Brute‑force solution

def can_allow_bruteforce(history, now_ts, N=5, window_s=60):
    cnt = sum(1 for t in history if now_ts - t < window_s)
    return cnt < N

Optimized solution

from collections import deque
def can_allow(history_deque, now_ts, N=5, window_s=60):
    while history_deque and now_ts - history_deque[0] >= window_s:
        history_deque.popleft()
    if len(history_deque) >= N: return False
    history_deque.append(now_ts)
    return True


⸻

40. Queue waiting time (FCFS)

Problem

Each customer has (arrival_time, service_time). Single server, return total waiting time.

Input

customers = [(0,3),(1,9),(2,6)]

Output

14

Brute‑force solution

def total_wait_time_bruteforce(customers):
    cur, total = 0, 0
    for arrive, service in sorted(customers):
        if cur < arrive: cur = arrive
        total += cur - arrive
        cur += service
    return total

Optimized solution

# Same as brute; this is already optimal O(n log n) due to sort.
def total_wait_time(customers):
    cur, total = 0, 0
    for arrive, service in sorted(customers):
        if cur < arrive: cur = arrive
        total += cur - arrive
        cur += service
    return total


⸻

41. Merge intervals

Problem

Merge overlapping intervals and return a simplified list.

Input

intervals = [(1,3),(2,6),(8,10),(15,18)]

Output

[(1, 6), (8, 10), (15, 18)]

Brute‑force solution

def merge_intervals_bruteforce(intervals):
    if not intervals: return []
    intervals = sorted(intervals)
    out = [intervals[0]]
    for s,e in intervals[1:]:
        ls, le = out[-1]
        if s <= le:
            out[-1] = (ls, max(le, e))
        else:
            out.append((s,e))
    return out

Optimized solution

def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort()
    out = [intervals[0]]
    for s,e in intervals[1:]:
        ls, le = out[-1]
        if s <= le:
            out[-1] = (ls, max(le, e))
        else:
            out.append((s,e))
    return out


⸻

42. Calendar free slots

Problem

Given two calendars of busy intervals and working hours, return free slots >= min_dur.

Input

cal1=[(540,600),(660,690)]  # 9:00-10:00, 11:00-11:30
cal2=[(570,630)]            # 9:30-10:30
work_start, work_end = 540, 1020  # 9:00-17:00
min_dur = 30

Output

[(600, 660), (690, 1020)]

Brute‑force solution

def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort()
    out = [intervals[0]]
    for s,e in intervals[1:]:
        ls, le = out[-1]
        if s <= le:
            out[-1] = (ls, max(le, e))
        else:
            out.append((s,e))
    return out

def free_slots_bruteforce(calendar1, calendar2, work_start, work_end, min_dur):
    busy = sorted(calendar1 + calendar2)
    busy = merge_intervals(busy)
    clamped = []
    for s,e in busy:
        s = max(s, work_start); e = min(e, work_end)
        if s < e: clamped.append((s,e))
    clamped = merge_intervals(clamped)
    free = []
    cur = work_start
    for s,e in clamped:
        if cur < s and s - cur >= min_dur:
            free.append((cur, s))
        cur = max(cur, e)
    if cur < work_end and work_end - cur >= min_dur:
        free.append((cur, work_end))
    return free

# Optimized solution

# Same complexity; logic kept clear and minimal.
def free_slots(calendar1, calendar2, work_start, work_end, min_dur):
    busy = merge_intervals(sorted(calendar1 + calendar2))
    clamped = []
    for s,e in busy:
        s = max(s, work_start); e = min(e, work_end)
        if s < e: clamped.append((s,e))
    clamped = merge_intervals(clamped)
    free, cur = [], work_start
    for s,e in clamped:
        if cur < s and s - cur >= min_dur:
            free.append((cur, s))
        cur = max(cur, e)
    if cur < work_end and work_end - cur >= min_dur:
        free.append((cur, work_end))
    return free

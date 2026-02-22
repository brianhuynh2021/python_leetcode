
import queue
import time
import threading

# Simulate connection pool with 3 connections
pool = queue.Queue(maxsize=3)

# Pre-create connections
for i in range(3):
    pool.put(f"Connection-{i+1}")

def handle_request(user_id):
    print(f"User {user_id} waiting for connection...")
    conn = pool.get()
    print(f"User {user_id} using {conn}")
    time.sleep(2)
    print(f"User {user_id} releasing {conn}")
    pool.put(conn)

threads = []
for i in range(5):  # 5 users
    t = threading.Thread(target=handle_request, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All users processed.")

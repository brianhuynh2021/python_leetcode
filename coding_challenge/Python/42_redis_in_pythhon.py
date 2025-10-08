import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Set a value
r.set("name", "Brian")

# Get the value
print(r.get("name"))  # Output: b'Brian'

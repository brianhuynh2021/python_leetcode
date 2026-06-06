import time


def cpu_work():
    start = time.perf_counter()
    total = 0
    for i in range(10_000_000):
        total += i
        
    print("CPU:", (time.perf_counter() - start)*1000, "ms")
    
cpu_work()
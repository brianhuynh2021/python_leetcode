
# Complexity of this is O(n^3)
def min_cost_bruteforce_loops_trace(ropes):
    n = len(ropes)
    if n <= 1:
        return 0
    
    best = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            merged = ropes[i] + ropes[j]
            copy = []
            for k in range(n):
                if k != i and k != j:
                    copy.append(ropes[k])
            copy.append(merged) # push back merge into the list
            
            total = merged + min_cost_bruteforce_loops_trace(copy)
            best = min(best, total)
    return best

# Using heap data structure to optimize it
import heapq
def min_cost_connect_ropes_optimize(ropes: list[int]) -> list[int]:
    n = len(ropes)
    if n <= 1:
        return []
    
    heapq.heapify(ropes)
    while len(ropes) > 1:
        a = heapq.heappop(ropes) # take out 2 smallest of ropes
        b = heapq.heappop(ropes)
        
        total = a + b
        # push back to the heap
        heapq.heappush(ropes, total)
    return ropes

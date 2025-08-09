def asteroid_collision(asteroids: list[int]) -> list[int]:
    if not asteroids:
        raise ValueError("Asteroids must not be emtpy")
    
    pos = []
    out = []
    for a in asteroids:
        if a > 0:
            pos.append(a)
            continue
        
        # if a < 0 and hit with pos if it has
        alive = True
        while pos and pos[-1] < -a:
            pos.pop()
            
        if pos and pos[-1] == -a:
            pos.pop()
            alive = False
            
        elif pos and pos[-1] > -a:
            alive = False
            
        if alive and not pos:
            out.append(a)
    return pos + out
        
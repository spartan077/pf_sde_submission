def chakrvyu_game(p, enemies, skips, recharges):
    n = len(enemies)
    stack = [(enemies[i], i) for i in range(n)]
    stack.sort(reverse=True)
    
    skip_pos = set()
    for i in range(min(skips, n)):
        skip_pos.add(stack[i][1])
    
    curr_power = p
    recharges_left = recharges
    max_reach = 0

    for i in range(n):
        if i > max_reach:
            return False
            
        if i in skip_pos:
            max_reach = i + 1
            continue

        
        if i == 3:
            extra = enemies[2] // 2
            if curr_power < extra:
                if recharges_left <= 0:
                    return False
                curr_power = p
                recharges_left -= 1
            curr_power -= extra

        
        if i == 7:
            extra = enemies[6] // 2
            if curr_power < extra:
                if recharges_left <= 0:
                    return False
                curr_power = p
                recharges_left -= 1
            curr_power -= extra

        if curr_power >= enemies[i]:
            curr_power -= enemies[i]
        else:
            if recharges_left <= 0:
                return False
            curr_power = p - enemies[i]
            recharges_left -= 1

        max_reach = max(max_reach, i + 1)

    return True

result1 = chakrvyu_game(110,[2,3,8,10,7,12,14,20],2,2)
print(result1) 
res2=chakrvyu_game(33,[20,30,50,70,80],1,1) 
print(res2)
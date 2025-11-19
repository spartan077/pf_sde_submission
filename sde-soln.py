def chakrvyu_game(p, enemies, skips, recharges):
    #dictt={}
    #for i,v in enumerate(enemies):
    ##    dictt[v]=i
    ##enemy_skipped=sorted(enemies,reverse=True)[:skips]
    #skip_pos=set()
    #for skip_power in enemy_skipped:
    #    for i in range(len(enemies)):
    #        if enemies[i] == skip_power and i not in skip_pos:
    #            skip_pos.add(i)
    stack = []
    to_skip = skips
    
    
    for i, power in enumerate(enemies):
        stack.append((power, i))
    
    
    stack.sort(reverse=True)
    skip_pos = set()
    for j in range(min(to_skip, len(stack))):
        skip_pos.add(stack[j][1])
    curr_power=p
    skips_used=0
    recharges_curr=recharges
    for i in range(len(enemies)):
        enemy_power = enemies[i]
        
        
        if i in skip_pos and skips_used < skips:
            skips_used += 1
            continue
        
        
        
        if i == 3:  
            regen_power = enemies[2] // 2
            if curr_power < regen_power:
                if recharges_curr > 0:
                    curr_power = p
                    recharges_curr -= 1
                else:
                    return False
            curr_power -= regen_power
        
         
        if i == 7:  
            regen_power = enemies[6] // 2
            if curr_power < regen_power:
                if recharges_curr > 0:
                    curr_power = p
                    recharges_curr -= 1
                else:
                    return False
            curr_power -= regen_power

        if curr_power >= enemy_power:
            curr_power -= enemy_power
        else:

            if recharges_curr > 0:
                curr_power = p - enemy_power
                recharges_curr -= 1
            else:
                return False
    
    return True
result1 = chakrvyu_game(110,[2,3,8,10,7,12,14,20],2,2)
print(result1) 
res2=chakrvyu_game(33,[20,30,50,70,80],1,1) 
print(res2)
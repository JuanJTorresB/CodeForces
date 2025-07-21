n, k = map(int, input().split())

contestants = (str(input()).split(" "))

minimun_score = int(contestants[k - 1])

if len(contestants) == int(n):
    
    extra = 0
    
    if minimun_score > 0:
        
        for i in range(k, n):
            contestant = int(contestants[i])
            if contestant >= minimun_score:
                extra += 1
            else:
                break
        advanced_contestants = k + extra
    
    else:
        
        for i in range(k - 1, -1, -1):
            contestant = int(contestants[i])
            if contestant >= minimun_score and contestant > 0:
                extra += 1
            
        advanced_contestants = extra
    
else:
    advanced_contestants = "N Contestans Do Not Match"


print(advanced_contestants)
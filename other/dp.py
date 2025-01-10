def climbStairs(n: int) -> int:
    dps = [0] * (n + 1)
    dps[0] = 1
    dps[1] = 1


    for i in range(2, n + 1):
        dps[i] = dps[i-1] + dps[i-2]
    

    return dps[n]

def numDecodings(s: str) -> str:
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    previous, current = 1,1

    for i in range(1,n):
        temp = 0

        if s[i] != '0':
            temp += current
        
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            temp += previous
        
        previous, current = current, temp

        if current == 0:
            return 0
    
    return current

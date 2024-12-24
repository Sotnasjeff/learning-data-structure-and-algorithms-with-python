def reverseWords(s: str) -> str:
    res = ''
    l, r = 0,0

    while r < len(s):
        if s[r] != ' ':
            r += 1
        else:
            res += s[l:r+1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]

def invertWords(s: str) -> str:
    left, right = 0,len(s) - 1
    convert_to_list = list(s)

    while left < right:
        convert_to_list[left], convert_to_list[right] = convert_to_list[right], convert_to_list[left]
        right-=1
        left+=1
    
    return ''.join(convert_to_list)

print(invertWords("jessica"))
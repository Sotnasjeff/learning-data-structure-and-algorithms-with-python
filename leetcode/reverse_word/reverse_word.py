def reverseWords(s: str) -> str:
    s = s.split()
    left, right = 0, len(s) - 1
    
    while right > left:
        s[left], s[right] = s[right], s[left]
        right -= 1
        left += 1
    
    return " ".join(s)

print(reverseWords("the sky is blue"))
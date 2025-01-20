def gcd(len1:int, len2:int) -> int:
    while len2:
        len1, len2 = len2, len1 % len2
    return len1

def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    return str1[:gcd(len(str1), len(str2))]

print(gcdOfStrings("ABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "ABAB"))
print(gcdOfStrings("LEET", "CODE"))
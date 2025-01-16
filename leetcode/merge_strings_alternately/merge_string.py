def mergeAlternately(word1: str, word2: str) -> str:
    p1 = 0
    p2 = 0
    word_merged = []
    
    while p1 < len(word1) and p2 < len(word2) :
        word_merged.append(word1[p1])
        word_merged.append(word2[p2])
        p1 += 1
        p2 += 1
    
    if p2 < len(word2):
        word_merged.append(word2[p2:])
        
    if p1 < len(word1):
        word_merged.append(word1[p1:])
    
    return "".join(word_merged)


print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq"))
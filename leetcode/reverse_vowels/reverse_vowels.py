def reverseVowels(s: str) -> str:
    left, right = 0, len(s) - 1
    vowels_changed = list(s)
    hasher = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True, 
    'A': True, 'E': True, 'I': True, 'O': True, 'U': True}
    while left < right:
        if vowels_changed[left] in hasher:
            while right > left:
                if vowels_changed[right] in hasher:
                    vowels_changed[left], vowels_changed[right] = vowels_changed[right], vowels_changed[left]
                    right -= 1
                    left += 1
                    break
                right -= 1
        else:
            left += 1

    return "".join(vowels_changed)


print(reverseVowels("IceCreAm"))
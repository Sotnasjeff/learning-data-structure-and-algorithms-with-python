def reverseWords(sentence: str) -> str:
    response = ''
    left, right = 0,0

    while right < len(sentence):
        if sentence[right] != ' ':
            right += 1
        else:
            response += sentence[left:right+1][::-1]
            right += 1
            left = right
    response += ' '
    response += sentence[left:right + 2][::-1]
    return response[1:]

def invertWords(s: str) -> str:
    left, right = 0,len(s) - 1
    convert_to_list = list(s)

    while left < right:
        convert_to_list[left], convert_to_list[right] = convert_to_list[right], convert_to_list[left]
        right-=1
        left+=1
    
    return ''.join(convert_to_list)

print(invertWords("jefferson"))
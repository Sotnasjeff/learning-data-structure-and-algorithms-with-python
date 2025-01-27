from typing import List

phone_keyboard = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y","z"]
}

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    pointer = 0
    res = []
    
    def backtracking(permutation: str, pointer: int):
        if pointer == len(digits):
            res.append(permutation)
            return 
        
        for letter in phone_keyboard[digits[pointer]]:
            backtracking(permutation+letter, pointer+1)
                    
    backtracking("", pointer)
    return res
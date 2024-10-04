def min_window_substring(s, t):
    char_count = {}
    for char in t:
        # print(f'char: {char}')
        char_count[char] = char_count.get(char, 0) + 1
        # print(f'char_count[char]: {char_count[char]} ')
    
    required = len(char_count)
    formed = 0
    start = 0
    end = 0
    min_length = float('inf')
    window_size = float('inf')
    
    while end < len(s):
        char = s[end]
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                formed += 1
                
        while start <= end and formed == required:
            char = s[start]
            if char in char_count:
                if char_count[char] == 0:
                    formed -= 1
                char_count[char] += 1
            if end - start + 1 < window_size:
                window_size = end - start + 1
                min_window = s[start:end+1]
                
            start += 1
            
        end += 1
        
    return min_window if window_size != float('inf') else ''

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window_substring(s, t)
    print(result)  # Output: "BANC"
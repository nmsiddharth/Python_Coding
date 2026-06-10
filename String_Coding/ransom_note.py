# Can the string "aa" be constructed from the characters in the string "aab"

from collections import Counter

note_input = "aa"
mag_input = "aab"

def check(note_input, mag_input):
    mag_count = Counter(mag_input)
    note_count = Counter(note_input)
    
    for char, count in mag_count.items():
        if note_count[char] < count:
            return False
    return True

print(check(mag_input,note_input))
    
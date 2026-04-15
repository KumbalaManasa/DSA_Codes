#brute force
def rev_words(s):
    word = ""
    words = []
    for ch in s:
        if ch!=" ":
            word+=ch
        # If space and we have collected a word    
        elif word:
            words.append(word)
            word = ""
    # Add the last word if present ********remember this point its imp******
    if word:
        words.append(word) 
    words.reverse()
    return " ".join(words)
s = "hello im kumbala manasa"
print(rev_words(s))  
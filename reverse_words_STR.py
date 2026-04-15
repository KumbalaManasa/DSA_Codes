#optimal Approach 
def reverse_words(s):
    result = ""
    i = len(s)-1
    while i>=0:
        while i>=0 and s[i]==" ":
            i-=1
        if i<0:
            break
        end = i
        while i>=0 and s[i]!=" ":
            i-=1
        word = s[i+1:end+1]
        if result!="":
            result+=" "
        result+=word
    return result    
s = " amazing coding skills "
print(reverse_words(s))


'''#brute force
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
print(rev_words(s))  '''

#brute force
#We only add parentheses to the result when we are NOT at the outermost level.
#As long as level > 0, we are insideAny ( or ) here → ✅ include
#TC = O(N) SC = O(1)
def rem_outer_parenthesis(s):
    result = ""
    level = 0
    for chr in s:
        if chr == "(":
            if level>0:
                result+=chr
            level+=1
        elif chr == ")":
            level-=1
            if level>0:
                result+=chr
    return result
s = "(()())(())"
print(rem_outer_parenthesis(s))                    

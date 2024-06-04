str2 = '50'
def my_lower(str2):
    ans = ''
    for i in range(len(str2)):
        ch= str2[i]
        if ch.isupper():
            ans = ans + ch.lower()
        else:
            ans += ch
    return ans
print (my_lower(str2))


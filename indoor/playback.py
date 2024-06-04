str = 'This is CS50'

def my_playspeed(str):
    ans = ''
    for i in range(len(str)):
        ch = str[i]
        if ord(ch) == 32:
            ans += "..."
        else:
            ans += ch
    return ans

print(my_playspeed(str))
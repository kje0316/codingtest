S = input()
import string
al = list(string.ascii_lowercase)
for i in al:
    if i in S:    
        print(S.index(i), end=" ")
    else:
        print(-1, end=" ")
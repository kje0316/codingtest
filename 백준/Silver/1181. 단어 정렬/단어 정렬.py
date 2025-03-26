N = int(input())
text = [input() for _ in range(N)]
dic = {t:len(t) for t in text} #입력받은 순서대로 . {but:3, i:1}
sort_dict = dict(sorted(dic.items(), key=lambda x: (x[1],x[0])))
for i in sort_dict:
    print(i)

def DocFile(n):
    a = []
    count = 0
    file = open('login/fileclone.txt', 'r', encoding='utf-8')
    for i in file:
        count = count + 1
        a.append(i.strip('\n'))
        if count == n:
            break
    file.close()
    return a

# n=int(input())
# x = DocFile(n)
# print(x)
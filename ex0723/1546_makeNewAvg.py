n = int(input())
li = list(map(int, input().split()))
# newli = []
# for i in range(n) :
#     newli.append(li[i]/max(li)*100)
# newAvg = sum(newli)/len(newli)
# print(newAvg)
print(sum(li)/max(li)/len(li)*100)
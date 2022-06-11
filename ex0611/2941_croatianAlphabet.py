import sys

croList = ['c=','s=','z=','dz=','c-','d-','lj','nj']

word = sys.stdin.readline().rstrip()
for c in croList :
    word = word.replace(c, '0')

print(len(word))


# word = input()
# alphabetList = list(word)
# temp = len(alphabetList)
# for i in range(len(alphabetList)) :
#     # =가 있는지 확인한다.
#     if alphabetList[i] == '=' :
#         temp = temp -1
#         # z=가 있다면 앞글자가 d인지 확인한다.
#         if alphabetList[i-1] == 'z' and (i-1)>0 :
#             if alphabetList[i-2] == 'd' :
#                 temp = temp -1
#     # j가 있는지 확인한다. 앞글자가 l,n인지 확인한다.
#     elif alphabetList[i] == 'j' and (i) > 0 :
#         l = ['l','n']
#         if alphabetList[i-1] in l :
#             temp = temp -1
#     elif alphabetList[i] == '-':
#         temp = temp -1
# print(temp)



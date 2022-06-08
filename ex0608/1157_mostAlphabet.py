import operator

# 알파벳 대소문자로 된 단어가 주어지면,이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

word = input().strip()
word = word.upper()

count = {} #딕셔너리 사용
list1 = list(word)
#print(type(count)) #<class 'dict'>
for i in list1 : #알파벳을 하나씩 꺼낸다
    try: count[i] += 1 #이미 존재하면 +1
    except: count[i] = 1 #없으면 1
#print(type(count)) #<class 'dict'>

# key=operator.itemgetter(1) 는 두번째 인자값을 기준으로 정렬한다
count = sorted(count.items(), key=operator.itemgetter(1), reverse=True) #딕셔너리 정렬은 sorted(). sorted()하면 list타입이 된다.

#print(type(count)) #<class 'list'>
#print(count)
#print(count[0])
if len(count) > 1 and count[0][1] == count[1][1] :
    print('?')
else :
    print(count[0][0])


# import operator

# word = input().strip()
# word = word.upper()

# count = {}
# list1 = list(word)

# #출현빈도 저장
# for i in list1 :
#     try: count[i] += 1
#     except: count[i] = 1
        
# #정렬
# count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)

# if len(count) > 1 and count[0][1] == count[1][1] :
#     print('?')
# else :
#     print(count[0][0])
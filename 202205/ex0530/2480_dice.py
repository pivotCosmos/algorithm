#같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
#모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

num1,num2,num3 = map(int,input().split())
if num1==num2 and num2==num3 : #3개 다 같다
    print(10000 + num1*1000)
elif num1==num2: #2개만 같다
    print(1000 + num1*100)
elif num2==num3: #2개만 같다
    print(1000 + num2*100)
elif num3==num1: #2개만 같다
    print(1000 + num3*100)
else : #같은 눈이 없다
    number = [num1, num2, num3]
    print(max(number)*100)


# num_list = list(map(int, input().split()))
# temp=0 #몇 개가 같은지
# i=0 #뭐랑 뭐가 같은지

# if num_list[0]==num_list[1] :
#     temp = temp +1
#     i =0
# if num_list[1]==num_list[2] :
#     temp = temp +1
#     i =1
# if num_list[2]==num_list[0] :
#     temp = temp +1
#     i =2

# if temp==0 :
#     print(max(num_list)*100)
# elif temp==1 :
#     print(1000 + num_list[i]*100)
# else :
#     print(10000 + num_list[0]*1000)





N = int(input())
radius_list = list(map(int, input().split()))

first_radius = radius_list[0]
left_radius = radius_list
left_radius.remove(first_radius)

def get_gcd(num1,num2) :
    while num2 != 0 :
        temp = num1
        num1 = num2
        num2 = temp%num1
    return num1

def get_simple_fraction(bunmo, bunja):
    gcd = get_gcd(bunmo, bunja)
    result = str(bunmo//gcd) + '/' + str(bunja//gcd)
    return result

for radius in left_radius :
    result = get_simple_fraction(first_radius, radius)
    print(result)
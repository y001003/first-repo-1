# 과제: 1부터 10까지 반복하는 과정에서  3의배수일 경우, year를 출력하시오.
# 나머지 모든 경우는 숫자 그대로 출력


for i in range(1, 20):
    if i%15 ==0:
        print('yeardream')
    elif i%3==0 :
        print('year')
    elif i%5 == 0:
        print('dream')
    else :
        print(i)

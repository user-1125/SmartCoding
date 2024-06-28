import random

random_number = random.randint(1, 100)

count = 1

while True: 
    try :

        MyNum = int(input("1부터 100 사이의 숫자를 입력하세요 >"))
        
        if MyNum > random_number :
            print("더 작은 수로 다시 시도해보세요")
            print()

        elif MyNum < random_number :
            print("더 큰 수로 다시 시도해보세요")
            print()

        elif MyNum == random_number :
            print(f"정답입니다.{count}번 만에 맞추셨군요")
            print()
            break

        count = count + 1 

    except:
    print ("숫자로 입력하세요")

#ทบทวนก่อนสอบ
#import math
#n = int(input())
#i = 0
#minsumm = math.inf

#while i < n:
    #i += 1
    #summ = i + (n // i)
    
    #if n % i == 0 and summ < minsumm:
        #minsumm = summ
#print(minsumm)

#x = int(input())
#i = 0
#if x >=0 and x <= 4000000000:
    #while x>0:
        #y = x % 10
        #x = x // 10
        #if y % 2 == 1:
            #i += y
    #if i > 0:
        #print(i)
    #else:
        #print(-1)
        i = 0
        
while True:
    dice1 = int(input())
    dice2 = int(input())

    if dice1 < 1 or dice1 > 6 or dice2 < 1 or dice2 > 6:
        print("ERROR")
    else:
        i += 1
        
        if dice1 + dice2 == 7 or dice1 + dice2 == 11:
            print(i, dice1 + dice2, "W")
            break
        elif dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
            print(i, dice1 + dice2, "L")
            break
        else:
            target = dice1 + dice2
        
            while True:
                dice1 = int(input())
                dice2 = int(input())
                
                if dice1 < 1 or dice1 > 6 or dice2 < 1 or dice2 > 6:
                    print("ERROR")
                else:
                    i += 1
                    
                    if dice1 + dice2 == 7:
                        print(i, dice1 + dice2, "L")
                        break
                    if dice1 + dice2 == target:
                        print(i, dice1 + dice2, "W")
                        break
            break
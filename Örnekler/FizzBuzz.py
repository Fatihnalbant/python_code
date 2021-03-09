numara1 = int(input("Baslangic sayisi: "))
numara2 = int(input("bitis sayisi: "))
for numara1 in range(numara1,numara2) :
    if numara1 % 3 == 0 :
        if numara1 % 5 == 0 : 
            print("FizzBuzz")
        else :
            print("Fizz")
    elif numara1 % 5== 0 :
        print("Buzz")
    else : 
        print(numara1)

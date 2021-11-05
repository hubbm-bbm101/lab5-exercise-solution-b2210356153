a = int(input("please enter a number ")) 
b = 0
c= 0
d=0
for i in range(1,a+1) :
    if i%2 == 0 :
        b += i
        d+=1
    else :
        c+=i
        
print("the average of the even numbers : " , b/d)
print("the sum of the odd numbers : " , c)
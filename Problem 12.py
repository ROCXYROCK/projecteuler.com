#Problem 12
#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#Let us list the factors of the first seven triangle numbers:
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?
a=0
b=0
x=0
i=0
    
while x < 502:
    x=0
    a += 1
    b += a
    #print(a, b)
    if b%2 == 0:
        j = b/2
    if b%2 == 1:
        j = (b+1)/2
        
    for i in range(1,int(j)):
        if b%i==0:
            x +=1
    print(b, i, x)  

#the answer is: 76576500, verified by projecteuler.net

    
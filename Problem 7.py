#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

y=2     # y should start with 2 because the i start my for loop with 2, then is the pime number 2 out of the operation
i=2

while y<10001:
    a=False

    for j in range(2,i-1):
        if i%j!=0: 
           a=True
        elif i%j==0:
            a=False 
            break 

    if a==True:
        y+=1

    if y<10001:
        i=i+1    

print(y,"th prime number is", i)


#the answer is: 104743, verified by projecteuler.net
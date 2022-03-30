#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
x=4
y=False
add=0
while x < 2000001:

    if x%2==0:
        n=int(x/2)
    elif x%2!=0:
        n=int((x+1)/2)

    for i in range(2,int(n)):
        if x%i==0:
            y=False
            break
        elif x%i!=0:
            y=True
    
    if y == True:
        add += x

    x += 1

print(add+2+3)

#the answer is: 142913828922, verified by projecteuler.net
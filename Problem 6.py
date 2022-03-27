#Problem 6
#The sum of the squares of the first ten natural numbers is, 1²+2²+...+10¹=385
#The square of the sum of the first ten natural numbers is, (1+2+...+10)²=55²=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#3025-385=2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
x=0
y=0

for i in range (1,101):
    x=x+(i*i)
    y=y+i

y=y*y
print(y-x) 

#the answer is: 25164150, verified by projecteuler.net
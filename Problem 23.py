#Problem 23
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

abundant_numbs = []
non_2abundant_sum =[]
abundant_sum = 0
for i in range(2,int(28124)):
    sum_j = 0
    x = i/2
    
    if i%2 != 0:
        x = (i+1)/2

    for j in range(1,int(x)+1):
        if i%j == 0:
            sum_j += j
    
    if sum_j > i:
        abundant_numbs.append(i)

#print(abundant_numbs)
for i in range (0,28124):
    non_2abundant_sum.append(i)

for i in abundant_numbs:
        
    for j in abundant_numbs:
        k = i+j
        if k in non_2abundant_sum:
            non_2abundant_sum.remove(k)

for i in non_2abundant_sum:
    abundant_sum += i

print(abundant_sum)
    

#the anwser is: 31475770, verified by projecteuler.net
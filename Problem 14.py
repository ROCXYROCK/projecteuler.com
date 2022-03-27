#Problem 14
#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?

b=0
y=0

for i in range (1,1000000):
    
    x=i
    a=0
    
    while x != 1:
        
        if x % 2 == 0:
            x = x/2
            a += 1
        else:
            x = 3*x+1
            a +=1

        if a > b:
            b = a
            y = i
    
print("start num:",y, "times", b)

#the answer is: 837799, verified by projecteuler.net
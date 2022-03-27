#Problem 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
c=[]
x = 0
s = 0
for i in range (2,10000):
    if i in c:
        continue
    a = []
    b = []
    y = 1
    z = 1
   
    if i%2==0:
        x=i/2
   
    elif i%2!=0:
        x = (i+1)/2
    
    for j in range (2,int(x+1)):
        if i%j ==0:
            a.append(j)
            y = y + j
            
    if y%2==0:
        x = y/2
    elif y%2!=0:
        x= (y+1)/2
    
    for j in range(2,int(x+1)):
        if y%j == 0:
            b.append(j)
            z = z + j
    
    if  i==z and y!=z:        
        c.append(i)
        c.append(y)

print(c)
for i in c:
    s = s + i
print (s)

#the answer is: 31626, verified by projecteuler.net
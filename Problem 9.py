#Problem 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a² + b² = c²
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import random
x=False

while x!=True:
    a = int(random.uniform(1,500))
    b = int(random.uniform(1,500))
    c = pow(a*a+b*b,0.5)
    if b < a:
        continue
    
    if a < b < c and a+b+c==1000 and c==pow(a*a+b*b,0.5):
        print("a =",a,", b =",b,", c =",c,", a+b+c =",a+b+c,", a*b*c =",a*b*c)
        x=True


#the answer is: 31875000, verified by projecteuler.net

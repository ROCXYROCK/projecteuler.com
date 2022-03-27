#Problem 20
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

n = 100
p = 1 #product
string = "" #string to get the product digits in
s = 0 #sum of all product digits

for i in range(1,n+1):
    p = p * i

string = str(p)
for i in range(0,len(string)):
    s = s + int(string[i])

print(s)

#the answer is: 648, verified by projecteuler.net
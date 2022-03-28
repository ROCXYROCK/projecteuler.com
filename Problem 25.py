#Problem 25
#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

x = [1,1]

digits_count = 0

i= 2
while digits_count < 1000:
   y = x[i-1] + x[i-2]
   x.append(y)
   digits_count = len(str(x[i]))
   i += 1

print(i, digits_count)

#the answer is: 4782, verified by projecteuler.net
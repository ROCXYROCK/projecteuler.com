#Problem 16
#2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2¹⁰⁰⁰?

x = 2**1000
y = "{}".format(x)
z = 0
for i in range (0, len(y)):
    z = z + int(y[i])    

print (z)


#the asnwer is: 1366, verified by projecteuler.net
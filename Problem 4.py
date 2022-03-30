#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

numb_sum = ""
x = 0
y = 0
End = 0

for i in range(100,1000):

    for j in range (100,1000):
        numb_sum = str(i*j)

        
        for k in range(0,len(numb_sum)):
            if numb_sum[k] == numb_sum[-k-1]:
                y = True
            else: 
                y = False
                break
        if y == True:

            if int(numb_sum) > int(End):
                End = int(numb_sum)
        
print(End)

#the answer is: 906609, verified by pojecteuler.net
#Problem 3 (projecteuler.net)
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

numb = 600851475143
factor_list = [1]
x = 0
y = False


for i in range(int((numb+1)/2),1,-1):
    
    if numb % i== 0:
        x = i/2
        if i%2!=0:
            x = (i+1)/2
        for j in range(2,int(x)):
            if i%j == 0:
                y = False
                break
            else:
                y = True
        if y == True:
            factor_list.append(i)
            break

print(factor_list[-1])

#the answer is: 6857, verified by projecteuler.net
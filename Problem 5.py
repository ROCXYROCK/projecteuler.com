#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for i in range(1,100000000000):

    for j in range(1,21):
        if i%j !=0:
            x=False
            break
        if i%j ==0:
            x=True

    if x == True:
        print(i)
        break 


#the answer is: 232792560, verified by projecteuler.net
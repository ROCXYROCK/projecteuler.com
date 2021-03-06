#Problem 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

numb_list = [1,2]
sum_even = 2
num = 0

for i in range(2,1000):
    
    num = numb_list[i-1] + numb_list[i-2]
    numb_list.append(num)
    if num%2 == 0 and num < 4000000:
        sum_even += num
    
print(sum_even)

#the answer is: 4613732, verified by projecteuler.net

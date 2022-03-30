#Problem 19
#You are given the following information, but you may prefer to do some research for yourself.
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
a = 0
b = 0
x=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(0,101):
    
    for j in range(0,12):
    
        x[1]=28
        if (year%4 == 0 and year%100 != 0) or (year%4 ==0 and year%100==0 and year%400==0):
            x[1]=29
        
        a += x[j] #count how many days to currently month
               
        if (a)%7 ==0: #if the moth starts with sunday; so i added the one to look at the next month
            b += 1 #how many months start with sunday
    
    year += 1  #next year   

print(f"in the 20th centry there are {b-2} years start with sunday")# the -2 is because 1900 have 2 months, which starts with sunday

#the Answer is: 171, verified by projecteuler.net
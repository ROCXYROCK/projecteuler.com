#Problem 17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 

one15=["one", "two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","forteen","fifteen"]
tens=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
teen="teen"
hundred="hundred"
thousand="thousand"
numbs=0
a=0

for x in range(0,10):
    
    if a == 1:
        numbs = numbs + len(one15[x-1]) + len(hundred)

    for i in one15:
        numbs = numbs + len(i) # for 1 to 15
        if a == 1:
            numbs = numbs + len(one15[x-1]) + len(hundred) + 3
        
    for i in range(0,4):
        numbs = numbs + len(one15[6+i]) + len(teen) # for 16 to 19
        if a == 1:
            numbs = numbs + len(one15[x-1]) + len(hundred) + 3 # for onehundred and sixteen

    for i in range(2,9):
        numbs = numbs + len(tens[i]) # for the 20 , 30, 40 and 50 etc. 
        if a == 1:
            numbs = numbs + len(one15[x-1]) + len(hundred) # for 20 etc with one hundred or twohundred
        for j in range(0,9):
            numbs = numbs + len(tens[i]) + len(one15[j])
            if a == 1:
                numbs = numbs + len(one15[x-1]) + len(hundred) + 3 # for every number when it comes 1 to 9 with hundred it needs it with and

    if a == 1:
        numbs= numbs - 3 # for the one hundred (and) ten, because it will be counted at first and here i take it out
    a = 1


numbs = numbs +len("onethousand")
print(numbs)

       
# answer is: 18688 , rejected by projecteuler.net  
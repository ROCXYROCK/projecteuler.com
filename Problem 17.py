#Problem 17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 

one15=["one", "two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
teen="teen"
hundred="hundred"
thousand="thousand"
and_word="and"
numbs=0

for i in one15: # for 1 to 19 
    numbs += len(i)


for i in range (1,9): # for 21 to 99
    numbs += len(tens[i]) # for 20 to 90 (tens)
    
    for j in range(0,9):
        numbs += len(one15[j]) + len(tens[i]) #for 21 to 99(without tens)

##########for hundreds #################
for i in range(0,9):
    numbs += len(one15[i]) + len(hundred) # for 100 to 900 (hundreds)
    
    for j in one15: # for 1 to 19 with hundreds
        numbs += len(j) + len(one15[i]) + len(hundred) + len(and_word)

    for j in range (1,9): # for 21 to 99
        numbs += len(tens[j]) + len(one15[i]) + len(hundred) + len(and_word) # for 20 to 90 (tens)

        for k in range(0,9):
            numbs += len(one15[k]) + len(tens[j]) + len(one15[i]) + len(hundred) + len(and_word) #for 21 to 99(without tens)
           

print(numbs+len("onethousand"))

#the answer is: 21124, verified by projecteuler.net
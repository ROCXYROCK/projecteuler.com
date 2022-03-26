#Problem 15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

x = 2
y = 0
for i in range(1,21):
   y = y + (x**i)
   print(y) 

#   answer is: 2097150
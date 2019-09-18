# Number to input into collatz 
n = 20

#keep looping until it reaches 1
while n !=1:
    #print current value of n
    print(n)
    #check if the number is even
    if n % 2 == 0:
        # if n is even
        n = n / 2
    else:
        # If n is odd
        n = (3 * n) + 1
# Print 1
print(n)
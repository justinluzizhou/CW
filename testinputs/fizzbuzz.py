# Write a program that prints the numbers from 1 to 100 each on it's own line.
# But for multiples of three print "Fizz" instead of the number and for the
# multiples of five print Buzz".
#
# For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    s = str(x)
    if x%15==0:
        s = "FizzBuzz"
    elif x%3==0:
        s="Fizz"
    elif x%5==0:
        s="Buzz"
    print(s)
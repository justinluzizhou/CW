def average_rainfall(input_list):
    # Here is where your code should go
    i = 0
    sum = 0
    count = 0
    while (input_list[i]!= -999):
        if input_list[i] >=0:
            sum += input_list[i]
            count += 1
            i += 1

    return sum/count

    #return "Your computed average as a integer" #<-- change this!

# Don't touch anything below this line.
if __name__ == "__main__":
    import sys

    # We get the arguments assuming that they are a list of *integers*
    # We parse the input to get the right type.
    # There's no error checking!
    rainfall_measurements = list(map(int, sys.argv[1:]))

    # We print the average.
    print(average_rainfall(rainfall_measurements))
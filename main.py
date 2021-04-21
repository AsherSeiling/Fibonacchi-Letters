# Number
num = 0

numbers = []
# Function that creates all the fibonachi numbers
def fib_create(run_times):
    num = 1
    num2 = 1
    for i in range(run_times):
        buffernum = num
        num = num + num2
        num2 = buffernum
        numbers.append(num2)



# Run
fib_create(100)
print(numbers)

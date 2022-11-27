def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

print(factorial(5))


def sum_all_numbers(x):
    if x<= 1:
        return x
    else:
        return x + sum_all_numbers(x-1)

print(sum_all_numbers(5))

def _sum_all_array_numbers(arr,n):
    if n <= 0:
        return 0
    else:
        return _sum_all_array_numbers(arr, n - 1) + arr[n - 1]
#5 + 4 + 3 + 2 + 1

arr = [1,2,3,4,5]

print(_sum_all_array_numbers(arr,len(arr))) 

def product_of_array_numbers(arr,n):
    if n <= 0:
        return 1
    else:
        return product_of_array_numbers(arr,n - 1) * arr[n - 1]

print(product_of_array_numbers(arr,len(arr)))

def find_average_of_array(arr):
    return _sum_all_array_numbers(arr,len(arr)) / len(arr)

print(find_average_of_array(arr))


# Below is the implementation of the above approach
def printSubsequence(input, output):
 
    # Base Case
    # if the input is empty print the output string
    if len(input) == 0:
        print(output, end=' ')
        return
 
    # output is passed with including the
    # 1st character of input string
    printSubsequence(input[1:], output+input[0])
 
    # output is passed without including the
    # 1st character of input string
    printSubsequence(input[1:], output)
 
 
# Driver code
# output is set to null before passing in
# as a parameter
output = ""
input = "abcd"
 
printSubsequence(input, output)

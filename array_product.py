import numpy

numbers = [4,6,7,3,6,9]

output_division = []
output_no_division = []


# Outputs an array with the product of all elements of 
# the input array except for the current element
def productExceptSelf(nums):
    length = len(nums)
    sum = numpy.prod(numbers)

    for i in range(0, length):
        product = sum / numbers[i]
        output_division.append(product.astype(int))

    return output_division

# Outputs an array with the product of all elements of 
# the input array except for the current element, without division
def productExceptSelfNoDivision(nums):
    length = len(nums)
    if length == 0:
        return 'Empty Array'
    
    L, R, answer = [0] * length, [0] * length, [0] * length

    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i - 1] * L[i - 1]

    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        R[i] = nums[i + 1] * R[i + 1]


    for i in range(0,length):
        # outputNoDivision.append(L[i] * R[i])
        answer[i] = L[i] * R[i]

    return answer



def main():
    user_numbers = []
    useInput = input('Enter 1 to use default array, Enter 2 to enter your own array, "x" to exit: ')
    while useInput.lower() != 'x':
        if useInput == '1':
            print(productExceptSelfNoDivision(numbers))
            break
        elif useInput == '2':
            arrayInput = input('Enter a value to add to the array (x to finish): ')
            while arrayInput.lower() != 'x': 
                # if type(arrayInput) != int:
                if arrayInput.isdigit():
                    user_numbers.append(int(arrayInput))
                    arrayInput = input('Enter a value to add to the array (x to stop): ')
                else:
                    print('That was not an integer')
                    arrayInput = input('Enter a value to add to the array (x to stop): ')
            print(productExceptSelfNoDivision(user_numbers))
            break
        else:
            print('Invalid Input')
            useInput = input('Enter 1 to use default array, Enter 2 to enter your own array, "x" to exit: ')

            

    # print(numbers)
    # print(productExceptSelf(numbers))
    # print(productExceptSelfNoDivision(numbers))

if __name__ == "__main__":
    main()
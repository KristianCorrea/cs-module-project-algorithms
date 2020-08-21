'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0
    
    for integer in range(len(arr)):
        if arr[integer] != 0:
            arr[count] = arr[integer]
            count += 1
            
    for i in range(count, len(arr)): #fill rest with zeros
        arr[i] = 0
        
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
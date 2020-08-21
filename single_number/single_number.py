'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    #loop to go through each index
    for numberIndex in range(len(arr)):
        current_number = arr[numberIndex]
        current_number_times_seen = 0
        for number in range(len(arr)):
            if current_number == arr[number]:
                current_number_times_seen += 1
        if current_number_times_seen == 1:
            return current_number


if __name__ == '__main__':
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
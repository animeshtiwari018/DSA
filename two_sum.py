""" Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array [index1, index2] where:

             1 <= index1 < index2 <= numbers.length 
             numbers[index1 - 1] + numbers[index2 - 1] == target

You may assume that each input has exactly one solution, and you may not use the same element twice. """



''' Brute Force '''
"""def two_sum():
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1,n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

numbers = [ 1, 2, 4, 7, 8]
target = 8

result = two_sum()
print(result)"""
#---------------------------------------------------#


''' Optimize solution '''

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]
        
        elif current_sum < target:
            left += 1
            
        else: 
            right -= 1


numbers = [1, 4, 7, 9, 11]
target = 8
result = two_sum(numbers, target)

print(result)
 
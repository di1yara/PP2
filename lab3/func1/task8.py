"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
python
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False

"""
def spy_game(numbers):
    order = ""
    num = "007"
    for i in range(len(numbers)):
        if numbers[i] == 0 or numbers[i] == 7:
            order += str(numbers[i])
        if num in order:  
            return True
    return False

numbers = list(map(int, input("Enter numbers: ").split()))
print(spy_game(numbers))


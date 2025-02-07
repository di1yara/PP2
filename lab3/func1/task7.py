"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
python
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False


"""
def has_33(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] ==3 and numbers[i+1]==3:
            return True
    return False
numbers=list(map(int,input("Enter numbers:").split()))
print(has_33(numbers))
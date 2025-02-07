"""
Write a function that computes the volume of a sphere given its radius.

"""
def volume(radius):
    volume_sphere=(4/3)*3.14*radius**3
    return int(volume_sphere)
radius=int(input("Enter radius: "))
print(volume(radius))
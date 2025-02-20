#Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2
N = int(input(" enter a number: "))
for square in generate_squares(N):
    print(square, end=" ")

# DSC 510
# Week 4
# BlackBoard Post 4.2: Interests
# Author: Michael Hotaling
# 06/26/2020


def mean(numbers):
    # This one is pretty easy. We can just create a variable named summer and set it equal to 0.
    # For every element in the list, we can add the value to the summer and once we reach the end of the list
    # we can divide the summer by the number of elements.
    summer = 0
    for i in numbers:
        summer += i
    average = (summer / len(numbers))
    return average


def median(numbers):
    # This function will find the median value in a list
    # We will first sort the list from lowest to highest and find the length of the list
    # If the list length is even, we will need to use floor division to find the two middle values and average them
    # If the list is odd, we just need to pull the middle value
    numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        med1 = numbers[length // 2]
        med2 = numbers[length // 2 - 1]
        med = (med1 + med2) / 2
        return med
    else:
        med = numbers[(length // 2)]
        return med


def variance(numbers):
    # Variance can be understood as a measurement of the spread between numbers in an array of numbers
    # Simplified, variance can be though of as how far each value in a set is from the mean of the set and,
    # therefore, from every other number in the set.
    # We can create a new list and fill it with the calculated values. Once that's done, we can take the mean
    var_list = []
    mu = mean(numbers)
    for i in numbers:
        var_list.append((i - mu) ** 2)
    return mean(var_list)


def square_root(number):
    # https://www.cse.wustl.edu/~cytron/101Pages/f08/Notes/SquareRoot/sqrt.html
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    # https://en.wikipedia.org/wiki/Newton%27s_method
    # This one was actually pretty tricky. We could just use the built in exponential function ** and use 0.5 as the
    # exponent, but that wouldn't be any fun. Instead, we can create a recursive function to approximate the square
    # root of a number. This is known as Newtons Method

    start = 0
    end = number
    guess = 0
    threshold = 0.0000000000001

    while end - start > threshold:
        guess = (start + end) / 2
        m_square = guess * guess
        if abs(m_square - number) <= threshold:
            return guess
        elif m_square < number:
            start = guess
        else:
            end = guess
    return guess


def standard_deviation(numbers):
    # Now that we have defined square root and variance, all we need to do here is use both to find the square root.
    return square_root(variance(numbers))


if __name__ == "__main__":

    lst = [1, 5, 7, 22, 94, -59, 0, 2, 5, 7, 88, 49, 51]
    print("The mean is " + str(mean(lst)))
    print("The median is " + str(median(lst)))
    print("The variance is " + str(variance(lst)))
    print("The standard deviation is " + str(standard_deviation(lst)))

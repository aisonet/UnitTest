
def is_prime(number):
    for elem in range (2,number):
        if number % elem == 0:
            return False

    return True

def print_next_prime(number):
    index = number
    while True:
        index += number
        if is_prime(index):
            print  index

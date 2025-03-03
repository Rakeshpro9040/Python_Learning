def is_prime(num):
    '''
    Naive method of checking for primes.
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

# Call inisde local file
# is_prime(1)

# Now we will test this function by calling in outer/foreign file
# https://www.geeksforgeeks.org/python-call-function-from-another-file/
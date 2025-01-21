import math

def allPrimesUpTo(num):
    """
    Returns a list of all prime numbers up to the given number 'num' using the Linear Sieve (Sieve of Euler).

    Parameters:
        num (int): The upper limit to find prime numbers.

    Returns:
        List[int]: A list containing all prime numbers up to 'num'.
    """
    print(f"Starting the Linear Sieve to find all primes up to {num}.")

    if num < 2:
        print("No primes available. The smallest prime number is 2.")
        return []

    # Initialize a list to track prime status of numbers from 0 to num
    is_prime = [True] * (num + 1)
    is_prime[0] = False  # 0 is not a prime
    is_prime[1] = False  # 1 is not a prime

    # List to store discovered primes
    primes = []

    # Iterate through each number from 2 to num
    for current in range(2, num + 1):
        if is_prime[current]:
            primes.append(current)
            print(f"Found a prime number: {current}")
        
        # Iterate through primes and mark multiples
        for prime in primes:
            if prime * current > num:
                break
            is_prime[prime * current] = False
            print(f"Marking {prime * current} as non-prime because it is a multiple of {prime}.")
            
            # If current is divisible by prime, no need to continue
            if current % prime == 0:
                break

    print("Final list of prime statuses:")
    print(is_prime)
    
    print(f"List of primes up to {num}:")
    print(primes)
    
    return primes



# Second Method

def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor == 0:
                # Not prime
                break
            if factor > sqrtNum:
                # Its prime
                primes.append(number)
                break
    return primes
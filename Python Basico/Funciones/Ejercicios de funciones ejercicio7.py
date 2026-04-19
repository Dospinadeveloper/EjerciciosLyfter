def filter_primes(numbers):
    primes = []
    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
    
    return primes

my_list = [1, 4, 6, 7, 13, 9, 67]


result = filter_primes(my_list)
print(f"Prime numbers: {result}")

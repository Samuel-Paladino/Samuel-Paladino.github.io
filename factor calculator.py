def find_factors(number):
    factors = []
    for possible_factor in range(1, abs(number) + 1):
        if number % possible_factor == 0:
            factors.append(possible_factor)
            factors.append(-possible_factor)
    return sorted(set(factors))

number = int(input("Enter a number: "))

factors = find_factors(number)

print(f"The factors of {number} are: {factors}")
import time
print("\nThis window will close in 2 minutes...")
time.sleep(120)

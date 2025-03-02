# Write a recursive function to find the sum of all digits of a given number until a single-digit number remains(digital root).

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int, str(n))))

# Test the function

print(digital_root(1234567890)) 

print(digital_root(942))  

print(digital_root(145))  
import random
import string

def generate_random_number(start=0,end=100):
    return random.randint(start,end)

def generate_random_lists():
    list1 = [generate_random_number() for _ in range(10)]
    list2 = [generate_random_number() for _ in range(10)]
    return list1, list2

def generate_random_password(length=6):
    chars=string.ascii_letters +string.digits+string.punctuation
    return ''.join(random.choice(chars)for _ in range(length))

def random_sample(data,n):
    pass

def generate_otp(len=4):
    return ''.join(str(random.randint(0,9))for _ in range(len))
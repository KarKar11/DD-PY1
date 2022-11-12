import random
def get_random_password(n=8) -> str:
    str_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_small = 'abcdefghijklmnopqrstuvwxyz'
    str_number = '0123456789'
    str_ = str_high + str_small + str_number
    return (''.join((random.sample(str_,n))))
print(get_random_password())

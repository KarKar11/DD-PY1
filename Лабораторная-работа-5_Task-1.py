# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
for num in range(0, 16):
    list_dict = {'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num) }
    pprint(list_dict)
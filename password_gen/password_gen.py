'''
  @author: craig
  @date: 2022/06/21
'''

from random import choice
from string import printable

def random_password(length):
    """
      Generates a random password of n length.
      :param int length: The length of the password to generate.
    """

    return "".join([choice(printable) for x in range(int(length))])

if __name__ == "__main__":
    amount = int(input("How many passwords would you like to generate? "))
    number = int(input("Length of said password(s)? "))

    for i in range(1, amount + 1):
        print(f"{repr(random_password(number))}")

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
    pAmount = int(input("How many passwords would you like to generate? "))
    pLength = int(input("Length of said password(s)? "))

    if pAmount > 0:
        if pLength > 0:
            for i in range(1, pAmount + 1):
                print(f"{repr(random_password(pLength))}")
        else:
            print("Password length must exceed 0.")
    else:
        print("Looks like you don't want to generate any passwords?")
